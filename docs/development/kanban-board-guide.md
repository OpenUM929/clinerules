# 관리자용 진행현황 칸반보드 표준 지침

> 이 문서는 Flask 기반 웹시스템에서 **관리자(admin) 전용 칸반보드 페이지**를 구현하기 위한 범용 컴포넌트 명세다.
> wordcloud 프로젝트의 `src/routes/plans_routes.py` + `web/templates/plans_kanban.html`을 기준으로 추출하였다.
> **도메인(업무명·데이터명)은 일절 포함하지 않으며**, 신규 프로젝트에서 함수명·경로 등을 adapt하여 사용한다.

---

## 1. 개요 및 적용 대상

- **목적**: 마크다운 인덱스 파일(`_index.md`)을 단일 정보원으로 하여, 작업/문서의 진행 상태를 6개 컬럼으로 시각화
- **적용 대상**: 관리자(admin) 권한을 가진 사용자
- **기술 스택**: Python Flask (백엔드) + HTML/CSS/JavaScript (프론트엔드, Bootstrap 5 Modal)
- **데이터 저장소**: 파일시스템 (별도 DB 불필요)
- **확장 기능(4탭)**:
  - 📋 **계획 현황**(칸반) — 6컬럼 보드
  - 📊 **월별 CR 현황** — 별도 CR 문서 폴더 연동 집계
  - 📅 **간트차트** — 에픽 스윔레인 + CR 마일스톤 + 선행 DAG
  - 📈 **추세 그래프** — 연도별/유형별 CR·계획서 추세
  - (예정) **링크 린터** — 관련CR/선행 실존·순환 검증 (API만 존재, UI 미연결)
- **API 계약서**: 본 지침의 백엔드 스키마는 `kanban-board-api-contract.md` (프레임워크 중립 JSON 계약)와 1:1 대응 — 신규 시스템 구축 시 해당 문서를 단일 소스로 사용

---

## 2. 데이터 계약 (Data Contract / SSOT)

### 2.1 인덱스 파일 스키마

칸반보드의 단일 정보원(Single Source of Truth)은 마크다운 인덱스 파일이다. 모든 데이터는 이 파일에서 파생된다.

**파일명**: `_index.md`  
**위치 규칙**: `{BASE_DIR}/{MM}/_index.md` — 월별 폴더로 분할

```markdown
# {연도} 계획서 인덱스

| 항목 | 작업 요약 | 상태 | 작성일 |
|------|-----------|------|--------|
| {id} | {요약 텍스트} | {상태} | {YYYY-MM-DD} |
```

**컬럼 설명**:

| 컬럼 | 필수 | 설명 |
|------|------|------|
| `항목` | Y | 고유 식별자. 슬러그 형식 권장 (`DD_NN_작업명`) |
| `작업 요약` | Y | 항목을 설명하는 요약 텍스트 |
| `상태` | Y | 6개 약어 중 하나 (아래 표 참조). Emoji **절대 금지** |
| `작성일` | Y | `YYYY-MM-DD` 형식 |
| `관련CR` (5) | N | 쉼표 구분 CR ID 목록 (예: `REQ-001,REQ-002`) — 링크/간트 CR연결용 |
| `선행` (6) | N | 쉼표 구분 선행 항목 ID 목록 — 간트 선행간선·린터 DAG용 |
| `에픽` (7) | N | 에픽(대분류) 명칭 — 간트 스윔레인 그룹핑용 |

> **파싱 규칙**: `TABLE_RE`는 4컬럼(항목/요약/상태/작성일)을 고정 매칭하고, 매칭된 전체 행에서 5·6·7컬럼을 추가 추출한다(누락 시 `[]`/`""`).  
> **`end_date`(완료일)**: `_index.md`가 아닌 항목 폴더 메인 `.md` 헤더의 `완료일:` 또는 `완료일시:` 에서 추출 — 간트 가로축 종료좌표.

### 2.2 상태 어휘 (6종)

| 상태명 | Kanban 컬럼 | 의미 |
|--------|-------------|------|
| `Todo` | 📋 Todo | 대기/예정 |
| `Doing` | 🔄 Doing | 분석/검토/구현 진행 중 |
| `Pre-Done` | 🔶 Pre-Done | 구현·단위검증 완료, 최종 점검 대기 |
| `Done` | ✅ Done | 작업 완료 |
| `Hold` | 📌 Hold | 보류 종결 (나중에 재개 가능) |
| `Drop` | 🗑️ Drop | 폐기 종결 (되살리지 않음) |

**규칙**:
- `_index.md`에는 반드시 **약어만** 기재 (emoji 금지)
- Kanban UI 레이어가 emoji를 자동 부여
- 6종 외 미등록 토큰 사용 시 파서 미매칭 → 보드 누락

### 2.3 월별 인덱스 병합

```
{BASE_DIR}/
├── 01/
│   └── _index.md
├── 02/
│   └── _index.md
├── ...
└── 12/
    └── _index.md
```

칸반보드는 **모든 월의 `_index.md`를 병합**하여 전체 데이터를 구성한다. 각 항목에 소속 월(`MM`) 태그를 부여한다.

### 2.4 부가 정보 파싱

인덱스 파일만으로 부족한 정보는 개별 항목 폴더에서 파싱한다:

| 정보 | 파싱 대상 | 파싱 방식 |
|------|-----------|-----------|
| 작업 유형 | 항목 폴더 내 메인 `.md` 헤더 | 정규식 `작업\s*유형\s*[:：]\s*(.+)` |
| 산출물 수 | 항목 폴더 내 `result/` 디렉토리 | 디렉토리 내 파일 개수 |
| 검증 파일 수 | 항목 폴더 내 `test/` 디렉토리 | 디렉토리 내 파일 개수 |
| 상세 내용 | 항목 폴더 내 메인 `.md` | mistune HTML 변환 또는 JS 마크다운 렌더 |

**항목 폴더 구조 예시**:
```
{MM}/
├── _index.md
└── {item_id}/
    ├── {item_id}.md          ← 메인 문서
    ├── result/                 ← 산출물
    │   └── report.md
    └── test/                  ← 검증
        └── test_xxx.py
```

---

## 3. 백엔드 패턴 (Flask Blueprint)

### 3.1 설정

```python
# config/settings.py
# 칸반보드 대상 베이스 디렉토리 (환경변수로 오버라이드 가능)
PLANS_DIR = os.getenv('PLANS_DIR', os.path.join(PROJECT_ROOT, '..', 'plans', '2026'))
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
- `CR_DIR` 유도: `PLANS_DIR` 3단 상위 + `.clinerules/docs/cr` (호스트 주입형으로 교체 권장)

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

## 4. 프론트엔드 패턴 (HTML/CSS/JS)

### 4.1 레이아웃 구조

```
┌────────────────────────────────────────────────────────────┐
│ [📋 계획 현황] [📊 월별 CR] [📅 간트차트] [📈 추세 그래프] │ ← 뷰 탭 (data-view)
├────────────────────────────────────────────────────────────┤
│ 📋 Plans Kanban  ✅ 26완료  🔄 5작업중  📋 13예정  · 총 48│
│ [▼ 월 선택] 2026/07                                        │
├─────────┬──────────┬──────────┬─────────┬───────┬─────────┤
│ 📋 Todo│ 🔄 Doing │ 🔶 Pre-  │ ✅ Done │ 📌Hold│ 🗑️ Drop│
│ (13)   │ (5)      │ Done (2) │ (26)    │ (1)   │ (1)     │
│ ┌─────┐│ ┌──────┐ │ ┌──────┐ │ ┌─────┐ │ ┌───┐ │ ┌─────┐│
│ │card ││ │card  │ │ │card  │ │ │card │ │ │card│ │ │card ││
│ └─────┘│ └──────┘ │ └──────┘ │ └─────┘ │ └───┘ │ └─────┘│
└─────────┴──────────┴──────────┴─────────┴───────┴─────────┘
```

- 뷰 탭은 `class="view-tab"` + `data-view` 속성(`kanban`/`git`/`gantt`/`trend`)으로 전환.
- 월 선택 드롭다운은 모든 탭 공용; 변경 시 AJAX로 해당 탭 데이터 재로드.

### 4.2 6컬럼 색상 토큰

```css
:root {
  --todo-color: #856404;  --todo-bg: #fff3cd;  --todo-border: #ffc107;
  --doing-color: #4338ca; --doing-bg: #e9d5ff; --doing-border: #17a2b8;
  --predone-color: #e65100; --predone-bg: #fff3e0; --predone-border: #ff9800;
  --done-color: #155724;  --done-bg: #d4edda;  --done-border: #28a745;
  --hold-color: #4a3b6b;  --hold-bg: #e7e0f5;  --hold-border: #7e57c2;
  --drop-color: #6c757d;  --drop-bg: #e9ecef;  --drop-border: #adb5bd;
}
```

### 4.3 카드 구성 (Chip 순서)

각 카드는 다음과 같은 칩을 순서대로 표시한다:

```
┌─────────────────────────────────────┐
│ DD_NN_작업명                        │  ← 항목 ID (bold)
│ 작업 요약 텍스트                     │  ← 요약 (muted)
│ [07월] [✅ Done] [B] [📄3] [🧪1]   │  ← 칩
└─────────────────────────────────────┘
```

- **첫 칩**: 소속 월 (`MM월`)
- **두 번째 칩**: 상태 배지 (색상 + emoji + 상태명)
- **세 번째 칩**: 작업 유형 (있을 때만)
- **네 번째 칩**: 산출물 수 (`📄N`, 0이면 생략)
- **다섯 번째 칩**: 검증 파일 수 (`🧪N`, 0이면 생략)

### 4.4 Done 컬럼 월별 그룹카드

- Done 컬럼만 **월별 그룹카드**로 표시
- **현재월**: 개별 카드로 펼쳐서 표시
- **과거월**: 그룹카드 `📦 MM월 완료 (N건)` 1장
- 그룹카드 클릭 시 → 해당 월 Done 일람 모달
- 그룹카드에는 월 칩을 붙이지 않음 (제목에 월이 있으므로 중복)

### 4.5 정렬

- 모든 컬럼이 동일한 정렬 방향(date 기준)을 공유
- 컬럼 헤더 우측 `↓`/`↑` 버튼 클릭으로 내림차순↔오름차순 전환
- 빈 date는 항상 리스트 마지막

### 4.6 자동 갱신 (10초 폴링)

```
setInterval → GET /admin/api/plans/check?month=XX
  └─ modified_at 변경 감지 → GET /admin/api/plans?month=XX
       └─ 카드 재렌더링 (renderCards)
```

### 4.7 월 필터 드롭다운

- 상단 `<select>` 드롭다운으로 월 선택
- `ALL`(전체) 또는 특정 월 선택
- 변경 시 전체 페이지 리로드 없이 카드 교체 (AJAX)
- 현재월 기본 선택

### 4.8 모달 상세

카드 클릭 시 Bootstrap Modal로 항목 상세 표시:

```
┌─────────────────────────────────────────────────────┐
│ 📄 DD_NN_작업명                             [✕]    │
├─────────────────────────────────────────────────────┤
│  (markdown → HTML 렌더 — 코드블록·테이블·리스트 등)  │
│                                                     │
│  📁 폴더 열기  ·  📄 result/ (N)  ·  🧪 test/ (N)  │
├─────────────────────────────────────────────────────┤
│                                        [닫기]        │
└─────────────────────────────────────────────────────┘
```

### 4.9 탭 전환: 칸반보드 / 월별 CR 현황

> 4탭 시스템(`kanban`/`git`/`gantt`/`trend`) 중 **첫 두 탭**의 전환 동작 설명.
- 칸반/CR 전환 탭: `📋 칸반보드` / `📊 월별 CR 현황`
- CR 현황 탭: 월별 아코디언, 각 CR 행에 REQ-ID/타입/변경요약/FP/공수 표시
- CR 행 클릭 시 상세 모달
- 최신월 자동 오픈

### 4.10 간트차트 탭 (`data-view="gantt"`)

- 데이터: `GET /admin/api/plans/gantt`
- **스윔레인**: `epics[]` — 에픽(대분류)별 행 그룹 (좌측 고정 컬럼)
- **작업 바**: `tasks[]` — `date`(시작)→`end_date`(종료) 가로축; 상태 색상 토큰 적용
- **마일스톤(◆)**: `milestones[]` — CR를 다이아몬드 마커로 표시 (상단 CR 범례 `#6f42c1` 점선)
- **선행 간선**: `deps[{from,to}]` — 작업 간 화살표 (DAG); `dep_warnings[]` 미해결은 경고 표시
- **CR 링크**: `cr_links[{plan,cr}]` — plan↔CR 연결선
- **요약**: `plan_by_type{}` / `plan_total` — 작업유형별 집계 헤더

### 4.11 추세 그래프 탭 (`data-view="trend"`)

- 데이터: `GET /admin/api/plans/trend` + `GET /admin/api/plans/trend-type`
- **추세 차트** (`loadTrend`): 연도별 월 추세 — CR건수/FP/공수/계획서건수를 금년(cur)·전년(prev) 대조 라인차트 (`renderTrendChart`)
- **유형 차트** (`loadMonthlyType` / `loadYearly`): 작업유형(A~E/other)·CR 요청타입별 집계 — `mode=monthly`(월별) / `mode=yearly`(연별, `mStart`~`mEnd`) — `renderChart` (막대/누적)
- `work_type_labels` 로 범례 한글 라벨 매핑

### 4.12 링크 린터 (예정)

- 데이터: `GET /admin/api/plans/lint`
- 현재 **프론트엔드 UI 미연결** — 서버 API만 존재. 향후 탭 또는 패널로 `violations[]`(`dangling_cr`/`unresolved_dep`/`cycle_dep`)·`pass` 표시 예정
- 설계 의도: 린터는 좌표/선행 DAG를 **검증**할 뿐 자동 채우지 않음 (미확정 빈칸 ≠ 확인된 빈칸 구분)

---

## 5. 보안 / 리스크

| 항목 | 대책 |
|------|------|
| 인증 | `admin_required` 데코레이터 — 모든 라우트에 적용 |
| 경로 탐색 | `dir` 파라미터는 `os.path.abspath` → `os.path.isdir` 2중 검증 |
| 인코딩 | `utf-8-sig`로 읽어 CP949/UTF-8 BOM 혼재 대응, 파싱 실패 시 graceful 생략 |
| 데이터 일관성 | 파일시스템 기반 stateless — WAS 다중 인스턴스 문제 없음 |
| 성능 | 항목 수가 200+ 건이면 `parse_all_months` 매 요청 부하 가능 → mtime 체크 후 필요한 경우만 전체 파싱 (check/list 분리) |

---

## 6. 재사용 체크리스트 (신규 프로젝트 적용 절차)

신규 Flask 웹시스템에 칸반보드를 도입할 때 다음 순서로 적용한다:

- [ ] 1. `settings.py`에 `PLANS_DIR` 설정 추가 (칸반 대상 베이스 폴더)
- [ ] 2. `src/routes/plans_routes.py` 생성 — **라우트 10종** (§3.3) + 핵심 함수 전사
- [ ] 3. `web/templates/plans_kanban.html` 생성 — CSS/HTML/JS 전사 (도메인명 replace)
- [ ] 4. `web/app.py`에 `plans_bp` 블루프린트 등록
- [ ] 5. `web/templates/base.html`에 네비 링크 추가 (관리자 전용)
- [ ] 6. `BASE_DIR/MM/_index.md` 초기 데이터 작성 (1개월부터 시작, 5·6·7컬럼 선택 사용)
- [ ] 7. 관리자 로그인 체계 확인 (`admin_required` 연동)
- [ ] 8. 브라우저 `/admin/plans` 접속 → 6컬럼 정상 표시 확인
- [ ] 9. CR 현황 탭 사용 시: `cr_dir` 설정 + `REQ-*.md` 문서 포맷 준수
- [ ] 10. `_index.md` 상태값 변경 → 10초 내 칸반보드 자동 갱신 확인
- [ ] 11. **4탭** 확인: 칸반(`kanban`) / CR(`git`) / 간트(`gantt`) / 추세(`trend`) 전환 정상
- [ ] 12. 간트: `epic`/`end_date`/`depends`/`related_cr` 컬럼 채워 스윔레인·간선·마일스톤 표시
- [ ] 13. 추세: `trend` / `trend-type`(monthly·yearly) 차트 정상 렌더
- [ ] 14. 링크 린터(`/api/plans/lint`) UI wiring 시 `violations`·`pass` 표시 (선택)
- [ ] 15. **`kanban-board-api-contract.md` 를 API 단일 소스로 준수** (스키마 변경 시 계약서 동기화)
