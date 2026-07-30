# data_spec_routes

**ë¬¸ì„œ ?„ì¹˜**: `.clinerules/projects/msys/routes/data-spec-routes.md`

## ?Œì¼
- `D:\dev\msys\routes\data_spec_routes.py` (159ì¤?

## ??• 
?°ì´??ëª…ì„¸??ê´€ë¦?- CRUD, URL ?¤í¬?˜í•‘

## Blueprint
```python
bp = Blueprint('data_spec', __name__, url_prefix='/')
```

## ?”ë“œ?¬ì¸??
| ê²½ë¡œ | ë©”ì„œ??| ?¨ìˆ˜ | ?¤ëª… |
|------|--------|------|------|
| `/data_spec` | GET | `data_spec_page()` | ëª…ì„¸???˜ì´ì§€ |
| `/api/data-spec` | GET, POST | `handle_data_specs()` | ëª©ë¡ ì¡°íšŒ/?ì„± |
| `/api/scrape-spec` | POST | `scrape_spec_from_url()` | URL ?¤í¬?˜í•‘ |
| `/api/data-spec/check-name` | GET | `check_data_spec_name()` | ?´ë¦„ ì¤‘ë³µ ?•ì¸ |
| `/api/data-spec/<id>` | GET, PUT, DELETE | `handle_data_spec_by_id()` | ?ì„¸/?˜ì •/?? œ |

## ?°ì½”?ˆì´??- `@log_menu_access`: ë©”ë‰´ ?‘ê·¼ ë¡œê·¸ ê¸°ë¡

## ?˜ì¡´??- Service: `service/data_spec_service.py`
- DAO: `dao/analytics_dao.py`

## ?°ê? ë¬¸ì„œ
- [../services/data-spec-service.md](../services/data-spec-service.md)
- [../templates/data_spec.md](../templates/data_spec.md)
