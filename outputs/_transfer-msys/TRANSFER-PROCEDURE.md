# MSYS 이관 절차 — 실측 기준

> 작성 2026-07-28. 아래 수치·상태는 이 날짜에 두 저장소를 **직접 나열·비교해 실측**한 값이다.
> 일반 절차는 [`../../common/core/25-project-onboarding.md`](../../common/core/25-project-onboarding.md), 실행 주체는 `guideline-rollout` 에이전트.

---

## 1. 실측 상태

| 항목 | 값 |
|------|-----|
| 두 `.clinerules` 의 origin | **동일** (`feelmydream80-sys/clinerules`) |
| 공통 조상 | `b20787a` = **msys 의 HEAD** (wordcloud 가 앞섬) |
| `b20787a` 레이아웃 | 최상위 `core/` · `docs/` (구 레이아웃) |
| wordcloud 워킹트리 | 4구역 재편 **454건 미커밋** |
| msys 워킹트리 | HEAD 파일 238건 삭제 + `common/`·`projects/msys/` **미추적(untracked)** |

**모드는 C(마이그레이션)가 아니라 B(개정분 전파)에 가깝다** — 갈라진 것이 아니라 msys 가 뒤처져 있다. 다만 양쪽 다 미커밋이라 지금은 어느 쪽도 pull 로 받을 수 없다.

## 2. 차단 사항 (해소 전 이관 금지)

| # | 내용 | 위험 |
|---|------|------|
| B1 | msys 의 `projects/msys/` **168개 문서가 git 미추적**이다 | `.clinerules` 를 교체·체크아웃하면 **영구 소실**. 커밋 또는 저장소 밖 백업이 선행돼야 한다 |
| B2 | 이관본(`_transfer-msys/` 146개)은 msys 원본의 **상위집합이 아니다** | 덮어쓰면 아래 §3 목록이 사라진다 |
| B3 | wordcloud 의 재편이 미커밋 | 푸시 전에는 msys 가 받을 수 없다 |
| B4 | msys 에 `plans/` 폴더 없음 | `paths.plans_root` 실존 필요(린터 `P3`), 계획서 규약이 걸린다 |

## 3. 차집합 (B2 근거)

**msys 에만 있고 이관본에 없는 것** — 9개 실내용 문서 + `operator-manual-iso/` 28개:

```
build-completion-report-guideline.md
functional-point-assessment-guideline.md      ← fp-estimator 가 요구하는 정본
functional-point-validation-report.md
dao/{api-key-mngr-dao, popup-dao, sql-loader}.md
mapper/{grp-memo-mapper, mngr-sett-mapper}.md
services/{popup-service, spec-scraper-service}.md
utils/README.md
operator-manual-iso/**                        (28개)
```

**이관본에만 있는 것** — `operator-manual/` 재편분(탭 분할·`00-index`·`integrated-manual`) 14개 + `status-code-extension-guide.md`.

`operator-manual-iso/` ↔ `operator-manual/` 은 **같은 문서의 다른 판**이다. 표본 3건 비교 결과 이관본이 더 짧다(97→36, 135→74, 134→102줄). 어느 판을 정본으로 삼을지는 **사용자 판단 사항** — 자동 병합하지 말 것.

## 4. 순서 (바꾸지 말 것)

1. **B1 해소** — msys `projects/msys/` 를 백업하거나 커밋한다. 이것보다 앞서는 작업은 없다.
2. **B2 판정** — §3 차집합을 보고 어느 판을 남길지 사용자가 결정한다.
3. **wordcloud `.clinerules` 커밋·푸시** (서브모듈 먼저, 상위 포인터는 그다음).
4. **msys 에서 `.clinerules` 갱신** — 4구역 레이아웃 수신. `PROJECTS-REGISTRY.md` 와 `tools/lint_guidelines.py` 는 **한 쌍으로** 들어가야 한다(레지스트리만 가면 격리 검사가 무성으로 꺼진다).
5. **`projects/msys/` 복원** — 2번 결정에 따라 배치.
6. **`project.json` 작성** (§5) + `plans/` 생성.
7. **`.claude/agents/` 복사** — 본문 무수정. **도메인 전용 2종(`sentiment-judge`·`dataset-curator`)은 제외**한다.
8. **린터 error 0 확인** → `guideline-reviewer` 검증.

4번을 건너뛰고 `.claude/agents/` 만 옮기면 정의가 거는 `.clinerules/...` 참조가 전부 깨진 채 통과한다(`A5` 는 마크다운 링크를 보지 않는다).

## 5. `project.json` 초안 (msys 실구조 기준)

msys 는 **저장소 루트가 곧 앱 루트**다.

```json
{
  "schema_version": "1.0",
  "project_id": "msys",
  "project_name": "MSYS",
  "aliases": ["msys"],
  "guideline": { "root": ".clinerules", "common_dir": "common", "project_dir": "projects/msys" },
  "paths": {
    "app_root": ".", "plans_root": "plans", "scripts_root": "scripts",
    "deploy_artifact": "msys.zip", "venv": "msys_venv"
  },
  "entrypoint": "msys_app.py"
}
```

## 6. 예행 결과 (2026-07-28 실행)

임시 폴더에 `.clinerules` + `.claude/agents` + 위 `project.json` 만 놓고(=`projects/wordcloud/` 제거, `projects/msys/` 생성) 린터를 돌린 결과:

| 구성 | 결과 |
|------|------|
| 정의 16종 전부 | `error 2` — `sentiment-judge`·`dataset-curator` 의 `A3`(타 프로젝트 고유어 `kote`) |
| 도메인 전용 2종 제외 | **`error 0`** (warn 은 문서 길이 `C2` 34건 + 예행용 stub 2건) |

**바꾼 것은 `project.json` 과 `projects/<id>/` 뿐이다.** 공통 문서·에이전트 정의 본문은 한 줄도 고치지 않았다. 남은 `error 2` 는 결함이 아니라 설계된 신호다 — 도메인 전용 정의를 제외하라는 표시(AGT-10).
