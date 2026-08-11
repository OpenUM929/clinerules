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

## 3. 측정·수치 잠금 (DL-13 ~ DL-15)

| # | 잠금 | 무엇을 보는가 | 심각도 | 정본 |
|---|------|---------------|--------|------|
| DL-13 | 측정 조건 전제 | 실행 조건(필드 프리픽스 주입 여부 등)을 **가정**으로 두고 측정했는가. "산출물에 값이 없다"를 "그 실행은 그 값 없이 돌았다"로 읽었는가 — **분포 역검정**으로 조건을 확정했는가 | 높음 | [operator-manual/developer-manual/06-batch.md](operator-manual/developer-manual/06-batch.md) §필드 소재 지도 |
| DL-14 | 추정치 신뢰 범위 | 부분집합 + 보정으로 추정하면서 **보정계수의 안정성만 근거로 신뢰 범위**를 제시했는가. 계수 일치는 계수의 안정성만 보증하며 **지표별 편향 방향·크기는 다르다**. 전수 확정 경로를 먼저 제안했는가 | 높음 | [`17-hallucination-prevention/09-data-absence.md`](../../common/core/17-hallucination-prevention/09-data-absence.md) ABS-6 |
| DL-15 | 폐기값 잔존 | 수치가 개정·대체됐을 때 요약·부록·자료 목록·재현 명령에 **구 값이 남아** 있는가. 폐기 산출물에 "인용 금지" 표시를 했는가. 추정이 실측으로 바뀐 경우 **빗나간 정도를 문서에 남겼는가**(조용한 교체 금지) | 중간 이상 | [`common/core/16-report-writing.md`](../../common/core/16-report-writing.md) |

> DL-13~DL-15 는 2026-07-29 완료 보고서 작업에서 실제 발생한 사고에서 도출했다. DL-13 은 연도별 판정 분포를 운영 조건과 다른 조건으로 재판정해 보고한 사고, DL-14 는 제시한 신뢰 범위를 전수 실측이 전 항목 벗어난 사고, DL-15 는 개정 시 요약·목록에 구 수치가 남은 사고다.

---

## 4. 검수·부재 판정 잠금 (DL-16 ~ DL-18)

| # | 잠금 | 무엇을 보는가 | 심각도 | 정본 |
|---|------|---------------|--------|------|
| DL-16 | 접근 통제 부재 판정 | 화면 템플릿에 개인 식별 정보가 렌더된다는 이유로 **"통제 없음"을 선언하는가**. 선언 전에 ① 템플릿의 `{% extends %}` 상위 레이아웃(전역 관리자 인증 오버레이) ② 라우트의 서버측 세션 가드 ③ 가명 매핑의 암호화 저장 ④ 세션 컨텍스트 주입부를 **모두** 확인했는가 | 높음 | [modules/pseudonym-manager.md](modules/pseudonym-manager.md) |
| DL-17 | 연도별 자료 부재 판정 | **"2023·2025년 자료·라벨이 없다"** 계열 서술을 근거로 쓰는가. 이 서술은 이미 **오기로 정정 완료**(2025년 2026-07-28 · 2023년 2026-07-29 칸별 재추출)됐고 3개 연도 전수 확정값이 존재한다. **대조용 전수 자료**(3개 연도 보유)와 **외부 기준 채점 표본**(구간 한정)은 서로 다른 축이며, 한 문장으로 합치면 정정 전 프레임이 되살아난다 | 높음 | [operator-manual/developer-manual/06-batch.md](operator-manual/developer-manual/06-batch.md) §필드 소재 지도 |
| DL-18 | 확장자 ≠ 형식 | `.csv` 파일을 CSV 로 단정했는가. **내부망→외부망 반출 게이트가 JSONL·JSON 을 「정상적이지 않은 데이터」로 차단**하므로 내용과 무관하게 `.csv` 로 개명해 내보낸다 — `data/` 의 연도별 코퍼스·필드별 코퍼스는 **JSONL**, 판정 패킷은 **단일 JSON** 이다. `head -1` 로 판별하고, **「csv 밖에 없으니 산출물이 없다」 결론 금지**. 되돌려 반입할 때도 같은 제약이 걸린다 | 높음 | [`17-hallucination-prevention/09-data-absence.md`](../../common/core/17-hallucination-prevention/09-data-absence.md) |

> **DL-16·DL-17 은 2026-08-04 인수검수 에이전트 구동에서 실제 발생한 오탐에서 도출했다.** 검수가 화면 템플릿의 표시 코드 5줄만 읽고 "개인정보가 납품 화면에서 차단되지 않음"을, 그리고 채점 표본 편중을 "2023·2025년 검증 0건"으로 적어 **이 둘을 인수 불가 2대 사유로 올렸다.** 실측 결과 전자는 상위 레이아웃의 전역 관리자 인증 게이트와 PBKDF2→Fernet 암호화가 이미 존재했고, 후자는 사용자가 이미 자료를 제공해 전수 확정으로 종결한 항목이었다. **오탐 판정은 폐기했다.** 두 건 모두 "안 보였다"를 "없다"로 승격시킨 것이 원인이며, 부재 판정의 증명 부담을 충족 판정보다 높게 두는 것이 이 잠금의 취지다. 에이전트 측 일반 규칙은 정의 본문의 N-1~N-5 에 있다.

> **DL-18 은 2026-08-06 특허 문서 검수에서 발생한 오보고에서 도출했다.** 판정 패킷을 찾으면서 코드가 쓰는 폴더만 보고 확장자로 걸러 "신 형식 패킷 0건"이라 보고했으나, 실제로는 반출 게이트를 통과시키려고 `.csv` 로 개명해 둔 단일 JSON 패킷이 존재했다. **근본 원인은 데이터 부재가 아니라 출처 기록의 부재**이며, 그래서 데이터 출처 대장(`_분석데이터_출처대장_*.md`) 관리가 함께 도입됐다.

---

## 갱신 규칙

새 사고가 발생하면 **행을 추가**하고 번호는 재사용하지 않는다. 정본 문서가 없는 항목은 정본을 먼저 만들고 링크한다 — 상세 서술을 이 표에 채우지 않는다.
