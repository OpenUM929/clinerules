# 25. 프로젝트 온보딩 (타 프로젝트 적용 가이드)

> 이식할 때 프로젝트마다 바꾸는 파일은 **`project.json` 하나**여야 한다. 그 외를 손대야 한다면 공통/프로젝트 분리가 잘못된 것이다.

---

## Step 0. 사전 확인

| 확인 | 방법 |
|------|------|
| git 저장소인가 | `git -C <repo> rev-parse --show-toplevel` |
| 기존 `.clinerules` 가 있는가 | 있으면 Step 5(기존 프로젝트), 없으면 Step 1 |

## Step 1. 지침 저장소 연결

```
git -C <repo> submodule add <지침 저장소 URL> .clinerules
```

## Step 2. `project.json` 작성

저장소 루트에 생성. 스키마는 [`19-project-identity.md`](19-project-identity.md) §2.

`project_id` 는 소문자 케밥 3~20자, 저장소를 대표하는 최단 이름. [`../PROJECTS-REGISTRY.md`](../PROJECTS-REGISTRY.md) 에서 **중복 여부를 먼저 확인**한다.

## Step 3. 프로젝트 지침 폴더 생성

```
.clinerules/projects/<project_id>/README.md
```

`README.md` 는 프로젝트 나침반이므로 60줄 이하([`23-compass-rule.md`](23-compass-rule.md) CMP-2), 라우팅 표 중심(CMP-3).

## Step 4. 레지스트리 등록

[`../PROJECTS-REGISTRY.md`](../PROJECTS-REGISTRY.md) 의 등록 목록과 금칙어 표에 행을 추가한다 — **`이름`·`경로·구조` 두 분류 모두**(고유 폴더·파일·테이블명은 저장소를 직접 나열해 실재 확인분만). **등록하지 않으면 그 프로젝트의 이름도 구조도 `common/` 에 새어 들어간 채 린터를 통과한다.**

## Step 5. 기존 프로젝트 마이그레이션

| # | 작업 | 검증 |
|---|------|------|
| 5-1 | 기존 `.clinerules` 백업(`git bundle`) | 백업 경로 기록 |
| 5-2 | 정본 저장소와 차분 산출 → 이 프로젝트 고유분 추출 | 파일 목록 |
| 5-3 | 서브모듈 origin 을 정본으로 교체 | `git remote set-url` |
| 5-4 | 고유분을 `projects/<project_id>/` 로 재배치 | N-PRJ 준수 |
| 5-5 | `common/` 에 남은 타 프로젝트 문자열 제거 | 린터 `L2` 0건 |
| 5-6 | 링크 수리 | 린터 `K1` 0건 |

> 5-2 를 건너뛰지 말 것. 양쪽 저장소가 갈라져 있으면 한쪽에만 있는 문서와 더 새로운 내용이 존재한다. 목록 차집합과 내용 해시를 모두 확인한 뒤 처리한다.

## Step 6. 에이전트 정의 이관 (해당 시)

`.claude/agents/*.md` 를 **본문 수정 없이 그대로** 복사한다([`26-agent-definitions.md`](26-agent-definitions.md) AGT-7). 도메인 전용 정의는 그 도메인이 없으면 **제외**하고 제외 목록을 보고한다(AGT-10). 카탈로그 `README.md` 를 대상 구성에 맞게 갱신한다.

## Step 7. 검증

```
python .clinerules/tools/lint_guidelines.py
```

error 0건이어야 온보딩 완료. **옮기기 전에 사본으로 예행**하면 실패를 대상 저장소 밖에서 확인할 수 있다 — 임시 폴더에 `.clinerules`·`.claude/agents`·대상용 `project.json` 만 놓고 린터를 돌린다. 남는 `A3` error 가 곧 제외해야 할 도메인 전용 정의다.

## Step 8. 커밋

`.clinerules`(서브모듈) 먼저 커밋·푸시 → 상위 저장소에서 포인터 갱신 커밋. **두 커밋을 분리**한다.

---

## 서브모듈 공동 운영 규칙

여러 프로젝트가 같은 지침 저장소를 공유하므로:

| 규칙 | 내용 |
|------|------|
| 변경 전 pull | `common/` 을 고치기 전에 최신을 받는다 |
| 소규모 커밋 | 주제 단위로 나눠 충돌 범위를 줄인다 |
| `common/` 변경은 승격 심사 후 | [`24-common-criteria.md`](24-common-criteria.md) COM 통과 + 린터 통과 |
| 프로젝트 사정은 `projects/` 에서 | 공통을 자기 사정에 맞게 고치지 않는다 |

---

## 체크리스트

- [ ] `project.json` 작성 (필수 4키)
- [ ] `project_id` 중복 없음 → 레지스트리 등록 완료
- [ ] `.clinerules` 서브모듈 연결
- [ ] `projects/<project_id>/README.md` 작성 (60줄 이하)
- [ ] 루트 `CLAUDE.md` 에 0단계(project.json 확인) 포함
- [ ] `.claude/agents/` 복사 시 본문 무수정 · 도메인 전용 정의 제외
- [ ] `common/` 에 손대지 않음
- [ ] 린터 error 0건
- [ ] 서브모듈·상위 저장소 커밋 분리
