# 06. 통합 메뉴얼 생성 규칙 (레거시 · 오프라인 PDF 대체 경로)

> 나침반: [../DEVELOPMENT.md](../DEVELOPMENT.md) · 정본: [00-a4-authoring-guide.md](00-a4-authoring-guide.md)

> 🟡 **레거시 안내(2026-07-21):** 편집·인쇄·PDF의 정본 렌더는 **md_editor(00 정본)** 다. 아래 HTML 통합빌드(`build_integrated.py`+`print.css`)는 md_editor를 못 쓰는 환경에서 **오프라인 PDF를 뽑기 위한 대체 경로**로만 유지한다.
> - 통합빌드가 삽입하는 `<!-- pagebreak -->`·`print.css`의 `img{max-width:640px}` 규칙은 **작성 마크업 규칙이 아니다.** 문서 원본에는 `---pb---`·`![]()` 만 쓴다(00 §2-2·§2-5). 통합빌드는 원본을 읽어 자기 파이프라인용 마커로 변환할 뿐이다.
> - 도구를 삭제하지 않되, 신규 작성·변환은 00 정본을 기준으로 한다.

> 개별 파일을 일일이 인쇄하지 않도록, **순서대로 이어붙인 통합본**을 생성한다.

---

## 1. 산출물

- `integrated-manual.md` — 모든 메뉴얼을 순서대로 연결한 **단일 md**(열람/탐색용).
- `integrated-manual.html` — `print.css`(A4) 적용 **단일 HTML**(브라우저 → 인쇄 → PDF).
- `build/print.css` — A4 페이지/폭 규칙.
- `build/MANIFEST.txt` — 통합 순서(파일 목록, 한 줄에 하나).
- `build/build_integrated.py` — 빌드 스크립트(순수 표준 라이브러리, 외부 의존성 없음).

## 2. 빌드 실행

```powershell
cd .clinerules/docs/msys/operator-manual
python build/build_integrated.py
```

- `MANIFEST.txt` 순서대로 md를 읽어 파일 경계마다 `<!-- pagebreak -->` 삽입 후 연결.
- 상대 이미지/링크 경로를 출력 위치 기준으로 재작성.
- md → HTML 변환 후 `print.css` 임베드하여 `integrated-manual.html` 생성.

## 3. print.css 핵심 규칙

```css
@page { size: A4; margin: 18mm 16mm; }
.container { max-width: 170mm; margin: 0 auto; }
.pagebreak { break-before: page; }
img { max-width: 640px; height: auto; }
table { width: 100%; max-width: 640px; border-collapse: collapse; }
@media screen { body { background: #eee; } .container { background: #fff; padding: 16mm; } }
```

## 4. 오프라인 환경 고려

- weasyprint/pandoc 미설치 환경 가정 → **별도 변환기 없이 브라우저 인쇄**로 PDF 생성.
- 자동 PDF가 필요하면 weasyprint 설치 후 `build_integrated.py`에 PDF 출력 분기 추가(선택).
