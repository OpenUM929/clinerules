# 지침 문서 채번 대장

> 신규 문서는 이 대장의 **최대 번호 + 1** 로 채번한다. 파일 목록이 아니라 **이 대장**이 근거다.
> 삭제된 번호는 재사용하지 않는다(결번 영구 유지). 채번 절차는 [`common/core/22-doc-numbering.md`](common/core/22-doc-numbering.md) NUM-5.
>
> **순서**: ① 대장에 행을 먼저 추가(번호 선점) → ② 파일 생성 → ③ 나침반 라우팅 표에 링크 추가.

## 번호 대역

| 대역 | 용도 |
|------|------|
| `00` | 폴더 나침반 |
| `01`–`09` | 불변 규율 (신규 추가는 사용자 승인 필수) |
| `10`–`29` | 절차·산출물 규칙 (통상 신규는 여기) |
| `30`–`89` | 예비 |
| `90`–`99` | 폐기 예정(DEPRECATED) |

## 이동·결번 이력

| 구 번호·파일 | 신 번호·파일 | 사유 | 일자 |
|--------------|--------------|------|------|
| `core/02.hallucination-prevention.md` | `common/core/17-hallucination-prevention.md` | 번호 02 중복 해소 (NUM-7: 후행 추가분 이동, 최초 추가 2026-07-22) | 2026-07-28 |
| `core/15-backup-before-modify.md` | `common/core/18-backup-before-modify.md` | 번호 15 중복 해소 (NUM-7: 후행 추가분 이동, 커밋 `6abcce2`) | 2026-07-28 |
| `core/11-performance-optimization-plan.md` | `common/core/11-performance-optimization.md` | slug 길이 정리 (번호 유지) | 2026-07-28 |

> 위 3건 외 `common/core/` 전 파일은 2026-07-28 구분자 통일(점·언더스코어 → 하이픈)만 적용했고 번호는 유지했다.

## 번호 필수 구역 등록 현황

### `common/core/`

| NN | slug | 파일 | 상태 | 비고 |
|----|------|------|------|------|
| 00 | core | `common/core/00-core.md` | 활성 |  |
| 01 | legacy-protection | `common/core/01-legacy-protection.md` | 활성 |  |
| 02 | documentation | `common/core/02-documentation.md` | 활성 |  |
| 03 | workflow | `common/core/03-workflow.md` | 활성 |  |
| 04 | design-change | `common/core/04-design-change.md` | 활성 |  |
| 05 | testing | `common/core/05-testing.md` | 활성 |  |
| 06 | git-rules | `common/core/06-git-rules.md` | 활성 |  |
| 07 | recovery-rules | `common/core/07-recovery-rules.md` | 활성 |  |
| 08 | guideline-modification | `common/core/08-guideline-modification.md` | 활성 |  |
| 09 | question-rules | `common/core/09-question-rules.md` | 활성 |  |
| 10 | project-compass | `common/core/10-project-compass.md` | 활성 |  |
| 11 | performance-optimization | `common/core/11-performance-optimization.md` | 활성 |  |
| 12 | impact-analysis-report | `common/core/12-impact-analysis-report.md` | 활성 |  |
| 13 | requirements-clarification | `common/core/13-requirements-clarification.md` | 활성 |  |
| 14 | comment-log-removal | `common/core/14-comment-log-removal.md` | 활성 |  |
| 15 | schedule-rules | `common/core/15-schedule-rules.md` | 활성 |  |
| 16 | report-writing | `common/core/16-report-writing.md` | 활성 |  |
| 17 | hallucination-prevention | `common/core/17-hallucination-prevention.md` | 활성 |  |
| 18 | backup-before-modify | `common/core/18-backup-before-modify.md` | 활성 |  |
| 19 | project-identity | `common/core/19-project-identity.md` | 활성 |  |
| 20 | repo-layout | `common/core/20-repo-layout.md` | 활성 |  |
| 21 | project-isolation | `common/core/21-project-isolation.md` | 활성 |  |
| 22 | doc-numbering | `common/core/22-doc-numbering.md` | 활성 |  |
| 23 | compass-rule | `common/core/23-compass-rule.md` | 활성 |  |
| 24 | common-criteria | `common/core/24-common-criteria.md` | 활성 |  |
| 25 | project-onboarding | `common/core/25-project-onboarding.md` | 활성 |  |
| 26 | agent-definitions | `common/core/26-agent-definitions.md` | 활성 |  |
| 27 | document-output-standard | `common/core/27-document-output-standard.md` | 활성 |  |
| 28 | agent-bootstrap | `common/core/28-agent-bootstrap.md` | 활성 | 에이전트 공통 0단계(실행 절차). 정의 파일 규약은 26 |

### `common/core/00-core/`

| NN | slug | 파일 | 상태 | 비고 |
|----|------|------|------|------|
| 01 | global-rules | `common/core/00-core/01-global-rules.md` | 활성 |  |
| 02 | triggers | `common/core/00-core/02-triggers.md` | 활성 |  |
| 03 | plan-mode | `common/core/00-core/03-plan-mode.md` | 활성 |  |
| 04 | reference-verification | `common/core/00-core/04-reference-verification.md` | 활성 |  |

### `common/core/00-core/03-plan-mode/`

| NN | slug | 파일 | 상태 | 비고 |
|----|------|------|------|------|
| 01 | type-a-bugfix | `common/core/00-core/03-plan-mode/01-type-a-bugfix.md` | 활성 |  |
| 02 | type-b-feature | `common/core/00-core/03-plan-mode/02-type-b-feature.md` | 활성 |  |
| 03 | type-c-design | `common/core/00-core/03-plan-mode/03-type-c-design.md` | 활성 |  |
| 04 | type-d-refactor | `common/core/00-core/03-plan-mode/04-type-d-refactor.md` | 활성 |  |
| 05 | type-e-migration | `common/core/00-core/03-plan-mode/05-type-e-migration.md` | 활성 |  |
| 06 | type-f-recovery | `common/core/00-core/03-plan-mode/06-type-f-recovery.md` | 활성 |  |
| 10 | storage-naming | `common/core/00-core/03-plan-mode/10-storage-naming.md` | 활성 |  |
| 11 | status-and-index | `common/core/00-core/03-plan-mode/11-status-and-index.md` | 활성 |  |
| 12 | test-and-result | `common/core/00-core/03-plan-mode/12-test-and-result.md` | 활성 |  |
| 13 | fact-verification | `common/core/00-core/03-plan-mode/13-fact-verification.md` | 활성 |  |
| 14 | bugfix-gate | `common/core/00-core/03-plan-mode/14-bugfix-gate.md` | 활성 |  |
| 15 | atomization | `common/core/00-core/03-plan-mode/15-atomization.md` | 활성 |  |
| 16 | self-containment | `common/core/00-core/03-plan-mode/16-self-containment.md` | 활성 |  |
| 17 | execution-log | `common/core/00-core/03-plan-mode/17-execution-log.md` | 활성 |  |
| 18 | role-split | `common/core/00-core/03-plan-mode/18-role-split.md` | 활성 |  |
| 19 | link-graph | `common/core/00-core/03-plan-mode/19-link-graph.md` | 활성 |  |
| 20 | git-clinerules | `common/core/00-core/03-plan-mode/20-git-clinerules.md` | 활성 |  |
| — | — | `common/core/00-core/03-plan-mode/README.md` | 활성 | 무번호 허용(README/메타) |

### `common/core/03-workflow/`

| NN | slug | 파일 | 상태 | 비고 |
|----|------|------|------|------|
| 01 | precheck | `common/core/03-workflow/01-precheck.md` | 활성 |  |
| 02 | request-analysis | `common/core/03-workflow/02-request-analysis.md` | 활성 |  |
| 03 | debugging-lessons | `common/core/03-workflow/03-debugging-lessons.md` | 활성 |  |
| 04 | execution-steps | `common/core/03-workflow/04-execution-steps.md` | 활성 |  |
| 05 | post-guideline-change | `common/core/03-workflow/05-post-guideline-change.md` | 활성 |  |
| 06 | common-module-impact | `common/core/03-workflow/06-common-module-impact.md` | 활성 |  |
| — | — | `common/core/03-workflow/README.md` | 활성 | 무번호 허용(README/메타) |

### `common/core/04-design-change/`

| NN | slug | 파일 | 상태 | 비고 |
|----|------|------|------|------|
| 01 | scale | `common/core/04-design-change/01-scale.md` | 활성 |  |
| 02 | light | `common/core/04-design-change/02-light.md` | 활성 |  |
| 03 | standard | `common/core/04-design-change/03-standard.md` | 활성 |  |
| 04 | principles | `common/core/04-design-change/04-principles.md` | 활성 |  |
| 05 | checklist | `common/core/04-design-change/05-checklist.md` | 활성 |  |
| 06 | scenarios | `common/core/04-design-change/06-scenarios.md` | 활성 |  |
| — | — | `common/core/04-design-change/README.md` | 활성 | 무번호 허용(README/메타) |

### `common/core/06-git-rules/`

| NN | slug | 파일 | 상태 | 비고 |
|----|------|------|------|------|
| 01 | commit-rules | `common/core/06-git-rules/01-commit-rules.md` | 활성 |  |
| 02 | submodule | `common/core/06-git-rules/02-submodule.md` | 활성 |  |
| 03 | plan-mode-collect | `common/core/06-git-rules/03-plan-mode-collect.md` | 활성 |  |
| 04 | cr-trigger | `common/core/06-git-rules/04-cr-trigger.md` | 활성 |  |
| 05 | cr-id | `common/core/06-git-rules/05-cr-id.md` | 활성 |  |
| 06 | commit-message | `common/core/06-git-rules/06-commit-message.md` | 활성 |  |
| 07 | cr-template | `common/core/06-git-rules/07-cr-template.md` | 활성 |  |
| 08 | release-note-template | `common/core/06-git-rules/08-release-note-template.md` | 활성 |  |
| 09 | lessons | `common/core/06-git-rules/09-lessons.md` | 활성 |  |

### `common/core/06-git-rules/07-cr-template/`

| NN | slug | 파일 | 상태 | 비고 |
|----|------|------|------|------|
| 01 | basic | `common/core/06-git-rules/07-cr-template/01-basic.md` | 활성 |  |
| 02 | fp-estimation | `common/core/06-git-rules/07-cr-template/02-fp-estimation.md` | 활성 |  |
| 03 | detailed | `common/core/06-git-rules/07-cr-template/03-detailed.md` | 활성 |  |

### `common/core/08-guideline-modification/`

| NN | slug | 파일 | 상태 | 비고 |
|----|------|------|------|------|
| 01 | plan-mode | `common/core/08-guideline-modification/01-plan-mode.md` | 활성 |  |
| 02 | modification-procedure | `common/core/08-guideline-modification/02-modification-procedure.md` | 활성 |  |
| 03 | document-separation | `common/core/08-guideline-modification/03-document-separation.md` | 활성 |  |
| 04 | folder-naming | `common/core/08-guideline-modification/04-folder-naming.md` | 활성 |  |
| 05 | post-modification | `common/core/08-guideline-modification/05-post-modification.md` | 활성 |  |
| 06 | missing-rules-analysis | `common/core/08-guideline-modification/06-missing-rules-analysis.md` | 활성 |  |

### `common/core/10-project-compass/`

| NN | slug | 파일 | 상태 | 비고 |
|----|------|------|------|------|
| 01 | scan | `common/core/10-project-compass/01-scan.md` | 활성 |  |
| 02 | design | `common/core/10-project-compass/02-design.md` | 활성 |  |
| 03 | templates | `common/core/10-project-compass/03-templates.md` | 활성 |  |
| 04 | split-rule | `common/core/10-project-compass/04-split-rule.md` | 활성 |  |
| 05 | quality-checklist | `common/core/10-project-compass/05-quality-checklist.md` | 활성 |  |

### `common/core/10-project-compass/03-templates/`

| NN | slug | 파일 | 상태 | 비고 |
|----|------|------|------|------|
| 01 | main-guide | `common/core/10-project-compass/03-templates/01-main-guide.md` | 활성 |  |
| 02 | compass-guide | `common/core/10-project-compass/03-templates/02-compass-guide.md` | 활성 |  |
| 03 | detail-guide | `common/core/10-project-compass/03-templates/03-detail-guide.md` | 활성 |  |
| 04 | api-router | `common/core/10-project-compass/03-templates/04-api-router.md` | 활성 |  |
| 05 | component | `common/core/10-project-compass/03-templates/05-component.md` | 활성 |  |

### `common/core/15-schedule-rules/`

| NN | slug | 파일 | 상태 | 비고 |
|----|------|------|------|------|
| 01 | architecture | `common/core/15-schedule-rules/01-architecture.md` | 활성 |  |
| 02 | execution | `common/core/15-schedule-rules/02-execution.md` | 활성 |  |
| 03 | ui | `common/core/15-schedule-rules/03-ui.md` | 활성 |  |
| 04 | implementation | `common/core/15-schedule-rules/04-implementation.md` | 활성 |  |
| 05 | testing | `common/core/15-schedule-rules/05-testing.md` | 활성 |  |
| 06 | cautions | `common/core/15-schedule-rules/06-cautions.md` | 활성 |  |
| 07 | references | `common/core/15-schedule-rules/07-references.md` | 활성 |  |

### `common/core/17-hallucination-prevention/`

| NN | slug | 파일 | 상태 | 비고 |
|----|------|------|------|------|
| 01 | principles | `common/core/17-hallucination-prevention/01-principles.md` | 활성 |  |
| 02 | comparison-rules | `common/core/17-hallucination-prevention/02-comparison-rules.md` | 활성 |  |
| 03 | verification | `common/core/17-hallucination-prevention/03-verification.md` | 활성 |  |
| 04 | false-info | `common/core/17-hallucination-prevention/04-false-info.md` | 활성 |  |
| 05 | checklists | `common/core/17-hallucination-prevention/05-checklists.md` | 활성 |  |
| 06 | doc-drift | `common/core/17-hallucination-prevention/06-doc-drift.md` | 활성 |  |
| 07 | violation | `common/core/17-hallucination-prevention/07-violation.md` | 활성 |  |
| 08 | exceptions | `common/core/17-hallucination-prevention/08-exceptions.md` | 활성 |  |

---

## 번호 선택 구역

`common/development/`, `common/ui/`, `common/verification/`, `common/operator-manual/`, `projects/**` 는 사전(dictionary)형 폴더로 번호가 선택이다(NUM-3). 번호를 쓰는 경우 NUM-1 형식(`NN-<slug>.md`)을 지킨다. 이 구역은 대장 등재 대상이 아니다.
