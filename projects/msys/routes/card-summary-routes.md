# card_summary_routes

**ë¬¸ì„œ ?„ì¹˜**: `.clinerules/projects/msys/routes/card-summary-routes.md`

## ?Œì¼
- `D:\dev\msys\routes\card_summary_routes.py` (18ì¤?

## ??• 
ì¹´ë“œ ?”ì•½ ?˜ì´ì§€ ?Œë”ë§?
## Blueprint
```python
card_summary_bp = Blueprint('card_summary', __name__)
```

## ?”ë“œ?¬ì¸??
| ê²½ë¡œ | ë©”ì„œ??| ?¨ìˆ˜ | ?¤ëª… |
|------|--------|------|------|
| `/card_summary` | GET | `card_summary_page()` | ì¹´ë“œ ?”ì•½ ?˜ì´ì§€ |

## ?°ì½”?ˆì´??- `@login_required`: ë¡œê·¸???„ìš”
- `@log_menu_access`: ë©”ë‰´ ?‘ê·¼ ë¡œê·¸ ê¸°ë¡
- `@card_summary_required`: card_summary ê¶Œí•œ

## ?œí”Œë¦?- `card_summary.html`

## ?˜ì¡´??- Service: `service/card_summary_service.py`

## ?°ê? ë¬¸ì„œ
- [../services/card-summary-service.md](../services/card-summary-service.md)
- [../templates/card_summary.md](../templates/card_summary.md)
