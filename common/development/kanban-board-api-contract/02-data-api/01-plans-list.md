# 계획 목록·조회 API

> 상위 나침반 [`../02-data-api.md`](../02-data-api.md) 에서 분리.

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
