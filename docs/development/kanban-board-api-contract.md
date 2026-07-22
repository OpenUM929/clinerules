# 계획 현황 보드 — API 계약서 (프레임워크 중립)

> 본 문서는 관리자용 **계획 현황 보드**(칸반 / CR / 간트 / 추세) 백엔드 API의
> 요청·응답 JSON 스키마를 프레임워크 중립적으로 정의한다.
> 기준 소스: `wordcloud_project/src/routes/plans_routes.py` (Blueprint `plans_bp`, `url_prefix='/admin'`).
> 도메인(업무명·데이터명)은 일절 포함하지 않으며, 신규 프로젝트는 경로·함수명만 adapt하여 동일 제품을 재구성할 수 있다.
> 표준 지침: `kanban-board-guide.md` §3 이 문서를 참조하도록 개편됨.

---

## 0. 공통 규칙

- **모든 API는 `admin_required` 데코레이터로 보호** — 미인증 시
  `{ "success": false, "error": "관리자 로그인이 필요합니다." }` + HTTP 401.
- **공통 에러 포맷**:
  ```json
  { "success": false, "error": "<한글 메시지>", "status": 401 | 404 | 500 }
  ```
- **시간**: `_index.md` `os.path.getmtime` (epoch float, 폴링용 `modified_at`).
- **연도 기준**: `PLANS_DIR` 마지막 세그먼트(예: `2026`) — `_plans_year()`.
- **월 파라미터**: `MM` 2자리 또는 빈값(`ALL`=전체 병합). `?month=07` / 생략.

---

## 1. 페이지

### `GET /admin/plans`
- 설명: 보드 페이지 서버사이드 렌더링 (HTML).
- 인자: 없음.
- 응답: `text/html` (칸반/CR/간트/추세 4탭 SPA).

---

## 2. 데이터 API (9종)

### `GET /admin/api/plans/check`
- 설명: `_index.md` 수정시각만 반환 (10초 폴링용).
- 인자: `?month=` (선택, `MM`).
- 응답:
  ```json
  { "success": true, "modified_at": 1750000000.0 }
  ```

### `GET /admin/api/plans`
- 설명: 전체 항목 목록을 6개 상태로 그룹화.
- 인자: `?month=` (선택, 필터).
- 응답:
  ```json
  {
    "success": true,
    "grouped": {
      "todo":   [ <plan> ],
      "doing":  [ <plan> ],
      "predone":[ <plan> ],
      "done":   [ <plan> ],
      "hold":   [ <plan> ],
      "drop":   [ <plan> ]
    },
    "stats": { "total": 90, "todo": 9, "doing": 8, "predone": 14, "done": 54, "hold": 2, "drop": 3 },
    "modified_at": 1750000000.0,
    "board_month": "2026-07",
    "month": "07"
  }
  ```
- `<plan>` 객체 스키마 (각 항목 폴더 파싱 결과):
  ```json
  {
    "id": "14_03_kanban-board-guide",
    "summary": "칸반보드 표준 지침화",
    "status": "done",
    "date": "2026-07-14",
    "has_main": true,
    "work_type": "B",
    "result_count": 3,
    "test_count": 1,
    "folder": "<abs path>",
    "main_md": "<abs path> 또는 null",
    "extra_files": ["14_03_kanban-onepager.md"],
    "related_cr": ["REQ-001"],
    "depends": ["07_14_01"],
    "epic": "표준화",
    "end_date": "2026-07-14"
  }
  ```
  - `status`: `todo|doing|predone|done|hold|drop` (내부 키).
  - `related_cr` / `depends` / `epic`: `_index.md` 선택 컬럼 5·6·7 (없으면 `[]` / `""`).
  - `end_date`: 메인 `.md` 헤더 `완료일:` 또는 `완료일시:` (없으면 `null`).

### `GET /admin/api/plans/<id>/content`
- 설명: 특정 항목 메인 `.md` 원문 + 산출물/검증 파일 목록.
- 인자: `?dir=` (월 폴더 절대경로 — `abspath`→`isdir` 2중 검증, 없으면 `PLANS_DIR`).
- 응답:
  ```json
  {
    "success": true,
    "raw": "<markdown 원문>",
    "folder": "<abs path>",
    "result_files": ["report.md"],
    "test_files": ["test_x.py"]
  }
  ```

### `GET /admin/api/plans/cr-monthly`
- 설명: 변경요청(CR) 월별 집계 (별도 CR 폴더 연동).
- 인자: 없음.
- 응답:
  ```json
  {
    "success": true,
    "months": [
      { "ym": "2026-06", "label": "2026년 6월", "count": 12,
        "crs": [ { "req_id": "REQ-001", "type": "기능개선", "summary": "…", "date": "2026-06-04", "fp": 8, "hours": 16.0 } ],
        "fp_total": 80, "hours_total": 177.5, "cum_fp": 80, "cum_hours": 177.5 }
    ],
    "total_crs": 53, "total_fp": 80, "total_hours": 177.5
  }
  ```

### `GET /admin/api/plans/cr/<req_id>`
- 설명: 특정 CR 상세.
- 인자: 없음.
- 응답:
  ```json
  {
    "success": true,
    "cr": {
      "req_id": "REQ-001", "type": "기능개선", "summary": "…",
      "date": "2026-06-04", "ym": "2026-06", "month_label": "2026년 6월",
      "fp": 8, "hours": 16.0, "work_type": "B", "raw": "<markdown 원문>"
    }
  }
  ```

### `GET /admin/api/plans/trend`
- 설명: 연도별 월 추세 (금년/전년 대조) — CR 건수·FP·공수·계획서 건수.
- 인자: `?year=` (선택, 기본 `_plans_year()`).
- 응답:
  ```json
  {
    "success": true,
    "year": 2026, "prev_year": 2025,
    "series": {
      "cr_count":   { "cur": [<12개월>], "prev": [<12개월>] },
      "fp":         { "cur": [<12개월>], "prev": [<12개월>] },
      "hours":      { "cur": [<12개월>], "prev": [<12개월>] },
      "plan_count": { "cur": [<12개월>], "prev": [<12개월>] }
    },
    "totals": {
      "cr_count":   { "cur": 53, "prev": 0 },
      "fp":         { "cur": 80, "prev": 0 },
      "hours":      { "cur": 177.5, "prev": 0 },
      "plan_count": { "cur": 90, "prev": 0 }
    }
  }
  ```
  - 배열은 1~12월 순 `['01'…'12']` 에 대응하는 숫자 12개.

### `GET /admin/api/plans/trend-type`
- 설명: 유형(작업유형 A~E/other, CR 요청유형)별 집계 — 그래프 탭 전용.
- 인자:
  - `?mode=monthly&year=YYYY` → 월별 유형별 (금년/전년)
  - `?mode=yearly&mStart=1&mEnd=12` → 연별 유형별 (기본 1~현재월)
- 응답 (monthly):
  ```json
  {
    "success": true, "mode": "monthly", "year": 2026, "prev_year": 2025,
    "work_type_labels": { "A": "버그수정", "B": "기능개선", "C": "설계/아키텍처", "D": "리팩토링", "E": "DB마이그레이션", "other": "미분류" },
    "cr_by_type":  { "types": ["기능개선","버그수정"], "cur": [<12개월 dict>], "prev": [<12개월 dict>] },
    "plan_by_type":{ "types": ["A","B","C","D","E","other"], "cur": [<12개월 dict>], "prev": [<12개월 dict>] }
  }
  ```
- 응답 (yearly):
  ```json
  {
    "success": true, "mode": "yearly", "years": [2025, 2026], "mStart": 1, "mEnd": 12, "cur_month": 7,
    "work_type_labels": { "A": "버그수정", "B": "기능개선", "C": "설계/아키텍처", "D": "리팩토링", "E": "DB마이그레이션", "other": "미분류" },
    "series": {
      "cr_count":   { "2026": 53 }, "fp": { "2026": 80 }, "hours": { "2026": 177.5 }, "plan_count": { "2026": 90 },
      "cr_by_type":   { "types": ["기능개선"], "data": { "2026": { "기능개선": 30 } } },
      "plan_by_type": { "types": ["A","B","C","D","E","other"], "data": { "2026": { "A": 0, "B": 40, "C": 5, "D": 3, "E": 2, "other": 0 } } }
    }
  }
  ```

### `GET /admin/api/plans/gantt`
- 설명: 간트차트 데이터 — 에픽 스윔레인 + 작업task + CR마일스톤 + 선행간선 + CR링크.
- 인자: `?year=` (선택).
- 응답:
  ```json
  {
    "success": true, "year": "2026",
    "epics":   [ { "name": "표준화", "plans": [ <plan> ] } ],
    "tasks":   [ { "id": "14_03_…", "summary": "…", "status": "done", "date": "2026-07-14", "month": "07", "epic": "표준화", "end_date": "2026-07-14", "work_type": "B" } ],
    "milestones": [ { "req_id": "REQ-001", "summary": "…", "date": "2026-06-04", "ym": "2026-06", "fp": 8, "hours": 16.0 } ],
    "deps":        [ { "from": "14_03_…", "to": "07_14_01" } ],
    "dep_warnings":[ { "plan": "14_03_…", "ref": "07_99_zzz", "warning": "unresolved" } ],
    "cr_links":    [ { "plan": "14_03_…", "cr": "REQ-001" } ],
    "plan_total": 90,
    "plan_by_type": { "A": 0, "B": 40, "C": 5, "D": 3, "E": 2, "other": 0 }
  }
  ```
  - `tasks[].end_date` / `milestones[].date` 가 간트 가로축 좌표.
  - `deps` 는 선행 DAG 간선 (`from`→`to` 모두 실존 plan id).
  - `cr_links` 는 plan↔CR 연결선.

### `GET /admin/api/plans/lint`
- 설명: 링크 린터 — 관련CR 실존 + 선행 실존 + 선행 DAG 순환 검증.
  **현재 프론트엔드 UI 미연결(서버 API만 존재) — 향후 탭/패널 wiring 예정.**
- 인자: 없음.
- 응답:
  ```json
  {
    "success": true,
    "violations": [
      { "type": "dangling_cr",   "plan": "14_03_…", "ref": "REQ-999", "msg": "CR REQ-999 not found in <CR_DIR>" },
      { "type": "unresolved_dep","plan": "14_03_…", "ref": "07_99_zzz", "msg": "…" },
      { "type": "cycle_dep",     "plan": "…", "ref": "…", "msg": "…" }
    ],
    "pass": false
  }
  ```
  - `pass` = `violations` 가 비어있으면 `true`.

---

## 3. 엔드포인트 요약표

| # | 메서드 | 경로 | 핵심 응답 |
|---|--------|------|-----------|
| 1 | GET | `/admin/plans` | HTML 페이지 (4탭) |
| 2 | GET | `/admin/api/plans/check` | `modified_at` |
| 3 | GET | `/admin/api/plans` | `grouped` / `stats` / `modified_at` |
| 4 | GET | `/admin/api/plans/<id>/content` | `raw` / `result_files` / `test_files` |
| 5 | GET | `/admin/api/plans/cr-monthly` | `months[]` / `total_crs` / `total_fp` / `total_hours` |
| 6 | GET | `/admin/api/plans/cr/<req_id>` | `cr{}` |
| 7 | GET | `/admin/api/plans/trend` | `series` / `totals` (금·전년 12개월) |
| 8 | GET | `/admin/api/plans/trend-type` | `cr_by_type` / `plan_by_type` (monthly\|yearly) |
| 9 | GET | `/admin/api/plans/gantt` | `epics` / `tasks` / `milestones` / `deps` / `cr_links` |
| 10 | GET | `/admin/api/plans/lint` | `violations[]` / `pass` |

---

## 4. 프론트엔드 탭 ↔ API 매핑

| 탭 (`data-view`) | 라벨 | 호출 API |
|------------------|------|----------|
| `kanban` | 📋 계획 현황 | `/api/plans`, `/api/plans/check`, `/api/plans/<id>/content` |
| `git` | 📊 월별 CR 현황 | `/api/plans/cr-monthly`, `/api/plans/cr/<req_id>` |
| `gantt` | 📅 간트차트 | `/api/plans/gantt` |
| `trend` | 📈 추세 그래프 | `/api/plans/trend`, `/api/plans/trend-type` (monthly\|yearly) |
| (예정) | 링크 린터 | `/api/plans/lint` (UI 미연결) |
