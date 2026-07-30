# Wordcloud Project — 프로젝트 나침반

> 🧭 **나침반 문서** — 내용을 담지 않고 위치만 가리킨다.
> 공통 규칙은 `common/core/00-core.md` 를 따른다. 이 문서는 **이 프로젝트 고유 사항**만 가리킨다.

---

## 🔴 최우선 규칙

| 주제 | 문서 |
|------|------|
| **PseudonymManager(가명 관리) — 절대 실수 금지** | [modules/pseudonym-manager.md](modules/pseudonym-manager.md) |
| **도메인 잠금 점검 — 코드·계획 검토 시 전항 확인** | [domain-locks.md](domain-locks.md) |

---

## 프로젝트 개요

| 항목 | 값 |
|------|-----|
| 백엔드 | Python + Flask |
| 핵심 모델 | KoTE (Korean Text Emotion) |
| 앱 루트 | `wordcloud_project/` (정본은 `project.json` 의 `paths.app_root`) |

---

## 영역별 문서

| 영역 | 위치 |
|------|------|
| 모듈(감정·리더십·NLP·욕설·반어·워드클라우드) | [modules/](modules/) |
| 라우트 | [routes/](routes/) |
| 서비스 | [services/](services/) |
| 템플릿·화면 | [templates/screen-domain.md](templates/screen-domain.md) |
| 배포 | [deployment.md](deployment.md) |
| 운영자·개발자 메뉴얼 | [operator-manual/DEVELOPMENT.md](operator-manual/DEVELOPMENT.md) |
| 시나리오 테스트 | [scenario-test_project.md](scenario-test_project.md) |

---

## 자주 여는 문서

| 작업 | 문서 |
|------|------|
| 비속어 필터 | [modules/profanity-filter.md](modules/profanity-filter.md) |
| 배치 처리 | [services/batch-processor.md](services/batch-processor.md) |
| 분석 서비스 | [services/analysis-service.md](services/analysis-service.md) |
| 감정 분석 규칙 | [modules/emotion-analysis.md](modules/emotion-analysis.md) |
