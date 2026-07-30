# 19. 프로젝트 식별 (project.json)

> 지침 문서는 프로젝트 고유값을 **담지 않는다**. 값은 저장소 루트 `project.json` 에 있고, 문서는 키를 참조한다.

---

## 1. 해석 순서 (추측 금지)

| 순위 | 방법 | 조건 |
|------|------|------|
| 1 | `<git 루트>/project.json` 의 `project_id` | 파일 존재 + JSON 파싱 성공 |
| 2 | **폴백** — git 저장소 루트 폴더명을 정규화(소문자, 공백·언더스코어→하이픈) | 1 실패 |
| 3 | **중단 후 질문** — "이 저장소의 `project_id` 는 무엇입니까?" | 1·2 모두 실패 |

폴백(2순위)을 사용했다면 **응답에 "폴더명 폴백으로 판별함"을 반드시 표시**한다. 조용히 넘어가면 오판을 잡을 수 없다.

폴더명을 1순위로 쓰지 않는 이유: 한 저장소 안에 유사 폴더가 여럿 존재할 수 있고(사본·배포본·워크트리), 폴더명 하나로는 `plans_root` 같은 부속 경로를 결정할 수 없다.

---

## 2. 스키마 (v1.0)

```json
{
  "schema_version": "1.0",
  "project_id": "example",
  "project_name": "표시용 이름",
  "aliases": ["ex"],
  "guideline": {
    "root": ".clinerules",
    "common_dir": "common",
    "project_dir": "projects/example"
  },
  "paths": {
    "app_root": "src",
    "work_root": "work",
    "plans_root": "work/plans",
    "cr_root": "work/cr",
    "deploy_artifact": "example.zip",
    "venv": "venv"
  },
  "entrypoint": "src/app.py"
}
```

| 키 | 필수 | 형식 | 의미 |
|----|------|------|------|
| `schema_version` | ✅ | `"1.0"` | 파서 호환 판단 |
| `project_id` | ✅ | `^[a-z][a-z0-9-]{2,19}$` | **식별자 정본**. 폴더명·검사·로그가 이 값을 쓴다 |
| `project_name` | ✅ | 문자열 | 사람이 읽는 이름(한글 가능). 식별에 쓰지 않음 |
| `aliases` | ⬜ | 문자열 배열 | 사용자가 부르는 다른 이름 |
| `guideline.root` | ✅ | 상대경로 | 지침 저장소 위치 |
| `guideline.common_dir` | ✅ | 상대경로 | `root` 기준 공통 지침 폴더 |
| `guideline.project_dir` | ✅ | 상대경로 | `root` 기준 프로젝트 지침 폴더. **`projects/<project_id>` 여야 한다** |
| `paths.*` | ⬜ | 상대경로 | 문서가 참조할 프로젝트 경로들 |
| `paths.work_root` | ⬜ | 상대경로 | 계획서·CR 등 진행 산출물을 담는 상위 폴더 |
| `paths.plans_root` | ⬜ | 상대경로 | 계획서 저장 위치. 통상 `{{paths.work_root}}/plans` |
| `paths.cr_root` | ⬜ | 상대경로 | CR 보고서·릴리즈 노트 저장 위치(프로젝트 저장소 소속 — `.clinerules/outputs/`가 아니다). 통상 `{{paths.work_root}}/cr` |
| `entrypoint` | ⬜ | 상대경로 | 앱 진입점 |

**모든 경로는 저장소 루트 기준 상대경로.** 절대경로(`D:\...`)는 다른 머신·워크트리에서 깨지므로 금지.

---

## 3. 플레이스홀더 문법

공통 문서는 프로젝트 값을 `{{키}}` 로 적는다.

| 표기 | 해소 |
|------|------|
| `{{project_id}}` | `project_id` 값 |
| `{{project_name}}` | `project_name` 값 |
| `{{guideline.project_dir}}` | `guideline.project_dir` 값 |
| `{{paths.plans_root}}` | `paths.plans_root` 값 |
| `{{paths.cr_root}}` | `paths.cr_root` 값 |

읽기 편의를 위해 **현 프로젝트에서의 해소값을 괄호로 병기**할 수 있다. 병기값은 참고이며 **정본은 언제나 `project.json`** 이다.

```
예) 계획서는 `{{paths.plans_root}}/YYYY/MM/` 아래 저장한다.
```

정의되지 않은 키를 쓰면 린터 `P4` 위반이다.

---

## 4. 수정 권한

`project.json` 은 **사용자가 요청할 때만** 수정한다. AI가 임의로 값을 고치면 §1의 설계 목적(수기 편집 제거)이 무너진다.

---

## 5. 검사

| 항목 | 린터 ID |
|------|---------|
| 파일 존재·파싱·`project_id` 정규식 | `P1` |
| `guideline.project_dir` == `projects/<project_id>` | `P2` |
| `paths.*` 실존 | `P3` |
| 플레이스홀더가 스키마 정의 키만 사용 | `P4` |
