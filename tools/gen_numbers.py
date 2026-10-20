#!/usr/bin/env python3
"""NUMBERS.md 의 '등록 현황' 섹션을 파일 시스템에서 재생성한다.

수기 섹션(대역 정의·이동/결번 이력)은 보존하고 표만 갱신한다.
채번 자체는 사람이 대장에 먼저 적는다(NUM-5) — 이 스크립트는 대사·동기화용이다.

**수기로 적은 '상태'·'비고' 열은 기존 표를 파싱해 그대로 이월한다.**
이월 키는 파일 경로(= 폴더 + `NN-slug.md`)다. 이월하지 않던 구판은 실행할 때마다
비고를 전부 공란으로 덮어써서 채번 경위 기록을 통째로 지웠다(2026-08-25 실사고).
대장에만 있고 파일이 없는 행(결번·이동 기록)은 표에서 빠지므로 경고로 알린다.
"""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
CR = Path(__file__).resolve().parent.parent
MARK = "## 번호 필수 구역 등록 현황"
NAME = re.compile(r"^(\d{2})-(.+)\.md$")
ROW = re.compile(r"^\|[^|]*\|[^|]*\|\s*`([^`]+)`\s*\|\s*([^|]*?)\s*\|\s*(.*?)\s*\|\s*$")

led = CR / "NUMBERS.md"
text = led.read_text(encoding="utf-8")

# 기존 표의 수기 열(상태·비고)을 파일 경로 키로 읽어 둔다
prev = {}
for line in text.partition(MARK)[2].splitlines():
    m = ROW.match(line)
    if m:
        prev[m.group(1)] = (m.group(2) or "활성", m.group(3))

dirs = {}
for p in sorted((CR / "common" / "core").rglob("*.md")):
    dirs.setdefault(p.parent.relative_to(CR).as_posix(), []).append(p)

seen = set()
rows = []
for d in sorted(dirs):
    rows.append(f"\n### `{d}/`\n")
    rows.append("| NN | slug | 파일 | 상태 | 비고 |")
    rows.append("|----|------|------|------|------|")
    for p in sorted(dirs[d]):
        m = NAME.match(p.name)
        rel = p.relative_to(CR).as_posix()
        seen.add(rel)
        nn, slug = (m.group(1), m.group(2)) if m else ("—", "—")
        default = "" if m else "무번호 허용(README/메타)"
        state, note = prev.get(rel, ("활성", default))
        rows.append(f"| {nn} | {slug} | `{rel}` | {state} | {note} |")

head, _, tail = text.partition(MARK)
footer = ""
if "## 번호 선택 구역" in tail:
    footer = "\n---\n\n## 번호 선택 구역" + tail.split("## 번호 선택 구역", 1)[1]
led.write_text(head + MARK + "\n" + "\n".join(rows) + "\n" + footer, encoding="utf-8")
print(f"등록 현황 갱신: {sum(len(v) for v in dirs.values())}개 파일")

carried = sum(1 for rel in seen if prev.get(rel, ("", ""))[1])
print(f"수기 비고 이월: {carried}건")
missing = [rel for rel in prev if rel.startswith("common/core/") and rel not in seen]
if missing:
    print(f"⚠ 대장에는 있으나 파일이 없는 행 {len(missing)}건 — 표에서 빠졌다. "
          f"결번·이동 기록이면 '이동·결번 이력' 절로 옮겨 보존할 것:")
    for rel in missing:
        print(f"  - {rel}")
