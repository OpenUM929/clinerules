# 📌 Plan Mode

> 🧭 **나침반 문서** — 내용을 담지 않고 위치만 가리킨다.

Plan Mode 에서는 **읽기만** 한다. 실행은 사용자가 "수행"이라고 **명시적으로 요청**할 때까지 대기한다.
계획서는 파일 시스템에 **저장만** 하고 실제 코드 변경은 하지 않는다.
계획서를 안내할 때는 대화 마지막에 **파일 전체 경로와 파일명**을 함께 출력한다.

---

## 계획서 작성 규칙

| 주제 | 문서 |
|------|------|
| 저장 위치·폴더/파일명·연도 기준 | [03-plan-mode/10-storage-naming.md](03-plan-mode/10-storage-naming.md) |
| 상태 관리·수정 이력·`_index.md` | [03-plan-mode/11-status-and-index.md](03-plan-mode/11-status-and-index.md) |
| `test/`·`result/` 폴더 규약 | [03-plan-mode/12-test-and-result.md](03-plan-mode/12-test-and-result.md) |
| 함수·경로·설정 실측 확인(예측 금지) | [03-plan-mode/13-fact-verification.md](03-plan-mode/13-fact-verification.md) |
| 버그 계획서 — 증거 우선·원인 확정 게이트 | [03-plan-mode/14-bugfix-gate.md](03-plan-mode/14-bugfix-gate.md) |
| 요구사항 원자화 및 답변 대장 | [03-plan-mode/15-atomization.md](03-plan-mode/15-atomization.md) |
| 자기완결성 | [03-plan-mode/16-self-containment.md](03-plan-mode/16-self-containment.md) |
| 실행 로그와 상위 AI 확인 | [03-plan-mode/17-execution-log.md](03-plan-mode/17-execution-log.md) |
| 역할군 분리(저비용/고비용 AI) | [03-plan-mode/18-role-split.md](03-plan-mode/18-role-split.md) |
| 문서 간 연결(링크 그래프) | [03-plan-mode/19-link-graph.md](03-plan-mode/19-link-graph.md) |
| Git 커밋 시 `.clinerules` 취급 | [03-plan-mode/20-git-clinerules.md](03-plan-mode/20-git-clinerules.md) |

---

## 작업 유형별 표준 템플릿

[03-plan-mode/README.md](03-plan-mode/README.md) 의 공통 양식·유형 선택 기준을 먼저 읽고, 아래 유형 템플릿을 추가로 참조한다. 템플릿의 필수 섹션이 빠지면 지침 위반이다.

| 작업 유형 | 템플릿 |
|-----------|--------|
| A. 버그 수정/핫픽스 | [03-plan-mode/01-type-a-bugfix.md](03-plan-mode/01-type-a-bugfix.md) |
| B. 기능 개선/신규 기능 | [03-plan-mode/02-type-b-feature.md](03-plan-mode/02-type-b-feature.md) |
| C. 설계/아키텍처/데이터셋 | [03-plan-mode/03-type-c-design.md](03-plan-mode/03-type-c-design.md) |
| D. 리팩토링/성능 개선 | [03-plan-mode/04-type-d-refactor.md](03-plan-mode/04-type-d-refactor.md) |
| E. DB 마이그레이션 | [03-plan-mode/05-type-e-migration.md](03-plan-mode/05-type-e-migration.md) |
| F. 복구/롤백 | [03-plan-mode/06-type-f-recovery.md](03-plan-mode/06-type-f-recovery.md) |

---

## 관련 문서

| 주제 | 문서 |
|------|------|
| 지침 추가/삭제/수정 | [../08-guideline-modification.md](../08-guideline-modification.md) |
| 상위 나침반 | [../00-core.md](../00-core.md) |
