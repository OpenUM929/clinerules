# 프론트엔드 패턴 (HTML/CSS/JS)

> 상위 나침반 [`../kanban-board-guide.md`](../kanban-board-guide.md) 에서 분리.

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
