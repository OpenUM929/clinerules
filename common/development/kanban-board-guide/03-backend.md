# 백엔드 패턴 (Flask Blueprint)

> 상위 나침반 [`../kanban-board-guide.md`](../kanban-board-guide.md) 에서 분리.

## 3. 백엔드 패턴 (Flask Blueprint)

### 3.1 설정

```python
# config/settings.py
# 칸반보드 대상 베이스 디렉토리 (환경변수로 오버라이드 가능)
# 기본값은 project.json 의 paths.plans_root 를 따른다 (예: "work/plans")
PLANS_DIR = os.getenv('PLANS_DIR', os.path.join(PROJECT_ROOT, '{{paths.plans_root}}', '2026'))
```

### 3.2 관리자 인증 데코레이터

모든 칸반 라우트는 `admin_required` 데코레이터로 보호한다:

```python
def admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get('admin_logged_in'):
            if request.is_json:
                return jsonify({'success': False, 'error': '로그인이 필요합니다.'}), 401
            return render_template('admin_login.html', error='로그인이 필요합니다.')
        return f(*args, **kwargs)
    return decorated
```

### 3.3 라우트 명세

| 라우트 | 메서드 | 설명 | 인자 |
|--------|--------|------|------|
| `GET /admin/plans` | HTML | 보드 페이지 (칸반/CR/간트/추세 4탭) 서버사이드 렌더링 | 없음 |
| `GET /admin/api/plans/check` | JSON | `_index.md` 수정시각만 반환 (폴링용) | `?month=` (선택) |
| `GET /admin/api/plans` | JSON | 전체 항목 목록 (상태별 그룹) | `?month=` (선택, 필터) |
| `GET /admin/api/plans/<id>/content` | JSON | 특정 항목 메인 `.md` 원문 반환 | `?dir=` (월 폴더 경로) |
| `GET /admin/api/plans/cr-monthly` | JSON | CR 월별 집계 (별도 CR 폴더 연동) | 없음 |
| `GET /admin/api/plans/cr/<req_id>` | JSON | 특정 CR 상세 | 없음 |
| `GET /admin/api/plans/trend` | JSON | 연도별 월 추세(금·전년): CR건수/FP/공수/계획서건수 | `?year=` (선택) |
| `GET /admin/api/plans/trend-type` | JSON | 유형별 집계: `mode=monthly&year=` / `mode=yearly&mStart=&mEnd=` | 모드별 |
| `GET /admin/api/plans/gantt` | JSON | 간트: 에픽/작업task/CR마일스톤/선행간선/CR링크 | `?year=` (선택) |
| `GET /admin/api/plans/lint` | JSON | 링크 린터: 관련CR·선행 실존·순환 검증 (UI 미연결) | 없음 |

> **정확한 요청/응답 JSON 스키마는 `kanban-board-api-contract.md` 를 단일 소스로 따른다.**

### 3.4 핵심 함수 명세

#### `_parse_index_md(plans_dir)` → `(list[dict], float)`
- `plans_dir` 내 `_index.md` 읽어 테이블 파싱
- 각 행의 `{id, summary, status, date, folder, main_md, has_main, work_type, result_count, test_count, extra_files}` 반환
- 상태 매핑: `STATUS_MAP`으로 외부 상태명 → 내부 키 변환
- 두 번째 반환값: `os.path.getmtime` (폴링용)

```python
STATUS_MAP = {
    'Todo': 'todo',
    'Doing': 'doing',
    'Pre-Done': 'predone',
    'Done': 'done',
    'Hold': 'hold',
    'Drop': 'drop',
}
STATUS_LABEL = {
    'done': '✅ Done', 'doing': '🔄 Doing',
    'todo': '📋 Todo', 'predone': '🔶 Pre-Done',
    'hold': '📌 Hold', 'drop': '🗑️ Drop',
}
TABLE_RE = re.compile(
    r'^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*(Todo|Doing|Pre-Done|Done|Hold|Drop)\s*\|\s*(\d{4}-\d{2}-\d{2})\s*\|',
    re.MULTILINE
)
```

#### `_resolve_plan_folder(plans_dir, item_id)` → `str`
- `{plans_dir}/{item_id}` 폴더 해석
- 정확 일치 폴더가 없으면 유사 폴더 탐색 (plan_id ≠ 폴더명 완화)

#### `_find_main_md(folder, item_id)` → `str`
- 폴더 내 메인 `.md` 파일 해석
- `{item_id}.md` → `{item_id}_*.md` → 첫 `.md` 순서로 fallback

#### `_group_by_status(plans)` → `dict`
- plan 리스트를 6개 상태 키(`todo/doing/predone/done/hold/drop`)로 그룹화

#### `parse_all_months(base_dir)` → `list[dict]`
- `base_dir/MM/` 하위 모든 `_index.md` 병합
- 각 plan dict에 `month`(MM) 키 추가

#### `_discover_month_dirs(base_dir)` → `list[(str, str)]`
- `base_dir` 하위 `MM/` 패턴 폴더 중 `_index.md` 보유 폴더 반환

#### `_plans_year(base_dir)` → `str`
- `base_dir`의 마지막 경로 세그먼트(연도) 반환

#### CR 월별 집계 (별도 CR 폴더 연동 시)
- `_scan_all_crs(cr_dir)`: CR 문서 폴더 내 `REQ-*.md` 전수 스캔
- `_group_crs_by_month(crs)`: 월별 그룹화, FP/공수 합계, 누적 집계
- CR 문서 포맷: 헤더에 요청유형·날짜·FP·공수·변경요약 포함

#### 추세/유형 집계 (그래프 탭)
- `_cr_monthly_for_year(year)` / `_plans_monthly_for_year(year)`: 연도별 월별 집계 dict 반환
- `_cr_by_type_for_year(year)` → `(agg, types)`: CR 요청유형 기준 월별 집계
- `_plans_by_type_for_year(year)` → `(table, total)`: 작업유형(A~E/other) 기준 월별 집계
- `_available_years()`: CR 연도 ∪ plans 연도 폴더 합집합
- `WORK_TYPE_LABELS`: `{A:버그수정, B:기능개선, C:설계/아키텍처, D:리팩토링, E:DB마이그레이션, other:미분류}`

#### 간트/린터 보조
- 에픽 그룹화: `epic` 키로 스윔레인 분할 (`epic_order` 유지)
- `_resolve_ref(plans, ref)`: 선행 ID → 실존 plan 해석 (유사 폴더 탐색)
- `_link_linter(plans)` → `[{type:'dangling_cr'|'unresolved_dep'|'cycle_dep', plan, ref, msg}]`: 관련CR 실존 + 선행 실존 + 선행 DAG 순환 검증
- `CR_DIR`: `project.json` 의 `{{paths.cr_root}}` 를 그대로 쓴다(프로젝트 저장소 소속 — `.clinerules/`가 아니다). `PLANS_DIR`로부터 상대경로를 역산하지 않는다

### 3.5 응답 형식 예시 (`/admin/api/plans`)

```json
{
  "success": true,
  "grouped": {
    "todo": [{"id": "...", "summary": "...", "status": "todo", "date": "2026-07-01", "month": "07", "work_type": "B", "result_count": 0, "test_count": 1, ...}],
    "doing": [...],
    "predone": [...],
    "done": [...],
    "hold": [...],
    "drop": [...]
  },
  "stats": {"total": 48, "todo": 13, "doing": 5, "predone": 2, "done": 26, "hold": 1, "drop": 1},
  "modified_at": 1750000000.0,
  "board_month": "2026-07",
  "month": "07"
}
```

---
