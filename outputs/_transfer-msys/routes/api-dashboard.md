# api/dashboard_api

**문서 위치**: `.clinerules/docs/msys/routes/api-dashboard.md`

## 파일
- `D:\dev\msys\routes\api\dashboard_api.py` (128줄)

## 역할
대시보드 REST API

## Blueprint
```python
dashboard_api_bp = Blueprint('dashboard_api', __name__, url_prefix='/api/dashboard')
```

## 엔드포인트

| 경로 | 메서드 | 함수 | 설명 |
|------|--------|------|------|
| `/api/dashboard/summary` | GET | `get_dashboard_summary()` | 대시보드 요약 데이터 |
| `/api/dashboard/day-stats/<date_str>` | GET | `get_day_stats_api()` | 일별 통계 (deprecated) |
| `/api/dashboard/min-max-dates` | GET | `get_min_max_dates_api()` | 데이터 최소/최대 날짜 |
| `/api/dashboard/event-log` | GET | `get_event_log_api()` | 이벤트 로그 |

## 파라미터
| 파라미터 | 타입 | 필수 | 설명 |
|----------|------|------|------|
| start_date | string | 일부 | 시작 날짜 (YYYY-MM-DD) |
| end_date | string | 일부 | 종료 날짜 (YYYY-MM-DD) |
| all_data | boolean | 아니오 | 전체 데이터 조회 여부 |

## 의존성
- Service: `service/dashboard_service.py`

## 연관 문서
- [../services/dashboard-service.md](../services/dashboard-service.md)
