# 도메인 잠금 점검 (wordcloud)

> 이 프로젝트의 **실제 사고 이력**에서 도출한 점검 목록. 에이전트 정의(`.claude/agents/*.md`)는 본문에 이 표를 복사하지 않고 이 문서를 Read 한다 → [`../../common/core/26-agent-definitions.md`](../../common/core/26-agent-definitions.md) AGT-5.
>
> 이 문서는 **무엇을 보는가**만 적는다. 규칙 상세는 각 행의 **정본** 문서에 있으며, 그 내용을 여기에 복사하지 않는다.
> 걸린 항목은 "해당 없음"으로 넘기지 말고 정본을 열어 확인한 뒤 보고한다. 해당 없음도 확인했다는 사실을 기록한다.

---

## 1. 코드·구현 잠금 (DL-1 ~ DL-9)

| # | 잠금 | 무엇을 보는가 | 심각도 | 정본 |
|---|------|---------------|--------|------|
| DL-1 | 가명화 범위 | `target_employee_id` 외 필드를 가명화하는가. 이미 가명인 값을 다시 가명화하는가(이중 가명화). 재실행이 멱등한가 | 높음 | [modules/pseudonym-manager.md](modules/pseudonym-manager.md) |
| DL-2 | 평가 키잉 | `evaluation_id` 로 감정 보정·매칭을 거는가. **이 값은 고유하지 않다** — DB row `id`(`_db_id`) 로 키잉해야 한다 | 높음 | [operator-manual/developer-manual/04-data-layer.md](operator-manual/developer-manual/04-data-layer.md) |
| DL-3 | 배치 복잡도 | 배치 대상 약 1.9만 명. 추적·중복 검사 자료구조가 O(n²) 인가 (O(n) 이하 유지) | 높음 | [operator-manual/developer-manual/06-batch.md](operator-manual/developer-manual/06-batch.md) |
| DL-4 | 감정 극성 | 규칙·모델 변경이 **긍정↔부정 오분류**를 만들 여지가 있는가(중립→긍정은 허용 범위). **장점·단점 코퍼스 양쪽** 적대셋으로 검증했는가 — 한쪽만 보면 거짓 자신감 | 높음 | [modules/emotion-analysis.md](modules/emotion-analysis.md) · [operator-manual/developer-manual/03-emotion-engine.md](operator-manual/developer-manual/03-emotion-engine.md) |
| DL-5 | 필드 신호 보존 | 장점/단점 필드 프리픽스가 판정·재추론 경로에서 유실되는가 (train/serve 정합) | 높음 | [operator-manual/developer-manual/03-emotion-engine.md](operator-manual/developer-manual/03-emotion-engine.md) |
| DL-6 | 날짜·수치 필드 타입 | 원천이 `int` 인 값을 문자열로 가정하고 필터·비교하는가 (연/월 필터 전건 탈락 사고 이력) | 높음 | [operator-manual/developer-manual/04-data-layer.md](operator-manual/developer-manual/04-data-layer.md) |
| DL-7 | 학습 데이터 위치 | 학습용 데이터·코퍼스·상시 현황 문서를 `{{paths.plans_root}}/_datasets/kote_finetune/` 밖에 쓰는가 (`plans/` 는 배포 제외 폴더 — 유출 방지) | 높음 | [operator-manual/developer-manual/07-finetune-pipeline.md](operator-manual/developer-manual/07-finetune-pipeline.md) |
| DL-8 | 공통 모듈 침범 | `{{paths.app_root}}` 의 공통 모듈·서비스를 요청 범위 밖에서 고쳤는가. 호출처 전수 Grep 결과를 첨부했는가 | 중간 이상 | [`common/core/01-legacy-protection.md`](../../common/core/01-legacy-protection.md) · [`03-workflow/06-common-module-impact.md`](../../common/core/03-workflow/06-common-module-impact.md) |
| DL-9 | 원데이터 취급 | PII·내부망 원데이터가 코드·로그·커밋·배포 패키지에 남는가 | 높음 | [operator-manual/developer-manual/05-build-deploy.md](operator-manual/developer-manual/05-build-deploy.md) §배포 제외 목록 |

---

## 2. 계획·절차 잠금 (DL-10 ~ DL-12)

| # | 잠금 | 무엇을 보는가 | 심각도 | 정본 |
|---|------|---------------|--------|------|
| DL-10 | 완료 판정 근거 | 단위 테스트만으로 `Done`(DN) 을 주장하는가. **실동작 검증 전이면 `Pre-Done`(PND) + 체크리스트**여야 한다 | 높음 | [`00-core/03-plan-mode/11-status-and-index.md`](../../common/core/00-core/03-plan-mode/11-status-and-index.md) |
| DL-11 | 계획서 저장 규약 | 저장 위치·파일명이 `{{paths.plans_root}}/YYYY/MM/DD_NN_작업명/`(폴더명=파일명) 인가. 해당 월 `_index.md` 를 함께 갱신했는가 | 중간 | [`00-core/03-plan-mode/10-storage-naming.md`](../../common/core/00-core/03-plan-mode/10-storage-naming.md) |
| DL-12 | 서버 무단 기동 | 검증·재현 절차에 **사용자 승인 없는 서버 실행**이 들어 있는가. 필요하면 명령을 안내만 하고, 확인은 독립 스크립트로 한다 | 높음 | 공통 정본 없음 — 사용자 상시 지시 |

> DL-10·DL-11 은 공통 규칙이지만 이 프로젝트에서 반복 위반이 있었으므로 잠금 목록에 넣는다. 상태 약어 `DN`·`PND` 는 공통 정본의 `Done`·`Pre-Done` 을 가리키는 통칭이다.

---

## 갱신 규칙

새 사고가 발생하면 **행을 추가**하고 번호는 재사용하지 않는다. 정본 문서가 없는 항목은 정본을 먼저 만들고 링크한다 — 상세 서술을 이 표에 채우지 않는다.
