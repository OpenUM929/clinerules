# Dashboard Service (dashboard_service.py)

## 파일 위치

`service/dashboard_service.py` (398줄)

## 역할

대시보드 및 분석 데이터 조회, 통계, 이벤트 기록

## 주요 함수

| 함수 | 기능 |
|------|------|
| `get_summary(start_date, end_date, all_data, user)` | 대시보드 요약 데이터 |
| `get_daily_trend_data(start_date, end_date, user)` | 일별 트렌드 데이터 |
| `get_event_counts(user)` | 이벤트 통계 |
| `save_event(con_id, job_id, status, rqs_info)` | 이벤트 저장 |
| `get_con_mst_data(user)` | 연결 마스터 데이터 |
| `get_menu_data(user)` | 메뉴 데이터 |
| `get_icon_menu_mapping()` | 아이콘-메뉴 매핑 |

## 데이터 흐름

1. `get_summary()` - 메인 요약 데이터 조회
   - `_fetch_manager_settings_with_icons()` - 설정 + 아이콘
   - `_get_allowed_job_ids()` - 권한 기반 job 필터링
   - `_fetch_daily_data()` - 일별 데이터 병합

2. `save_event()` - 사용자 이벤트 기록

## 의존성

- `mapper/dashboard_mapper.py` - 대시보드 SQL
- `mapper/user_mapper.py` - 사용자 SQL
- `mapper/mngr_sett_mapper.py` - 설정 SQL
- `mapper/mst_mapper.py` - 마스터 SQL
- `service/icon_service.py` - 아이콘 서비스
- `service/collection_schedule_service.py` - 일정 서비스

## 관련 문서

- [services/README.md](README.md) - services 개요
- [routes/admin-routes.md](../routes/admin-routes.md) - 관리자 라우트
- [routes/dashboard-routes.md](../routes/ui-routes.md) - 대시보드 라우트