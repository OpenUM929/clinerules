# 20. 지침 저장소 레이아웃

> 임의의 지침 파일은 **경로만 보고** 공통인지 어느 프로젝트인지 판별할 수 있어야 한다.

---

## 1. 구역(zone)

```
.clinerules/
├── CLAUDE.md                  ← 저장소 안내 나침반
├── NUMBERS.md                 ← 채번 대장
├── common/                    ← 【공통 구역】
│   ├── PROJECTS-REGISTRY.md
│   ├── core/                  ← 작업 규율·절차
│   ├── development/           ← 코드 작성 표준
│   ├── ui/                    ← 화면·디자인 시스템
│   ├── verification/          ← 테스트·검증
│   └── operator-manual/       ← 인쇄·제출용 문서 작성 양식
├── projects/                  ← 【프로젝트 구역】
│   └── <project_id>/          ← 자기 프로젝트 1개만
│       └── README.md          ← 프로젝트 나침반 (필수)
├── outputs/                   ← 【산출물 구역】 규칙이 아닌 기록물
└── tools/                     ← 【도구 구역】
```

| 구역 | 담을 것 | 금지 |
|------|---------|------|
| `common/**` | 모든 프로젝트에 적용 가능한 규칙 | 프로젝트명·고유 경로·프로젝트 전용 예시 (→ `{{...}}` 플레이스홀더) |
| `projects/<id>/**` | 해당 프로젝트 전용 규칙·구조 문서 | 다른 프로젝트 참조 |
| `outputs/**` | CR 보고서 등 이력 기록 | 규칙 문서 |
| `tools/**` | 린터·빌드 스크립트 | 규칙 문서(사용법 README만 허용) |

---

## 2. 프로젝트 폴더 명칭 — 규칙 N-PRJ

| 조항 | 내용 |
|------|------|
| N-PRJ-1 | 경로는 `projects/<project_id>/`. `projects/` 라는 상위 폴더가 이미 성격을 나타내므로 **접두사를 덧붙이지 않는다** |
| N-PRJ-2 | `<project_id>` 는 `project.json` 의 `project_id` **값과 정확히 일치**. 축약·변형 금지 |
| N-PRJ-3 | 형식: `^[a-z][a-z0-9-]{2,19}$` |
| N-PRJ-4 | 한 저장소의 `projects/` 아래에는 **자기 프로젝트 폴더 1개만** 존재한다 |
| N-PRJ-5 | 프로젝트 폴더 최상위에 `README.md`(프로젝트 나침반) 필수 |
| N-PRJ-6 | 프로젝트 폴더 **내부**의 하위 폴더는 [`08-guideline-modification/04-folder-naming.md`](08-guideline-modification/04-folder-naming.md) 규칙(나침반 문서명 = 폴더명)을 따른다 |

> N-PRJ-1 과 `04-folder-naming.md` 의 "프로젝트 접두사 불필요"는 **같은 방향의 규칙**이다. 전자는 `projects/` 직하 폴더, 후자는 그 내부 분리 폴더를 대상으로 한다.

---

## 3. 신규 문서 배치 결정 — 규칙 PLACE

```
Q1. 이 규칙이 프로젝트가 바뀌어도 그대로 유효한가?
    ├─ 아니오 → projects/{{project_id}}/
    └─ 예 → Q2
Q2. 규칙 본문에 특정 프로젝트의 경로·이름·산출물명이 등장하는가?
    ├─ 예 → project.json 키로 뽑아낼 수 있는가?
    │        ├─ 예 → 플레이스홀더로 치환 후 common/
    │        └─ 아니오 → projects/{{project_id}}/
    └─ 아니오 → common/ 의 주제별 하위
```

공통 자격의 상세 판정 기준은 [`24-common-criteria.md`](24-common-criteria.md).

### common/ 주제별 하위 선택

| 하위 | 담는 것 |
|------|---------|
| `core/` | 작업 진행 방식·규율(워크플로우, 금지사항, 계획·보고 절차) |
| `development/` | 코드 작성 표준(네이밍, 시간 처리, SQL, 라이브러리, 스택 설계) |
| `ui/` | 화면·디자인 시스템 |
| `verification/` | 테스트·검증·체크리스트 |
| `operator-manual/` | 인쇄·제출용 문서 작성 양식 |

---

## 4. 검사

| 항목 | 린터 ID |
|------|---------|
| 구역 존재·미정의 최상위 폴더 없음 | `L5` |
| `projects/` 직하가 자기 프로젝트 1개 | `L4` |
