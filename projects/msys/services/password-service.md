# Password Service (password_service.py)

## 파일 위치

`service/password_service.py` (142줄)

## 역할

비밀번호 해싱 및 검증 - PBKDF2 + SHA-512

## 주요 함수

| 함수 | 기능 |
|------|------|
| `hash_password(password)` | 비밀번호 해싱 (salt$hash 형식) |
| `check_password(password, hashed_password)` | 비밀번호 검증 |
| `validate_password_policy_detailed(password)` | 비밀번호 정책 검증 |
| `generate_random_password(length)` | 랜덤 비밀번호 생성 |

## 해싱 방식

- 알고리즘: PBKDF2 + SHA-512
- iterations: 260,000
- salt size: 16 bytes

## 관련 문서

- [services/README.md](README.md) - services 개요
- [routes/auth-routes.md](../routes/auth-routes.md) - 인증 라우트