# Con Hist DAO (con_hist_dao.py)

## 파일 위치

`dao/con_hist_dao.py` (262줄)

## 역할

연결 이력 데이터 접근 - TB_CON_HIST 조회

## 주요 함수

| 함수 | 기능 |
|------|------|
| `get_summary(start_date, end_date, all_data)` | 대시보드 요약 데이터 |
| `get_collection_history(start_date, end_date, job_ids)` | 수집 이력 조회 |
| `get_history_detail(job_id, date)` | 이력 상세 조회 |

## SQL 의존성

- `dashboard/get_dashboard_summary.sql`

## 관련 문서

- [dao/README.md](README.md) - DAO 개요
- [services/dashboard-service.md](../services/dashboard-service.md) - 대시보드 서비스