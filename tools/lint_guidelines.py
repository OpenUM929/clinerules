#!/usr/bin/env python3
"""지침 저장소 린터.

common/core/19~26 의 규칙을 검사한다. 규칙 문서와 검사 ID 는 1:1 대응한다.
표준 라이브러리만 사용한다(내부망 실행 보장).

사용:
    python .clinerules/tools/lint_guidelines.py                 # 전체
    python .clinerules/tools/lint_guidelines.py --severity error
    python .clinerules/tools/lint_guidelines.py --baseline tools/lint_baseline.txt
    python .clinerules/tools/lint_guidelines.py --json
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import defaultdict
from pathlib import Path

# Windows 콘솔(cp949)에서도 한글·기호가 깨지지 않게 강제
for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

# ---------------------------------------------------------------- 상수

ZONES = {"common", "projects", "outputs", "tools"}
META_FILES = {"README.md", "CLAUDE.md", "NUMBERS.md", "PROJECTS-REGISTRY.md"}
NUMBERED_ZONE = ("common", "core")          # 번호 필수 구역 (NUM-3)
SKIP_DIRS = {".git", "outputs"}             # 검사 제외 (산출물·이관 대기분)
GENERATED = {"integrated-manual.md"}        # 빌드 생성물 — 줄수 검사 제외
AGENT_DIR = (".claude", "agents")           # 에이전트 정의 위치 (저장소 루트 기준, AGT)
AGENT_FM_KEYS = ("name", "description", "tools")   # AGT-3
# Finding.path 가 지침 저장소(.clinerules) 가 아니라 저장소 루트 기준인 경우
REPO_RELATIVE = (".claude/", "project.json")

COMPASS_MAX = 60                            # CMP-2
DETAIL_WARN = 80
DETAIL_MAX = 160
SLUG_MAX = 30                               # NUM-1

NAME_RE = re.compile(r"^(\d{2})-([a-z0-9][a-z0-9-]*)\.md$")
PROJECT_ID_RE = re.compile(r"^[a-z][a-z0-9-]{2,19}$")
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
IMG_RE = re.compile(r"<img[^>]+src=[\"']([^\"']+)[\"']")
PLACEHOLDER_RE = re.compile(r"\{\{([a-z_][a-z0-9_.]*)\}\}")
FENCE_RE = re.compile(r"^\s*(```|~~~)")
NUMBERED_STEP_RE = re.compile(r"^\s*\d+\.\s+\S")
CHECKBOX_RE = re.compile(r"^\s*[-*]\s+\[[ xX]\]")
FM_KEY_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*)\s*:\s*(.*)$")
CR_PATH_RE = re.compile(r"(?<![\w./-])\.clinerules/([A-Za-z0-9._/-]+)")

# A7 — 사전으로 잡을 수 없는 '프로젝트 귀속 식별자'. 형식은 범용이나 값은 그 프로젝트 이력에만 참이다.
IDENT_PATTERNS = (
    (re.compile(r"\bREQ-\d{4}-\d{2,3}\b"), "요구사항·CR ID"),
    (re.compile(r"(?<![\w.])[vV]\d+\.\d+\.\d+(?!\w)"), "릴리스 버전"),
    # 커밋 해시: 숫자와 a-f 를 모두 포함하는 7~40자리 hex 만 (순수 숫자·순수 알파·`#` 색상값 제외)
    (re.compile(r"(?<![\w/.#])(?=[0-9a-f]*\d)(?=[0-9a-f]*[a-f])[0-9a-f]{7,40}(?![\w.])"),
     "커밋 해시"),
)


class Finding:
    __slots__ = ("path", "line", "check", "severity", "message")

    def __init__(self, path, line, check, severity, message):
        self.path = path
        self.line = line
        self.check = check
        self.severity = severity
        self.message = message

    def key(self):
        return f"{self.path}|{self.check}|{self.message}"

    def __str__(self):
        return f"{self.path}:{self.line}  [{self.check}] {self.severity}  {self.message}"


# ---------------------------------------------------------------- 유틸


def read(path: Path):
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return None


def strip_code_fences(lines):
    """코드블록 안은 예시이므로 링크·형식 검사에서 제외한다."""
    out, inside = [], False
    for i, ln in enumerate(lines, 1):
        if FENCE_RE.match(ln):
            inside = not inside
            out.append((i, "", True))
            continue
        out.append((i, ln, inside))
    return out


def md_files(root: Path):
    for p in sorted(root.rglob("*.md")):
        if any(part in SKIP_DIRS for part in p.relative_to(root).parts):
            continue
        yield p


# ---------------------------------------------------------------- 검사


def check_project_json(repo: Path, cr: Path, out: list):
    pj = repo / "project.json"
    rel = "project.json"
    if not pj.exists():
        out.append(Finding(rel, 1, "P1", "error", "project.json 이 없다"))
        return None
    try:
        cfg = json.loads(pj.read_text(encoding="utf-8"))
    except Exception as e:
        out.append(Finding(rel, 1, "P1", "error", f"JSON 파싱 실패: {e}"))
        return None

    pid = cfg.get("project_id", "")
    if not PROJECT_ID_RE.match(pid or ""):
        out.append(Finding(rel, 1, "P1", "error",
                           f"project_id 형식 위반: {pid!r} (^[a-z][a-z0-9-]{{2,19}}$)"))
    for k in ("schema_version", "project_name", "guideline"):
        if k not in cfg:
            out.append(Finding(rel, 1, "P1", "error", f"필수 키 누락: {k}"))

    g = cfg.get("guideline", {})
    expect = f"projects/{pid}"
    if g.get("project_dir") != expect:
        out.append(Finding(rel, 1, "P2", "error",
                           f"guideline.project_dir 는 {expect!r} 여야 한다 "
                           f"(현재 {g.get('project_dir')!r})"))

    for k, v in (cfg.get("paths") or {}).items():
        if not (repo / v).exists():
            out.append(Finding(rel, 1, "P3", "warn", f"paths.{k} 경로 없음: {v}"))
    ep = cfg.get("entrypoint")
    if ep and not (repo / ep).exists():
        out.append(Finding(rel, 1, "P3", "warn", f"entrypoint 경로 없음: {ep}"))
    return cfg


def flatten_keys(cfg, prefix=""):
    keys = set()
    for k, v in cfg.items():
        full = f"{prefix}{k}"
        keys.add(full)
        if isinstance(v, dict):
            keys |= flatten_keys(v, full + ".")
    return keys


def check_placeholders(cr: Path, cfg, out: list):
    if not cfg:
        return
    valid = flatten_keys(cfg)
    for p in md_files(cr):
        txt = read(p)
        if txt is None:
            continue
        rel = p.relative_to(cr).as_posix()
        for i, ln in enumerate(txt.splitlines(), 1):
            for m in PLACEHOLDER_RE.finditer(ln):
                if m.group(1) not in valid:
                    out.append(Finding(rel, i, "P4", "error",
                                       f"정의되지 않은 플레이스홀더: {{{{{m.group(1)}}}}}"))


def load_registry(cr: Path):
    """PROJECTS-REGISTRY.md 금칙어 표에서 분류별 토큰을 읽는다.

    반환: {project_id: {"name": [...], "path": [...]}}
    정본은 3열(`project_id` | 분류 | 금칙어)이며, 2열 구형식은 전부 '이름'으로 본다.
    첫 칸이 `project_id` 형식이 아닌 행(설명용 표·헤더)은 무시한다.
    """
    reg = cr / "common" / "PROJECTS-REGISTRY.md"
    tokens: dict = {}
    if not reg.exists():
        return tokens
    section = False
    for ln in reg.read_text(encoding="utf-8").splitlines():
        if ln.startswith("## 금칙어"):
            section = True
            continue
        if section and ln.startswith("## "):
            break
        if not (section and ln.startswith("|") and "`" in ln):
            continue
        cells = [c.strip() for c in ln.strip("|").split("|")]
        if len(cells) < 2:
            continue
        pid = cells[0].strip("` ")
        if not PROJECT_ID_RE.match(pid):
            continue
        if len(cells) >= 3:
            cls = "path" if ("경로" in cells[1] or "구조" in cells[1]) else "name"
            words = re.findall(r"`([^`]+)`", cells[2])
        else:
            cls, words = "name", re.findall(r"`([^`]+)`", cells[1])
        if not words:
            continue
        slot = tokens.setdefault(pid, {"name": [], "path": []})
        slot[cls].extend(words)
    return tokens


def registry_class(tokens: dict, cls: str, pids=None):
    """분류별 토큰을 소문자·길이 내림차순으로 모은다."""
    src = tokens if pids is None else {k: v for k, v in tokens.items() if k in pids}
    return sorted({w.lower() for t in src.values() for w in t.get(cls, [])},
                  key=len, reverse=True)


def path_matchers(words):
    """경로·구조 토큰 매칭기.

    - 경로 토큰(`/` 포함)은 앞 경계를 본다 — `statistics_dao/` 를 `dao/` 로 치지 않는다.
    - 이름형 토큰(테이블·폴더명)은 부분 문자열로 본다 — `IDX_TB_STS_CD_MST_USE` 처럼
      접두·접미가 붙어도 그 프로젝트의 테이블을 가리키는 건 같다.
    - 슬래시로 끝나는 토큰은 뒤에 대문자가 오면 넘긴다 — `DDL/SQL`·`DAO/SQL` 처럼
      개념을 나열한 슬래시이지 폴더 경로가 아니다. 그래서 원문(대소문자 보존)에 대고 찾는다.
    """
    out = []
    for w in words:
        pat = (r"(?<![A-Za-z0-9_])" if "/" in w else "") + re.escape(w)
        if w.endswith("/"):
            # (?-i:) 로 대소문자 구분을 되살린다 — IGNORECASE 아래서 [A-Z] 는 소문자도 잡는다
            pat += r"(?!(?-i:[A-Z]))"
        out.append((w, re.compile(pat, re.IGNORECASE)))
    return out


def first_path_hit(matchers, text):
    for w, rx in matchers:
        if rx.search(text):
            return w
    return None


def check_isolation(cr: Path, cfg, out: list):
    pid = (cfg or {}).get("project_id", "")
    tokens = load_registry(cr)
    allwords = registry_class(tokens, "name")
    path_words = registry_class(tokens, "path")
    own_paths = set(registry_class(tokens, "path", pids={pid}))
    own_path_rx = path_matchers(sorted(own_paths, key=len, reverse=True))
    other_path_rx = path_matchers([w for w in path_words if w not in own_paths])

    # ISO-9 자가진단 — 사전이 없거나 한 분류라도 비면 L2·L6·A3·A4·A6 이 조용히 꺼진다.
    # 파일 부재 자체가 실패다: 레지스트리를 안 옮긴 저장소에서 오염이 0건으로 통과한 사례가 있다.
    if not (cr / "common" / "PROJECTS-REGISTRY.md").exists():
        out.append(Finding("common/PROJECTS-REGISTRY.md", 1, "L2", "error",
                           "금칙어 사전 파일이 없다 "
                           "(격리 검사 L2·L6·A3·A4·A6 가 전부 무력화된다 — 정본에서 함께 가져올 것)"))
    elif not allwords or not path_words:
        empty = "이름" if not allwords else "경로·구조"
        out.append(Finding("common/PROJECTS-REGISTRY.md", 1, "L2", "error",
                           f"금칙어 사전의 '{empty}' 분류를 한 건도 읽지 못했다 "
                           "(표 형식 확인 — 격리 검사가 무력화된다)"))

    common = cr / "common"
    # 레지스트리 자신은 금칙어 사전이므로 격리 검사 면제
    exempt = {"PROJECTS-REGISTRY.md"}
    concrete = [pid for pid in tokens]
    if common.exists():
        for p in md_files(common):
            if p.name in exempt:
                continue
            txt = read(p)
            if txt is None:
                continue
            rel = p.relative_to(cr).as_posix()
            for i, ln, inside in strip_code_fences(txt.splitlines()):
                low = ln.lower()
                # L1 은 "projects/" 라는 개념어가 아니라 구체 프로젝트 경로만 잡는다
                for other_pid in concrete:
                    if f"projects/{other_pid}" in low:
                        out.append(Finding(rel, i, "L1", "error",
                                           f"common/ 문서가 구체 프로젝트 경로 참조: projects/{other_pid}"))
                        break
                for w in allwords:
                    if w in low:
                        out.append(Finding(rel, i, "L2", "error",
                                           f"common/ 에 프로젝트 고유어: {w!r}"))
                        break
                hit = first_path_hit(other_path_rx, ln)   # L6 — 구조 가정 (ISO-7)
                if hit:
                    out.append(Finding(rel, i, "L6", "error",
                                       f"common/ 에 타 프로젝트 구조 토큰: {hit!r} "
                                       "(그 계층은 이 프로젝트에 없다 — 이식 오염)"))
                else:
                    hit = first_path_hit(own_path_rx, ln)
                    if hit:
                        out.append(Finding(rel, i, "L6", "warn",
                                           f"common/ 에 프로젝트 구조 토큰: {hit!r} "
                                           "(경로·계층 가정도 프로젝트 고유값 — 플레이스홀더화 또는 projects/ 로 강등)"))

    projects = cr / "projects"
    if projects.exists():
        dirs = [d.name for d in projects.iterdir() if d.is_dir()]
        for d in dirs:
            if d != pid:
                out.append(Finding(f"projects/{d}", 1, "L4", "error",
                                   f"자기 프로젝트({pid}) 외 폴더가 존재"))
        for p in md_files(projects):
            rel = p.relative_to(cr).as_posix()
            txt = read(p)
            if txt is None:
                continue
            for other in dirs:
                if other == pid:
                    continue
                for i, ln in enumerate(txt.splitlines(), 1):
                    if f"projects/{other}" in ln:
                        out.append(Finding(rel, i, "L3", "error",
                                           f"타 프로젝트 참조: projects/{other}"))
    else:
        out.append(Finding("projects", 1, "L4", "error", "projects/ 구역이 없다"))

    tops = {d.name for d in cr.iterdir() if d.is_dir() and d.name != ".git"}
    for missing in ZONES - tops:
        out.append(Finding(missing, 1, "L5", "error", f"구역 폴더 누락: {missing}/"))
    for extra in tops - ZONES:
        out.append(Finding(extra, 1, "L5", "error", f"정의되지 않은 최상위 폴더: {extra}/"))


def in_numbered_zone(rel_parts):
    return tuple(rel_parts[:2]) == NUMBERED_ZONE


def check_numbering(cr: Path, out: list):
    seen = defaultdict(list)  # (dir, NN) -> [name]
    for p in md_files(cr):
        rel = p.relative_to(cr)
        relstr = rel.as_posix()
        name = p.name
        numbered_zone = in_numbered_zone(rel.parts)

        if name in META_FILES:
            continue

        m = NAME_RE.match(name)
        if not m:
            if numbered_zone:
                out.append(Finding(relstr, 1, "N2", "error",
                                   "번호 필수 구역인데 NN-<slug>.md 형식이 아니다"))
            elif (re.search(r"[A-Z_]", name.replace(".md", ""))
                  and name not in META_FILES
                  and rel.parts[0] == "common"
                  and not (p.parent / p.stem).is_dir()):
                out.append(Finding(relstr, 1, "N4", "warn",
                                   "소문자 케밥 권장 (대문자·언더스코어 사용)"))
            continue

        nn, slug = m.group(1), m.group(2)
        if len(slug) > SLUG_MAX:
            out.append(Finding(relstr, 1, "N4", "error",
                               f"slug {len(slug)}자 — 상한 {SLUG_MAX}자"))
        seen[(rel.parent.as_posix(), nn)].append(name)

    for (d, nn), names in sorted(seen.items()):
        if len(names) > 1:
            out.append(Finding(f"{d}/", 1, "N1", "error",
                               f"번호 {nn} 중복: {', '.join(sorted(names))}"))

    # N5: 나침반 파일명 == 하위 폴더명
    for p in md_files(cr):
        sib = p.parent / p.stem
        if sib.is_dir():
            continue
    for d in sorted(cr.rglob("*")):
        if not d.is_dir() or any(x in d.parts for x in SKIP_DIRS | {".git"}):
            continue
        rel_parts = d.relative_to(cr).parts
        if len(rel_parts) <= 2 and rel_parts[0] in ZONES:
            continue
        parent_md = d.parent / (d.name + ".md")
        readme = d / "README.md"
        if not parent_md.exists() and not readme.exists() and d.name != "images":
            rel = d.relative_to(cr).as_posix()
            if in_numbered_zone(d.relative_to(cr).parts):
                out.append(Finding(f"{rel}/", 1, "N5", "warn",
                                   "동명 나침반 파일도 README.md 도 없다"))


def check_numbers_ledger(cr: Path, out: list):
    led = cr / "NUMBERS.md"
    if not led.exists():
        out.append(Finding("NUMBERS.md", 1, "N3", "error", "채번 대장이 없다"))
        return
    text = led.read_text(encoding="utf-8")
    # 수기 섹션(이동·결번 이력)의 구 경로가 오탐되지 않도록 등록 현황 이후만 대사한다
    _, _, tail = text.partition("## 번호 필수 구역 등록 현황")
    listed = set(re.findall(r"`([^`]+\.md)`", tail or text))
    actual = set()
    for p in md_files(cr / "common" / "core"):
        # README 도 대장에 등재한다(무번호 허용 표기). 대장 생성기와 대사 범위를 맞춘다.
        actual.add(p.relative_to(cr).as_posix())
    for miss in sorted(actual - listed):
        out.append(Finding(miss, 1, "N3", "error", "대장(NUMBERS.md)에 미등재"))
    for ghost in sorted(listed - actual):
        if ghost.startswith("common/core/"):
            out.append(Finding("NUMBERS.md", 1, "N3", "warn",
                               f"대장에 있으나 파일 없음: {ghost} (결번이면 상태를 '삭제'로 표기)"))


def is_compass(p: Path, cr: Path) -> bool:
    """CMP-1 구조 기반 판정. 폴더의 나침반은 하나뿐이다."""
    if (p.parent / p.stem).is_dir():
        return True
    if p.name == "CLAUDE.md":
        return True
    # 00-* 는 '번호 필수 구역'에서만 나침반이다.
    # 사전형 폴더의 00- 은 단순 첫 문서(예: 양식 정본)일 수 있다.
    if p.name.startswith("00-") and in_numbered_zone(p.relative_to(cr).parts):
        return True
    if p.name == "README.md":
        # 동명 상위 나침반(`<폴더명>.md`)이 있으면 그쪽이 나침반이고 README 는 상세 문서다
        if (p.parent.parent / (p.parent.name + ".md")).exists():
            return False
        if p.parent.parent.name == "projects":
            return True
        sibs = [x for x in p.parent.glob("*.md") if x.name != "README.md"]
        if len(sibs) >= 2:
            return True
    return False


def check_compass(cr: Path, out: list):
    for p in md_files(cr):
        txt = read(p)
        if txt is None:
            continue
        rel = p.relative_to(cr).as_posix()
        lines = txt.splitlines()
        n = len(lines)
        compass = is_compass(p, cr)
        if p.name in GENERATED or p.name in META_FILES - {"README.md"}:
            continue

        if compass:
            if n > COMPASS_MAX:
                out.append(Finding(rel, 1, "C1", "error",
                                   f"나침반 {n}줄 — 상한 {COMPASS_MAX}줄"))
            if "🧭" not in txt:
                out.append(Finding(rel, 1, "C4", "warn", "나침반 배지 없음"))
            for i, ln, inside in strip_code_fences(lines):
                if inside or not ln:
                    continue
                if FENCE_RE.match(ln):
                    continue
                if CHECKBOX_RE.match(ln):
                    out.append(Finding(rel, i, "C3", "error", "나침반에 체크리스트 금지"))
                elif NUMBERED_STEP_RE.match(ln) and not ln.lstrip().startswith("|"):
                    out.append(Finding(rel, i, "C3", "warn", "나침반에 절차 서술 금지"))
            if (p.parent / p.stem).is_dir() and "|" not in txt:
                out.append(Finding(rel, 1, "C5", "error",
                                   "하위 폴더를 가진 나침반에 라우팅 표가 없다"))
        else:
            if n > DETAIL_MAX:
                out.append(Finding(rel, 1, "C2", "error",
                                   f"상세 문서 {n}줄 — 상한 {DETAIL_MAX}줄"))
            elif n > DETAIL_WARN:
                out.append(Finding(rel, 1, "C2", "warn",
                                   f"상세 문서 {n}줄 — 권장 {DETAIL_WARN}줄"))


def check_links(cr: Path, out: list):
    for p in md_files(cr):
        txt = read(p)
        if txt is None:
            out.append(Finding(p.relative_to(cr).as_posix(), 1, "K1", "warn",
                               "UTF-8 이 아니라 검사 불가"))
            continue
        rel = p.relative_to(cr).as_posix()
        for i, ln, inside in strip_code_fences(txt.splitlines()):
            if inside:
                continue
            for m in LINK_RE.finditer(ln):
                t = m.group(1)
                if t.startswith(("http://", "https://", "#", "mailto:")):
                    continue
                t = t.split("#")[0]
                if not t or any(c in t for c in "{<[…") or not t.isascii():
                    continue
                if not (p.parent / t).exists():
                    out.append(Finding(rel, i, "K1", "error", f"링크 해소 실패: {t}"))
            for m in IMG_RE.finditer(ln):
                t = m.group(1)
                if t.startswith(("http://", "https://", "data:")):
                    continue
                if any(c in t for c in "{<[…") or not t.isascii():
                    continue
                if not (p.parent / t).exists():
                    out.append(Finding(rel, i, "K2", "error", f"이미지 없음: {t}"))


# ---------------------------------------------------------------- 에이전트 정의 (AGT)


def agent_files(repo: Path):
    """저장소 루트의 .claude/agents/*.md. 폴더가 없으면 빈 목록(다른 프로젝트 대응)."""
    d = repo.joinpath(*AGENT_DIR)
    if not d.is_dir():
        return []
    return sorted(p for p in d.glob("*.md") if p.is_file())


def parse_frontmatter(lines):
    """`---` 로 감싼 프론트매터의 최상위 키를 읽는다. 실패하면 None."""
    if not lines or lines[0].strip() != "---":
        return None
    keys = {}
    last = None
    for ln in lines[1:]:
        if ln.strip() == "---":
            return keys
        if ln[:1] in (" ", "\t", "-"):      # 중첩·목록 줄은 최상위 키가 아니다
            # 값이 빈 키 뒤의 들여쓰기·목록 줄은 그 키의 값이다(YAML 블록/리스트).
            # 이 처리가 없으면 `tools:` + `  - Read` 형식이 '값 없음'으로 오검출된다.
            if last and not keys.get(last) and ln.strip():
                keys[last] = "<block>"
            continue
        m = FM_KEY_RE.match(ln.strip())
        if m:
            keys[m.group(1)] = m.group(2).strip()
            last = m.group(1)
        else:
            last = None
    return None                             # 닫는 --- 없음


def check_agent_definitions(repo: Path, cr: Path, cfg, out: list):
    """common/core/26-agent-definitions.md 의 AGT-1~5 검사."""
    files = agent_files(repo)
    if not files:
        return
    prefix = "/".join(AGENT_DIR)
    pid = (cfg or {}).get("project_id", "")
    tokens = load_registry(cr)
    own = set(registry_class(tokens, "name", pids={pid}))
    others = [w for w in registry_class(tokens, "name") if w not in own]
    own_sorted = sorted(own, key=len, reverse=True)
    own_paths = set(registry_class(tokens, "path", pids={pid}))
    own_path_rx = path_matchers(sorted(own_paths, key=len, reverse=True))
    other_path_rx = path_matchers([w for w in registry_class(tokens, "path")
                                   if w not in own_paths])

    names = defaultdict(list)
    for p in files:
        rel = f"{prefix}/{p.name}"
        txt = read(p)
        if txt is None:
            out.append(Finding(rel, 1, "A1", "error", "UTF-8 이 아니라 검사 불가"))
            continue
        lines = txt.splitlines()

        # A1·A2 — 카탈로그(README.md)는 정의가 아니므로 면제 (26 §4)
        if p.name != "README.md":
            fm = parse_frontmatter(lines)
            if fm is None:
                out.append(Finding(rel, 1, "A1", "error", "프론트매터(--- 블록) 파싱 실패"))
            else:
                for k in AGENT_FM_KEYS:
                    if not fm.get(k):
                        out.append(Finding(rel, 1, "A1", "error",
                                           f"프론트매터 필수 키 누락: {k}"))
                nm = fm.get("name", "")
                if nm and nm != p.stem:
                    out.append(Finding(rel, 1, "A2", "error",
                                       f"name({nm!r}) 이 파일명({p.stem!r})과 다르다"))
                if nm:
                    names[nm].append(p.name)

        for i, ln, inside in strip_code_fences(lines):
            if inside or not ln:
                continue
            low = ln.lower()
            for w in others:                                     # A3 — 타 프로젝트 오염
                if w in low:
                    out.append(Finding(rel, i, "A3", "error",
                                       f"타 프로젝트 고유어: {w!r}"))
                    break
            else:
                for w in own_sorted:                             # A4 — 자기 고유값 하드코딩
                    if w in low:
                        out.append(Finding(
                            rel, i, "A4", "warn",
                            f"자기 프로젝트 고유값 하드코딩: {w!r} "
                            "(플레이스홀더 또는 프로젝트 지침 문서 참조로 외재화)"))
                        break
            hit = first_path_hit(other_path_rx, ln)               # A6 — 구조 가정 (AGT-8)
            if hit:
                out.append(Finding(rel, i, "A6", "error",
                                   f"타 프로젝트 구조 토큰: {hit!r} "
                                   "(그 계층은 이 프로젝트에 없다 — 이식 오염)"))
            else:
                hit = first_path_hit(own_path_rx, ln)
                if hit:
                    out.append(Finding(rel, i, "A6", "warn",
                                       f"자기 프로젝트 구조 토큰 하드코딩: {hit!r} "
                                       "(프로젝트 지침 문서 참조로 외재화)"))
            for rx, kind in IDENT_PATTERNS:                       # A7 — 귀속 식별자 (AGT-9)
                m = rx.search(ln)
                if m:
                    out.append(Finding(rel, i, "A7", "warn",
                                       f"프로젝트 귀속 식별자({kind}): {m.group(0)!r} "
                                       "(사고 이력은 domain-locks.md 로 외재화)"))
                    break
            for m in CR_PATH_RE.finditer(ln):                    # A5 — 참조 실존
                t = m.group(1).rstrip(".,)·")
                if t and not (cr / t).exists():
                    out.append(Finding(rel, i, "A5", "warn",
                                       f"지침 경로 없음: .clinerules/{t}"))

    for nm, fs in sorted(names.items()):
        if len(fs) > 1:
            out.append(Finding(f"{prefix}/", 1, "A2", "error",
                               f"name 중복: {nm} ({', '.join(fs)})"))


# ---------------------------------------------------------------- main


def display_path(repo: Path, cr: Path, rel: str) -> Path:
    """Finding.path 는 지침 저장소 기준이 기본이나, 일부는 저장소 루트 기준이다."""
    if rel.startswith(REPO_RELATIVE):
        return repo / rel
    return cr / rel


def main():
    ap = argparse.ArgumentParser(description="지침 저장소 린터")
    ap.add_argument("--repo", default=None, help="저장소 루트 (기본: 자동 탐지)")
    ap.add_argument("--severity", choices=["error", "warn", "all"], default="all")
    ap.add_argument("--baseline", default=None, help="기존 위반 목록 파일")
    ap.add_argument("--write-baseline", default=None, help="현재 위반을 baseline 으로 저장")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    here = Path(__file__).resolve()
    cr = here.parent.parent
    repo = Path(args.repo).resolve() if args.repo else cr.parent

    out: list[Finding] = []
    cfg = check_project_json(repo, cr, out)
    check_placeholders(cr, cfg, out)
    check_isolation(cr, cfg, out)
    check_numbering(cr, out)
    check_numbers_ledger(cr, out)
    check_compass(cr, out)
    check_links(cr, out)
    check_agent_definitions(repo, cr, cfg, out)

    if args.write_baseline:
        Path(args.write_baseline).write_text(
            "\n".join(sorted(f.key() for f in out)) + "\n", encoding="utf-8")
        print(f"baseline 저장: {args.write_baseline} ({len(out)}건)")
        return 0

    base = set()
    if args.baseline and Path(args.baseline).exists():
        base = set(Path(args.baseline).read_text(encoding="utf-8").split("\n"))
        out = [f for f in out if f.key() not in base]

    if args.severity != "all":
        out = [f for f in out if f.severity == args.severity]

    order = {"error": 0, "warn": 1}
    out.sort(key=lambda f: (order[f.severity], f.check, f.path, f.line))

    if args.json:
        print(json.dumps([{"path": f.path, "line": f.line, "check": f.check,
                           "severity": f.severity, "message": f.message}
                          for f in out], ensure_ascii=False, indent=2))
    else:
        for f in out:
            print(f"{display_path(repo, cr, f.path)}:{f.line}  [{f.check}] "
                  f"{f.severity}  {f.message}")
        errs = sum(1 for f in out if f.severity == "error")
        warns = sum(1 for f in out if f.severity == "warn")
        nfiles = sum(1 for _ in md_files(cr))
        nagents = len(agent_files(repo))
        print(f"\n요약: error {errs} / warn {warns}  "
              f"(지침 문서 {nfiles} + 에이전트 정의 {nagents})")

    return 1 if any(f.severity == "error" for f in out) else 0


if __name__ == "__main__":
    sys.exit(main())
