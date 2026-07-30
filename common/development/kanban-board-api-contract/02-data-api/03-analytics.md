# 추이·작업유형·간트·린트 API

> 상위 나침반 [`../02-data-api.md`](../02-data-api.md) 에서 분리.

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
