# auth_routes

**문서 위치**: `.clinerules/docs/msys/routes/auth-routes.md`

## 파일
- `D:\dev\msys\routes\auth_routes.py` (492줄)

## 역할
사용자 인증 - 로그인, 로그아웃, 회원가입, 비밀번호 변경/초기화, 게스트 로그인

## Blueprint
```python
auth_bp = Blueprint('auth', __name__)
```

## 엔드포인트

| 경로 | 메서드 | 함수 | 설명 |
|------|--------|------|------|
| `/login` | GET, POST | `login()` | 로그인 (세션 관리, 권한 설정) |
| `/logout` | GET | `logout()` | 로그아웃 |
| `/register` | POST | `register()` | 회원가입 신청 |
| `/change_password` | GET, POST | `change_password()` | 비밀번호 변경 |
| `/guest_login` | GET | `guest_login()` | 게스트 로그인 (collection_schedule만) |
| `/request-reset-password` | POST | `request_reset_password()` | 비밀번호 초기화 요청 |

## 권한 데코레이터
| 데코레이터 | 권한 |
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
| `check_password_change_required` | 비밀번호 변경 강제 |

## 주요 기능

### 로그인 프로세스
1. 사용자 인증 (AuthService.verify_user)
2. 기본 권한 추가 (dashboard, collection_schedule)
3. 데이터 접근 권한 조회 및 세션 저장
4. 관리자 권한 확인 및 부여
5. 세션 만료 시간 설정 (관리자: PERMANENT_SESSION_LIFETIME, 일반: 20분)
6. 메뉴 기반 첫 페이지 리다이렉트
7. 로그인 이벤트 기록

### 세션 관리
- 세션 데이터 접근 권한: `session['user']['data_permissions']`
- 비밀번호 초기화 강제: user_id == password

## 의존성
- Service: `service/auth_service.py`, `service/dashboard_service.py`
- Mapper: `mapper/user_mapper.py`
- Model: `models/user.py`

## 연관 문서
- [../services/auth-service.md](../services/auth-service.md)
- [../services/password-service.md](../services/password-service.md)
- [../mapper/user-mapper.md](../mapper/user-mapper.md)
- [../templates/login.md](../templates/login.md)
- [../templates/change_password.md](../templates/change_password.md)
