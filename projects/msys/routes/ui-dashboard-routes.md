# ui/dashboard_routes

**ë¬¸ì„œ ?„ì¹˜**: `.clinerules/projects/msys/routes/ui-dashboard-routes.md`

## ?Œì¼
- `D:\dev\msys\routes\ui\dashboard_routes.py` (59ì¤?

## ??• 
?€?œë³´???˜ì´ì§€ ?Œë”ë§?
## Blueprint
```python
dashboard_bp = Blueprint('dashboard', __name__)
```

## ?”ë“œ?¬ì¸??
| ê²½ë¡œ | ë©”ì„œ??| ?¨ìˆ˜ | ?¤ëª… |
|------|--------|------|------|
| `/dashboard` | GET | `dashboard()` | ?€?œë³´???˜ì´ì§€ |

## ?°ì½”?ˆì´??- `@login_required`: ë¡œê·¸???„ìš”
- `@check_password_change_required`: ë¹„ë?ë²ˆí˜¸ ë³€ê²??„ìš” ??ì²´í¬
- `@log_menu_access`: ë©”ë‰´ ?‘ê·¼ ë¡œê·¸ ê¸°ë¡

## ê¶Œí•œ
- `dashboard` ê¶Œí•œ ?„ìš”

## ?œí”Œë¦?- `dashboard.html`

## ?°ê? ë¬¸ì„œ
- [../services/dashboard-service.md](../services/dashboard-service.md)
- [../dao/analytics-dao.md](../dao/analytics-dao.md)
- [../templates/dashboard.md](../templates/dashboard.md)
