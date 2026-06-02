# login

## 파일
- Template: `D:\dev\msys\templates\login.html`
- Route: `D:\dev\msys\routes\auth_routes.py`

## 도메인
사용자 인증 - 로그인, 회원가입, 비밀번호 초기화 요청

## 엔드포인트
| 용도 | URL | 메서드 |
|------|-----|--------|
| 로그인 | GET/POST /login | 로그인 처리 |
| 회원가입 | POST /register | 사용자 등록 |
| 게스트 로그인 | GET /guest_login | 게스트 세션 |
| 비밀번호 초기화 요청 | POST /request-reset-password | 이메일 발송 |

## 폼/입력
| 필드 | ID/Name | 타입 | 필수 |
|------|---------|------|------|
| 사용자 ID | user_id | text | ✓ |
| 비밀번호 | password | password | ✓ |
| 비밀번호 확인 | password_confirm | password | ✓ (회원가입) |

## 기능
- 탭 전환: 로그인 / 회원가입 / 비밀번호 초기화 요청
- 비밀번호 정책 검증 (8자 이상, 특수문자, 연속숫자 불가, 반복숫자 불가)
- 게스트 로그인
- 비밀번호 초기화 이메일 요청

## 연관 문서
- Service: [../services/auth-service.md](../services/auth-service.md)
- DAO: [../dao/user-dao.md](../dao/user-dao.md)
- Mapper: [../mapper/user-mapper.md](../mapper/user-mapper.md)
- Route: [../routes/auth-routes.md](../routes/auth-routes.md)
