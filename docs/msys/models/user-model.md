# User Model (user.py)

## 파일 위치

`models/user.py` (6줄)

## 역할

Flask-Login 사용자 모델 - 세션 관리용 UserMixin 상속

## 클래스

| 클래스 | 상속 | 기능 |
|--------|------|------|
| `User` | UserMixin | Flask-Login 세션 관리 |

## 속성

| 속성 | 타입 | 설명 |
|------|------|------|
| `id` | str | 사용자 ID |
| `permissions` | list | 권한 목록 |

## 관련 문서

- [msys/README.md](../README.md) - 프로젝트 개요
- [routes/auth-routes.md](../routes/auth-routes.md) - 인증 라우트