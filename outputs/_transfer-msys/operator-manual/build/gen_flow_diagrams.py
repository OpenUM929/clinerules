# -*- coding: utf-8 -*-
"""메뉴 문서의 '전체 데이터 흐름도'·'전체 화면 구조' ASCII 아트를 실제 PNG 이미지로 렌더링.
matplotlib만 사용(외부 폰트/graphviz 의존 없음). 한글 폰트는 Malgun Gothic 사용.

사용법: python gen_flow_diagrams.py <출력폴더>
  - DIAGRAMS(데이터 흐름도, 박스+화살표)와 WIREFRAMES(화면 구조, 스택 패널) 둘 다 생성.
"""
import textwrap
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.patches import FancyBboxPatch
from matplotlib.patches import FancyArrowPatch

FONT_PATH = r"C:\Windows\Fonts\malgun.ttf"
try:
    fm.fontManager.addfont(FONT_PATH)
    FONT_NAME = fm.FontProperties(fname=FONT_PATH).get_name()
except Exception:
    FONT_NAME = "Malgun Gothic"
plt.rcParams["font.family"] = FONT_NAME
plt.rcParams["axes.unicode_minus"] = False

BOX_W = 2.6
BOX_H = 0.62
ROW_GAP = 0.95
COL_GAP = 3.0


def wrap(text, width=18):
    return "\n".join(textwrap.wrap(text, width=width, break_long_words=False)) or text


def draw_box(ax, x, y, text, w=BOX_W, h=BOX_H, fc="#f2f2f2", ec="#333333"):
    box = FancyBboxPatch(
        (x - w / 2, y - h / 2), w, h,
        boxstyle="round,pad=0.06,rounding_size=0.06",
        linewidth=1.1, edgecolor=ec, facecolor=fc, zorder=2,
    )
    ax.add_patch(box)
    ax.text(x, y, wrap(text), ha="center", va="center", fontsize=9.5, zorder=3)


def arrow(ax, xy_from, xy_to, color="#555555"):
    a = FancyArrowPatch(
        xy_from, xy_to, arrowstyle="-|>", mutation_scale=12,
        linewidth=1.1, color=color, shrinkA=2, shrinkB=2, zorder=1,
    )
    ax.add_patch(a)


def render(out_path, head, branches=None, tail=None, title=None):
    """head: list[str] 세로 순차 박스. branches: [[str,...], [str,...], [str,...]] 3열 병렬.
    tail: 병합 후 세로 순차 박스(branches 없으면 무시)."""
    n_head = len(head)
    n_branch_rows = max((len(b) for b in branches), default=0) if branches else 0
    n_tail = len(tail) if tail else 0

    total_rows = n_head + (n_branch_rows if branches else 0) + n_tail
    fig_h = max(2.2, total_rows * ROW_GAP + 0.8)
    fig_w = COL_GAP * 2 + BOX_W + 1.0 if branches else BOX_W + 2.0
    fig, ax = plt.subplots(figsize=(fig_w, fig_h), dpi=150)
    ax.set_xlim(-fig_w / 2, fig_w / 2)
    ax.set_ylim(-total_rows * ROW_GAP - 0.4, 0.6)
    ax.axis("off")

    y = 0.0
    cx = 0.0
    prev_xy = None
    for label in head:
        draw_box(ax, cx, y, label)
        if prev_xy is not None:
            arrow(ax, (prev_xy[0], prev_xy[1] - BOX_H / 2), (cx, y + BOX_H / 2))
        prev_xy = (cx, y)
        y -= ROW_GAP

    if branches:
        split_y = y + ROW_GAP / 2
        col_x = [-COL_GAP, 0.0, COL_GAP]
        top_branch_y = y
        for cxi in col_x:
            arrow(ax, (cx, prev_xy[1] - BOX_H / 2), (cxi, top_branch_y + BOX_H / 2))
        col_prev_y = [None, None, None]
        for r in range(n_branch_rows):
            for ci, branch in enumerate(branches):
                if r >= len(branch):
                    continue
                by = y
                draw_box(ax, col_x[ci], by, branch[r])
                if col_prev_y[ci] is not None:
                    arrow(ax, (col_x[ci], col_prev_y[ci] - BOX_H / 2), (col_x[ci], by + BOX_H / 2))
                col_prev_y[ci] = by
            y -= ROW_GAP
        merge_y = y
        if tail:
            for ci in range(3):
                if col_prev_y[ci] is not None:
                    arrow(ax, (col_x[ci], col_prev_y[ci] - BOX_H / 2), (cx, merge_y + BOX_H / 2 - ROW_GAP + ROW_GAP))
            prev_xy = (cx, merge_y + ROW_GAP)
            y = merge_y
            for label in tail:
                draw_box(ax, cx, y, label)
                arrow(ax, (prev_xy[0], prev_xy[1] - BOX_H / 2), (cx, y + BOX_H / 2))
                prev_xy = (cx, y)
                y -= ROW_GAP

    plt.tight_layout(pad=0.3)
    fig.savefig(out_path, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"[ok] {out_path}")


# --- 09개 메뉴별 흐름도 정의 -------------------------------------------------
DIAGRAMS = {}

DIAGRAMS["01-dashboard"] = dict(
    head=["사용자", "dashboard.html", "dashboard.js", "events.js",
          "fetchDashboardSummary()", "GET /api/dashboard/summary",
          "DashboardService.get_summary()"],
    branches=[
        ["DashboardMapper", "DashboardSQL.get_summary()", "TB_CON_HIST (과거 데이터)"],
        ["CollectionScheduleService", "get_schedule_only()", "TB_CON_HIST + 스케줄 (오늘 데이터)"],
        ["MngrSettMapper", "get_all_settings()", "TB_MNGR_SETT"],
    ],
    tail=["_combine_historical_and_today_data()",
          "_apply_settings_and_filters() (CHRT_DSP_YN 필터)",
          "_add_fail_streaks() (연속 실패 계산)",
          "JSON 응답 → updateSummaryCards() + renderDashboardSummaryTable()"],
)

DIAGRAMS["02-collection-schedule"] = dict(
    head=["사용자", "collection_schedule.html", "collection_schedule.js",
          "fetch('/api/collection_schedule')", "collection_schedule_routes.py",
          "CollectionScheduleService.get_schedule_only()"],
    branches=[
        ["_generate_scheduled_tasks()", "cron + tb_con_mst", "예정된 스케줄 생성"],
        ["_fetch_and_group_history_data()", "DashboardMapper", "TB_CON_HIST 조회 (실제 실행 기록)"],
        ["MngrSettService", "tb_mngr_sett", "그룹화 임계값"],
    ],
    tail=["_match_schedule_with_history()", "날짜별 순차 매칭 → 상태 결정",
          "JSON 응답 → 캘린더 그리드 렌더링"],
)

DIAGRAMS["03-chart-analysis"] = dict(
    head=["사용자", "chart_analysis.html", "chart_analysis.js",
          "fetch('/api/chart_data')", "analysis_routes.py",
          "AnalysisService.get_dynamic_chart_data()"],
    branches=[
        ["AnalysisMapper", "sql/analytics/analytics_sql.py", "TB_CON_HIST 집계"],
        ["UserMapper", "data_permissions 조회", "TB_USER_DATA_PERM_AUTH_CTRL"],
        ["MstMapper", "Job ID 목록", "TB_CON_MST"],
    ],
    tail=["JSON 응답 → Chart.js 렌더링"],
)

DIAGRAMS["04-data-analysis"] = dict(
    head=["사용자", "data_analysis.html", "data_analysis.js",
          "fetch('/api/data_analysis')", "analysis_routes.py", "AnalysisService"],
    branches=[
        ["AnalysisMapper", "sql/analytics/analytics_sql.py", "TB_CON_HIST 집계"],
        ["UserMapper", "data_permissions 조회", "TB_USER_DATA_PERM_AUTH_CTRL"],
        ["MstMapper", "Job ID 목록", "TB_CON_MST"],
    ],
    tail=["JSON 응답 → 테이블 렌더링"],
)

DIAGRAMS["05-data-spec"] = dict(
    head=["사용자", "data_spec.html", "data_spec.js"],
    branches=[
        ["메타데이터 파싱", "JSON/XML 파서", "폼 필드 채움", "모달 표시"],
        ["명세서 CRUD", "API 호출", "DB 저장/조회", "목록 갱신"],
        ["URL 분석", "HTTP 요청", "응답 파싱", "파라미터 추출"],
    ],
    tail=None,
)

DIAGRAMS["06-card-summary"] = dict(
    head=["사용자", "card_summary.html", "card_summary.js",
          "fetch('/api/card_summary')", "card_summary_routes.py",
          "CardSummaryService.get_summary()"],
    branches=[
        ["CardSummaryMapper", "sql/card_summary/*.sql", "TB_CON_HIST 집계"],
        ["UserMapper", "data_permissions 조회", "TB_USER_DATA_PERM_AUTH_CTRL"],
        ["MngrSettMapper", "설정 정보", "TB_MNGR_SETT"],
    ],
    tail=["JSON 응답 → 카드 렌더링"],
)

DIAGRAMS["07-mapping"] = dict(
    head=["사용자", "mapping_management.html", "mapping.js",
          "fetch('/api/mappings')", "mapping_routes.py", "MappingService",
          "MappingMapper", "sql/mapping/*.sql", "TB_COL_MAPP"],
    branches=None, tail=None,
)

DIAGRAMS["08-api-key-mngr"] = dict(
    head=["사용자", "api_key_mngr.html", "api_key_mngr.js",
          "fetch('/api/api_key_mngr')", "api_key_mngr_routes.py",
          "ApiKeyMngrService", "ApiKeyMngrMapper", "TB_API_KEY_MNGR",
          "메일 스케줄러 연동"],
    branches=None, tail=None,
)

DIAGRAMS["09-jandi"] = dict(
    head=["사용자", "jandi.html", "jandi.js", "fetch('/api/jandi')",
          "jandi_routes.py", "JandiService", "JandiMapper",
          "sql/jandi/jandi_sql.py", "TB_CON_HIST",
          "JSON 응답 → SVG 히트맵 렌더링"],
    branches=None, tail=None,
)

# --------------------------------------------------------------------------- #
# 화면 구조(wireframe) 렌더링 — 실캡처 화면이 없는 메뉴의 "전체 화면 구조" ascii 대체
# --------------------------------------------------------------------------- #
def _panel_height(p):
    h = 0.55
    h += 0.34 * len(p.get("lines", []))
    if p.get("table"):
        h += 0.85
    if p.get("inner_box"):
        h += 1.35
    return h + 0.22


def draw_wireframe(out_path, panels, width=9.0):
    heights = [_panel_height(p) for p in panels]
    total_h = sum(heights) + 0.3
    fig, ax = plt.subplots(figsize=(width, max(2.4, total_h)), dpi=150)
    ax.set_xlim(0, width)
    ax.set_ylim(-total_h, 0.3)
    ax.axis("off")
    outer = FancyBboxPatch(
        (0.08, -total_h + 0.08), width - 0.16, total_h - 0.16,
        boxstyle="round,pad=0.02,rounding_size=0.05",
        linewidth=1.3, edgecolor="#333333", facecolor="white", zorder=1,
    )
    ax.add_patch(outer)

    y = -0.15
    first = True
    for p, h in zip(panels, heights):
        if not first:
            ax.plot([0.2, width - 0.2], [y, y], color="#aaaaaa", linewidth=0.8, zorder=2)
        first = False
        cy = y - 0.34
        ax.text(0.4, cy, p["title"], fontsize=11, fontweight="bold",
                va="center", ha="left", zorder=3, color="#1a1a1a")
        cy -= 0.34
        for line in p.get("lines", []):
            ax.text(0.4, cy, line, fontsize=9, va="center", ha="left",
                    zorder=3, color="#444444")
            cy -= 0.3
        if p.get("inner_box"):
            box_w = width - 0.8
            box_h = 1.05
            rect = plt.Rectangle((0.4, cy - box_h), box_w, box_h,
                                  linewidth=0.9, edgecolor="#777777",
                                  facecolor="#fafafa", linestyle="--", zorder=2)
            ax.add_patch(rect)
            ax.text(0.4 + box_w / 2, cy - box_h / 2, wrap(p["inner_box"], 40),
                    fontsize=8.8, ha="center", va="center", color="#555555", zorder=3)
            cy -= box_h + 0.15
        if p.get("table"):
            cols = p["table"]
            tbl_w = width - 0.8
            col_w = tbl_w / len(cols)
            tbl_top = cy - 0.05
            tbl_h = 0.6
            for i, col in enumerate(cols):
                cxp = 0.4 + i * col_w
                rect = plt.Rectangle((cxp, tbl_top - tbl_h), col_w, tbl_h,
                                      linewidth=0.8, edgecolor="#777777",
                                      facecolor="#f2f2f2", zorder=2)
                ax.add_patch(rect)
                ax.text(cxp + col_w / 2, tbl_top - 0.3, wrap(col, 10),
                        fontsize=7.8, ha="center", va="center", zorder=3)
            cy = tbl_top - tbl_h - 0.18
        y -= h

    plt.tight_layout(pad=0.3)
    fig.savefig(out_path, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"[ok] {out_path}")


WIREFRAMES = {}

WIREFRAMES["07-mapping"] = [
    {"title": "컬럼 매핑 관리",
     "lines": ["데이터베이스 테이블 컬럼의 변경 이력을 관리하고 레거시 코드와의 호환성을 유지합니다."]},
    {"title": "매핑되지 않은 신규 컬럼", "lines": ["[새로고침]"],
     "table": ["테이블명", "컬럼명", "작업"]},
    {"title": "매핑 관리", "lines": ["[신규 매핑 추가]"],
     "table": ["ID", "이전 테이블", "이전 컬럼", "새 테이블", "새 컬럼", "설명", "작업"]},
]

WIREFRAMES["10-raw-data"] = [
    {"title": "필터 (접이식)",
     "lines": ["시작일: [____]   종료일: [____]   Job ID: [전체 ▼]   [조회]"]},
    {"title": "원본 데이터 테이블", "lines": ["총 1,234건   [검색]   [행 수: 20개 ▼]"],
     "table": ["날짜", "Job ID", "상태", "요청", "응답", "소요시간", "수집건수"]},
]

WIREFRAMES["11-admin"] = [
    {"title": "통계 탭 / 템플릿 탭", "lines": ["(탭 전환)"]},
    {"title": "통계 탭 내용", "lines": ["기간: [____] ~ [____]   메뉴: [전체 ▼]   [조회]"],
     "inner_box": "접근 통계 차트 (막대 / 선 / 파이 — 메뉴 접근 횟수 시각화)",
     "table": ["메뉴", "접근횟수", "사용자수", "평균체류"]},
    {"title": "템플릿 탭 내용", "lines": ["[파일 선택]   [업로드]"],
     "table": ["파일명", "크기", "등록일", "작업"]},
]

WIREFRAMES["12-api-test"] = [
    {"title": "요청 패널",
     "lines": ["URL: [__________________________________]",
               "메서드: [GET ▼]   Content-Type: [application/json ▼]", "헤더:"],
     "table": ["키", "값"]},
    {"title": "요청 바디 / 실행", "lines": ["{ \"param1\": \"value1\" }", "[실행]"]},
    {"title": "응답 패널", "lines": ["상태: 200 OK    소요시간: 245ms"],
     "inner_box": "{ \"result\": \"success\", \"data\": [...] }"},
]

if __name__ == "__main__":
    import sys
    out_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    for name, spec in DIAGRAMS.items():
        render(f"{out_dir}/{name}-data-flow.png", spec["head"],
               spec.get("branches"), spec.get("tail"))
    for name, panels in WIREFRAMES.items():
        draw_wireframe(f"{out_dir}/{name}-layout.png", panels)
