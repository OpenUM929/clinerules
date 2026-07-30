# auth_routes

**문서 ?�치**: `.clinerules/projects/msys/routes/auth-routes.md`

## ?�일
- `D:\dev\msys\routes\auth_routes.py` (492�?

## ??��
?�용???�증 - 로그?? 로그?�웃, ?�원가?? 비�?번호 변�?초기?? 게스??로그??
## Blueprint
```python
auth_bp = Blueprint('auth', __name__)
```

## ?�드?�인??
| 경로 | 메서??| ?�수 | ?�명 |
|------|--------|------|------|
| `/login` | GET, POST | `login()` | 로그??(?�션 관�? 권한 ?�정) |
| `/logout` | GET | `logout()` | 로그?�웃 |
| `/register` | POST | `register()` | ?�원가???�청 |
| `/change_password` | GET, POST | `change_password()` | 비�?번호 변�?|
| `/guest_login` | GET | `guest_login()` | 게스??로그??(collection_schedule�? |
| `/request-reset-password` | POST | `request_reset_password()` | 비�?번호 초기???�청 |

## 권한 ?�코?�이??| ?�코?�이??| 권한 |
|-----------|------|
| `admin_required` | mngr_sett |
| `collection_schedule_required` | collection_schedule |
| `analysis_required` | analysis |
| `data_analysis_required` | data_analysis |
| `card_summary_required` | card_summary |
| `data_report_required` | data_report |
| `data_spec_required` | data_spec |
| `jandi_required` | jandi |
| `mapping_required` | mapping |
| `api_key_mngr_required` | api_key_mngr |
| `mngr_sett_required` | mngr_sett |
| `check_password_change_required` | 비�?번호 변�?강제 |

## 주요 기능

### 로그???�로?�스
1. ?�용???�증 (AuthService.verify_user)
2. 기본 권한 추�? (dashboard, collection_schedule)
3. ?�이???�근 권한 조회 �??�션 ?�??4. 관리자 권한 ?�인 �?부??5. ?�션 만료 ?�간 ?�정 (관리자: PERMANENT_SESSION_LIFETIME, ?�반: 20�?
6. 메뉴 기반 �??�이지 리다?�렉??7. 로그???�벤??기록

### ?�션 관�?- ?�션 ?�이???�근 권한: `session['user']['data_permissions']`
- 비�?번호 초기??강제: user_id == password

## ?�존??- Service: `service/auth_service.py`, `service/dashboard_service.py`
- Mapper: `mapper/user_mapper.py`
- Model: `models/user.py`

## ?��? 문서
- [../services/auth-service.md](../services/auth-service.md)
- [../services/password-service.md](../services/password-service.md)
- [../mapper/user-mapper.md](../mapper/user-mapper.md)
- [../templates/login.md](../templates/login.md)
- [../templates/change_password.md](../templates/change_password.md)
