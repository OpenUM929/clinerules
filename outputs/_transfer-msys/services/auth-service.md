# Auth Service (auth_service.py)

## 파일 위치

`service/auth_service.py` (66줄)

## 역할

인증 관련 비즈니스 로직 - 사용자 검증, 비밀번호 변경, 권한 조회

## 주요 함수

| 함수 | 기능 | 반환 |
|------|------|------|
| `get_user_by_id(user_id)` | ID로 사용자 조회 | user_info, permissions |
| `verify_user(user_id, password)` | 사용자 ID/비밀번호 검증 | (user_info, message) |
| `change_password(user_id, current_password, new_password)` | 비밀번호 변경 | (success, message) |

## 검증 로직

1. 사용자 ID 존재 확인
2. 계정 상태가 `APPROVED`인지 확인
3. 비밀번호 일치 검증
4. 권한 조회 후 반환

## 의존성

- `mapper/user_mapper.py` - 사용자 SQL 매핑
- `service/password_service.py` - 비밀번호 검증/해시

## 관련 문서

- [services/README.md](README.md) - services 개요
- [routes/auth-routes.md](../routes/auth-routes.md) - 인증 라우트
- [services/password-service.md](password-service.md) - 비밀번호 서비스