#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
운영자/개발 메뉴얼 — 통합 빌드 스크립트 (print.css 양식이 정본)
- MANIFEST.txt 순서대로 모든 .md를 읽어 단일 integrated-manual.md + integrated-manual.html 생성
- 외부 의존성 없음 (표준 라이브러리만)
- HTML은 print.css(@page A4)를 임베드하므로 브라우저 "인쇄 → PDF 저장"로 A4 출력
- 대제목 밑줄 경계선 등 매뉴얼 양식(form)은 전적으로 print.css가 그린다(md는 순수 시맨틱).

이 스크립트는 `docs/common/operator-manual/build/`의 **모든 프로젝트 공용 단일 사본**이다.
프로젝트별 사본을 두지 않는다 — 각 프로젝트는 자신의 `operator-manual/build/MANIFEST.txt`만 갖는다.

사용법 (프로젝트 폴더에서 상대경로로 공용 스크립트 호출):
    cd .clinerules/docs/<프로젝트키>/operator-manual
    python ../../common/operator-manual/build/build_integrated.py .                  # 운영 메뉴얼(현재 폴더)
    python ../../common/operator-manual/build/build_integrated.py developer-manual   # 개발 메뉴얼(임의 매뉴얼 폴더)

인자:
    [BASE_DIR]  통합할 매뉴얼 폴더(생략 시 현재 작업 디렉터리).
                해당 폴더의 build/MANIFEST.txt 순서로 빌드하며, build/print.css가
                없으면 ① 그 프로젝트의 operator-manual/build/print.css → ② 이 스크립트와
                같은 폴더의 print.css(모든 프로젝트 공용 정본)를 순서대로 자동 사용한다.
"""

import os
import re
import sys
import posixpath
from pathlib import Path

# 통합 대상 매뉴얼 폴더(인자로 임의 폴더 지정 가능 — 개발 메뉴얼 등). 생략 시 현재 작업 디렉터리.
BASE = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path.cwd()
MANIFEST = BASE / "build" / "MANIFEST.txt"
CSS = BASE / "build" / "print.css"
if not CSS.exists():                # 그 프로젝트의 상위(operator-manual)가 갖는 공용 print.css
    CSS = BASE.parent / "build" / "print.css"
if not CSS.exists():                # 모든 프로젝트 공용 정본(이 스크립트와 같은 폴더)
    CSS = Path(__file__).resolve().parent / "print.css"
OUT_MD = BASE / "integrated-manual.md"
OUT_HTML = BASE / "integrated-manual.html"

# 페이지 나눔 토큰: 정본은 `---pb---`(00-a4-authoring-guide), `<!-- pagebreak -->`는 구 별칭.
PAGEBREAK_TOKEN = "---pb---"
PAGEBREAK_TOKENS = ("---pb---", "<!-- pagebreak -->")

NUMBERING_SKIP = {"00-index.md"}   # 목차는 채번 대상이 아니다
TAB_RE = re.compile(r'^(.*)\.tab\d+$')
APPENDIX_DIR = "appendix"
HEADING_RE = re.compile(r'^(#{1,4})\s+(.*)$')
FENCE_RE = re.compile(r'^\s*```')


class Numberer:
    """MANIFEST 순서를 따라 1 / 1.1 / 1.1.1 / 1.1.1.1 계층 번호를 build 시점에 자동 부여.

    md 원본에는 번호를 손으로 적지 않는다(01-structure.md §1 참조) — 손으로 적으면
    파일이 늘어날 때마다 계층이 어긋나는 사고(예: "1.1 → 1" 역행)가 재발한다.

    규칙:
    - 독립 최상위 파일(폴더 밖) = 새 챕터(레벨1).
    - 폴더(예: 04-common-menus/) 안의 모든 파일은 그 폴더가 공유하는 챕터의 항목(레벨2)이다
      — 폴더 진입 시 레벨1을 1회만 올리고, 폴더 내 각 파일이 레벨2를 파일 단위로 올린다.
    - `<base>.tabN.md` 는 base 파일 자신의 깊이(own_depth)+1에서 "이어서" 올린다 — base의
      본문 절과 같은 자리를 공유(탭이 곧 base 뒤에 이어지는 절처럼 취급).
    - 파일 내부 H2/H3/H4는 그 파일의 own_depth를 기준으로 한 단계씩 깊어지며, **전역**
      카운터를 그대로 이어 쓴다(그래야 뒤에 오는 tabN이 base의 본문 절 수를 이어받는다).
    - `appendix/`는 숫자 챕터에서 제외 — 부록 A/B/… 로 별도 채번(전역 카운터와 분리된
      파일별 로컬 하위 카운터 사용).
    """

    def __init__(self):
        self.L = [0, 0, 0, 0, 0]   # 인덱스 1..4만 사용
        self.open_dir = None
        self.own_depth = {}        # "dir/stem" -> own_depth(D)
        self.appendix_n = 0

    def bump(self, depth):
        self.L[depth] += 1
        for d in range(depth + 1, 5):
            self.L[d] = 0

    def numstr(self, depth):
        return ".".join(str(self.L[d]) for d in range(1, depth + 1))

    def file_prefix(self, rel):
        """rel(MANIFEST 경로)의 (prefix, own_depth, appendix_letter) 반환."""
        rel = rel.replace("\\", "/")
        d = posixpath.dirname(rel)
        stem = posixpath.splitext(posixpath.basename(rel))[0]
        key = posixpath.join(d, stem) if d else stem

        m = TAB_RE.match(stem)
        if m:
            base_key = posixpath.join(d, m.group(1)) if d else m.group(1)
            base_D = self.own_depth.get(base_key)
            if base_D is not None:
                D = min(base_D + 1, 4)
                self.bump(D)
                self.own_depth[key] = D
                return self.numstr(D), D, None

        if d == APPENDIX_DIR:
            self.appendix_n += 1
            letter = chr(ord('A') + self.appendix_n - 1)
            self.own_depth[key] = 1
            return f"부록 {letter}", 1, letter

        if d:
            if self.open_dir != d:
                self.bump(1)
                self.open_dir = d
            self.bump(2)
            self.own_depth[key] = 2
            return self.numstr(2), 2, None

        self.bump(1)
        self.open_dir = None
        self.own_depth[key] = 1
        return self.numstr(1), 1, None


ELEMENT_LABEL_RE = re.compile(r'^[①-⑳㉑-㉟㊱-㊿]')


def apply_heading_numbers(numberer, content, prefix, own_depth, is_appendix):
    """content 안의 (#~####) 헤딩에 계층 번호를 주입한다. 코드펜스 내부(``` … ```)는
    건드리지 않는다 — 쉘 주석(`# Windows` 등)을 헤딩으로 오인하지 않기 위함.
    `#### ① 요소명`처럼 원문자(①②③…)로 시작하는 헤딩은 "요소 표 규격"(01-structure.md)의
    별도 라벨 체계이므로 챕터 번호를 매기지 않는다(카운터도 건드리지 않음)."""
    lines = content.split("\n")
    local = [0, 0, 0, 0]   # appendix 전용: base로부터 분리된 파일-로컬 하위 카운터
    in_fence = False
    out = []
    for line in lines:
        if FENCE_RE.match(line):
            in_fence = not in_fence
            out.append(line)
            continue
        if not in_fence:
            m = HEADING_RE.match(line)
            if m and ELEMENT_LABEL_RE.match(m.group(2).strip()):
                out.append(line)
                continue
            if m:
                level = len(m.group(1))
                title = m.group(2).strip()
                if level == 1:
                    number = prefix
                elif is_appendix:
                    idx = level - 2
                    local[idx] += 1
                    for j in range(idx + 1, 4):
                        local[j] = 0
                    number = prefix + "." + ".".join(str(local[j]) for j in range(idx + 1))
                else:
                    eff = min(own_depth + (level - 1), 4)
                    numberer.bump(eff)
                    number = numberer.numstr(eff)
                out.append(f"{m.group(1)} {number} {title}")
                continue
        out.append(line)
    return "\n".join(out)


def strip_frontmatter(text: str) -> str:
    """선두 YAML 프론트매터(--- … ---) 블록을 제거한다.

    md 파일 상단의 `reportTheme:` 등 메타데이터는 print.css 렌더 대상이 아니다.
    제거하지 않으면 통합 HTML에 `<hr>` + `reportTheme: report` 문단으로 새어 나온다.
    """
    if not text.startswith("---"):
        return text
    lines = text.split("\n")
    if lines[0].strip() != "---":
        return text
    for j in range(1, len(lines)):
        if lines[j].strip() in ("---", "..."):
            return "\n".join(lines[j + 1:]).lstrip("\n")
    return text  # 닫는 --- 없으면 원본 유지(오검출 방지)


NAV_LINE_RE = re.compile(r'^>?\s*↑')


def strip_nav_links(text: str) -> str:
    """`↑ [목록으로](...)` · `↑ [← 이전: ...] [다음: ... →]` 등 개별 문서 탐색 링크를 제거한다.

    이 탐색 링크는 파일을 낱개로 열어 볼 때(00-index.md로 돌아가기·이전/다음 파일 이동)
    필요한 것이지, 모든 파일이 순서대로 이어붙는 통합 문서 안에서는 의미가 없다
    (다음 절이 바로 이어지므로 "다음 문서" 안내가 불필요). 코드펜스 내부는 건드리지 않는다.
    """
    lines = text.split("\n")
    out = []
    in_fence = False
    for line in lines:
        if FENCE_RE.match(line):
            in_fence = not in_fence
            out.append(line)
            continue
        if not in_fence and NAV_LINE_RE.match(line.strip()):
            continue
        out.append(line)
    return "\n".join(out)


# --------------------------------------------------------------------------- #
# 경로 재작성: 소스 md 위치 기준 상대경로 -> 출력 위치(BASE) 기준 상대경로
# --------------------------------------------------------------------------- #
def rel_from_root(md_rel_dir: str, target: str) -> str:
    """md 파일이 위치한 상대 디렉터리(md_rel_dir)에서 target(상대/절대/외부)을
    BASE 기준 상대경로로 변환. 외부(http/https/mailto/앵커)는 그대로 반환."""
    if not target:
        return target
    if re.match(r"^(https?:|mailto:|#|data:)", target, re.I):
        return target
    if posixpath.isabs(target):
        return target
    if md_rel_dir:
        joined = posixpath.normpath(posixpath.join(md_rel_dir, target))
    else:
        joined = posixpath.normpath(target)
    return joined


def rewrite_markdown_paths(md_rel_dir: str, text: str) -> str:
    """마크다운 링크/이미지의 상대 경로를 BASE 기준으로 재작성."""
    def repl(m):
        kind = m.group(1)          # '!' 이미지 or '' 링크
        alt = m.group(2)
        url = m.group(3)
        new_url = rel_from_root(md_rel_dir, url)
        title = m.group(4) or ""
        t = f' "{title}"' if title else ""
        return f'{kind}[{alt}]({new_url}{t})'
    # 이미지 ![alt](url "title") 또는 링크 [alt](url "title")
    pattern = re.compile(r'(!?)\[([^\]]*)\]\(([^)\s]+)(?:\s+&quot;([^&]+)&quot;|\s+&quot;([^&]+)&quot;)?\)')
    # 위 패턴은 title 처리가 복잡하므로 단순 패턴 2종 사용
    img_pat = re.compile(r'(!\[[^\]]*\]\()([^)\s]+)(\))')
    link_pat = re.compile(r'(\[[^\]]*\]\()([^)\s]+)(\))')
    text = img_pat.sub(lambda m: m.group(1) + rel_from_root(md_rel_dir, m.group(2)) + m.group(3), text)
    text = link_pat.sub(lambda m: m.group(1) + rel_from_root(md_rel_dir, m.group(2)) + m.group(3), text)
    return text


def rewrite_html_paths(md_rel_dir: str, text: str) -> str:
    """HTML <img>/<a> 태그의 상대 경로를 BASE 기준으로 재작성."""
    def attr_repl(attr):
        pat = re.compile(rf'({attr}\s*=\s*["\'])([^"\']+)(["\'])', re.I)
        def sub(m):
            return m.group(1) + rel_from_root(md_rel_dir, m.group(2)) + m.group(3)
        return pat, sub
    for attr in ("src", "href"):
        pat, sub = attr_repl(attr)
        text = pat.sub(sub, text)
    return text


# --------------------------------------------------------------------------- #
# 인라인 마크다운 변환
# --------------------------------------------------------------------------- #
def inline(text: str) -> str:
    # 코드
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    # 굵게 **text** or __text__
    text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'__([^_]+)__', r'<strong>\1</strong>', text)
    # 기울임 *text* or _text_
    text = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'<em>\1</em>', text)
    # 링크 [text](url)
    text = re.sub(r'\[([^\]]+)\]\(([^)\s]+)\)', r'<a href="\2">\1</a>', text)
    return text


# --------------------------------------------------------------------------- #
# 목록: 들여쓰기 기반 중첩 파싱 (□/○ 글머리표·계층 문단번호는 print.css가 그린다)
# --------------------------------------------------------------------------- #
BULLET_RE = re.compile(r'^(\s*)([-*+])\s+(.*)$')
ORDERED_RE = re.compile(r'^(\s*)(\d+)\.\s+(.*)$')


def parse_list_block(lines, i, n):
    """들여쓰기 깊이가 커지면 중첩 <ul>/<ol>을 만든다. 반환: (html, 다음 i)."""
    stack = []   # [{'indent':int, 'tag':'ul'|'ol', 'items':[str,...]}]
    root = []

    def close_to(indent):
        while stack and stack[-1]['indent'] > indent:
            done = stack.pop()
            html = f"<{done['tag']}>" + "".join(done['items']) + f"</{done['tag']}>"
            if stack:
                parent_items = stack[-1]['items']
                parent_items[-1] = parent_items[-1][:-len('</li>')] + html + '</li>'
            else:
                root.append(html)

    while i < n:
        line = lines[i]
        bm = BULLET_RE.match(line)
        om = None if bm else ORDERED_RE.match(line)
        if not bm and not om:
            break
        indent = len(bm.group(1)) if bm else len(om.group(1))
        tag = 'ul' if bm else 'ol'
        text = bm.group(3) if bm else om.group(3)
        close_to(indent)
        if stack and stack[-1]['indent'] == indent and stack[-1]['tag'] == tag:
            stack[-1]['items'].append(f"<li>{inline(text)}</li>")
        elif stack and stack[-1]['indent'] == indent:
            # 같은 들여쓰기인데 목록 종류가 바뀜 -> 이전 것을 닫고 새로 연다
            done = stack.pop()
            html = f"<{done['tag']}>" + "".join(done['items']) + f"</{done['tag']}>"
            if stack:
                parent_items = stack[-1]['items']
                parent_items[-1] = parent_items[-1][:-len('</li>')] + html + '</li>'
            else:
                root.append(html)
            stack.append({'indent': indent, 'tag': tag, 'items': [f"<li>{inline(text)}</li>"]})
        else:
            stack.append({'indent': indent, 'tag': tag, 'items': [f"<li>{inline(text)}</li>"]})
        i += 1

    close_to(-1)
    return "".join(root), i


# --------------------------------------------------------------------------- #
# 블록 단위 마크다운 -> HTML 변환 (경량)
# --------------------------------------------------------------------------- #
def md_to_html(md: str, md_rel_dir: str) -> str:
    md = rewrite_markdown_paths(md_rel_dir, md)
    lines = md.split("\n")
    out = []
    i = 0
    n = len(lines)

    def is_table_sep(line):
        return bool(re.match(r'^\s*\|?[\s:|-]+\|?\s*$', line)) and '-' in line

    while i < n:
        line = lines[i]

        # 빈 줄
        if line.strip() == "":
            i += 1
            continue

        # 페이지 나누기 (정본 `---pb---` + 구 `<!-- pagebreak -->`)
        if line.strip() in PAGEBREAK_TOKENS:
            out.append('<div class="pagebreak"></div>')
            i += 1
            continue

        # 코드 펜스
        if line.strip().startswith("```"):
            lang = line.strip()[3:].strip()
            i += 1
            buf = []
            while i < n and not lines[i].strip().startswith("```"):
                buf.append(lines[i])
                i += 1
            i += 1  # closing fence
            code = "\n".join(buf)
            cls = f' class="language-{lang}"' if lang else ""
            out.append(f"<pre><code{cls}>{code}</code></pre>")
            continue

        # HTML 패스스루 (줄이 < 로 시작하는 블록)
        if line.lstrip().startswith("<"):
            buf = []
            while i < n and lines[i].lstrip().startswith("<"):
                buf.append(lines[i])
                i += 1
            block = "\n".join(buf)
            block = rewrite_html_paths(md_rel_dir, block)
            out.append(block)
            continue

        # 제목
        m = re.match(r'^(#{1,6})\s+(.*)$', line)
        if m:
            level = len(m.group(1))
            out.append(f"<h{level}>{inline(m.group(2).strip())}</h{level}>")
            i += 1
            continue

        # 수평선
        if re.match(r'^\s*([-*_])(\s*\1){2,}\s*$', line):
            out.append("<hr>")
            i += 1
            continue

        # 표
        if "|" in line and i + 1 < n and is_table_sep(lines[i + 1]):
            header = [c.strip() for c in line.strip().strip("|").split("|")]
            i += 2  # header + separator
            rows = []
            while i < n and "|" in lines[i] and lines[i].strip():
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                rows.append(cells)
                i += 1
            thead = "<tr>" + "".join(f"<th>{inline(c)}</th>" for c in header) + "</tr>"
            tbody = ""
            for r in rows:
                tbody += "<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>"
            out.append(f"<table><thead>{thead}</thead><tbody>{tbody}</tbody></table>")
            continue

        # 인용
        if line.lstrip().startswith(">"):
            buf = []
            while i < n and lines[i].lstrip().startswith(">"):
                buf.append(lines[i].lstrip()[1:].strip())
                i += 1
            out.append(f"<blockquote>{inline(' '.join(buf))}</blockquote>")
            continue

        # 목록 (순서 없음/있음, 들여쓰기 기반 중첩 지원 — §00-a4 §3-5 □/○ 계층 + 문단번호)
        if BULLET_RE.match(line) or ORDERED_RE.match(line):
            html, i = parse_list_block(lines, i, n)
            out.append(html)
            continue

        # 문단 (위 분기에서 걸러지지 않은 모든 줄 — 다음 빈 줄/블록 경계까지)
        # else 폴백: 블록 시작이 아닌 이상 현재 줄은 반드시 수집되므로 i가 항상 전진(무한루프 방지)
        buf = []
        while i < n and lines[i].strip() != "" \
                and not re.match(r'^#{1,6}\s', lines[i]) \
                and not lines[i].lstrip().startswith(">") \
                and not re.match(r'^\s*[-*+]\s+', lines[i]) \
                and not re.match(r'^\s*\d+\.\s+', lines[i]) \
                and not lines[i].strip().startswith("```") \
                and not lines[i].lstrip().startswith("<") \
                and lines[i].strip() != PAGEBREAK_TOKEN \
                and not re.match(r'^\s*([-*_])(\s*\1){2,}\s*$', lines[i]) \
                and not ("|" in lines[i] and i + 1 < n and is_table_sep(lines[i + 1])):
            buf.append(lines[i])
            i += 1
        para = " ".join(buf).strip()
        if para:
            # 이미지 단독 줄은 p로 감싸지 않음
            if re.match(r'^!\[[^\]]*\]\([^)\s]+\)$', para):
                out.append(_standalone_image(md_rel_dir, para))
            else:
                out.append(f"<p>{inline(para)}</p>")
        continue

    return "\n".join(out)


def _standalone_image(md_rel_dir: str, para: str) -> str:
    m = re.match(r'^!\[([^\]]*)\]\(([^)\s]+)\)$', para)
    if not m:
        return para
    alt, url = m.group(1), m.group(2)
    return f'<img alt="{alt}" src="{rel_from_root(md_rel_dir, url)}">'


# --------------------------------------------------------------------------- #
# 메인
# --------------------------------------------------------------------------- #
def main():
    if not MANIFEST.exists():
        raise SystemExit(f"MANIFEST.txt 없음: {MANIFEST}")

    entries = []
    for raw in MANIFEST.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        entries.append(line)

    md_parts = []
    html_parts = []
    numberer = Numberer()

    for rel in entries:
        src = BASE / rel
        if not src.exists():
            print(f"[경고] 파일 없음 (건너뜀): {rel}")
            continue
        md_rel_dir = posixpath.dirname(rel.replace("\\", "/"))
        content = strip_nav_links(strip_frontmatter(src.read_text(encoding="utf-8")))
        if rel.replace("\\", "/") not in NUMBERING_SKIP:
            prefix, own_depth, letter = numberer.file_prefix(rel)
            content = apply_heading_numbers(numberer, content, prefix, own_depth, letter is not None)
        md_parts.append(content)
        html_parts.append(md_to_html(content, md_rel_dir))
        print(f"[ok] {rel}")

    # 통합 md (파일 경계마다 pagebreak)
    integrated_md = ("\n\n" + PAGEBREAK_TOKEN + "\n\n").join(md_parts)
    OUT_MD.write_text(integrated_md, encoding="utf-8")

    # 통합 html
    css = CSS.read_text(encoding="utf-8") if CSS.exists() else ""
    body = ('\n<div class="pagebreak"></div>\n').join(html_parts)
    html_doc = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<title>운영자 메뉴얼 (통합)</title>
<style>{css}</style>
</head>
<body>
<div class="container">
{body}
</div>
</body>
</html>
"""
    OUT_HTML.write_text(html_doc, encoding="utf-8")

    print(f"\n생성 완료:")
    print(f"  - {OUT_MD}")
    print(f"  - {OUT_HTML}")
    print(f"\n[인쇄] {OUT_HTML} 를 브라우저에서 열고 '인쇄 → PDF 저장' (용지 A4) 선택")


if __name__ == "__main__":
    main()
