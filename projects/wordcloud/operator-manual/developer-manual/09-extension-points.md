---
reportTheme: technical
---

# 확장 포인트 / 주의

↑ [목록으로](00-index.md)

> **핵심**: 기능을 늘릴 때는 **공통 모듈·표준을 재사용**하고(새로 짓지 말 것), 감정 규칙은 **긍↔부 0** 계약 안에서만 손댄다. 표준 위반은 배포·정확도 사고로 직결된다.
> **기준 버전 / 최종 확인일**: v1.1.0 · 2026-07-22 (commit `7b106b5`)

---

## 기능을 추가할 때 (Where to plug in)

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

## 표준 준수 (링크)

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

## 감정 규칙을 고칠 때 (가장 위험한 변경)

1. **긍↔부 0 계약**: 어떤 분기도 긍정↔부정을 직접 뒤집지 않는다. 규칙이 바꾸는 방향은 →중립 또는 한 방향뿐. [[project_sentiment_core_value]]
2. **양쪽 코퍼스 검증**: 장점/단점 양쪽 적대셋으로 검증한다(한쪽만 보면 거짓 자신감). [[feedback_validate_both_pos_neg_corpora]]
3. **그룹 단위 감사**: 문장 두더지잡기 대신 패턴 그룹별 일치율로 검증한다(`group_audit_*.py`). [[feedback_audit_by_group_not_sentence]]
4. **부→긍은 override로 고치지 않는다**: 모델이 명백 긍정을 부정으로 본 것은 **재학습(Track1) 몫**. 좁은 긍→중 규칙만 override로 얹는다. [[project_override_bypass_is_correct]]
5. **`_explain`과 본 함수 동기화**: `_sentence_sentiment_override_explain`와 `sentence_sentiment_override`의 분기·점수는 **완전히 동일**해야 한다(`perspective_service.py:1226`).

---

## 하지 말아야 할 것 (사고 예방 요약)

- ❌ 서버 무단 실행 · ❌ dev에서 배치 실행 · ❌ 원데이터 요청(내부망 매핑 UI로 in-place 수집). [[feedback_no_raw_data_build_ui_instead]]
- ❌ `plans/` 밖에 학습 데이터 저장 · ❌ append-only 스트림 수정/삭제.
- ❌ 배포 시 `build/`·옛 소스 사본 반입 · ❌ 모델 교체 후 VERSION.json 미갱신.
- ❌ 전면 블러 오버레이(장시간 작업) · ❌ 모바일/반응형 고려(데스크톱 전용).

---

## 관련 지침 진입점

- 프로젝트 나침반: `wordcloud_project/CLAUDE.md` → [`core/00-core.md`](../../../../common/core/00-core.md) 작업 유형 분류표
- 보고서/문서 공통규칙: [`core/16-report-writing.md`](../../../../common/core/16-report-writing.md)
- 배포 절차: [`project_wordcloud/deployment.md`](../../deployment.md)
- 데이터셋 상시 절차: `wordcloud_project/plans/_datasets/kote_finetune/RUNBOOK.md`

---
↑ [목록으로](00-index.md) · [← 이전: 08. 개발 환경·테스트·트러블슈팅](08-dev-setup-troubleshooting.md)

*개발 메뉴얼 끝. 운영 관점은 [운영자 메뉴얼](../../../../outputs/_transfer-msys/operator-manual/00-index.md) 참조.*
