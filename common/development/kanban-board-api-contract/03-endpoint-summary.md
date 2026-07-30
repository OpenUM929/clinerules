# 엔드포인트 요약표·탭 매핑

> 상위 나침반 [`../kanban-board-api-contract.md`](../kanban-board-api-contract.md) 에서 분리.

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
