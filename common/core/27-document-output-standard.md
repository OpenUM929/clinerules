# 27. 인쇄·제출용 문서 출력 규격

> **적용 대상 — 인쇄·제출(A4)을 전제로 산출하는 문서.** 화면 열람만 하는 내부 메모는 대상이 아니다(COM-4).
>
> 내용이 옳아도 지면에서 잘리면 제출물로는 실패한다. 이 규격은 **출력 단계의 규율**이며, 보고서의 **내용 규칙**은 [16-report-writing.md](16-report-writing.md), **양식·마크업 정본**은 [`../operator-manual/DEVELOPMENT/00-a4-authoring-guide.md`](../operator-manual/DEVELOPMENT/00-a4-authoring-guide.md) 다. 규격 본문을 에이전트 정의나 개별 보고서에 복사하지 않는다 — 여기를 링크한다.

---

## 1. 규칙 — OUT

| 조항 | 내용 | 검사 |
|------|------|------|
| OUT-1 | 양식(용지·여백·타이포·페이지 나눔)은 **양식 정본 가이드가 정한다.** 문서마다 규격을 새로 정의하지 않는다 | 수동 |
| OUT-2 | 마크업·페이지 나눔·블록 크기 제약은 **양식 정본의 절대 규칙을 그대로 따른다**(§2). 여기에 다시 적지 않는다 — 두 벌이 되면 갈라진다 | 수동 |
| OUT-3 | **전체화면 캡처 금지.** 설명 대상 요소만 단위 캡처하고, 넣기 전 **가독성 검산**(축소율 × 원본 글자 크기 ≥ 판독 가능)을 한다 | 수동 |
| OUT-4 | 이미지에 **픽셀 폭 속성을 주지 않는다.** 표준 이미지 표기(`![대체텍스트](경로)`)만 쓰고, 파일 실존을 확인한다 | `K2` |
| OUT-5 | 저장 후 **깨진 참조 0건 대사**를 실행하고 결과를 보고에 포함한다. 0건이 아니면 출고하지 않는다 | `K1`·`K2` |
| OUT-6 | 파일명이 비슷하다는 이유로 **대체 자산을 쓰지 않는다.** 열어서 내용을 확인한 뒤 참조한다 | 수동 |

---

## 2. 양식 정본은 어디인가 (OUT-1)

| 알고 싶은 것 | 정본 |
|--------------|------|
| 용지·여백·인쇄 가능 폭/높이·타이포 | [`00-a4-authoring-guide/01-spec.md`](../operator-manual/DEVELOPMENT/00-a4-authoring-guide/01-spec.md) |
| 페이지 나눔 토큰·금지 마크업·치환표 | [`00-a4-authoring-guide/02-absolute-rules.md`](../operator-manual/DEVELOPMENT/00-a4-authoring-guide/02-absolute-rules.md) |
| 한 페이지 = 한 주제 구성 규칙 | [`00-a4-authoring-guide/03-page-composition.md`](../operator-manual/DEVELOPMENT/00-a4-authoring-guide/03-page-composition.md) |
| 작성·변환 체크리스트 / 검증 기준 | [`00-a4-authoring-guide/06-checklist.md`](../operator-manual/DEVELOPMENT/00-a4-authoring-guide/06-checklist.md) · [`07-acceptance.md`](../operator-manual/DEVELOPMENT/00-a4-authoring-guide/07-acceptance.md) |

**렌더 경로를 작성 전에 확정한다.** 같은 마크다운도 어떤 경로로 출력하느냐에 따라 양식 정본이 갈린다(통합 빌드 스타일시트 경로 / 외부 편집기 테마 경로). 어느 경로인지 모른 채 시작하면 양식을 두 번 만든다 — 판단 기준은 [`00-a4-authoring-guide/00-principles.md`](../operator-manual/DEVELOPMENT/00-a4-authoring-guide/00-principles.md) 상단에 있다.

> **문서 상단 인라인 스타일 블록은 양식 지정 수단이 아니다.** 편집기 경로에서는 저장·렌더 시 떨궈지고, 통합 빌드 경로에서는 스타일시트가 그린다. 양식은 프론트매터 메타데이터 또는 빌드 스타일시트로 지정한다([`02-absolute-rules.md`](../operator-manual/DEVELOPMENT/00-a4-authoring-guide/02-absolute-rules.md) §2-3).

---

## 3. 출고 게이트 — 깨진 참조 0건 대사 (OUT-5)

문서를 저장한 뒤 **이미지 참조 목록 vs 실제 보유 파일**을 대사한다. 절차·스크립트 정본은 [`00-core/04-reference-verification.md`](00-core/04-reference-verification.md) §3.

- "참조되었으나 없음"이 **0건**이어야 출고한다. 대사 결과를 보고에 그대로 적는다.
- 스크립트가 정상 종료했다는 사실은 **결과물이 목적지에 도달했다는 증거가 아니다.** 저장 경로를 직접 확인한다.

---

## 4. 내용 규칙과의 경계

출력 규격은 **지면·자산**만 다룬다. 수치 재계산·독자 적합성·집계값과 추정값 구분·정직 고지·참조 지침 명시·저장 경로 표시는 [16-report-writing.md](16-report-writing.md) §2 가 정본이며, 인쇄 문서에도 예외 없이 적용된다.

---

## 5. 검사

| 항목 | 린터 ID |
|------|---------|
| 참조 이미지 실존 | `K2` |
| 문서 링크 실존 | `K1` |
| 캡처 단위·가독성·양식 정본 준수 | 수동(작성자 자가 점검 + 검증 역할) |
