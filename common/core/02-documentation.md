# 02. Documentation Reference Rules (v2)

## 문서 구조 이해 (CRITICAL - 혼동 금지)

- **공통 지침** (`.clinerules/docs/`): 모든 프로젝트에 적용되는 범용 규칙
  - `design/common/` - 공통 설계 원칙
  - `development/` - 공통 개발 표준 (코딩 컨벤션, 기술 스택, 환경 설정)
  - `ui/common/` - 공통 UI 가이드
  - `verification/` - 공통 검증/분석 절차 (테스트 전략, 코드 리뷰, 파이프라인 분석)
  - `core/` - 핵심 작업 규칙 (Git, 복구, 질문, 관리 페이지 등)
- **프로젝트 지침** (`docs/` 또는 `.clinerules/docs/project_name/`): 특정 프로젝트 전용 규칙
  - 프로젝트별 설계, UI 화면 정의, 도메인 규칙 등
- **00-core.md**: 나침반 역할만 함. 구체적 내용은 위 문서들에 있음
- **하위 문서들도 나침반 역할 병행**: 각 문서는 상위 문서의 구체화이며, 다시 다른 문서를 안내할 수 있음

### 충돌 우선순위 (신규)
공통 지침과 프로젝트 지침의 내용이 서로 다를 경우:
1. **프로젝트 지침이 공통 지침을 오버라이드한다** (프로젝트 특수성이 범용 규칙보다 우선).
2. 단, 오버라이드 시 프로젝트 지침 문서에 "왜 공통 규칙과 다른지"에 대한 근거를 1줄 이상 명시해야 한다. 근거가 없으면 공통 지침을 따른다.
3. 두 문서 모두에 근거가 없고 판단이 애매하면 추측하지 말고 사용자에게 확인한다.

### 문서 탐색 종료 조건 (신규)
"하위 문서가 다시 다른 문서를 안내"하는 구조에서 순환 참조나 무한 탐색을 막기 위해:
- 한 작업당 최대 **3단계**까지만 문서를 따라간다 (00-core.md → 유형별 문서 → 그 문서가 안내하는 문서, 여기까지).
- 3단계를 넘어가도 구체적 내용을 못 찾으면 탐색을 멈추고 사용자에게 "OO 문서를 찾지 못했다"고 알린다.

---

## 문서 읽기 원칙

> ⚠️ **모든 문서를 매번 전부 읽지 않는다. 작업 유형에 해당하는 문서만 읽는다.**
> 00-core.md 분류표가 어떤 문서를 읽을지 이미 안내한다. 그 외 문서는 읽지 않아도 된다.

---

## 작업 유형별 필수 문서 (해당 작업 시에만 읽기)

### 공통 — 모든 작업 시 필수
- `common/development/coding-standards.md` — 코딩 컨벤션
- `common/development/code-size.md` — 코드 크기 제한

### UI / 디자인 변경 시
- `common/ui/common/screen-domain.md` ← **자주 변경됨. 반드시 최신본 확인**
- `common/ui/common/layout-and-components.md`

### 백엔드 API / 데이터 작업 시
- `docs/design/api-design.md`
- `docs/design/database-design.md`

### 신규 기능 추가 / 아키텍처 변경 시
- `docs/design/system-design.md`
- `docs/design/architecture.md`
- `common/development/tech-stack.md`
- `common/development/setup.md`

### 테스트 / 코드 리뷰 시
- `common/verification/testing-strategy.md` - 테스트 전략
- `common/verification/code-review-checklist.md` - 코드 리뷰 체크리스트

### 메뉴얼 / 문서 작성 시
- `{{guideline.project_dir}}/operator-manual/DEVELOPMENT.md` - 운영자 메뉴얼 작성 규칙 및 템플릿

---

## 문서 읽기 판단 기준

| 상황 | 행동 |
|------|------|
| 00-core.md 분류표에 명시된 문서 | 반드시 읽는다 |
| 위 작업 유형별 표에 해당하는 문서 | 해당 작업 시 읽는다 |
| 그 외 문서 | 읽지 않아도 된다 (필요 시 사용자에게 확인) |
| 문서가 없거나 경로가 틀린 경우 | 추측하지 말고 사용자에게 알린다 |

---

## 문서 최신성 확인 (신규)

- `screen-domain.md`처럼 "자주 변경됨" 표시가 있는 문서 외에도, **작업 시작 전 해당 문서의 최종 수정일을 확인**하고 30일 이상 지났으면 사용자에게 "이 문서 기준으로 진행해도 되는지" 1회 확인한다.
- 계획서(plans/) 작성 시, **참조한 지침 문서 목록을 계획서 상단에 명시**한다 (예: `> 참조 문서: common/verification/testing-strategy.md`). 이는 나중에 지침이 바뀌었을 때 어떤 계획서가 영향받는지 추적하기 위함이다.

## 작업 유형 ↔ 요구사항 확인(13-requirements-clarification.md) 연결 (신규)

요구사항 확인 단계에서 작업 유형(UI/백엔드/신규기능/테스트/문서화)이 정해지면, 그 즉시 본 문서의 "작업 유형별 필수 문서" 표를 조회해 어떤 문서를 읽어야 하는지 확정한다. 요구사항 정의서의 "범위" 항목에 참조할 지침 문서를 함께 기록한다.
