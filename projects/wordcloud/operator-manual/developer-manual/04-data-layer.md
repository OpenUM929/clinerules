---
reportTheme: technical
---

# 데이터 계층

↑ [목록으로](00-index.md)

> **핵심**: 단일 SQLite(`.sessions/deploy_sessions.db`, WAL)에 모든 상태를 두고, 접근은 `deploy_session_service._get_conn()` 하나로 통일한다. 스키마는 `schema_version` 테이블로 버전 관리하며 부팅 시 자동 마이그레이션한다.
> **기준 버전 / 최종 확인일**: v1.1.0 · 2026-07-22 (commit `7b106b5`)

---

## 저장소 구성

| 저장소 | 위치 | 내용 | 배포 |
|--------|------|------|------|
| 운영 DB | `.sessions/deploy_sessions.db` (SQLite, WAL) | 세션·평가·배치·갤러리·욕설·취득문장 | **제외**(런타임 생성) |
| 런타임 설정·매핑 | `src/configs/` | 매핑(`mappings/`)·가명 매핑(`pseudonym_mappings.enc`)·불용어·가중치 | 포함 |
| 산출물 | `outputs/`, `processed_data/` | 워드클라우드 PNG·배치 중간물 | **제외** |

- 연결 헬퍼: `_get_conn()`(`deploy_session_service.py:12`) — `PRAGMA journal_mode=WAL` + `row_factory=sqlite3.Row`.
- **DAO 단일 진입**: `batch_work_order_service` 등 다른 서비스도 이 헬퍼(`_get_conn`/`_init_db`)를 재사용해 순환 임포트·중복 초기화를 피한다(`batch_work_order_service.py:12`).

> ⚠️ **앱 설정과 DB는 한 쌍**: 앱은 `.sessions` DB와 `src/configs` 매핑을 함께 읽는다. 둘을 교체할 땐 **한 쌍으로 함께 교체 + 서버 재시작**한다. [[project_db_mapping_pair_swap]]

---

## 주요 테이블 (`_init_db()` DDL, `deploy_session_service.py:20-131`)

| 테이블 | 키/제약 | 용도 |
|--------|---------|------|
| `deploy_sessions` / `deploy_tasks` | — | 배포 세션·작업 진행 |
| `gallery_entries` | — | 배포 갤러리 |
| `employees` | `employee_id` PK | 직원 마스터 |
| `evaluations` | `id` PK(AUTOINCREMENT) · **UNIQUE(`employee_id`, `fingerprint`)** | 평가 원문(JSON `data`) + 감정 보정 |
| `batch_work_orders` | `batch_id` UNIQUE | 배치 작업서(설정 스냅샷 + 진행) |
| `batch_work_order_items` | PK(`batch_id`, `employee_id`) | 완료 직원 목록(O(델타) append) |
| `schema_version` | `version` PK | 스키마 이력 |
| `acquired_sentences` | (마이그레이션 생성) | 취득 문장(데이터셋 연결) + KoTE 점수 |
| `profanity_employees` / `profanity_sentences` | (마이그레이션 생성) | 욕설 집계 |

### evaluations 컬럼 (`:80-93`)

```
id INTEGER PK AUTOINCREMENT | employee_id TEXT NOT NULL (FK) | evaluator_id TEXT
evaluation_date TEXT | batch_id TEXT | data TEXT NOT NULL | fingerprint TEXT
created_at TEXT | sentiment_corrections TEXT DEFAULT '{}'  (← 스키마 v4 추가)
```

- **`evaluation_id`는 고유하지 않다** → 감정 보정은 DB row `id`(=`_db_id`)로 키잉한다([03 문서](03-emotion-engine.md) §4). [[project_eval_id_not_unique]]
- 중복 방지는 `UNIQUE(employee_id, fingerprint)`. 실데이터 감사에서 중복률이 높았으므로(≈62.7%, [[project_prod25_audit]]) 집계 시 중복제거를 전제한다.
- ⚠️ `evaluation_date`는 int(예: 2025)로 들어올 수 있어 연/월 행필터가 탈락하는 버그가 있었다 → `_get_eval_field_value`(`perspective_service.py:1602`)에서 str 정규화. [[project_eval_date_int_filter_bug]]
- 🔴 **입력 칸 구분(장점/단점)의 정본은 `data` JSON 안의 `evaluation_document_field`** 다(`batch_processor.py:291`, 0707_01 Phase2). 극성 판정이 이 값의 프리픽스에 강하게 의존하므로([03 문서](03-emotion-engine.md) §1) **원본 DB가 이 값의 유일한 무손실 보관처**다. 파생 export 에서 이 값이 안 보인다고 "자료에 없다"고 결론내지 말 것 — 소재는 4곳이고 배치 실행 방식이 결정한다 → [06. 배치 처리 §필드 소재 지도](06-batch.md) · [[project_field_lost_in_260714_rebatch]]

---
---pb---

## 스키마 마이그레이션 (`_apply_schema_migrations()`, `:137`)

부팅 시 `schema_version`을 보고 누락 버전만 순차 적용한다. 확인된 변경 예:

| 버전 | 변경 | 근거 |
|------|------|------|
| v1 | 초기(gallery_entries·employees·evaluations) | `:129-130` |
| v4 | `evaluations`에 `sentiment_corrections TEXT DEFAULT '{}'` 추가(문장 단위 감정 override) | `:182-188` |
| (추가) | `acquired_sentences`에 `kote_pos/kote_neg/kote_neutral/override_score/source_kind` 컬럼 | `:254-258` |
| (추가) | `deploy_sessions`에 `started_at` | `:275` |

> **새 테이블/컬럼을 추가할 때**: `_init_db()`의 DDL(신규 설치용)과 `_apply_schema_migrations()`의 버전 분기(기존 DB 업그레이드용) **양쪽**에 추가한다. 한쪽만 넣으면 신규/기존 환경 중 하나가 깨진다.

---

## 부팅 자동 마이그레이션 (`web/app.py:125-126`)

`main()`이 `deploy_session_service._auto_migrate_evaluations()`(`:329`)를 호출 — DB `evaluations`가 비어 있으면 레거시 `users/*.json`을 테이블로 1회 이전한다. `_auto_migrate_manifest()`(`:307`)도 함께 존재. 이미 데이터가 있으면 건너뛴다(멱등).

---

## 가명화 데이터 취급

- 가명화 대상은 `target_employee_id`만. 가명 텍스트는 **DB·판정 패킷에만** 두고, 그 외는 원데이터로 다룬다. 이중 가명화 금지(멱등). [[project_pseudonymization_scope]]
- 가명 매핑은 `src/configs/pseudonym_mappings.enc`(암호화). 역가명은 `pseudonym_manager.py`(`src/modules/`)가 담당.
- `plans/`는 배포 제외 폴더이며 학습 데이터(가명)는 **이 폴더 외에 두지 않는다**(유출 방지, CLAUDE.md).

---
↑ [목록으로](00-index.md) · [← 이전: 03. 감정분석 엔진](03-emotion-engine.md) · [다음: 05. 빌드·배포 →](05-build-deploy.md)
