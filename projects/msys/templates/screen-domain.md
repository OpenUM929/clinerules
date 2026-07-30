# Screen Domain Map

**ë¬¸ì„œ ?„ì¹˜**: `.clinerules/projects/msys/templates/screen-domain.md`

## ê°œìš”

?”ë©´(URL)ê³??œí”Œë¦??Œì¼ ë§¤í•‘. UI ë³€ê²???ì°¸ì¡°.

## ?”ë©´-?œí”Œë¦?ë§¤í•‘

| ?”ë©´ëª?| ?œí”Œë¦?| URL | Route | ?„ë©”??|
|--------|--------|-----|-------|--------|
| base | base.html | - | - | ê¸°ë³¸ ?ˆì´?„ì›ƒ (navbar, CSS/JS) |
| login | login.html | /login | auth_routes.py | ?¸ì¦ (ë¡œê·¸???Œì›ê°€??ë¹„ë?ë²ˆí˜¸ì´ˆê¸°?? |
| dashboard | dashboard.html | /, /dashboard | dashboard_routes.py | ?¤ì‹œê°??˜ì§‘ ?„í™© |
| api_key_mngr | api_key_mngr.html | /api_key_mngr | api_key_mngr_routes.py | API ??ë§Œë£Œ ê´€ë¦?|
| mngr_sett | mngr_sett.html | /admin/mngr_sett | admin_routes.py | ë©”ë‰´/?¤ì • ê´€ë¦?|
| jandi | jandi.html | /jandi | jandi_routes.py | ì§€???°ì´???„í™© |
| card_summary | card_summary.html | /card/summary | card_summary_routes.py | ì¹´ë“œ ?”ì•½ |
| mapping | mapping_management.html | /mapping | mapping_routes.py | ì»¬ëŸ¼ ë§¤í•‘ ê´€ë¦?|
| data_spec | data_spec.html | /data/spec | data_spec_routes.py | ?°ì´???¬ì–‘ |
| data_report | data_report.html | /data/report | data_report_routes.py | ?°ì´??ë¦¬í¬??|
| data_analysis | data_analysis.html | /data_analysis | analysis_routes.py | ?°ì´??ë¶„ì„ |
| chart_analysis | chart_analysis.html | /chart_analysis | analysis_routes.py | ì°¨íŠ¸ ë¶„ì„ |
| collection_schedule | collection_schedule.html | /collection_schedule | collection_schedule_routes.py | ?˜ì§‘ ?¼ì • |
| change_password | change_password.html | /change-password | auth_routes.py | ë¹„ë?ë²ˆí˜¸ ë³€ê²?|
| navbar | navbar.html | - | - | ?¤ë¹„ê²Œì´??ë°?|
| collapsible_controls | collapsible_controls.html | - | - | ?‘ì´??ì»¨íŠ¸ë¡?(dashboard ?¬í•¨) |
| unauthorized | unauthorized.html | - | - | ê¶Œí•œ ?†ìŒ |
| empty_base | empty_base.html | - | - | ë¹?ê¸°ë³¸ ?ˆì´?„ì›ƒ |
| api_test | api_test.html | - | - | API ?ŒìŠ¤??|
| raw_data | raw_data.html | - | - | ?ì‹œ ?°ì´??|
| test_css | test_css.html | - | - | CSS ?ŒìŠ¤??|
| mngr_sett_test | mngr_sett_test.html | /mngr_sett_test | mngr_sett_routes.py | ë©”ë‰´ ?¤ì • ?ŒìŠ¤??|

## ê³„ì¸µ êµ¬ì¡°

```
base.html (ìµœìƒ???ˆì´?„ì›ƒ)
?œâ??€ navbar.html (?¤ë¹„ê²Œì´??
?œâ??€ collapsible_controls.html (?‘ì´??ì»¨íŠ¸ë¡?
?”â??€ {?”ë©´ëª?.html (base.html ?•ì¥)
    ?œâ??€ dashboard.html
    ?œâ??€ api_key_mngr.html
    ?œâ??€ mngr_sett.html
    ?”â??€ ...
```

## ê°œë³„ ë¬¸ì„œ

| ?”ë©´ëª?| ë¬¸ì„œ |
|--------|------|
| base | - |
| login | [login.md](login.md) |
| dashboard | [dashboard.md](dashboard.md) |
| api_key_mngr | [api_key_mngr.md](api_key_mngr.md) |
| mngr_sett | [mngr_sett.md](mngr_sett.md) |
| jandi | [jandi.md](jandi.md) |
| card_summary | [card_summary.md](card_summary.md) |
| mapping | [mapping.md](mapping.md) |
| data_spec | [data_spec.md](data_spec.md) |
| data_report | [data_report.md](data_report.md) |
| data_analysis | [data_analysis.md](data_analysis.md) |
| chart_analysis | [chart_analysis.md](chart_analysis.md) |
| collection_schedule | [collection_schedule.md](collection_schedule.md) |
| change_password | [change_password.md](change_password.md) |
