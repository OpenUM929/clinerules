# admin_routes

**ë¬¸ì„œ ?„ì¹˜**: `.clinerules/projects/msys/routes/admin-routes.md`

## ?Œì¼
- `D:\dev\msys\routes\admin_routes.py` (603ì¤?

## ??• 
ê´€ë¦¬ì ?¤ì • - ë©”ë‰´ ?¤ì •, ?µê³„, ?‘ì? ?œí”Œë¦?ê´€ë¦?
## Blueprint
```python
admin_bp = Blueprint('admin', __name__)
```

## ?”ë“œ?¬ì¸??
### ?˜ì´ì§€
| ê²½ë¡œ | ë©”ì„œ??| ?¨ìˆ˜ | ?¤ëª… |
|------|--------|------|------|
| `/admin/mngr_sett` | GET | `mngr_sett_page()` | ê´€ë¦¬ì ?¤ì • ?˜ì´ì§€ |

### API
| ê²½ë¡œ | ë©”ì„œ??| ?¨ìˆ˜ | ?¤ëª… |
|------|--------|------|------|
| `/api/statistics/config` | GET | `get_statistics_config()` | ?µê³„ ?¤ì • (?°ë„, ë©”ë‰´ ëª©ë¡) |
| `/api/statistics/recent_date` | GET | `get_recent_data_date()` | ìµœê·¼ ?°ì´??? ì§œ |
| `/api/statistics` | GET | `get_statistics()` | ?µê³„ ?°ì´??(?¼ë³„/ì£¼ë³„/?”ë³„/ë¹„êµ) |
| `/api/statistics/monthly_excel_download` | GET | `download_monthly_statistics_excel()` | ?”ë³„ ?µê³„ ?‘ì? ?¤ìš´ë¡œë“œ |
| `/api/excel_template/upload` | POST | `upload_excel_template()` | ?‘ì? ?œí”Œë¦??…ë¡œ??|
| `/api/excel_template/info` | GET | `get_excel_template_info()` | ?‘ì? ?œí”Œë¦??•ë³´ |
| `/api/excel_template/download` | GET | `download_excel_template()` | ?‘ì? ?œí”Œë¦??¤ìš´ë¡œë“œ |
| `/api/excel_template/delete` | DELETE | `delete_excel_template()` | ?‘ì? ?œí”Œë¦??? œ |

## ?°ì½”?ˆì´??- `@login_required`: ë¡œê·¸???„ìš”
- `@log_menu_access`: ë©”ë‰´ ?‘ê·¼ ë¡œê·¸ ê¸°ë¡

## ê¶Œí•œ
- `mngr_sett` ê¶Œí•œ ?„ìš”

## ?˜ì¡´??- DAO: `dao/analytics_dao.py`, `dao/mngr_sett_dao.py`
- Service: `service/dashboard_service.py`

## ?°ê? ë¬¸ì„œ
- [../services/dashboard-service.md](../services/dashboard-service.md)
- [../services/mngr-sett-service.md](../services/mngr-sett-service.md)
- [../dao/analytics-dao.md](../dao/analytics-dao.md)
- [../dao/mngr-sett-dao.md](../dao/mngr-sett-dao.md)
- [../templates/mngr_sett.md](../templates/mngr_sett.md)
