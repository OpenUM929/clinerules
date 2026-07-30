# 28. 에이전트 공통 0단계 (부팅 절차)

> **적용 대상 — 모든 서브에이전트 정의(`.claude/agents/*.md`).** 정의 *파일*의 작성 규약은 [26-agent-definitions.md](26-agent-definitions.md), 여기는 정의가 **실행될 때** 밟는 절차다.
>
> 정의는 프로젝트가 바뀌어도 그대로 쓰는 문서다([26](26-agent-definitions.md) AGT-7). 그러면 값은 실행 시점에 얻어야 하고, **그 얻는 절차가 정의마다 다르면 이식이 정의마다 다르게 깨진다.** 그래서 절차를 여기에 한 벌로 둔다.

---

## 1. 절차 — BOOT

| 조항 | 내용 | 실패 시 |
|------|------|---------|
| BOOT-1 | 저장소 루트 `project.json` 을 Read 해 `project_id`·`guideline`·`paths`·`entrypoint` 를 확정한다 ([19-project-identity.md](19-project-identity.md)) | 없으면 git 루트 폴더명으로 폴백하고 **폴백했음을 보고에 명시**. 둘 다 실패하면 멈추고 질문 |
| BOOT-2 | [00-core.md](00-core.md) 작업 유형 분류표에서 이번 작업 유형의 지정 문서를 찾아 읽는다 | 분류표에 없으면 추측하지 말고 사용자에게 유형을 묻는다 |
| BOOT-3 | `{{guideline.project_dir}}/README.md`(프로젝트 나침반)에서 대상 영역의 프로젝트 지침을 찾아 읽는다 | 없으면 건너뛰고 **건너뛴 사실을 보고** |
| BOOT-4 | `{{guideline.project_dir}}/domain-locks.md` 를 Read 해 도메인 점검 목록을 확보한다 ([26](26-agent-definitions.md) AGT-5) | 없으면 도메인 점검을 생략하고 **생략 사실을 보고**. 빈 표를 만들지 않는다 |
| BOOT-5 | **구조를 추측하지 않는다.** 폴더 계층·파일 경로·테이블명은 `paths.app_root` 아래를 Glob·Grep 으로 실측해 확인한다 | 실측 불가면 그 사실을 보고하고 진행 여부를 묻는다 |
| BOOT-6 | 보고에 **0단계에서 실제로 읽은 문서 목록**을 적는다 | — |

**BOOT-6 이 필요한 이유**: BOOT-3·BOOT-4 는 "없으면 건너뛴다". 건너뛴 것이 보고에 안 남으면, 지침이 없어서 생략된 점검과 지침을 어겨서 빠진 점검이 겉보기에 같아진다.

---

## 2. 값이 오는 곳

| 필요한 값 | 출처 | 정의 본문에 적어도 되는가 |
|-----------|------|---------------------------|
| 프로젝트 이름·식별자 | `project.json` `project_id`·`project_name` | ❌ ([26](26-agent-definitions.md) AGT-1) |
| 앱 루트·계획서 루트·배포 산출물 | `project.json` `paths.*` | ❌ — `{{paths.app_root}}` 등 플레이스홀더로 |
| 진입점 | `project.json` `entrypoint` | ❌ |
| 계층 구조(라우트·서비스·템플릿 폴더) | **실측**(BOOT-5) | ❌ ([26](26-agent-definitions.md) AGT-8) |
| 도메인 점검 목록·사고 이력 | `{{guideline.project_dir}}/domain-locks.md` | ❌ ([26](26-agent-definitions.md) AGT-9) |
| 역할·경계·절차·보고 형식 | 정의 본문 | ✅ — 프로젝트 무관한 것만 |

`project.json` 스키마와 플레이스홀더 표기(`{{키}}`)는 [19-project-identity.md](19-project-identity.md) §2·§3 이 정본이다.

---

## 3. 정의 본문에 적는 형태

정의는 절차를 재서술하지 않고 **이 문서를 가리킨다.** 각자 다르게 적으면 그 차이가 곧 이식 편차다.

```markdown
## 0단계
[`.clinerules/common/core/28-agent-bootstrap.md`](...) 의 BOOT-1~6 을 수행한다.
이 역할에 추가로 필요한 것: <해당 역할 고유 항목만>
```

추가 항목의 예 — 구현 역할이라면 "유사 기존 기능 1건을 계층 전체로 읽어 패턴 파악", 문서 역할이라면 "대상 문서 종류의 정본 양식 확정". **역할 고유가 아닌 것을 여기 적으면 중복이다.**

---

## 4. 위임 라우팅

어떤 요청을 어느 정의에 넘길지는 `.claude/agents/README.md`(카탈로그)가 정본이다([26](26-agent-definitions.md) §4). 이 문서는 **선택된 정의가 무엇을 먼저 읽는지**만 정한다.

작성 역할은 스스로 통과 판정하지 않는다 — 판정은 짝이 되는 검증 정의 또는 사용자가 한다([26](26-agent-definitions.md) AGT-6).

---

## 5. 검사

BOOT 절차는 실행 시점 행동이라 정적 린트 대상이 아니다. 린터가 보는 것은 정의 본문의 하드코딩(`A4`·`A6`·`A7`)과 참조 경로 실존(`A5`) 이며, **BOOT-1~6 을 실제로 밟았는지는 보고의 읽은 문서 목록(BOOT-6)으로 사람이 확인**한다.
