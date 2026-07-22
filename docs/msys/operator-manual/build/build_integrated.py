#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MSYS 운영자 메뉴얼 — 통합 빌드 스크립트
- MANIFEST.txt 순서대로 모든 .md를 읽어 단일 integrated-manual.md + integrated-manual.html 생성
- 외부 의존성 없음 (표준 라이브러리만)
- HTML은 print.css(@page A4)를 임베드하므로 브라우저 "인쇄 → PDF 저장"로 A4 출력

사용법:
    cd .clinerules/docs/msys/operator-manual
    python build_integrated.py
"""

import os
import re
import posixpath
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent   # operator-manual/ (build/ 상위)
MANIFEST = BASE / "build" / "MANIFEST.txt"
CSS = BASE / "build" / "print.css"
OUT_MD = BASE / "integrated-manual.md"
OUT_HTML = BASE / "integrated-manual.html"

PAGEBREAK_TOKEN = "<!-- pagebreak -->"


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

        # 페이지 나누기
        if line.strip() == PAGEBREAK_TOKEN:
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

        # 순서 없는 목록
        if re.match(r'^\s*[-*+]\s+', line):
            buf = []
            while i < n and re.match(r'^\s*[-*+]\s+', lines[i]):
                item = re.sub(r'^\s*[-*+]\s+', '', lines[i])
                buf.append(f"<li>{inline(item)}</li>")
                i += 1
            out.append("<ul>" + "".join(buf) + "</ul>")
            continue

        # 순서 있는 목록
        if re.match(r'^\s*\d+\.\s+', line):
            buf = []
            while i < n and re.match(r'^\s*\d+\.\s+', lines[i]):
                item = re.sub(r'^\s*\d+\.\s+', '', lines[i])
                buf.append(f"<li>{inline(item)}</li>")
                i += 1
            out.append("<ol>" + "".join(buf) + "</ol>")
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

    for rel in entries:
        src = BASE / rel
        if not src.exists():
            print(f"[경고] 파일 없음 (건너뜀): {rel}")
            continue
        md_rel_dir = posixpath.dirname(rel.replace("\\", "/"))
        content = src.read_text(encoding="utf-8")
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
<title>MSYS 운영자 메뉴얼 (통합)</title>
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
