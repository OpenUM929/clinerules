# 세부 문서 작성 개발 가이드 (나침반)

> ⚠️ **이 파일은 나침반이다.** 운영자 메뉴얼 각 세부 문서를 작성할 때 따르는 규칙·템플릿은 아래 원자 문서에 있다.
> 작업에 맞는 문서를 열어 읽은 뒤 작성한다. (분리 근거: `08-guideline-modification/03.document-separation.md` — 절차 규칙과 예시/시나리오가 한 파일에 혼재해 분리)
>
> **공용 지침**: 이 규칙은 **모든 프로젝트 운영자 매뉴얼**에 적용된다. 매뉴얼 위치는 `.clinerules/docs/<프로젝트키>/operator-manual/`(예: `msys/`, `project_wordcloud/`). 본 문서의 예시는 MSYS 예시이며, **각 프로젝트는 자기 실제 코드로 검증해 채운다(이식 금지)** — 상세 규약 [DEVELOPMENT/05-composition-nav.md](DEVELOPMENT/05-composition-nav.md) §1.0.

---

## 🔴 0. 최우선 정본 — A4 보고서 작성 통합 지침 (md_editor)

> **양식·페이지 구성·마크업(이미지·페이지나눔·표·개조식)의 정본은 [DEVELOPMENT/00-a4-authoring-guide.md](DEVELOPMENT/00-a4-authoring-guide.md) 이며, 본 나침반과 01~08 원자 문서보다 우선한다.**
> 충돌 시 **무조건 00 정본**을 따른다. 01~08에는 그 위에 얹히는 **메뉴얼 고유 사항**(구조 템플릿·요소 캡처·시나리오·용어사전·체크리스트 등)만 둔다.

핵심 5줄(정본 §0 요약):

1. **한 페이지 = 하나의 완결된 주제.**
2. **페이지 나눔은 작성자가 `---pb---` 로 명시**한다(자동 나눔에 맡기지 않음). ❌ `<!-- pagebreak -->`·`<div class="pagebreak">` 금지.
3. **한 블록 ≤ 한 페이지**(기본 인쇄 가능 높이 257mm·폭 170mm). 큰 이미지는 단독 페이지.
4. **표준 마크다운만 사용.** 인라인 `<style>`·`<div style>`·픽셀 폭 이미지(`<img width>`)는 md_editor(Tiptap)가 떨궈내거나 넘친다.
5. **양식은 프론트매터 `reportTheme` 로 지정**(구 인라인 `<style>`·`print.css` 임베드 대체).

---

## 문서 지도 (`DEVELOPMENT/`)

| 문서 | 다루는 내용 | 언제 보나 |
|------|------------|-----------|
| 🔴 [00-a4-authoring-guide.md](DEVELOPMENT/00-a4-authoring-guide.md) | **최우선 정본** — 양식(reportTheme)·페이지 나눔(`---pb---`)·마크업 치환(HTML→표준 md)·이미지 폴더(`img.<문서명>/`)·엔진 동작 | **작성·변환 전 반드시 먼저**(충돌 시 우선) |
| [01-structure.md](DEVELOPMENT/01-structure.md) | 네이밍 규칙 · **문서 구조 템플릿(예시급)** · 요소 표 규격 · 운영 시나리오 섹션 규칙 | **새 메뉴 문서를 쓸 때 먼저** |
| [02-image-capture.md](DEVELOPMENT/02-image-capture.md) | 요소 단위 캡처 원칙 · 삽입 방법 · **Playwright 요소 캡처 절차** | 이미지를 넣을 때 |
| [03-content-rules.md](DEVELOPMENT/03-content-rules.md) | 한글·테이블·강조 등 공통 작성 규칙 · 관리자 설정(mngr_sett) 특이사항 | 본문 서술·mngr_sett 작성 시 |
| [04-a4-print.md](DEVELOPMENT/04-a4-print.md) | A4 폭 예산 · 페이지 나누기 · 표/이미지 폭 규칙 | 작성 내내(폭 준수) |
| [05-composition-nav.md](DEVELOPMENT/05-composition-nav.md) | 파일 구성(진입점·탭 하위파일·부록) · 탐색 링크 · **운영 시나리오 문서(E2E)** | 파일 배치·탐색·시나리오 문서 |
| [06-integrated-build.md](DEVELOPMENT/06-integrated-build.md) | 통합본 산출물 · 빌드 실행 · print.css · 오프라인 | 통합/인쇄 빌드 시 |
| [07-checklist.md](DEVELOPMENT/07-checklist.md) | **작성 완료 체크리스트**(요소 이미지·시나리오·데이터 흐름·DB 절 등) | 문서 완료 처리 전 |
| [08-change-log.md](DEVELOPMENT/08-change-log.md) | 수정 이력 · 테스트 결과 · 검증 시나리오 | 지침 변경 기록 |

---

## 한눈 요약 (원칙)

- **운영자 우선 표준**: `접속 → 화면구성(요소 표) → 조작 → 운영 시나리오 → 모니터링 → 문제`를 앞에 두고, `데이터 흐름`·`DB/쿼리`는 `(참고·심화)`로 맨 뒤(운영자 건너뛰기 가능). 문서 상단 `기준 버전/최종 확인일` 필수(01-structure).
- **이미지**: 설명하는 모든 표·차트·메뉴·폼은 **요소만 캡처한 이미지** 1장을 붙이되(Playwright, 02), 삽입은 **`![설명](경로)` 표준 마크다운만**(❌ `<img width>`·`<div style>`). 크기·테두리·정렬은 `reportTheme`가 담당(00 §2-5).
- **운영 시나리오**: 메뉴마다 `운영 시나리오` 절 필수 + 매뉴얼 차원의 일상운영/장애대응/백업복구 E2E 문서(01·05).
- **A4·양식·탐색**: 프론트매터 `reportTheme` 지정, 페이지 나눔 `---pb---`, 한 블록 ≤ 257mm(00 정본) · 상단 목록·하단 이전/다음 링크(05). 구 HTML 통합빌드(`build_integrated.py`/`print.css`, 06)는 **오프라인 PDF 레거시 대체 경로**로만 남긴다.
- 완료 전 **체크리스트**(07)로 누락을 걸러낸다.
