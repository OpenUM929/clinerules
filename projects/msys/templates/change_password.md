# change_password

## ?Œì¼
- Template: `templates/change_password.html`
- Route: `routes/auth_routes.py`

## ?„ë©”??ë¹„ë?ë²ˆí˜¸ ë³€ê²?- ?„ì¬ ë¹„ë?ë²ˆí˜¸ ?•ì¸ ????ë¹„ë?ë²ˆí˜¸ ?¤ì •

## ?•ì¥
- `base.html`

## ?”ë“œ?¬ì¸??| ?©ë„ | URL | ë©”ì„œ??|
|------|-----|--------|
| ë¹„ë?ë²ˆí˜¸ ë³€ê²?| POST /auth/change_password | ???œì¶œ |
| ë¹„ë?ë²ˆí˜¸ ê²€ì¦?| POST /api/auth/validate-password | JSON |

## ???„ë“œ
| ?„ë“œ | ID | ?€??| ?¤ëª… |
|------|-----|------|------|
| ?„ì¬ ë¹„ë?ë²ˆí˜¸ | current_password | password | ?„ì¬ ë¹„ë?ë²ˆí˜¸ |
| ??ë¹„ë?ë²ˆí˜¸ | new_password | password | ??ë¹„ë?ë²ˆí˜¸ |
| ??ë¹„ë?ë²ˆí˜¸ ?•ì¸ | confirm_password | password | ?•ì¸ |

## ë¹„ë?ë²ˆí˜¸ ?•ì±…
- 8???´ìƒ
- ?°ì†???«ì (?? 123) ?¬ìš© ë¶ˆê?
- ?™ì¼???«ì ë°˜ë³µ (?? 111) ?¬ìš© ë¶ˆê?
- ?¹ìˆ˜ë¬¸ì 1ê°??´ìƒ ?¬í•¨

## JS ?Œì¼
- ?´ë¼?´ì–¸??ê²€ì¦??¬í•¨ (inline script)

## ?°ê? ë¬¸ì„œ
- Service: `service/auth_service.py`, `service/password_service.py`
- Route: `.clinerules/projects/msys/routes/auth-routes.md`
