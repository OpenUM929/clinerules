# API Routes (REST API)

**ë¬¸ì„œ ?„ì¹˜**: `.clinerules/projects/msys/routes/api-routes.md`

## ?Œì¼ ?„ì¹˜

`routes/api/` - REST API ?”ë“œ?¬ì¸??
## ??• 

JSON ê¸°ë°˜ REST API ?œê³µ (DataTables, Ajax ??

## ?Œì¼ ëª©ë¡

| ?Œì¼ | ??•  |
|------|------|
| auth_api.py | ?¸ì¦ REST API (49ì¤? |
| dashboard_api.py | ?€?œë³´??REST API |
| data_definition_api.py | ?°ì´???•ì˜ REST API |
| card_summary_api.py | ì¹´ë“œ ?”ì•½ REST API |
| api_key_mngr_routes.py | API ??ê´€ë¦?REST API |
| analysis_api.py | ë¶„ì„ REST API |

## ê°??Œì¼ë³??”ë“œ?¬ì¸??
### auth_api.py

| ?”ë“œ?¬ì¸??| ë©”ì„œ??| ê¸°ëŠ¥ |
|------------|--------|------|
| `/api/auth/status` | GET | ë¡œê·¸???íƒœ ?•ì¸ |
| `/api/auth/validate-password` | POST | ë¹„ë?ë²ˆí˜¸ ?•ì±… ê²€ì¦?|

### dashboard_api.py

| ?”ë“œ?¬ì¸??| ë©”ì„œ??| ê¸°ëŠ¥ |
|------------|--------|------|
| `/api/dashboard/stats` | GET | ?€?œë³´???µê³„ |
| `/api/dashboard/data` | GET | ?€?œë³´???°ì´??|

### data_definition_api.py

| ?”ë“œ?¬ì¸??| ë©”ì„œ??| ê¸°ëŠ¥ |
|------------|--------|------|
| `/api/data/definition` | GET | ?°ì´???•ì˜ ì¡°íšŒ |
| `/api/data/definition` | POST | ?°ì´???•ì˜ ?€??|

### card_summary_api.py

| ?”ë“œ?¬ì¸??| ë©”ì„œ??| ê¸°ëŠ¥ |
|------------|--------|------|
| `/api/card/summary` | GET | ì¹´ë“œ ?”ì•½ ?°ì´??|

### api_key_mngr_routes.py

| ?”ë“œ?¬ì¸??| ë©”ì„œ??| ê¸°ëŠ¥ |
|------------|--------|------|
| `/api/key/mngr` | GET | API ??ëª©ë¡ |
| `/api/key/mngr` | POST | API ??ì¶”ê? |
| `/api/key/mngr/<id>` | PUT | API ???˜ì • |
| `/api/key/mngr/<id>` | DELETE | API ???? œ |

### analysis_api.py

| ?”ë“œ?¬ì¸??| ë©”ì„œ??| ê¸°ëŠ¥ |
|------------|--------|------|
| `/api/analysis` | GET/POST | ë¶„ì„ ?°ì´??|

## ê´€??ë¬¸ì„œ

- [routes/README.md](README.md) - routes ê°œìš”
- [services/README.md](../services/README.md) - ë¹„ì¦ˆ?ˆìŠ¤ ë¡œì§
- [00-core.md](../../00-core.md) - ?˜ì¹¨ë°