# 08. Guideline Modification (지침 추가/삭제/수정)

> 🧭 **나침반 문서** — 내용을 담지 않고 위치만 가리킨다.

---

## ⛔ 최우선 잠금 규칙

**`.clinerules/` 내 파일은 사용자가 명시적으로 "지침 수정해줘", "규칙 바꿔줘", "clinerules 업데이트해줘"라고 요청한 경우에만 수정한다.**

---

## 수행 주체 (2인 체제)

| 단계 | 담당 | 원칙 |
|------|------|------|
| 작성·개정 | `guideline-curator` 서브에이전트 | 공통/프로젝트 판정 근거를 남긴다 |
| 검증 | `guideline-reviewer` 서브에이전트 (읽기 전용) | 보고를 믿지 않고 원본·린터로 재집계 |

작성자가 스스로 통과 판정하지 않는다. 정의는 `.claude/agents/`.

---

## 하위 문서 위치

| 주제 | 문서 위치 |
|------|-----------|
| Plan Mode 행동 규칙 | [core/08-guideline-modification/01-plan-mode.md](08-guideline-modification/01-plan-mode.md) |
| 수정 요청 시 절차 | [core/08-guideline-modification/02-modification-procedure.md](08-guideline-modification/02-modification-procedure.md) |
| 문서 분리 기준 | [core/08-guideline-modification/03-document-separation.md](08-guideline-modification/03-document-separation.md) |
| 폴더 명칭 규칙 | [core/08-guideline-modification/04-folder-naming.md](08-guideline-modification/04-folder-naming.md) |
| 지침 수정 후 의무 절차 | [core/08-guideline-modification/05-post-modification.md](08-guideline-modification/05-post-modification.md) |
| 누락된 규칙 분석 및 새 지침 추가 절차 | [core/08-guideline-modification/06-missing-rules-analysis.md](08-guideline-modification/06-missing-rules-analysis.md)