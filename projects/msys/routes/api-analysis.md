# api/analysis_api

**ë¬¸ì„œ ?„ì¹˜**: `.clinerules/projects/msys/routes/api-analysis.md`

## ?Œì¼
- `D:\dev\msys\routes\api\analysis_api.py` (371ì¤?

## ??• 
?°ì´??ë¶„ì„ REST API

## Blueprint
```python
analysis_api_bp = Blueprint('analysis_api', __name__, url_prefix='/api/analytics')
```

## ?”ë“œ?¬ì¸??
| ê²½ë¡œ | ë©”ì„œ??| ?¨ìˆ˜ | ?¤ëª… |
|------|--------|------|------|
| `/api/analytics/success_rate_trend` | GET | `get_analytics_success_rate_trend_api()` | ê¸°ê°„ë³??±ê³µë¥?ì¶”ì´ |
| `/api/analytics/trouble_by_code` | GET | `get_analytics_trouble_by_code_api()` | ?¥ì•  ì½”ë“œë³?ë¹„ìœ¨ |
| `/api/analytics/summary` | GET | `api_analysis_summary()` | ë¶„ì„ ?”ì•½ |
| `/api/analytics/trend` | GET | `api_analysis_trend()` | ì¶”ì´/ê²½í–¥ ?°ì´??|
| `/api/analytics/raw_data` | GET | `api_analysis_raw_data()` | ?ì‹œ ?°ì´??|
| `/api/analytics/job_ids` | GET | `api_analysis_job_ids()` | Job ID ëª©ë¡ |
| `/api/analytics/error_codes` | GET | `api_analysis_error_codes()` | ?¥ì• ì½”ë“œ ëª©ë¡ |
| `/api/analytics/error_code_map` | GET | `api_analysis_error_code_map()` | ?¥ì• ì½”ë“œ ë§¤í•‘ |
| `/api/analytics/dynamic-chart` | GET | `get_dynamic_chart_data()` | ?™ì  ì°¨íŠ¸ ?°ì´??|

## ?Œë¼ë¯¸í„°
| ?Œë¼ë¯¸í„° | ?€??| ?„ìˆ˜ | ?¤ëª… |
|----------|------|------|------|
| start_date | string | ?¼ë? | ?œì‘ ? ì§œ |
| end_date | string | ?¼ë? | ì¢…ë£Œ ? ì§œ |
| job_ids | array | ?„ë‹ˆ??| Job ID ëª©ë¡ |
| x_axis | string | ?™ì ì°¨íŠ¸ | Xì¶?ì°¨ì› (date, job_id, status) |
| y_axis | string | ?™ì ì°¨íŠ¸ | Yì¶?ì¸¡ì •??ª© |

## ?˜ì¡´??- Service: `service/dashboard_service.py`, `service/analysis_service.py`, `service/mst_service.py`

## ?°ê? ë¬¸ì„œ
- [../services/analysis-service.md](../services/analysis-service.md)
- [../services/dashboard-service.md](../services/dashboard-service.md)
