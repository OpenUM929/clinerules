# 06. 통합 메뉴얼 생성 · 양식 정본 (print.css)

> 나침반: [../DEVELOPMENT.md](../DEVELOPMENT.md) · 마크업 규칙 정본: [00-a4-authoring-guide.md](00-a4-authoring-guide.md)

> 🟢 **정본 안내(2026-07-23 개정):** **이 저장소가 관리하는 운영자·개발 메뉴얼의 정본 렌더와 시각 양식(form)은 아래 `print.css` 통합빌드다.** 대제목 밑줄 경계선·표 테두리·인용문 바 등 "보이는 양식"은 전적으로 `print.css`가 그리며, md 원본은 순수 시맨틱(`#`/`##`/표/`>`)만 담는다.
>
> - 이전(2026-07-21)에는 md_editor(Tiptap `reportTheme`)를 정본, 이 빌드를 "레거시"로 두었으나 — md_editor 테마 CSS는 **외부 저장소**라 이 리포에서 못 고치고, `reportTheme=report`의 대제목(회색 박스)과 우리가 채택한 디자인(밑줄 경계선)이 달라 **정본을 print.css로 되돌렸다**(사용자 결정 2026-07-23).
> - 프론트매터 `reportTheme:` 는 **선택적 메타데이터**(외부 md_editor에서만 의미)이며, 이 통합빌드는 프론트매터를 **무시**한다(선두 `--- … ---` 블록 제거). 그대로 두어도 무해하다.
> - `00-a4-authoring-guide.md`의 **마크업 위생 규칙**(표준 md만·`![]()`·`---pb---`·인라인 `<style>` 금지·`<img width>` 금지)은 렌더러 무관하게 계속 유효하다. 06은 그 위에 **시각 양식**을 확정한다.

> 개별 파일을 일일이 인쇄하지 않도록, **순서대로 이어붙인 통합본**을 생성한다. 빌드 스크립트(`build_integrated.py`)·양식(`print.css`)은 **모든 프로젝트가 공유하는 단일 사본**으로 이 폴더(`common/operator-manual/build/`)에 둔다. 각 프로젝트는 자기 `operator-manual/build/MANIFEST.txt`(통합 순서)만 갖는다.

---

## 1. 산출물

- `integrated-manual.md` — 모든 메뉴얼을 순서대로 연결한 **단일 md**(열람/탐색용, 프론트매터 제거·파일 경계마다 `---pb---`). 프로젝트의 `operator-manual/` 폴더에 생성된다.
- `integrated-manual.html` — `print.css`(A4) 적용 **단일 HTML**(브라우저 → 인쇄 → PDF). **이 파일이 최종 양식의 정본 미리보기다.**
- `common/operator-manual/build/print.css` — A4 페이지/폭 + **양식(제목 경계선·표·인용문 등)** 규칙. **모든 프로젝트 공용 정본**(단일 사본, 프로젝트별 복사본을 두지 않는다).
- `<프로젝트>/operator-manual/build/MANIFEST.txt` — 그 프로젝트의 통합 순서(파일 목록, 한 줄에 하나, `#` 주석). **프로젝트마다 자신의 것을 둔다.**
- `common/operator-manual/build/build_integrated.py` — 빌드 스크립트(순수 표준 라이브러리, 외부 의존성 없음, 모든 프로젝트 공용).

## 2. 빌드 실행

프로젝트 폴더에서 공용 빌드 스크립트를 상대경로로 호출한다(대상 폴더는 인자로 넘긴다).

```powershell
cd .clinerules/docs/<프로젝트키>/operator-manual
python ../../common/operator-manual/build/build_integrated.py .                  # 운영 메뉴얼(현재 폴더)
python ../../common/operator-manual/build/build_integrated.py developer-manual   # 개발 메뉴얼(임의 매뉴얼 폴더, 프로젝트 상대경로)
```

- 인자로 **임의 매뉴얼 폴더**(운영 메뉴얼 폴더 자신 `.` 또는 그 상위의 다른 매뉴얼 폴더)를 지정하면 그 폴더의 `build/MANIFEST.txt` 순서로 빌드한다.
- CSS 탐색 순서: ① 대상 폴더 자신의 `build/print.css` → ② 그 프로젝트 `operator-manual/build/print.css`(하위 매뉴얼이 운영 메뉴얼의 공용본을 씀) → ③ `common/operator-manual/build/print.css`(모든 프로젝트의 최종 공용 정본). 프로젝트에 로컬 사본이 없으면 자동으로 ③까지 내려가 공용 정본을 쓴다.
- `MANIFEST.txt` 순서대로 md를 읽어 파일 경계마다 페이지나눔을 삽입하고, 상대 이미지/링크 경로를 출력 위치 기준으로 재작성한 뒤 HTML로 변환해 `print.css`를 임베드한다.
- 페이지나눔 토큰: **정본 `---pb---`**, 구 `<!-- pagebreak -->` 는 별칭으로 함께 인식한다.
- **개별 문서 탐색 링크는 통합본에서 자동 제거된다**: `↑ [목록으로](...)` · `[← 이전: ...] [다음: ... →]` 등 `↑`로 시작하는 줄(코드펜스 내부 제외)은 낱개 파일 열람용이라 파일이 순서대로 이어지는 통합 문서에는 불필요하므로 빌드 시점에 걸러낸다(`strip_nav_links()`). 원본 파일에는 그대로 남겨 두어 낱개 열람 시 탐색은 유지된다.

## 3. print.css 양식 사양 (이 값이 정본 — `common/operator-manual/build/print.css`)

| 요소 | 마크다운 | 렌더 양식(print.css) |
|------|----------|----------------------|
| 대제목 | `# 제목` (h1) | 18pt, 강조색(네이비 `--accent` #1B1760) + **아래 3px 실선 경계선** + padding-bottom 8px |
| 섹션 | `## 제목` (h2) | 14pt, **왼쪽 4px 강조색 바** + padding-left 10px, 위 여백 20px |
| 소제목 / 세부 | `### ` / `#### ` | 12pt(강조색) / 11pt(회색 `--muted`) (경계선 없음) |
| 본문 | 일반 텍스트 | 맑은 고딕 10.5pt / 행간 1.5 / #1a1a1a |
| 표 | `\| … \|` | 폭 100%(≤640px), 헤더 연보라 틴트 배경(`--accent-light` #EEF0FA) + 강조색 글자, 테두리 #d7d7e0, 9.5pt |
| 인용/참고(주) | `> 문장` | 왼쪽 4px 강조색 바 + 연보라 틴트 배경(`--accent-light`) |
| 코드/코드블록 | `` ` `` / ```` ``` ```` | 연보라 틴트 배경, 강조색 글자(인라인) / 연회색 배경(블록), 9pt monospace |
| 이미지 | `![대체텍스트](경로)` | 폭 상한 640px 자동 맞춤 + 1px 테두리 + 3px 라운드 |
| 수평선 | `---` | **렌더하지 않음(2026-08-19)** — 장식용 구분선이 페이지 경계에 걸려 "밑줄 한 줄만 있는 페이지"가 생기는 문제가 있어 아예 생략한다. 절 제목(h1/h2)의 강조색 경계선이 이미 절 구분을 보여준다 |
| 용지 | — | `@page A4`, 여백 **9mm(상하) × 16mm(좌우)**, 컨테이너 170mm |
| 절 단위 나눔 방지 | h1~h4 + 그 아래 본문 | `break-inside: avoid-page` — 헤딩 하나와 **바로 다음 헤딩(레벨 무관) 전까지의 본문**을 `<section class="keep-together">`로 묶는다. 그 절이 남은 페이지에 다 안 들어가면 절 전체가 다음 페이지로 넘어간다 |

> **양식을 바꾸려면 `print.css` 한 곳만 고친다.** md 본문에 인라인 스타일·픽셀 폭·`<div>` 를 넣지 않는다(00 §2). 대제목 경계선을 md에서 `---` 로 흉내내지 말 것 — 경계선은 h1 스타일이 자동으로 그린다.
> 색상은 `print.css` 상단 `:root` 커스텀 프로퍼티(`--accent`·`--accent-light`·`--border`·`--muted`)로 관리한다. 강조색을 바꾸려면 이 4개 변수만 고치면 전체 요소(제목·표·인용·코드·글머리표)에 일괄 반영된다(2026-08-19 모던 디자인 개정).
>
> ⚠️ **`.keep-together`는 헤딩 레벨로 계층 중첩하지 않는다(2026-08-19, 실패 사례 확정).** h1 섹션이 그 안의 h2 섹션들을 전부 품는 방식으로 처음 구현했더니, h1 섹션이 챕터 전체 크기가 되어 `avoid-page`가 통째로 다음 페이지로 밀어버려 "챕터 제목만 있고 아래가 빈 페이지"가 나왔다(사용자 신고). 그래서 `build_integrated.py`의 `nest_sections()`는 **레벨과 무관하게 형제(sibling) 단위**로만 묶는다 — 헤딩 하나의 절은 바로 다음 헤딩이 나오는 순간 닫힌다. 이 함수를 고칠 때 계층 중첩으로 되돌리지 않는다.

> 🔴 **고정 규칙(2026-07-27)**: ① 챕터 제목(h1, 18pt)은 항상 섹션(h2, 14pt)보다 커야 한다. ② 경계선(HR)은 h1·h2(챕터·섹션, 레벨1·2)까지만 그린다 — h3/h4(소제목·세부)는 경계선 없이 크기만 작아진다. 둘 다 위 표의 `print.css` 값이 이미 만족하므로, `print.css`를 고칠 때 이 두 관계를 깨지 않는다.

## 3-1. 글머리표·문단번호 (nested list)

- 순서 없는 목록(`- 항목`)은 들여쓰기 깊이에 따라 **□(1단) → ○(2단) → -(3단)** 마커를 자동으로 그린다(00-a4-authoring-guide §3-5와 동일한 마커 체계).
- 순서 있는 목록(`1. 항목`)은 중첩할수록 **`1.` → `1.1.` → `1.1.1.`** 처럼 상위 번호를 이어받는 계층 문단번호를 CSS `counters()`로 자동 렌더링한다.
- md 원본은 표준 들여쓰기(중첩 시 2칸 이상 추가 들여쓰기)만 지키면 되고, □/○/번호 문자를 손으로 찍지 않는다(00 §3-5). `build_integrated.py`의 `parse_list_block()`이 들여쓰기 깊이를 보고 중첩 `<ul>`/`<ol>`을 만들고, `print.css`가 마커/번호를 그린다.

## 4. 새 메뉴얼 폴더를 이 양식으로 빌드하려면

1. 폴더에 `build/MANIFEST.txt` 생성(통합 순서). `build/print.css`는 만들지 않으면 §2의 fallback 순서로 상위/공용본을 쓴다.
2. 각 md는 시맨틱 마크다운으로만 작성(프론트매터는 선택). 페이지나눔은 `---pb---`.
3. `python <공용 build 경로>/build_integrated.py <폴더>` 실행 → 폴더 안에 `integrated-manual.{md,html}` 생성.

## 5. PDF 생성

- weasyprint/pandoc은 이 환경에 없는 것을 실측 확인(2026-08-19, `pip`/`ModuleNotFoundError`). `build_integrated.py`는 이 둘에 의존하지 않는다.
- **기본 경로 — 수동**: `integrated-manual.html`을 브라우저에서 열고 `인쇄 → PDF로 저장`(용지 A4) 선택. 별도 설치 없이 어디서나 된다.
- **자동 경로 — 로컬 Chrome/Edge 헤드리스**(설치돼 있으면, 실측 확인 2026-08-19): 별도 라이브러리 설치 없이 이미 깔린 브라우저의 헤드리스 인쇄 기능만 쓴다.
  ```powershell
  # Windows, Chrome 예시 (Edge면 msedge.exe로 경로만 교체 — 동일 플래그)
  & "C:\Program Files\Google\Chrome\Application\chrome.exe" `
    --headless --disable-gpu --no-pdf-header-footer `
    --print-to-pdf="<출력경로>\integrated-manual.pdf" `
    "file:///<integrated-manual.html 절대경로>"
  ```
  - 출력 대상 파일이 **다른 프로그램(PDF 뷰어 등)에서 열려 있으면 잠겨서 덮어쓰지 못한다** — 그 창을 닫거나 다른 파일명으로 출력한다(실사고 2026-08-19).
  - `@page` 여백·`.keep-together`·색상 등 `print.css`가 그리는 양식이 그대로 반영된다 — HTML을 별도로 손대지 않는다.
- 완전 자동 PDF가 CI 등에서 상시 필요해지면 weasyprint 설치 후 `build_integrated.py`에 PDF 출력 분기를 추가하는 방안도 있다(선택, 아직 미구현).

## 6. 챕터/헤딩 번호 자동 채번 (2026-07-27)

> 🔴 md 원본에는 헤딩 번호를 손으로 적지 않는다(01-structure.md §1). 아래 규칙에 따라 `build_integrated.py`의 `Numberer`가 **1 / 1.1 / 1.1.1 / 1.1.1.1** 4단 계층 번호를 통합 시점에 자동 주입한다 — 그래야 파일이 늘어나도 "1.1 → 1" 같은 역행 없이 항상 정합된다.

| 파일 유형 | own_depth(자기 H1 번호 깊이) | 예시 |
|-----------|------------------------------|------|
| 독립 최상위 파일(폴더 밖) | 1(새 챕터) | `00-getting-started.md` → `1`, `05-mngr-sett.md` → `6` |
| 폴더(예: `04-common-menus/`) 안의 파일(첫 파일 포함) | 2(그 폴더가 공유하는 챕터의 항목) | `01-dashboard.md` → `5.1`, `02-collection-schedule.md` → `5.2` |
| `<base>.tabN.md` | base own_depth + 1, **base 뒤에 이어지는 절처럼 전역 카운터를 이어받음** | `05-mngr-sett.tab1.md` → base(`6`)의 본문 절 수를 이어 `6.5` |
| `appendix/` 안의 파일 | 1이지만 숫자 챕터와 분리 — 부록 A/B/…로 별도 채번 | `appendix/command-cheatsheet.md` → `부록 A` |
| `00-index.md` | 채번 제외(목차) | — |

- 파일 내부 H2/H3/H4는 그 파일의 own_depth 기준으로 한 단계씩 깊어진다(전역 카운터를 그대로 이어 쓰므로, tabN이 base의 본문 절 수를 자연스럽게 이어받는다 — 예: `08-api-key-mngr.md`가 본문 절 6개를 쓰면 tab1은 `5.8.7`부터 시작. 숫자가 이어지는 것이 정상이며 "왜 .1이 아니냐"는 버그가 아니다 — 통합 문서를 순서대로 읽을 때 번호가 역행하지 않게 하기 위한 설계다).
- `#### ① 요소명`처럼 원문자(①②③…)로 시작하는 헤딩은 "요소 표 규격"(01-structure.md §3) 라벨이므로 채번 대상에서 제외한다(카운터도 건드리지 않음).
- 알고리즘·정확한 구현은 `build/build_integrated.py`의 `Numberer` 클래스·`apply_heading_numbers()` 참조.

## 7. 데이터 흐름도·화면 구성도는 실제 이미지로

> 🔴 ```(흐름도) [입력] → [프론트] → …``` 같은 ASCII 박스/화살표는 페이지 나눔·PDF·HWPX 변환에서 줄이 깨진다. **반드시 PNG 이미지로 렌더링해 `![]()`로 삽입한다.**

- 프로젝트별로 화면 구성도·데이터 흐름도를 PNG로 렌더링하는 스크립트를 둔다(예: matplotlib 기반, 외부 폰트/graphviz 불필요, 표준 Malgun Gothic 사용). 각 프로젝트의 실제 메뉴·데이터 흐름은 그 프로젝트 전용 문서(스크립트·`DIAGRAMS`/`WIREFRAMES` 정의 등)로 관리한다 — 다른 프로젝트 것을 이식하지 않는다.
- 새 메뉴 문서를 작성할 때 데이터 흐름도가 필요하면 프로젝트의 렌더링 스크립트에 항목을 추가해 생성하거나, 동등한 방식(matplotlib/graphviz 등)으로 직접 렌더링한다. 실제 화면 캡처가 아직 없는 경우에도 ASCII 박스 대신 와이어프레임 이미지 + `📷 화면 캡처 미보유` 안내문을 쓴다(운영자 배포 조건은 [07-checklist.md](07-checklist.md) 참조).
