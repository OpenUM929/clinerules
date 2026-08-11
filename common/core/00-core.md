# 🔴 00-Core (항상 최우선 적용)

> 🧭 **나침반 문서** — 내용을 담지 않고 위치만 가리킨다.
> 작업 유형 파악 → 분류표에서 찾기 → 지정 문서로 이동 → 읽고 시작. **추측 금지.**
> 현재 프로젝트는 저장소 루트 `project.json` 으로 확정한다 → [19-project-identity.md](19-project-identity.md)

---

## 작업 유형 분류표

| 작업 유형 | 이동할 문서 |
|-----------|-------------|
| **프로젝트 고유 작업 전반** | `{{guideline.project_dir}}/README.md` (프로젝트 나침반) |
| **🔴 계획서/기획서/설계서 작성** | [00-core/03-plan-mode.md](00-core/03-plan-mode.md) — 저장 위치·파일명 반드시 확인 |
| **비교/분석/현황 정리** | [17-hallucination-prevention.md](17-hallucination-prevention.md) — 원본 검증 필수 |
| **🔴 원자료 조사 · 수치 인용 · 세션 재개** | [17-hallucination-prevention/10-fact-ledger.md](17-hallucination-prevention/10-fact-ledger.md) — **파일 열기 전 `_FACTS.md` 부터.** 조사 결과는 즉시 적립 |
| **참조·링크·자산 검증** | [00-core/04-reference-verification.md](00-core/04-reference-verification.md) |
| **소스 수정 전 백업** | [18-backup-before-modify.md](18-backup-before-modify.md) |
| 리팩토링 | [01-legacy-protection.md](01-legacy-protection.md) FIRST |
| 문서 작성 가이드 | [02-documentation.md](02-documentation.md) |
| 백엔드 API · 기능 문제 분석/디버깅 | [03-workflow.md](03-workflow.md) |
| 공통 UI/디자인 | [04-design-change.md](04-design-change.md) |
| 테스트 | [05-testing.md](05-testing.md) |
| Git 작업 · CR | [06-git-rules.md](06-git-rules.md) |
| 복구/롤백 | [07-recovery-rules.md](07-recovery-rules.md) |
| **지침 수정/추가/삭제** | [08-guideline-modification.md](08-guideline-modification.md) — 사용자 요청 시에만 |
| 질문 규칙 | [09-question-rules.md](09-question-rules.md) |
| **프로젝트 분석/나침반 생성** | [10-project-compass.md](10-project-compass.md) |
| 성능 분석/최적화 계획 | [11-performance-optimization.md](11-performance-optimization.md) |
| 영향도 분석 보고서 | [12-impact-analysis-report.md](12-impact-analysis-report.md) |
| 요구사항 명확화 | [13-requirements-clarification.md](13-requirements-clarification.md) |
| 주석/로그 제거 | [14-comment-log-removal.md](14-comment-log-removal.md) |
| 스케줄 규칙 | [15-schedule-rules.md](15-schedule-rules.md) |
| **보고서/결과보고/완료보고** | [16-report-writing.md](16-report-writing.md) · 인쇄·제출 출력 규격 [27-document-output-standard.md](27-document-output-standard.md) |
| **프로젝트 식별 / project.json** | [19-project-identity.md](19-project-identity.md) |
| **지침 문서를 어디에 둘 것인가** | [20-repo-layout.md](20-repo-layout.md) → [24-common-criteria.md](24-common-criteria.md) |
| **프로젝트 간 지침 혼입 방지** | [21-project-isolation.md](21-project-isolation.md) |
| **문서 채번/파일명 · 개정 판번호** (지침·계획서·보고서·특허·메뉴얼 **전 문서 공통**) | [22-doc-numbering.md](22-doc-numbering.md) — 개정하면 NUM-9(RV-1~RV-5) 필수 |
| **나침반 문서 작성/분리** | [23-compass-rule.md](23-compass-rule.md) |
| **새 프로젝트에 지침 적용** | [25-project-onboarding.md](25-project-onboarding.md) |
| **에이전트 정의(`.claude/agents`) 작성/수정** | [26-agent-definitions.md](26-agent-definitions.md) |
| **에이전트 0단계 / 결과 검증·세션 종료 회고** | [28-agent-bootstrap.md](28-agent-bootstrap.md) 실행 0단계 · [29-agent-fit-review.md](29-agent-fit-review.md) 채택 전 검증·회고 |
| 시간 처리 | [../development/time-handling-rules.md](../development/time-handling-rules.md) |
| 필드명/네이밍 | [../development/field-naming-convention.md](../development/field-naming-convention.md) |
| 데이터베이스 / 테이블 / DDL | [../development/database-naming-standard.md](../development/database-naming-standard.md) |
| 서버 리로드/재시작 판단 | [../development/server-reload-guide.md](../development/server-reload-guide.md) |
| 스택 설계(아키텍처·API·DB) | [../development/design/system-design.md](../development/design/system-design.md) |
| UI 디자인 시스템 | [../ui/common/design-system/00-overview.md](../ui/common/design-system/00-overview.md) |
| **운영자 메뉴얼 작성/수정** | [../operator-manual/DEVELOPMENT.md](../operator-manual/DEVELOPMENT.md) |
| 공통 모듈 수정/추가 | Glob 으로 실제 경로 확인 후 상대 경로 계산 |
| 배포 패키지 생성 | `{{guideline.project_dir}}/deployment.md` |

## 하위 문서

| 문서 | 내용 |
|------|------|
| [00-core/01-global-rules.md](00-core/01-global-rules.md) | 전역 잠금 규칙 |
| [00-core/02-triggers.md](00-core/02-triggers.md) | 실행 트리거 |
| [00-core/03-plan-mode.md](00-core/03-plan-mode.md) | Plan Mode·계획서 규약 |
| [00-core/04-reference-verification.md](00-core/04-reference-verification.md) | 링크·자산 참조 검증 |
