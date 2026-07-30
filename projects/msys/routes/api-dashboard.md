# api/dashboard_api

**ë¬¸ì„œ ?„ì¹˜**: `.clinerules/projects/msys/routes/api-dashboard.md`

## ?Œì¼
- `D:\dev\msys\routes\api\dashboard_api.py` (128ì¤?

## ??• 
?€?œë³´??REST API

## Blueprint
```python
dashboard_api_bp = Blueprint('dashboard_api', __name__, url_prefix='/api/dashboard')
```

## ?”ë“œ?¬ì¸??
| ê²½ë¡œ | ë©”ì„œ??| ?¨ìˆ˜ | ?¤ëª… |
|------|--------|------|------|
| `/api/dashboard/summary` | GET | `get_dashboard_summary()` | ?€?œë³´???”ì•½ ?°ì´??|
| `/api/dashboard/day-stats/<date_str>` | GET | `get_day_stats_api()` | ?¼ë³„ ?µê³„ (deprecated) |
| `/api/dashboard/min-max-dates` | GET | `get_min_max_dates_api()` | ?°ì´??ìµœì†Œ/ìµœë? ? ì§œ |
| `/api/dashboard/event-log` | GET | `get_event_log_api()` | ?´ë²¤??ë¡œê·¸ |

## ?Œë¼ë¯¸í„°
| ?Œë¼ë¯¸í„° | ?€??| ?„ìˆ˜ | ?¤ëª… |
|----------|------|------|------|
| start_date | string | ?¼ë? | ?œì‘ ? ì§œ (YYYY-MM-DD) |
| end_date | string | ?¼ë? | ì¢…ë£Œ ? ì§œ (YYYY-MM-DD) |
| all_data | boolean | ?„ë‹ˆ??| ?„ì²´ ?°ì´??ì¡°íšŒ ?¬ë? |

## ?˜ì¡´??- Service: `service/dashboard_service.py`

## ?°ê? ë¬¸ì„œ
- [../services/dashboard-service.md](../services/dashboard-service.md)
