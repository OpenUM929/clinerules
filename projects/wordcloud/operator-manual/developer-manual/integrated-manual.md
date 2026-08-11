# 유지보수 개발자용 개발 메뉴얼 (v1.1.0)

> **대상 독자**: 이 시스템을 넘겨받아 유지보수·기능개선하는 개발자.
> **합격 기준**: 코드를 처음 보는 개발자가 이 문서로 아키텍처를 이해하고 안전하게 수정·빌드·배포할 수 있어야 한다.
> **기준 버전 / 최종 확인일**: system v1.1.0 · model `hr-sentiment-v1.0` · source_commit `7b106b5` · build 2026-07-16 · 문서 확인일 2026-07-22

---

## 이 문서는 무엇인가

한국어 인사평가 문서를 분석하여 **감정(긍정/부정/중립)·단어 빈도·워드클라우드**를 생성하고, 대량 배치·수집 대시보드를 제공하는 내부망 데스크톱 시스템의 **개발자 관점 설명서**다. 운영자용 사용법이 아니라, **소스 구조·엔진 동작·데이터 계층·빌드/배포·확장 시 주의점**을 코드 실증으로 다룬다.

- 앱 소스 루트: `wordcloud_project/`
- 백엔드: Python 3.10 + Flask (블루프린트 12개)
- 핵심 모델: 베이스 KoTE(44감정) + HR 도메인 파인튜닝 3분류 극성 모델
- 기준 버전 근거: `wordcloud_project/VERSION.json`

> ⚠️ 이 문서의 모든 경로·라인 번호는 확인일(2026-07-22, commit `7b106b5`) 기준 실측이다. 코드가 바뀌면 라인 번호는 어긋날 수 있으니 함수명·상징 이름으로 재탐색하라.

---

## 문서 구성 (읽는 순서)

| # | 문서 | 다루는 내용 |
|---|------|------------|
| 01 | [아키텍처 개요](01-architecture.md) | 실행 진입점 · Flask 앱 구성 · 요청 흐름 · 디렉터리 지도 |
| 02 | [모듈 지도](02-module-map.md) | 주요 패키지/서비스의 책임과 상호관계 |
| 03 | [감정분석 엔진](03-emotion-engine.md) | KoTE 로딩/추론 · 3-class 매핑 · 규칙 계층 · 절 단위 판정 · corrections 키잉 |
| 04 | [데이터 계층](04-data-layer.md) | `.sessions` DB · `src/configs` 매핑 · 스키마 · evaluation_id 함정 |
| 05 | [빌드·배포](05-build-deploy.md) | `build_deploy.ps1` · VERSION.json 재생성 · 배포 제외 폴더 |
| 06 | [배치 처리](06-batch.md) | 대규모(약 1.9만명) 배치 · 추적 복잡도 · 작업서(Work Order) |
| 07 | [파인튜닝 데이터 파이프라인](07-finetune-pipeline.md) | `hr-kote-finetune` 데이터셋 · RUNBOOK · gold 승격 · 재학습 경로 |
| 08 | [개발 환경·테스트·트러블슈팅](08-dev-setup-troubleshooting.md) | 로컬 세팅 · 실행 안내 · 자주 겪는 함정 |
| 09 | [확장 포인트/주의](09-extension-points.md) | 공통 모듈 보호 · 시간처리·필드네이밍 표준 |

---

## 상위 참조 지침 (정본)

- 프로젝트 나침반: `wordcloud_project/CLAUDE.md`, [`.clinerules/common/core/00-core.md`](../../../../common/core/00-core.md)
- 감정 규칙 상세(모듈 개요): [`project_wordcloud/modules/emotion-analysis.md`](../../modules/emotion-analysis.md)
- 배포 절차: [`project_wordcloud/deployment.md`](../../deployment.md)
- 시간 처리: [`development/time-handling-rules.md`](../../../../common/development/time-handling-rules.md) · 필드 네이밍: [`development/field-naming-convention.md`](../../../../common/development/field-naming-convention.md)
- 데이터셋 상시 절차: `wordcloud_project/plans/_datasets/kote_finetune/RUNBOOK.md`

> **정직 고지**: 본 문서는 코드 정적 조사(Read/Grep) 기반이다. 저자는 서버를 기동하거나 배치를 실행하지 않았다(무단 실행 금지 원칙). "동작한다"는 서술은 코드 경로 확인 수준이며, 런타임 검증이 필요한 항목은 각 문서에서 "확인 필요"로 명시했다.

---


---pb---

# 1 아키텍처 개요


> **핵심**: Flask 팩토리(`web/app.py`) → 12개 블루프린트 → 서비스 계층 → SQLite(`.sessions`) + 파일 산출물.
> **기준 버전 / 최종 확인일**: v1.1.0 · 2026-07-22 (commit `7b106b5`)

---

## 1.1 실행 진입점

| 항목 | 값 | 근거 |
|------|-----|------|
| 앱 팩토리 | `create_app()` | `web/app.py:53` |
| 실행 함수 | `main()` → `app.run(...)` | `web/app.py:121-141` |
| 모듈 실행 | `python -m web.app` | `web/app.py:144-145` (`if __name__ == '__main__': main()`) |
| 기본 포트/호스트 | `127.0.0.1:5001` | `src/config/settings.py:48-49`, `.env` |
| Debug 플래그 | `FLASK_DEBUG`(기본 True) | `src/config/settings.py:47` |
| 리로더 | `use_reloader=False`, `threaded=True` | `web/app.py:139-140` |

- Windows 인코딩 강제: `web/app.py:9-15`에서 `stdout/stderr`를 UTF-8로 재구성하고 로케일을 `ko_KR`로 고정한다.
- 프로젝트 루트를 `sys.path`에 추가: `web/app.py:18`.
- 배포 패키지의 `start.bat`도 동일하게 `python -m web.app`을 호출한다(`deploy/build_deploy.ps1:195-211`).

> ⚠️ **서버 실행은 안내만**: 이 문서는 기동 방법을 설명할 뿐, 저자는 서버를 직접 띄우지 않는다. 로컬 구동은 [08 문서](08-dev-setup-troubleshooting.md) 참조.

---

## 1.2 앱 부팅 시퀀스

`main()`(`web/app.py:121`) 실행 순서:

1. `create_app()` — Flask 인스턴스 생성, `template_folder`/`static_folder`를 절대경로로 지정(`web/app.py:55-57`).
2. 앱 설정: `SECRET_KEY`, `JSON_AS_ASCII=False`(한글 JSON 유지), 업로드 한도 `MAX_CONTENT_LENGTH=100MB`(`web/app.py:60-63`).
3. 블루프린트 12개 등록(`web/app.py:66-77`).
4. 컨텍스트 프로세서 2개 주입: 관리자 세션 상태(`inject_auth_state`)·버전 정보(`inject_version_info` → `version_service.get_version_info()`)(`web/app.py:79-86`).
5. 404/500 에러 핸들러 등록(`web/app.py:89-100`).
6. `/outputs/...` 정적 산출물 서빙 라우트 3종(`web/app.py:103-116`).
7. **부팅 마이그레이션**: `main()`이 `deploy_session_service._auto_migrate_evaluations()`를 호출(`web/app.py:125-126`) — DB가 비어 있으면 `users/*.json`을 `evaluations` 테이블로 1회 이전.

---

## 1.3 블루프린트(라우트) 지도

`web/app.py:40-51`에서 임포트하여 `web/app.py:66-77`에서 등록한다.

| 블루프린트 | URL prefix | 파일 | 책임 |
|-----------|-----------|------|------|
| `ui_bp` | (없음) | `src/routes/ui_routes.py` | HTML 페이지 렌더(대시보드·워드클라우드·설정 등) |
| `integrated_bp` (`metadata`) | `/api/integrated` | `src/routes/integrated_data_routes.py` | 통합 수집 데이터 API |
| `batch_bp` | `/api/batch` | `src/routes/batch_routes.py` | 배치 실행·진행·Resume API |
| `wordcloud_bp` | `/api/wordcloud` | `src/routes/wordcloud_routes.py` | 워드클라우드 생성 API |
| `api_bp` | `/api` | `src/routes/api_routes.py` | 공통/기타 API |
| `perspective_bp` | `/api/perspective` | `src/routes/perspective_routes.py` | 감정·관점(그룹) 분석 API |
| `test_bp` | (없음) | `src/routes/test_routes.py` | 감정/욕설/비꼬임 테스트 UI·API |
| `admin_bp` | `/admin` | `src/routes/admin_routes.py` | 관리자 로그인·설정 |
| `wordcloud_data_bp` | `/api/wordcloud` | `src/routes/wordcloud_data_routes.py` | 워드클라우드용 데이터 조회 |
| `wordcloud_preview_bp` | (없음) | `src/routes/wordcloud_preview_routes.py` | 미리보기 |
| `plans_bp` | `/admin` | `src/routes/plans_routes.py` | Plans 칸반보드·CR |
| `version_bp` | `/api/version` | `src/routes/version_routes.py` | 버전·무결성 정보 |

> 확인 필요: `wordcloud_bp`와 `wordcloud_data_bp`가 동일 prefix `/api/wordcloud`를 공유한다(`src/routes/wordcloud_routes.py:11`, `wordcloud_data_routes.py:10`). 엔드포인트 경로가 겹치지 않는지는 라우트 추가 시 반드시 확인하라.

---
---pb---

## 1.4 요청 흐름 (라우트 → 서비스 → DAO → DB)

계층 경계가 명확하다. 대표 예로 감정/단어 집계 흐름:

```
[HTTP 요청]
   ↓  src/routes/perspective_routes.py (Blueprint 핸들러: 파라미터 파싱·검증)
   ↓  src/services/perspective_service.py (도메인 로직: 문장→감정 override, 단어 점수 집계)
   ↓  src/modules/*.py (엔진: KoTE 추론·HR 감정모델·전처리·워드클라우드 렌더)
   ↓  src/services/deploy_session_service._get_conn() (DAO: SQLite 연결 헬퍼)
   ↓  .sessions/deploy_sessions.db (SQLite, WAL)
   ↑  응답(JSON) 또는 산출 이미지(/outputs/... 서빙)
```

- **DAO 계층**은 별도 ORM 없이 `deploy_session_service._get_conn()`(`src/services/deploy_session_service.py:12-17`)을 공유하는 얇은 SQLite 접근이다. `batch_work_order_service`도 이 헬퍼를 재사용해 순환 임포트·중복 초기화를 피한다(`src/services/batch_work_order_service.py:12`).
- **모듈(엔진)**은 상태를 갖는 싱글톤(KoTE·HR 감정모델)이라 프로세스 1회 로드 후 재사용된다([03 문서](03-emotion-engine.md)).
- **산출물**(워드클라우드 PNG 등)은 DB가 아니라 `outputs/` 하위에 저장되고 `/outputs/<path>` 라우트로 서빙된다(`web/app.py:103-116`).

---

## 1.5 디렉터리 지도 (`wordcloud_project/`)

| 폴더 | 역할 |
|------|------|
| `web/` | Flask 진입점(`app.py`)·`templates/`(Jinja HTML)·`static/`·`configs/` |
| `src/routes/` | 블루프린트(HTTP 계층) |
| `src/services/` | 도메인 서비스·DAO(감정 집계·배치·수집·판정패킷·갤러리 등) |
| `src/modules/` | 분석 엔진(KoTE·HR 감정·전처리·워드클라우드·욕설·리더십·비꼬임) |
| `src/models/` | 통합 데이터 매니저(`integrated_data_manager.py`) |
| `src/config/` | `settings.py`(경로·플래그 정본) |
| `src/configs/` | 런타임 설정 JSON·매핑(`mappings/`)·가명 매핑(`pseudonym_mappings.enc`)·불용어 등 |
| `scripts/` | 유지보수 스크립트(`gen_version.py`·`migrate_evaluations.py`·벤치) |
| `utils/` | 로거·날짜 정규화 공용 유틸 |
| `deploy/` | `build_deploy.ps1`(배포 빌더) |
| `.sessions/` | SQLite DB(`deploy_sessions.db`) — 배포 제외 |
| `outputs/` · `processed_data/` · `inputs/` | 산출·중간·입력 데이터 — 배포 제외 |
| `plans/` | 계획·데이터셋(`_datasets/kote_finetune/`) — 배포 제외 |
| `venv/` · `vendor_python_pkgs/` | 로컬 런타임 — 배포 제외 |

> 배포 제외 목록의 정확한 근거는 [05 빌드·배포](05-build-deploy.md) `$ExcludeDirs`/`$ExcludeFiles` 절 참조.

---


---pb---

# 2 모듈 지도


> **핵심**: 엔진(`src/modules`)은 상태를 가진 싱글톤, 서비스(`src/services`)는 도메인 로직·DAO. 감정 판정은 여러 파일에 걸쳐 계층화되어 있다.
> **기준 버전 / 최종 확인일**: v1.1.0 · 2026-07-22

---

## 2.1 엔진 계층 (`src/modules/`)

| 파일 | 책임 | 주요 심볼 |
|------|------|----------|
| `kote_shared.py` | 베이스 KoTE(44감정) 모델 싱글톤(스레드 안전). emotion·leadership이 GPU 인스턴스 공유(VRAM 중복로드 방지) | `KoTEModel`(`kote_shared.py:10`) |
| `emotion_analysis.py` | KoTE 추론 래퍼·44감정→3극성 후처리·top3 | `EmotionAnalysis`, `analyze_emotion`(`:297`), `analyze_emotion_batch`(`:323`) |
| `hr_sentiment.py` | HR 도메인 파인튜닝 3분류 극성 모델(별도 싱글톤·안전 폴백) | `predict_sentiments`(`:155`), `predict_proba`(`:173`), `model_status`(`:136`) |
| `sentence_emotion.py` | 문서→문장 분할 후 문장별 KoTE 원시 점수(배치 캐시·그룹 fallback 공유) | `compute_sentence_raw_scores`(`:13`) |
| `text_preprocessing.py` | 문장 분리·**절 분리**(혼합극성 분해) | `split_sentences`(`:27`), `split_clauses`(`:75`) |
| `wordcloud_generator.py` | 워드클라우드 이미지 렌더 | — |
| `nlp_analysis.py` | 형태소·명사 추출(빈도) | `NLPAnalysis` |
| `profanity_filter.py` | 욕설 탐지/필터(한/영) | `advanced_filter_profanity` |
| `leadership_analysis.py` | 리더십 특질 분석(KoTE 공유) | — |
| `sarcasm_analysis.py` | 비꼬임 분석 | — |
| `pseudonym_manager.py` | 가명화/역가명(암호화 매핑) | — |
| `stopword_manager.py` · `word_boost_manager.py` · `hr_context_lexicon.py` | 불용어·가중·도메인 렉시콘 | — |
| `integrated_analysis.py` | 통합(문장 override 질량 기반) 감정·단어 버킷 집계 | — |

> ⚠️ `.bak`/`.py.bak` 파일(`batch_manager.py.bak`, `wordcloud_data_service.py.bak` 등)은 **런타임에 로드되지 않는 잔재**다. 수정 대상으로 착각하지 말 것 — 임포트 경로에 없는 사본이다.

---

## 2.2 서비스 계층 (`src/services/`)

| 파일 | 책임 |
|------|------|
| `perspective_service.py` | **감정 판정 규칙 계층의 핵심**(문장/절 override·긍정구제·개선요청 부정화·모델 라벨 override)·단어 점수·감정 집계·corrections 로드([03 문서](03-emotion-engine.md)) |
| `batch_processor.py` | 대규모 배치 실행(청크 수집→병렬 직원 처리→요약)·체크포인트 |
| `batch_service.py` · `batch_manager.py` · `batch_events.py` · `batch_staging.py` | 배치 오케스트레이션·진행 이벤트·staging DB |
| `batch_work_order_service.py` | 배치 **작업서**(설정 스냅샷+진행) 영구화·Resume 지원 |
| `deploy_session_service.py` | SQLite 스키마 정의·마이그레이션·연결 헬퍼(**DAO 허브**)·부팅 마이그레이션 |
| `judgment_packet_service.py` | 감정 판정 작업 패킷(추출→AI판정→삽입, 가명 in-place) |
| `gallery_db_service.py` | 배포 갤러리(`gallery_entries`) |
| `wordcloud_data_service.py` · `wordcloud_service.py` | 워드클라우드용 데이터 조회·생성 |
| `integrated_data_service.py` | 수집 대시보드 데이터 |
| `profanity_db_service.py` | 욕설 집계 저장/조회 |
| `acquired_handoff.py` | 취득 문장(`acquired_sentences`) 핸드오프(데이터셋 연결) |
| `version_service.py` | `VERSION.json` 읽기·무결성 대조 |
| `perspective_service.py`(재게시) · `user_data_manager.py` | 직원/평가 데이터 접근 |
| `progress_time.py` | 진행률·경과시간 표시 |

---
---pb---

## 2.3 상호관계 (호출 그래프 요약)

```
routes/perspective_routes.py
   └─> services/perspective_service.py
          ├─> modules/sentence_emotion.compute_sentence_raw_scores
          │        └─> modules/emotion_analysis.analyze_emotion_batch
          │                 └─> modules/kote_shared.KoTEModel (싱글톤)
          ├─> modules/hr_sentiment.predict_sentiments (플래그 on 시)
          ├─> modules/text_preprocessing.split_sentences / split_clauses
          └─> services/deploy_session_service._get_conn  (corrections 로드)

routes/batch_routes.py
   └─> services/batch_processor.process_batch
          ├─> services/batch_staging (원문 적재 staging.db)
          ├─> services/batch_work_order_service (작업서·완료직원 items)
          ├─> models/integrated_data_manager
          └─> modules/nlp_analysis, profanity_filter, wordcloud_generator

web/app.py (부팅)
   └─> services/deploy_session_service._auto_migrate_evaluations
```

- **KoTE 단일 로드 원칙**: `emotion_analysis`와 `leadership_analysis`는 `KoTEModel` 싱글톤을 공유한다(`emotion_analysis.py:53-59`, `kote_shared.py:10-28`). 새 분석 모듈을 추가할 때 KoTE를 재로드하면 VRAM 한도를 초과할 수 있으니 반드시 이 싱글톤을 재사용하라.
- **HR 감정모델은 별도 싱글톤**(`hr_sentiment.py:36-37, 117-133`)이며 KoTE와 독립이다. 로드/추론 실패 시 `None`을 반환해 호출부가 규칙으로 폴백한다(무중단 설계).
- **DAO 단일 진입**: 모든 SQLite 접근은 `deploy_session_service._get_conn()`을 거친다. 새 테이블은 `_init_db()`의 DDL과 `_apply_schema_migrations()`의 버전 분기에 추가한다([04 문서](04-data-layer.md)).

---

## 2.4 서비스 vs 엔진 구분 원칙 (수정 시 판단 기준)

- **엔진(`src/modules`)에 두는 것**: 모델 추론, 형태소/문장/절 분리, 이미지 렌더 등 **도메인 무관 재사용 연산**.
- **서비스(`src/services`)에 두는 것**: "인사평가 감정은 이렇게 판정한다" 같은 **도메인 규칙**, DB 접근, 배치 오케스트레이션.
- 감정 **규칙**(긍정구제·개선요청 부정화 등)이 `perspective_service.py`에 있는 이유가 이것이다 — 모델 자체가 아니라 그 위에 얹는 도메인 판정이기 때문. 규칙 변경은 [03 문서](03-emotion-engine.md)의 안전 원칙을 반드시 따를 것.

---


---pb---

# 3 감정분석 엔진


> **핵심**: 문장/절 단위 KoTE 원시점수 → HR 파인튜닝 모델(선택) → **도메인 규칙 계층 override** → 사람 보정(corrections)의 4단 파이프라인. 규칙은 모두 `perspective_service.py`에 있고, 최우선 불변식은 **긍↔부 오분류 0**이다.
> **기준 버전 / 최종 확인일**: v1.1.0 · 2026-07-22 (commit `7b106b5`)
> **규칙 상세 정본**: [`project_wordcloud/modules/emotion-analysis.md`](../../modules/emotion-analysis.md)

---

## 3.1 두 개의 모델 (역할 분리)

| 모델 | 파일 | 역할 | 로드/폴백 |
|------|------|------|-----------|
| 베이스 KoTE(44감정) | `src/modules/kote_shared.py:10` `KoTEModel` | 문장별 44감정 확률 → 긍/부/중 원시 점수 | 스레드 안전 싱글톤. emotion·leadership이 **동일 GPU 인스턴스 공유**(VRAM 중복로드 방지) |
| HR 도메인 3분류 극성 | `src/modules/hr_sentiment.py:49` `_HRSentimentModel` | positive/negative/neutral **극성만** 결정(인사평가 파인튜닝) | 별도 지연로드 싱글톤. 디렉터리 부재·로드/추론 실패 시 **`None` 반환 → 규칙 폴백**(무중단) |

- HR 모델 라벨 순서: `0=positive, 1=negative, 2=neutral`(`hr_sentiment.py:19` `_ID2LABEL`).
- **필드 프리픽스 규약**(train/serve 정합): 장점/단점 필드가 있으면 입력을 `f'{field} 평가: {text}'`로 변환해 추론한다(`hr_sentiment.py:68-76` `_prefixed`). 재추론 대조 시 이 프리픽스를 빠뜨리면 오진한다.
- 캘리브레이션: 모델 디렉터리의 `calibration.json` temperature로 확률 눈금만 보정(`hr_sentiment.py:22-34`). **argmax 라벨은 T와 무관** — `predict_proba`의 confidence는 escalation 라우팅에만 쓴다.
- on/off 스위치: `USE_HR_SENTIMENT_MODEL`(기본 on, `src/config/settings.py:27`). 모델 실측 지문(sha256·loaded_at)은 `model_status()`(`hr_sentiment.py:136`)로 조회한다.

> **모델 파일 위치**: `settings.py:20,26` 기준 `D:\dev\wordcloud\model\`(= `wordcloud_project`의 형제 폴더). 배포 시 `-Package` 모드가 이 `model/`을 동봉한다([05 문서](05-build-deploy.md)).

---

## 3.2 문장·절 분리 (전처리)

`src/modules/text_preprocessing.py` — 무거운 의존이 없는 경량 모듈.

- `split_sentences(text)`(`:27`): `.!?\n`로 분할 + 인사말·5자 미만·깨진 HTML 엔티티(`&#NNNN;`)·자모 난타 노이즈 제외. **production 집계·갤러리가 쓰는 정본**.
- `split_clauses(sentence)`(`:75`): 역접·양보 연결어미(`으나/지만/는데/…`)·대조 접속부사(`그러나/반면/…`) 경계에서 절 분리. **혼합극성 문장**("좋으나 낮음")을 단일극성 절로 쪼갠다.
  - ⚠️ **데이터셋 빌드 전용**이다(주석 `:55-58`). production `split_sentences`는 건드리지 않는다(집계 영향 격리).
  - 부정 범위 보존: 연결어미는 완결 용언 뒤에 오므로 `않/없/안`을 절 중간에서 끊지 않는다("강압적이지 않으나"는 한 절 유지).
  - 표지 없으면 `[sentence]` 그대로 반환(안전한 기본값), 과분할은 4자 미만 조각 흡수(`_CLAUSE_MIN_LEN`).

---
---pb---

## 3.3 규칙 계층 (`perspective_service.py` — 엔진 위에 얹는 도메인 판정)

문장 override의 **단일 정의**는 `_sentence_sentiment_override_explain(pos, neg, sentence, …)`(`:1221`)이며, `sentence_sentiment_override`(`:1408`)는 이를 호출해 점수만 반환한다. **분기 조건·반환 점수는 두 함수가 완전히 동일해야 한다**(동작 보존 계약, `:1226`).

분기 **순서**가 곧 우선순위다(0702_03 reorder 반영). 대표 분기:

| 순서 | 분기(rule_id) | 방향 | 핵심 검출기 |
|------|--------------|------|-------------|
| 1 | 개인안녕/건강 조언 → 중립 | →중립 | `is_personal_wellbeing_neutral`(`:984`), `is_health_advice`(`:943`) |
| 2 | 광의 혼합 긍부 → 중립 | →중립 | `is_mixed_pos_neg`(`:1030`) (0715 사용자 카테고리3) |
| 3 | 무결점/무응답/약점-못찾음 선언 → 중립 | →중립 | `is_no_weakness_declaration`(`:857`), `is_no_response`(`:432`) |
| 4 | 긍정 구제(positive_rescue) | →긍정 | `has_positive_implying_phrase`(`:451`) + `has_improvement_request`(`:721`) 등 게이트 |
| 5 | 개선요청/결핍 프레이밍 → 부정 | →부정 | `_has_improvement_request_core`(`:667`), `has_constructive_need`(`:607`), `_is_speculative_need`(`:1071`), `_has_request_marker`(`:1129`) |

- **개선요청 화행 = 부정**(사용자 재정, [[feedback_improvement_request_is_negative_gold]]): "~할 필요/키워야"는 중립이 아니라 부정으로 확정. 단 명확한 긍정 절이 선행하는 혼합("뛰어나나 개선 필요")은 →중립(`improvement_request_neutral`, `:1362`).
- **긍↔부 안전 방향**: 규칙이 바꾸는 방향은 항상 →중립 또는 한 방향뿐이며, 긍정↔부정을 직접 뒤집는 분기는 두지 않는다. 다의·조사 트랩(`이나` 나열=or vs 양보) 때문에 대조어 게이트가 세분돼 있다(`_has_improve_blocking_contrast`, `:165`).

### 3.3.1 모델 라벨 override (파인튜닝 켜졌을 때)

`apply_model_label_override(model_label, sentence, field=None)`(`:1436`, 13_03 Track2)는 모델 출력 위에 얹는 **좁은 고정밀** 교정이다.

- 허용: 모델이 명백 긍정을 부정으로 본 것 등을 **부→긍은 하지 않는다** — 그건 override로 안전 교정 불가라 **재학습(Track1) 몫**(`:1452`).
- 필드신호 override(무서술어 단편→필드극성)는 **폐기**됨: 모델이 필드 프리픽스로 이미 내장(`:1448`). [[project_override_bypass_is_correct]] 참조.

> ⚠️ **규칙 수정 절대 원칙**: 어떤 분기를 추가·변경하든 **장점/단점 코퍼스 양쪽 적대셋**으로 긍↔부 0을 검증하고(한쪽만 보면 거짓 자신감), 그룹 단위 일치율로 감사한다. 문장 두더지잡기 금지.

---

## 3.4 사람 보정 (corrections) — 최종 권위

- 저장 위치: `evaluations.sentiment_corrections` 컬럼(TEXT JSON, 스키마 v4에서 추가 — [04 문서](04-data-layer.md)).
- 로드: `load_...corrections`가 `SELECT id, sentiment_corrections FROM evaluations WHERE employee_id=?`로 읽는다(`:2165-2172`).
- **키잉 = `_db_id`**: `evaluation_id`는 **중복될 수 있으므로** 보정값 키로 쓰지 않는다. 고유한 DB row `id`를 `ev_obj['_db_id']`에 실어(`:1766, 1879, 1947`) `corrections_map.get(ev.get('_db_id'))`로 조회한다(`:2293, 2471`). [[project_eval_id_not_unique]]
- 우선순위: corrections가 있으면 규칙·모델 출력을 덮어쓴다(사람 라벨이 정본).

---


---pb---

# 4 데이터 계층


> **핵심**: 단일 SQLite(`.sessions/deploy_sessions.db`, WAL)에 모든 상태를 두고, 접근은 `deploy_session_service._get_conn()` 하나로 통일한다. 스키마는 `schema_version` 테이블로 버전 관리하며 부팅 시 자동 마이그레이션한다.
> **기준 버전 / 최종 확인일**: v1.1.0 · 2026-07-22 (commit `7b106b5`)

---

## 4.1 저장소 구성

| 저장소 | 위치 | 내용 | 배포 |
|--------|------|------|------|
| 운영 DB | `.sessions/deploy_sessions.db` (SQLite, WAL) | 세션·평가·배치·갤러리·욕설·취득문장 | **제외**(런타임 생성) |
| 런타임 설정·매핑 | `src/configs/` | 매핑(`mappings/`)·가명 매핑(`pseudonym_mappings.enc`)·불용어·가중치 | 포함 |
| 산출물 | `outputs/`, `processed_data/` | 워드클라우드 PNG·배치 중간물 | **제외** |

- 연결 헬퍼: `_get_conn()`(`deploy_session_service.py:12`) — `PRAGMA journal_mode=WAL` + `row_factory=sqlite3.Row`.
- **DAO 단일 진입**: `batch_work_order_service` 등 다른 서비스도 이 헬퍼(`_get_conn`/`_init_db`)를 재사용해 순환 임포트·중복 초기화를 피한다(`batch_work_order_service.py:12`).

> ⚠️ **앱 설정과 DB는 한 쌍**: 앱은 `.sessions` DB와 `src/configs` 매핑을 함께 읽는다. 둘을 교체할 땐 **한 쌍으로 함께 교체 + 서버 재시작**한다. [[project_db_mapping_pair_swap]]

---

## 4.2 주요 테이블 (`_init_db()` DDL, `deploy_session_service.py:20-131`)

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

### 4.2.1 evaluations 컬럼 (`:80-93`)

```
id INTEGER PK AUTOINCREMENT | employee_id TEXT NOT NULL (FK) | evaluator_id TEXT
evaluation_date TEXT | batch_id TEXT | data TEXT NOT NULL | fingerprint TEXT
created_at TEXT | sentiment_corrections TEXT DEFAULT '{}'  (← 스키마 v4 추가)
```

- **`evaluation_id`는 고유하지 않다** → 감정 보정은 DB row `id`(=`_db_id`)로 키잉한다([03 문서](03-emotion-engine.md) §4). [[project_eval_id_not_unique]]
- 중복 방지는 `UNIQUE(employee_id, fingerprint)`. 실데이터 감사에서 중복률이 높았으므로(≈62.7%, [[project_prod25_audit]]) 집계 시 중복제거를 전제한다.
- ⚠️ `evaluation_date`는 int(예: 2025)로 들어올 수 있어 연/월 행필터가 탈락하는 버그가 있었다 → `_get_eval_field_value`(`perspective_service.py:1602`)에서 str 정규화. [[project_eval_date_int_filter_bug]]

---
---pb---

## 4.3 스키마 마이그레이션 (`_apply_schema_migrations()`, `:137`)

부팅 시 `schema_version`을 보고 누락 버전만 순차 적용한다. 확인된 변경 예:

| 버전 | 변경 | 근거 |
|------|------|------|
| v1 | 초기(gallery_entries·employees·evaluations) | `:129-130` |
| v4 | `evaluations`에 `sentiment_corrections TEXT DEFAULT '{}'` 추가(문장 단위 감정 override) | `:182-188` |
| (추가) | `acquired_sentences`에 `kote_pos/kote_neg/kote_neutral/override_score/source_kind` 컬럼 | `:254-258` |
| (추가) | `deploy_sessions`에 `started_at` | `:275` |

> **새 테이블/컬럼을 추가할 때**: `_init_db()`의 DDL(신규 설치용)과 `_apply_schema_migrations()`의 버전 분기(기존 DB 업그레이드용) **양쪽**에 추가한다. 한쪽만 넣으면 신규/기존 환경 중 하나가 깨진다.

---

## 4.4 부팅 자동 마이그레이션 (`web/app.py:125-126`)

`main()`이 `deploy_session_service._auto_migrate_evaluations()`(`:329`)를 호출 — DB `evaluations`가 비어 있으면 레거시 `users/*.json`을 테이블로 1회 이전한다. `_auto_migrate_manifest()`(`:307`)도 함께 존재. 이미 데이터가 있으면 건너뛴다(멱등).

---

## 4.5 가명화 데이터 취급

- 가명화 대상은 `target_employee_id`만. 가명 텍스트는 **DB·판정 패킷에만** 두고, 그 외는 원데이터로 다룬다. 이중 가명화 금지(멱등). [[project_pseudonymization_scope]]
- 가명 매핑은 `src/configs/pseudonym_mappings.enc`(암호화). 역가명은 `pseudonym_manager.py`(`src/modules/`)가 담당.
- `plans/`는 배포 제외 폴더이며 학습 데이터(가명)는 **이 폴더 외에 두지 않는다**(유출 방지, CLAUDE.md).

---


---pb---

# 5 빌드·배포


> **핵심**: 배포는 `deploy/build_deploy.ps1` 하나로 한다. 빌드 매 단계가 **VERSION.json을 현재 모델로 재생성**하는 것이 정본 규칙(모델 교체 후 미갱신 사고 방지). 잔재 소스(`build/`·`*.egg-info`)와 런타임 폴더는 반드시 제외한다.
> **기준 버전 / 최종 확인일**: v1.1.0 · 2026-07-22 (commit `7b106b5`)
> **절차 상세 정본**: [`project_wordcloud/deployment.md`](../../deployment.md)

---

## 5.1 두 가지 배포 모드 (`build_deploy.ps1`)

| 모드 | 실행 | 산출물 | 내용 |
|------|------|--------|------|
| 소스 전용(기본) | `.\deploy\build_deploy.ps1` | `wordcloud-project.zip` | 앱 소스만(제외 규칙 적용) |
| 패키지 전체 | `.\deploy\build_deploy.ps1 -Package` | `wordcloud-internal/` (+zip) | runtime(Python) + **model/** + driver + source + `start.bat` |

- `-Package`는 base Python `Lib`(site-packages 제외)를 복사하고(`:138`), `model/`을 동봉하며, 실행용 `start.bat`을 생성한다(`:192-212`). `start.bat`은 `python -m web.app`으로 서버를 띄운다.

---

## 5.2 배포 제외 목록 (`:34-41`) — 잔재·런타임·비밀 반입 방지

`$ExcludeDirs`:
```
venv, __pycache__, .git, .sessions, doc, vendor_python_pkgs, logs, temp,
node_modules, deploy, .pytest_cache, inputs, scripts, .opencode, .clinerules,
failed, plans, default, outputs, processed_data,
build, *.egg-info        ← setup.py 빌드 잔재(옛 소스 사본 반입 방지)
```
`$ExcludeFiles`:
```
*.pyc, .gitignore, CACHEDIR.TAG, README.md, mermaid.min.js,
.env, *.jsonl, *.zip, flask_err.txt, flask_out.txt
```

> ⚠️ **잔재 소스 트랩**: 과거 `build/`·`wordcloud-source/`(옛 사본)이 반입돼 구버전이 배포되는 사고가 있었다. 정본은 **이 스크립트가 새로 만든 zip**이며, 워킹트리에 미커밋 규칙이 남아 있지 않은지 확인한다. [[project_deploy_gap_worktree_stale_source]] · `.env`는 제외 목록에 있으므로 비밀키가 패키지에 들어가지 않는다.

---
---pb---

## 5.3 VERSION.json 동기화 (배포 정본)

빌드 시작 시 스크립트가 `scripts/gen_version.py`를 실행해 VERSION.json을 **현재 `model/hr_sentiment_finetuned` 기준으로 재생성**한다(`:57-80`, "항상 이 빌드 단계가 정본으로 만든다").

`gen_version.py`(`scripts/gen_version.py`)가 기록하는 값:

| 필드 | 산출 | 근거 |
|------|------|------|
| `system_version` | 고정 `1.1.0` | `:71` |
| `model_version` | 고정 `hr-sentiment-v1.0` | `:72` |
| `model_sha256` | `model/hr_sentiment_finetuned/model.safetensors`의 SHA-256(없으면 `-`) | `:43-55` |
| `model_trained` | 위 파일 mtime 날짜 | `:58-66` |
| `source_commit` | `git rev-parse --short HEAD` | `:30-40` |
| `build_date` | UTC ISO8601 | `:76` |

- 무결성 대조: 런타임에 `hr_sentiment` 싱글톤이 로드 시 디스크 가중치 sha256을 기록(`hr_sentiment.py:57-59`)하고, `version_service`가 **선언(VERSION.json)·디스크·메모리 3자**를 대조해 "파일 교체 후 서버 미재시작"을 버전 모달에서 탐지한다.

> 🔴 **모델을 교체했다면**: 반드시 `gen_version.py` 재생성 + 패키지 동봉 + **서버 재시작**. 안 하면 모달 학습일·무결성이 불일치한다. [[project_version_json_deploy_gap]]

---

## 5.4 배포 후 확인 체크리스트

1. `-Package` zip 안에 `model/hr_sentiment_finetuned/`가 포함됐는가.
2. VERSION.json의 `model_sha256`·`model_trained`가 실제 모델과 일치하는가(빌드 로그 `VERSION.json OK …` 확인, `:80`).
3. 잔재 폴더(`build/`, `*.egg-info`, 옛 소스 사본)가 zip에 없는가.
4. `start.bat` 실행 → 서버 기동 후 버전 모달에 무결성 경고가 없는가.

> 배포 패키지 정합성 점검은 `deploy-verifier` 에이전트의 담당 영역이다(빌드 산출물 포함/제외 대사).

---


---pb---

# 6 배치 처리


> **핵심**: 약 **1.9만명** 규모의 대량 처리를 청크 수집 → 직원별 처리 → 요약으로 수행하고, 진행 상황을 **작업서(Work Order)** 로 DB에 영구화해 중단 시 Resume한다. 추적 로직은 **O(n) 이하**(O(n²) 금지)를 지킨다.
> **기준 버전 / 최종 확인일**: v1.1.0 · 2026-07-22 (commit `7b106b5`)

---

## 6.1 구성 요소

| 파일 | 책임 |
|------|------|
| `src/services/batch_processor.py` | 대규모 배치 실행 오케스트레이션(청크 수집→직원 처리→요약)·체크포인트 |
| `src/services/batch_work_order_service.py` | 작업서(설정 스냅샷 + 진행) 영구화·Resume 지원 |
| `batch_service.py` · `batch_manager.py` · `batch_events.py` · `batch_staging.py` | 오케스트레이션·진행 이벤트·staging DB |
| `src/routes/batch_routes.py` | `/api/batch` 실행·진행·Resume API |

- 규모 제약: 배치 대상 약 1.9만명. 추적 자료구조는 선형 이하로 유지한다. [[project_batch_scale_19k]]
- **dev 환경은 배치 실행 불가**(원데이터 내부 전용), dev에는 CSV만 반입한다. [[project_dev_no_batch_csv_only]]

---

## 6.2 작업서(Work Order) 생명주기

`batch_work_order_service.py`가 관리하는 상태 전이:

```
create_work_order        → status='running'   (설정 스냅샷 저장, items 초기화)   :30
update_work_order_progress→ 헤더 카운트 갱신(진행/성공/실패/행수)                :70
add_completed_employees  → 완료 직원 items append (INSERT OR IGNORE, O(델타))    :92
complete_work_order      → status='completed'                                    :123
fail_work_order          → status='failed' (전체 중단 시만; 직원 단위 오류 아님) :139
```

- **완료 직원 목록은 별도 items 테이블**(`batch_work_order_items`, PK=(batch_id, employee_id))에 1직원 1행으로 append한다. JSON 배열 통째 재기록을 피해 수만 명에서도 **O(델타)**를 보장한다(`:92-107`).
- Resume 대상 조회: `get_latest_incomplete_work_order()`(`:180`)는 `status IN ('interrupted','failed')`만 반환한다. `running`은 서버가 살아 처리 중이므로 제외한다.
- Resume skip 대상: `get_completed_employee_ids(batch_id)`(`:110`)로 이미 완료한 직원을 건너뛴다.

---
---pb---

## 6.3 배치 이력 표시 규약

- 배치 이력은 **배치 작업서(batch_id) 기준**으로 출력한다. 평가 중복제거로 실제 반영 건수가 0이어도 작업서 자체는 이력에 표시한다(작업이 있었음을 숨기지 않음). [[project_batch_history_by_workorder]]
- 게시판 목록: `get_all_work_orders(limit)`(`:166`) — `created_at DESC, id DESC` 최신순.

---

## 6.4 필드 무관 처리 주의

실데이터 감사에서 **필드(장점/단점) 무관 배치** 산출이 발견됐다([[project_prod25_audit]]). 감정 판정은 필드 프리픽스에 강하게 의존하므로([03 문서](03-emotion-engine.md) §1), 배치가 필드를 올바로 전달하는지가 정확도의 핵심이다. 재추론·대조 시 필드 프리픽스를 반드시 포함한다. [[project_batch_260709_model_gap]]

---

## 6.5 장시간 작업 중 UI 처리

배치처럼 오래 걸리는 작업 중에는 **전면 블러 오버레이 금지**. Nav·버튼만 비활성화하고 진행 상황(진행률·경과시간, `progress_time.py`)은 계속 보이게 한다. [[feedback_busy_disable_not_block]]

---


---pb---

# 7 파인튜닝 데이터 파이프라인


> **핵심**: 감정/리더십 작업·데이터 도착 시 `hr-kote-finetune` 데이터셋을 **append-only**로 누적하고(상시 RUNBOOK 절차), 사람 검증 gold를 승격해 재학습한다. 최우선 가치는 **긍↔부 오분류 방지**다. 이 폴더(`plans/`)는 배포 제외 — 학습 데이터는 여기서만 다룬다.
> **기준 버전 / 최종 확인일**: v1.1.0 · 2026-07-22 (commit `7b106b5`)
> **상시 절차 정본**: `plans/_datasets/kote_finetune/RUNBOOK.md` (완료 개념 없는 상시 문서)

---

## 7.1 데이터셋 레이아웃 (`wordcloud_project/plans/_datasets/kote_finetune/`)

| 경로 | 내용 |
|------|------|
| `emotion/emotion.jsonl` | 감정어 스트림(append-only, 라인당 1 JSON) |
| `leadership/leadership.jsonl` | 리더십 스트림(append-only) |
| `RUNBOOK.md` | 상시 절차 + 누적 로그(단일 진입점) |
| `README.md` | 폴더 규약 · **문서 지도** |
| `AUDIT_STANDARD.md` | 실배치 감사 재현 절차·시드·스크립트 |
| `ROADMAP.md` · `MODELING_LEVERS_PLAN.md` | 상시 현황·로드맵 |
| `scripts/` | `promote_gold.py`, `finetune_sentiment.py`, `ensemble_eval_r8_260708.py` 등 |

- **누적 방식**: append-only(기존 행 수정·삭제 금지, 정정은 동일 `id` 신규 리비전). [[project_kote_dataset_runbook]]
- **문서 배치 규약**: 상시 현황·로드맵은 `plans` 금지, `_datasets/kote_finetune`에 둔다(일회성 설계만 `plans/2026/…`). 헷갈리면 `README.md §문서 지도`부터 본다. [[project_dataset_doc_placement]] · [[project_dataset_doc_map]]

---

## 7.2 트리거 (RUNBOOK §1)

다음 중 하나면 RUNBOOK §2 체크리스트 수행:
- 감정어/리더십 **분석·알고리즘 강화** 작업(검토 1회 = gold 확정 1회로 겸함).
- 취득 코퍼스 **CSV 도착**(`data/*.csv` 반입).
- `acquired_sentences`에 **신규 행 적재**(핸드오프: `acquired_handoff.py`).

> ⚠️ **범위 임의 축소 금지**: 과거 범위를 "규칙 트랙 한정"으로 줄여 데이터셋 빌드를 생략한 사고(입력 36만, 기록 0)가 있었다. RUNBOOK §2-0은 1~6단계를 **한 명령**으로 묶어 재량 개입을 차단한다. [[feedback_execute_plan_no_descope]]

---
---pb---

## 7.3 라벨링 원칙 (긍↔부 안전)

- **개선요청 화행 = 부정**("~할 필요/키워야", 사용자 재정). 양가 성향 서술만 중립. [[feedback_improvement_request_is_negative_gold]]
- 무종결 단편·긍부 혼재·극성 불명확 → **중립**. 요청 표지 → 부정. 명확한 행위 서술만 → 긍정. [[feedback_incomplete_fragment_neutral]]
- 양가 업무태도(꼼꼼·철저·객관·소신)는 **기업 관점 긍정**, 명시 해악표지(고압적/편향/기복)가 붙을 때만 부정. 사생활·성격은 중립. [[feedback_ambiguous_trait_employer_lens]]
- 판정은 **블라인드 선판정 → 모델과 대조 → 불일치/저확신만 escalation**, 일치는 silver. 큐에 gold(원본 라벨)를 담지 말 것(미판정 큐가 숨는 버그). [[feedback_prefill_judgment_escalate_uncertain]] · [[project_group_review_gold_conflation]]
- 사전 라벨(코퍼스 y/s/e = KoTE 출력)은 정답이 아니다 → 문장 직접 재판정. [[feedback_distrust_prelabels_reanalyze]]

---

## 7.4 gold 승격 · 재학습

| 스크립트 | 용도 | 주의 |
|----------|------|------|
| `scripts/promote_gold.py` | 검증된 사람 라벨을 정식 gold 스트림에 적립 | positive gold 826 적립 완료(2026-06-30, D5). [[project_gold_promotion_d5]] |
| `scripts/finetune_sentiment.py` | 파인튜닝(**seed42, 개발용**) | A/B 무효 기준 — 배포 비교에 쓰지 말 것 |
| `scripts/ensemble_eval_r8_260708.py` | 재학습·평가(**배포 정본 경로**) | `--save-seed 45`가 배포 기준선 |

> 🔴 **재학습 정본 = `ensemble_eval_r8 … --save-seed 45`**. `finetune_sentiment.py`(seed42)는 개발용이라 배포 A/B에 무효다. [[project_retrain_path_seed45]]

- **다음 이득 지점**: 쉬운 silver 증강은 정확도를 오히려 떨어뜨린다(천장). 하드샘플 능동학습·사람분 승격(현재 stranded 라벨 다수 미반영)이 다음 수. [[project_finetune_data_ceiling]] · [[project_training_promotion_gap]]
- **진짜 어려운 클래스는 중립**(긍↔부 아님): 모델은 중립→긍, 규칙은 중립→부로 파괴하므로 사람 라벨이 정본. [[project_neutral_is_the_hard_class]]
- 신규 그룹은 정서가 아니라 **화행**(개선요청·평가회피·역량서술), 기본 극성 neutral. [[project_finetune_groups_are_speechacts]]

> **데이터셋 작업 위임**: 이 파이프라인의 실행자는 `dataset-curator` 에이전트이며, RUNBOOK §0의 "핵심 엔지니어" 역할(가드레일 내장)로 일한다. [[feedback_dataset_core_engineer_role]]

---


---pb---

# 8 개발 환경·테스트·트러블슈팅


> **핵심**: Python 3.10 + Flask, 로컬 실행은 `python -m web.app`. 모델(`model/`)은 `wordcloud_project`의 형제 폴더에 둔다. **서버는 사용자 허락 없이 실행하지 않는다**(안내만).
> **기준 버전 / 최종 확인일**: v1.1.0 · 2026-07-22 (commit `7b106b5`)

---

## 8.1 런타임·의존성

| 항목 | 값 | 근거 |
|------|-----|------|
| Python | 3.10 (`.pyc` cpython-310 확인) | `pyproject.toml`, `__pycache__/*.cpython-310` |
| 웹 | Flask (블루프린트 12개) | `web/app.py` |
| ML | `torch`, `transformers`, `accelerate` 등 | `requirements.txt` |
| 형태소 | Kiwi / Okt | `src/modules/nlp_analysis.py` |
| 의존성 설치 | `pip install -r requirements.txt` (오프라인은 `vendor_python_pkgs/`) | `requirements.txt` |

- 모델 디렉터리(둘 다 `wordcloud_project`의 형제 `model/` 아래):
  - 베이스 KoTE: `../../model/kote_for_easygoing_people`(`settings.py:20`)
  - HR 파인튜닝: `../../model/hr_sentiment_finetuned`(`settings.py:26`)

---

## 8.2 로컬 구동 (안내 — 직접 실행 금지)

> ⚠️ **서버 무단 실행 금지.** 아래는 개발자가 **직접** 실행할 절차 안내이며, 문서 저자(AI)는 서버를 띄우지 않는다. 실행이 필요하면 사용자에게 `! python -m web.app` 형태로 요청한다. [[feedback_no_server_start]]

```
# (1) 가상환경·의존성
python -m venv venv && venv\Scripts\activate
pip install -r requirements.txt
# (2) 실행 (기본 127.0.0.1:5001)
python -m web.app
```

주요 환경변수(`src/config/settings.py`):

| 변수 | 기본 | 의미 |
|------|------|------|
| `FLASK_HOST` / `FLASK_PORT` | `127.0.0.1` / `5001` | 바인드(`:48-49`) |
| `FLASK_DEBUG` | `True` | 디버그(`:47`) |
| `USE_HR_SENTIMENT_MODEL` | `1`(on) | HR 파인튜닝 모델 사용(`:27`) |
| `SECRET_KEY` | `your_secret_key_here` | 세션 키 — **배포 전 교체**(`:52`) |
| `ADMIN_PASSWORD` | `admin1234` | 관리자 비번 — **배포 전 교체**(`:55`) |
| `PLANS_DIR` | `plans/2026` | Plans 보드 소스(`:61`) |

> `.env`는 배포 제외 목록(`build_deploy.ps1:41`)에 있으므로 비밀값이 패키지에 들어가지 않는다. 내부망 데스크톱 전용이므로 UI에 모바일/반응형은 고려하지 않는다. [[project_desktop_only_no_mobile]]

---
---pb---

## 8.3 자주 겪는 함정

| 증상 | 원인 | 대응 |
|------|------|------|
| 감정이 전부 규칙 폴백 | 모델 디렉터리 부재/로드 실패 → `predict_sentiments`가 `None` | `model_status()`(`hr_sentiment.py:136`)로 `dir_exists`·`load_failed` 확인 |
| 버전 모달에 무결성 경고 | 모델 파일 교체 후 **서버 미재시작**(디스크≠메모리 지문) | `gen_version.py` 재생성 + 서버 재시작. [[project_version_json_deploy_gap]] |
| `.bak` 파일 수정해도 반영 안 됨 | `*.py.bak`는 **임포트 경로에 없는 잔재** | 실제 로드되는 `.py`를 수정([02 모듈 지도](02-module-map.md) §1 주의) |
| 재추론이 배포본과 불일치 | 필드 프리픽스 누락 | `f'{field} 평가: {text}'` 규약 준수. [[project_batch_260709_model_gap]] |
| 특정 연/월 필터 시 전건 탈락 | `evaluation_date`가 int | `_get_eval_field_value` str 정규화. [[project_eval_date_int_filter_bug]] |
| 배포에 구버전 소스 | `build/`·옛 소스 사본 반입 | 새로 빌드한 zip이 정본. [[project_deploy_gap_worktree_stale_source]] |

---

## 8.4 디버깅 원칙

- 버그는 **증상 → 로그 → 재현**부터. 코드 존재는 원인이 아니며, 실제 파라미터로 재현해 게이트를 통과하기 전엔 수정하지 않는다(가설서 출발 금지). [[feedback_diagnose_from_symptom_not_hypothesis]]
- 로그 진단은 `STAGE`(예: `DB_LOAD`, `DB_LOAD_ALL`)부터 — `perspective_service.py`가 `request_id`·`stage`를 구조화 로깅한다(`:1763` 등).
- 테스트로 **완료(DN) 선언 금지**: 단위 테스트가 아니라 **실동작 검증** 후에만 DN, 그 전엔 PND + 체크리스트. [[feedback_dn_after_runtime_verify]]

---


---pb---

# 9 확장 포인트 / 주의


> **핵심**: 기능을 늘릴 때는 **공통 모듈·표준을 재사용**하고(새로 짓지 말 것), 감정 규칙은 **긍↔부 0** 계약 안에서만 손댄다. 표준 위반은 배포·정확도 사고로 직결된다.
> **기준 버전 / 최종 확인일**: v1.1.0 · 2026-07-22 (commit `7b106b5`)

---

## 9.1 기능을 추가할 때 (Where to plug in)

| 추가하려는 것 | 두는 위치 | 재사용할 공통 |
|---------------|-----------|---------------|
| 새 화면 | `web/templates/` + `src/routes/ui_routes.py` | 디자인 시스템 토큰([공통 UI 규칙](../../../../common/ui/common/design-system/00-overview.md)) |
| 새 API | 해당 도메인 블루프린트(`src/routes/*_routes.py`) → 서비스 | 계층 경계([01 아키텍처](01-architecture.md) §4) |
| 새 분석 모델 | `src/modules/` 싱글톤 | **KoTE는 `kote_shared.KoTEModel` 재사용**(재로드 금지, VRAM) |
| 새 테이블/컬럼 | `_init_db()` DDL + `_apply_schema_migrations()` 양쪽 | `_get_conn()` DAO([04 데이터 계층](04-data-layer.md) §3) |
| 새 수집 신호 | `defaultMetadataStructure`에 필드 추가 | 기존 매핑 UI가 처리 — 별도 셀렉터·예약키·자동감지 **짓지 말 것**. [[feedback_extend_metadata_structure_not_bespoke_ui]] |

- **KoTE 단일 로드 원칙**: `emotion_analysis`·`leadership_analysis`가 한 싱글톤을 공유한다(`emotion_analysis.py:53-59`). 새 모듈이 KoTE를 또 로드하면 VRAM 한도를 넘길 수 있다.
- **DAO 단일 진입**: 모든 SQLite 접근은 `deploy_session_service._get_conn()`을 거친다(직접 `sqlite3.connect` 금지).

---

## 9.2 표준 준수 (링크)

| 주제 | 정본 |
|------|------|
| 시간 처리(타임존·저장 포맷) | [`development/time-handling-rules.md`](../../../../common/development/time-handling-rules.md) |
| 필드명·네이밍 | [`development/field-naming-convention.md`](../../../../common/development/field-naming-convention.md) |
| DB/테이블/DDL 네이밍 | [`development/database-naming-standard.md`](../../../../common/development/database-naming-standard.md) |
| 레거시 보호(리팩토링 전) | [`core/01-legacy-protection.md`](../../../../common/core/01-legacy-protection.md) |
| 수정 전 백업 | [`core/18-backup-before-modify.md`](../../../../common/core/18-backup-before-modify.md) |
| 감정 규칙 상세 | [`project_wordcloud/modules/emotion-analysis.md`](../../modules/emotion-analysis.md) |

> 참조 경로는 확인일 기준 실존 확인분이다. 문서 구조가 바뀌면 상대 경로가 어긋날 수 있으니 파일명으로 재탐색하라.

---
---pb---

## 9.3 감정 규칙을 고칠 때 (가장 위험한 변경)

1. **긍↔부 0 계약**: 어떤 분기도 긍정↔부정을 직접 뒤집지 않는다. 규칙이 바꾸는 방향은 →중립 또는 한 방향뿐. [[project_sentiment_core_value]]
2. **양쪽 코퍼스 검증**: 장점/단점 양쪽 적대셋으로 검증한다(한쪽만 보면 거짓 자신감). [[feedback_validate_both_pos_neg_corpora]]
3. **그룹 단위 감사**: 문장 두더지잡기 대신 패턴 그룹별 일치율로 검증한다(`group_audit_*.py`). [[feedback_audit_by_group_not_sentence]]
4. **부→긍은 override로 고치지 않는다**: 모델이 명백 긍정을 부정으로 본 것은 **재학습(Track1) 몫**. 좁은 긍→중 규칙만 override로 얹는다. [[project_override_bypass_is_correct]]
5. **`_explain`과 본 함수 동기화**: `_sentence_sentiment_override_explain`와 `sentence_sentiment_override`의 분기·점수는 **완전히 동일**해야 한다(`perspective_service.py:1226`).

---

## 9.4 하지 말아야 할 것 (사고 예방 요약)

- ❌ 서버 무단 실행 · ❌ dev에서 배치 실행 · ❌ 원데이터 요청(내부망 매핑 UI로 in-place 수집). [[feedback_no_raw_data_build_ui_instead]]
- ❌ `plans/` 밖에 학습 데이터 저장 · ❌ append-only 스트림 수정/삭제.
- ❌ 배포 시 `build/`·옛 소스 사본 반입 · ❌ 모델 교체 후 VERSION.json 미갱신.
- ❌ 전면 블러 오버레이(장시간 작업) · ❌ 모바일/반응형 고려(데스크톱 전용).

---

## 9.5 관련 지침 진입점

- 프로젝트 나침반: `wordcloud_project/CLAUDE.md` → [`core/00-core.md`](../../../../common/core/00-core.md) 작업 유형 분류표
- 보고서/문서 공통규칙: [`core/16-report-writing.md`](../../../../common/core/16-report-writing.md)
- 배포 절차: [`project_wordcloud/deployment.md`](../../deployment.md)
- 데이터셋 상시 절차: `wordcloud_project/plans/_datasets/kote_finetune/RUNBOOK.md`

---

*개발 메뉴얼 끝. 운영 관점은 [운영자 메뉴얼](../../../../outputs/_transfer-msys/operator-manual/00-index.md) 참조.*
