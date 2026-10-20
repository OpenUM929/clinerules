## Change Request

- CR ID        : REQ-2608-001
- 레파지토리   : wordcloud (root 저장소, `.claude/agents/`)
- 요청 유형    : docs
- 대상 스코프  : `.claude/agents/` (서브에이전트 정의 카탈로그)
- 작업 유형    : 비기능 작업 (documentation)
- 요청자       : user
- 요청 날짜    : 2026.08.10

---

### 지침 진행 과정

1. `project.json` Read → `project_id: wordcloud`, `guideline.project_dir: projects/wordcloud`, `paths.app_root: wordcloud_project`
2. `00-core.md` 분류표 → "Git 작업 · CR" → `06-git-rules.md` 및 하위 01·02·04·05·06·07(01-basic, 02-fp-estimation)·09 Read
3. `projects/wordcloud/domain-locks.md` Read (DL-1~DL-18) → 이번 변경은 소스 0행·md 전용이므로 코드 잠금(DL-1~DL-9) 해당 없음. **DL-9(원데이터 취급)만 실질 적용** → 아래 §커밋 제외 근거
4. CR ID 채번: `.clinerules/outputs/cr/` 39건 조회, 최신 `REQ-2607-004` → **`REQ-2608-001` 부여**(2608 대역 최초)
5. 변경 실측: `git status --porcelain -- .claude/agents/`, `git diff --stat`, 각 파일 절 제목 grep 으로 주장 검증(문서 자기서술 아닌 실제 절 존재 확인)

---

### 변경 요약 (1줄, 50자 이내)
> 검수·감사 에이전트에 거짓보고 방지 규율 추가 + 미추적 정의 10종 편입

### 변경 배경 / 이유
> 같은 유형의 오보고가 실제 2회 발생했다. ① 문서의 배너 문구를 검증 없이 옮겨 적었고 ② 그 정정본조차 취소선 유무만 보고 「반영됐다」로 판정해 또 틀렸다. 원인은 **문서가 자기에 대해 한 말을 원자료로 취급**한 것이다. 이를 에이전트 정의 수준의 게이트로 막는다.

### 변경 전 → 변경 후
- Before: 감사·검수 정의에 「수치는 원자료로 확인」은 있으나 **문서 자기서술을 증거에서 배제하는 조항이 없음**. 개정본을 볼 때의 파급 점검 항목 부재. 지적을 목록으로만 내고 종결.
- After : 증거 등급/증거 규율 게이트, 표시≠상태 4칸, 개수는 재현 명령+단위 병기, 개정 파급 감사항목(patent-auditor §4-K / report-auditor H), 지적 3분류(감사자 확정 / 작성자 판단 / 사용자 결정), 데이터 활용 히스토리 3종(`_FACTS.md` · `_분석데이터_출처대장_*.md` · `IMPROVEMENT_HISTORY.md`) 선행 열람 의무.

### 영향 범위
> **애플리케이션 소스 변경 0행.** 런타임·배포 산출물에 영향 없다. 영향은 서브에이전트 구동 시 절차뿐이다. `.claude/agents/` 는 배포 패키지 대상이 아니다.

---

### 작업 상세 내역 (파일별)

#### (1) 이번 개정분 — 거짓보고 방지 규율 (7파일)

| 순번 | 파일 경로 | 변경 유형 | 상세 내용 | 파일 mtime |
|------|-----------|-----------|-----------|-----------|
| 1 | `.claude/agents/patent-auditor.md` | 수정 | §3.5 증거 규율(3.5-1 증거로 쓰지 않는 것 / 3.5-2 표시≠상태 / 3.5-3 개수 규율), §4-K 개정 파급, §9-1 되던지기 상한, §2-1 데이터 활용 히스토리 3종 | 2026-08-10 |
| 2 | `.claude/agents/report-auditor.md` | 수정 | 증거 등급 게이트(표시≠상태·개수 규율·「반영됐다」 게이트), 감사항목 H 개정 파급, 회귀 점검을 재감사와 분리(라운드 상한 예외), 지적 3분류, 출처대장 표본 재검증 | 2026-08-10 |
| 3 | `.claude/agents/report-writer.md` | 수정 | 개정 규율 0~5 신설(문서 자체 규약 우선·표시로 때우지 않고 구값 교체+grep 잔존 0건·파급 자리 표·서수 상호참조 금지·개수 단위 병기), 데이터 활용 히스토리 3종, 0단계(BOOT) 및 정본 경로 갱신 | 2026-08-10 |
| 4 | `.claude/agents/one-paper-writer.md` | 신규 | 절차 0 새 판 발행 3종 세트(새 파일·구판 폐기 배너·포인터 전량 갱신), §3 수치는 상세본을 베끼지 않고 `_FACTS.md`·원자료에서 | 2026-08-10 |
| 5 | `.claude/agents/metrics-measurer.md` | 신규 | 「측정 1건 = 대장 2행」(`_FACTS.md` + 출처대장), 탐색 범위 기록 의무 | 2026-08-07 |
| 6 | `.claude/agents/plan-reviewer.md` | 신규 | Step 1 에 승계되기 쉬운 주장 3종(개수·행 범위 / 선행 문서의 결론 / 암묵 전제) 전건 재확인 | 2026-08-07 |
| 7 | `.claude/agents/README.md` | 수정 | 카탈로그 갱신(작성↔검증 짝 표 신설, `plan-reviewer`·`report-auditor`·`patent-auditor`·`one-paper-writer`·`metrics-measurer`·`paper-specialist` 등재), 데이터 활용 히스토리 3종 공통 안내 | 2026-08-07 |

> ⚠️ mtime 실측 결과 7건 중 **당일(08-10) 갱신은 4건**이고 3건(`metrics-measurer`·`plan-reviewer`·`README`)은 **08-07 갱신**이다. 같은 개정 묶음으로 다루되, 파일 타임스탬프상 별개 시점 작업임을 기록해 둔다.

#### (2) 기존 미커밋분 — 이번 세션에서 손대지 않음 (15파일)

| 구분 | 파일 | 상태 |
|------|------|------|
| 수정(9) | `api-builder.md` · `bug-diagnostician.md` · `cr-scribe.md` · `dataset-curator.md` · `deploy-verifier.md` · `fp-estimator.md` · `guideline-curator.md` · `plan-writer.md` · `sentiment-judge.md` · `ui-builder.md` | 직전 커밋 `3298626` 이후 남아 있던 0단계(BOOT) 정합·경로 갱신분 |
| 신규(6) | `client-acceptance-reviewer.md` · `code-reviewer.md` · `guideline-reviewer.md` · `guideline-rollout.md` · `paper-specialist.md` | 08-04 이전 작성된 미추적 정의 |

> 위 표의 「수정」은 10건이다(카탈로그 `README.md` 는 (1)에 계상). git 실측 합계 = **수정 12 + 미추적 10 = 22파일**. 요청서에 적힌 「수정 12 + 미추적 11 = 23」과 **미추적 1건이 어긋난다** — 실측값 10을 채택했다. 그 결과 「기존 미커밋분」도 요청서의 17이 아니라 **15**다.

**변경 코드 요약(핵심 조항):**
```markdown
# Before (report-writer.md — 개정 시 규율 없음)
## 공통 규칙 (모든 문서 예외 없음)
4. 집계값 vs 추정값 구분 명시. 추정치는 범위 표기.

# After (개정 규율 신설)
1. **표시로 때우지 않는다.** 취소선·「반영 완료」 배너·「미반영 N건」 고지를 붙이는 것은
   반영이 아니다. **구값을 실제로 교체**한 뒤 구값 문자열을 전문 grep 해 잔존 0건을 확인한다.
   표시만 남기면 다음 감사자가 그 표시를 사실로 옮겨 **거짓 보고**가 만들어진다(실제 2회 발생).
```

```markdown
# After (report-auditor.md — 실패 모드 2번을 정의 서두에 못 박음)
2. **문서의 자기서술을 원자료로 삼는다** — 배너·취소선·「반영 완료」를 인용해 문서의 오류를
   인증해 준다. 1번은 "못 찾았다"로 끝나지만 2번은 **없는 사실을 만들어 낸다.**
```

---

### 작업 유형 판정 근거

`06-git-rules/04-cr-trigger.md` 작업 유형 구분표 적용:

| 판정 항목 | 실측 | 결론 |
|-----------|------|------|
| 애플리케이션 소스(`wordcloud_project/`) 변경 | 0행 (커밋 범위에 미포함) | 기능 아님 |
| 변경 파일 확장자 | 전량 `.md` (에이전트 정의) | documentation |
| 런타임 동작 변화 | 없음 | feat/refactor 불성립 |

→ **비기능 작업 (documentation)**. FP 산정 대상 아님(`FP: -`), 공수는 실투입 시간(H).

### 공수

| 항목 | 산정 | 값 |
|------|------|-----|
| 이번 개정분(7파일) | 규율 조항 설계·기존 정의 반영·상호 정합 확인 | 약 3.0H **(추정 — 실측 계측 기록 없음)** |
| 기존 미커밋분(15파일) | 과거 세션 산출물, 이번 커밋에서는 편입만 수행 | 0H (본 CR 계상 제외) |
| 커밋 절차(범위 확정·실측·CR 작성) | — | 0.5H |
| **합계** | | **3.5H (추정)** |

> 추정임을 명시한다. 실투입 시간 로그가 없으므로 산출 분량(+395/−177행 개정, 신규 1,553행) 기반 역산이다.

---

### 커밋 메시지 (실제 적용본)

```
📝 docs REQ-2608-001: 검수·감사 에이전트 거짓보고 방지 규율 + 미추적 정의 10종 편입

이번 개정분 (7파일) — 거짓보고 2회 재발 방지
- patent-auditor: 3.5 증거 규율(자기서술 배제/표시!=상태/개수 단위 병기),
  4-K 개정 파급, 9-1 되던지기 상한, 2-1 데이터 활용 히스토리 3종
- report-auditor: 증거 등급 게이트, 감사항목 H 개정 파급,
  회귀 점검을 재감사와 분리(라운드 상한 예외), 지적 3분류
- report-writer: 개정 규율 신설(문서 자체 규약 우선/구값 실교체+grep 확인/
  파급 자리 동시 수정/서수 상호참조 금지/개수 단위 병기)
- one-paper-writer: 새 판 발행 3종 세트, 수치는 _FACTS.md 원자료에서
- metrics-measurer: 측정 1건 = 대장 2행(_FACTS.md + 출처대장), 탐색 범위 기록
- plan-reviewer: Step 1 승계되기 쉬운 주장 3종 전건 재확인
- README: 작성/검증 짝 카탈로그 갱신 + 히스토리 3종 공통 안내

기존 미커밋분 (15파일) — 이번 세션 미수정, 직전 커밋 3298626 논리 단위 마감
- 수정 10: api-builder, bug-diagnostician, cr-scribe, dataset-curator,
  deploy-verifier, fp-estimator, guideline-curator, plan-writer,
  sentiment-judge, ui-builder
- 신규 5: client-acceptance-reviewer, code-reviewer, guideline-reviewer,
  guideline-rollout, paper-specialist

애플리케이션 소스 변경 0행. 배포 산출물 영향 없음.

Refs: REQ-2608-001
FP: - | 공수: 3.5H | 작업유형: 비기능 (documentation)
```

---

### 커밋 제외 항목과 근거 (의도적 보류)

| 제외 대상 | 건수 | 근거 |
|-----------|------|------|
| `wordcloud_project/plans/2026/07/27_03_completion-report/` | 95 | 보고서가 스스로 「마스킹 전 원문이 남은 증적 파일 3종」으로 고지한 `blind_judged_400.jsonl` · `blind_sample_260727.json` · `score_evidence_260727.json` 과 비공개 별첨 `별첨A_비공개_예시원문_260731.md` 포함. **반출 범위가 미결 내부 결정(상세 §2-3 D-6)** 이고 git 이력은 되돌리기 어렵다 → 결정 전 미편입 (DL-9 원데이터 취급) |
| `wordcloud_project/plans/2026/07/27_02_judge-packet-patent/` | 21 | 상동 묶음 |
| `.clinerules` 서브모듈 포인터 · `CLAUDE.md` · `q.txt` · `wordcloud_project/VERSION.json` · `1.PNG` · 삭제된 구 plans 다수 | 다수 | 이번 논리 단위(`.claude/agents/`)와 무관. 원자적 커밋 원칙(1커밋 1주제) |
| 본 CR 보고서 자신(`.clinerules/outputs/cr/REQ-2608-001.md`) | 1 | `.clinerules` 는 서브모듈이며 이번 커밋 범위 밖으로 지정됨 → 서브모듈 커밋·SHA 갱신 모두 미수행. **서브모듈 워킹트리에 미커밋 상태로 남는다** |

---

### 공지용 요약

**[상세 내용]**
> 검수·감사 계열 서브에이전트 정의에 「문서가 자기에 대해 한 말은 증거가 아니다」를 게이트로 명문화했다. 배너·취소선·「반영 완료」 문구는 인용 대상이 아니라 검수 대상이며, 개수는 재현 명령과 카운트 단위를 함께 적고, 개정본을 볼 때는 파급 자리(파생 수치·분모·서수 참조·그림 번호·조사)를 전용 항목으로 점검한다. 함께 미추적 상태였던 에이전트 정의 10종을 추적에 편입해 직전 커밋이 시작한 논리 단위를 닫는다.

**[요약]**
> 에이전트 정의 22파일 편입. 거짓보고 2회의 원인(문서 자기서술을 원자료로 인용)을 정의 수준 게이트로 차단. 소스 변경 0행.
