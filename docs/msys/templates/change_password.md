# change_password

## 파일
- Template: `templates/change_password.html`
- Route: `routes/auth_routes.py`

## 도메인
비밀번호 변경 - 현재 비밀번호 확인 후 새 비밀번호 설정

## 확장
- `base.html`

## 엔드포인트
| 용도 | URL | 메서드 |
|------|-----|--------|
| 비밀번호 변경 | POST /auth/change_password | 폼 제출 |
| 비밀번호 검증 | POST /api/auth/validate-password | JSON |

## 폼 필드
| 필드 | ID | 타입 | 설명 |
|------|-----|------|------|
| 현재 비밀번호 | current_password | password | 현재 비밀번호 |
| 새 비밀번호 | new_password | password | 새 비밀번호 |
| 새 비밀번호 확인 | confirm_password | password | 확인 |

## 비밀번호 정책
- 8자 이상
- 연속된 숫자 (예: 123) 사용 불가
- 동일한 숫자 반복 (예: 111) 사용 불가
- 특수문자 1개 이상 포함

## JS 파일
- 클라이언트 검증 포함 (inline script)

## 연관 문서
- Service: `service/auth_service.py`, `service/password_service.py`
- Route: `.clinerules/docs/msys/routes/auth-routes.md`
