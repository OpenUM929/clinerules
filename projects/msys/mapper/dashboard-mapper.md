# Dashboard Mapper (dashboard_mapper.py)

## 파일 위치

`mapper/dashboard_mapper.py` (204줄)

## 역할

대시보드 SQL 매핑 - 요약, 트렌드, 일정, 이력 데이터

## 주요 함수

| 함수 | 기능 |
|------|------|
| `get_summary(start_date, end_date, all_data, job_ids)` | 대시보드 요약 |
| `get_daily_trend_data(start_date, end_date, job_ids)` | 일별 트렌드 |
| `get_collection_history_for_schedule(start_date, end_date, job_ids)` | 수집 이력 |
| `get_event_counts()` | 이벤트 통계 |

## SQL 의존성

- `sql/dashboard/dashboard_sql.py` - DashboardSQL 클래스
- `sql/analytics/analytics_sql.py` - AnalyticsSQL 클래스
- `sql/raw_data/raw_data_sql.py` - RawDataSQL 클래스

## 관련 문서

- [mapper/README.md](README.md) - mapper 개요
- [services/dashboard-service.md](../services/dashboard-service.md) - 대시보드 서비스