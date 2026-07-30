# .clinerules — AI 지침 저장소

> 🧭 **나침반 문서** — 내용을 담지 않고 위치만 가리킨다.

---

## 진입 절차

| # | 행동 |
|---|------|
| 0 | 저장소 루트의 `project.json` 을 Read → `project_id`, `guideline.project_dir` 확정 |
| 1 | `common/core/00-core.md` 의 작업 유형 분류표 확인 |
| 2 | 분류표가 지정한 문서로 이동해 읽은 뒤 작업 시작 |

`project.json` 이 없으면 git 루트 폴더명으로 폴백하고 **폴백했음을 응답에 표시**한다. 둘 다 실패하면 작업을 멈추고 질문한다. → [`common/core/19-project-identity.md`](common/core/19-project-identity.md)

---

## 구역(zone)

| 구역 | 경로 | 담는 것 |
|------|------|---------|
| 공통 | `common/` | 모든 프로젝트에 적용되는 규칙. 프로젝트명 하드코딩 금지 |
| 프로젝트 | `projects/<project_id>/` | 해당 프로젝트 전용 규칙 |
| 산출물 | `outputs/` | CR 보고서 등 기록물(규칙 아님) |
| 도구 | `tools/` | 지침 린터 등 |

상세 → [`common/core/20-repo-layout.md`](common/core/20-repo-layout.md) · 격리 규칙 → [`common/core/21-project-isolation.md`](common/core/21-project-isolation.md)

---

## 메타 문서

| 문서 | 용도 |
|------|------|
| [`NUMBERS.md`](NUMBERS.md) | 채번 대장. 신규 문서 번호는 여기서 취한다 |
| [`common/PROJECTS-REGISTRY.md`](common/PROJECTS-REGISTRY.md) | 등록 프로젝트 목록(격리 검사 사전) |
| [`tools/README.md`](tools/README.md) | 린터 사용법 |

---

## 금지 사항

- `common/` 에 프로젝트명·프로젝트 고유 경로를 쓰지 않는다. 값이 필요하면 `{{project_id}}` 형식의 플레이스홀더를 쓴다.
- 다른 프로젝트의 `projects/` 폴더를 읽거나 수정하지 않는다.
- 이 저장소에는 **규칙 문서(md)** 와 그 규칙을 집행·생성하는 **도구**만 둔다. 애플리케이션 소스·바이너리·데이터는 금지.
