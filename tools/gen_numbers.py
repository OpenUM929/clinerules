#!/usr/bin/env python3
"""NUMBERS.md 의 '등록 현황' 섹션을 파일 시스템에서 재생성한다.

수기 섹션(대역 정의·이동/결번 이력)은 보존하고 표만 갱신한다.
채번 자체는 사람이 대장에 먼저 적는다(NUM-5) — 이 스크립트는 대사·동기화용이다.
"""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
CR = Path(__file__).resolve().parent.parent
MARK = "## 번호 필수 구역 등록 현황"
NAME = re.compile(r"^(\d{2})-(.+)\.md$")

dirs = {}
for p in sorted((CR / "common" / "core").rglob("*.md")):
    dirs.setdefault(p.parent.relative_to(CR).as_posix(), []).append(p)

rows = []
for d in sorted(dirs):
    rows.append(f"\n### `{d}/`\n")
    rows.append("| NN | slug | 파일 | 상태 | 비고 |")
    rows.append("|----|------|------|------|------|")
    for p in sorted(dirs[d]):
        m = NAME.match(p.name)
        rel = p.relative_to(CR).as_posix()
        if m:
            rows.append(f"| {m.group(1)} | {m.group(2)} | `{rel}` | 활성 |  |")
        else:
            rows.append(f"| — | — | `{rel}` | 활성 | 무번호 허용(README/메타) |")

led = CR / "NUMBERS.md"
text = led.read_text(encoding="utf-8")
head, _, tail = text.partition(MARK)
footer = ""
if "## 번호 선택 구역" in tail:
    footer = "\n---\n\n## 번호 선택 구역" + tail.split("## 번호 선택 구역", 1)[1]
led.write_text(head + MARK + "\n" + "\n".join(rows) + "\n" + footer, encoding="utf-8")
print(f"등록 현황 갱신: {sum(len(v) for v in dirs.values())}개 파일")
