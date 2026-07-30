# jandi_routes

**ë¬¸ì„œ ?„ì¹˜**: `.clinerules/projects/msys/routes/jandi-routes.md`

## ?Œì¼
- `D:\dev\msys\routes\jandi_routes.py` (92ì¤?

## ??• 
?”ë”” ëª¨ë‹ˆ?°ë§ - Job ID ëª©ë¡, ë§ˆìŠ¤???ì„¸?•ë³´, ?ˆíŠ¸ë§??°ì´??
## Blueprint
```python
bp = Blueprint('jandi', __name__, url_prefix='/')
```

## ?”ë“œ?¬ì¸??
| ê²½ë¡œ | ë©”ì„œ??| ?¨ìˆ˜ | ?¤ëª… |
|------|--------|------|------|
| `/jandi` | GET | `jandi_page()` | ?”ë”” ?˜ì´ì§€ |
| `/api/job-list` | GET | `get_job_list()` | Job ID ëª©ë¡ (DataTables) |
| `/api/job_mst_info` | GET | `get_job_mst_info()` | ë§ˆìŠ¤???ì„¸?•ë³´ |
| `/api/jandi-data` | GET | `get_jandi_data()` | ?”ë”” ?ˆíŠ¸ë§??°ì´??|
| `/api/jandi/raw_data` | GET | `get_jandi_data()` | ?ì‹œ ?°ì´??|

## ?Œë¼ë¯¸í„°
| ?Œë¼ë¯¸í„° | ?€??| ?¤ëª… |
|----------|------|------|
| start | int | DataTables ?œì‘ ?„ì¹˜ |
| length | int | DataTables ?˜ì´ì§€ ?¬ê¸° |
| search[value] | string | ê²€?‰ì–´ |
| start_date | string | ?œì‘ ? ì§œ |
| end_date | string | ì¢…ë£Œ ? ì§œ |
| allData | boolean | ?„ì²´ ?°ì´??ì¡°íšŒ |
| job_id | string | Job ID |

## ?˜ì¡´??- Service: `service/mst_service.py`, `service/jandi_service.py`

## ?°ê? ë¬¸ì„œ
- [../services/jandi-service.md](../services/jandi-service.md)
- [../templates/jandi.md](../templates/jandi.md)
