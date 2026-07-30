# Analytics DAO (analytics_dao.py)

## 파일 위치

`dao/analytics_dao.py` (352줄)

## 역할

분석 데이터 접근 - 사용자 접속 로그, 통계 데이터 조회

## 주요 함수

| 함수 | 기능 |
|------|------|
| `insert_user_access_log(user_id, menu_name)` | 접속 로그 삽입 |
| `get_menu_name_by_menu_id(menu_id)` | 메뉴 ID로 메뉴명 조회 |
| `get_user_access_stats(year, month, start_date, end_date)` | 기간별 접속 통계 |
| `get_available_years_months()` | 사용 가능한 연도/월 조회 |
| `get_most_recent_data_date()` | 가장 최근 데이터 날짜 |
| `get_menu_access_stats_weekly(year, menu_nm)` | 주별 메뉴 접근 통계 |
| `get_total_unique_users_by_week(year)` | 주별 고유 사용자 수 |
| `get_yearly_total_stats(year, menu_nm)` | 연간 통계 |

## SQL 의존성

- `analytics/insert_user_access_log.sql`
- `analytics/get_menu_name_by_id.sql`
- `analytics/get_user_access_stats.sql`

## 관련 문서

- [dao/README.md](README.md) - DAO 개요
- [services/dashboard-service.md](../services/dashboard-service.md) - 대시보드 서비스