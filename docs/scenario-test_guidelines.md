# 지침 시나리오 테스트 (Guidelines Scenarios)

**문서 위치**: `.clinerules/docs/scenario-test_guidelines.md`

---

## 시나리오 G-1: UI 변경 요청

### 상황
사용자: "배치 처리 페이지 디자인을 바꿔줘"

### 올바른 진행

| 단계 | 규칙 | 실행 내용 |
|------|------|----------|
| 1 | 00-core.md | 현재 프로젝트: `msys` 확인 |
| 2 | 작업 유형 분류 | "공통 UI/디자인" → 04.design-change.md |
| 3 | 04.design-change.md | docs/ui/common/screen-domain.md 참조 |
| 4 | msys | templates/screen-domain.md에서 파일 경로 확인 |
| 5 | 분석 | `templates/mngr_sett.html` 분석 |
| 6 | 계획 수립 | 사용자에게 예상 화면 제시 |
| 7 | 승인 후 구현 | 사용자 승인 후 코드 수정 |

### 결과
✅ msys 폴더의 문서를 통해 정확한 파일 경로 확인 가능

---

## 시나리오 G-2: 백엔드 API 문제

### 상황
사용자: "API에서 404 에러가 발생해"

### 올바른 진행

| 단계 | 규칙 | 실행 내용 |
|------|------|----------|
| 1 | 00-core.md | "기능 문제 분석/디버깅" |
| 2 | 03.workflow.md | pipeline-analysis.md 참조 |
| 3 | msys | routes/api-routes.md 확인 |
| 4 | 분석 | 엔드포인트 경로, 함수 로직 분석 |
| 5 | 원인 파악 | 프론트엔드 vs 백엔드 불일치 확인 |

### 결과
✅ msys/routes/ 문서로 정확한 엔드포인트 확인

---

## 시나리오 G-3: 모호한 요청

### 상황
사용자: "메타데이터 관련해서 확인할 거 있는데..."

### 올바른 진행

| 단계 | 규칙 | 실행 내용 |
|------|------|----------|
| 1 | 00-core.md | 요청 분석 |
| 2 | docs/core/question-rules.md | 구체적 파일 분석 후 안내 |
| 3 | msys | routes/mngr_sett_routes.md 또는 services/mngr_sett_service.md 제시 |
| 4 | 분석 | 해당 파일 확인 후 문제 파악 |

### 결과
✅ msys 폴더로 정확한 안내 가능

---

## 시나리오 G-4: 리팩토링 요청

### 상황
사용자: "batch_service.py 리팩토링 해줘"

### 올바른 진행

| 단계 | 규칙 | 실행 내용 |
|------|------|----------|
| 1 | 00-core.md | "리팩토링" |
| 2 | 01.legacy-protection.md | 기존 코드 보호 확인 |
| 3 | msys | services/dashboard-service.md 확인 |
| 4 | 분석 | 현재 구조, 함수 의존성 파악 |
| 5 | 계획 | 사용자에게 수정 계획 제시 |

### 결과
✅ msys/services/ 문서로 구조 파악 가능

---

## 시나리오 G-5: Git 작업 요청

### 상황
사용자: "커밋하고 태그 v2.1.0으로 생성해줘"

### 올바른 진행

| 단계 | 규칙 | 실행 내용 |
|------|------|----------|
| 1 | 00-core.md | "Git 작업" |
| 2 | 06.git-rules.md | 저장소 확인, 영향 범위 분석 |
| 3 | 실행 | git add → commit → tag 생성 |

### 결과
✅ git-rules.md 순수 참조로 해결 가능