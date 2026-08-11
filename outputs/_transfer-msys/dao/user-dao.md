# User DAO (user_dao.py)

## 파일 위치

`dao/user_dao.py` (95줄)

## 역할

사용자 데이터 접근 - 사용자 조회, 생성, 수정, 삭제

## 주요 함수

| 함수 | 기능 |
|------|------|
| `find_by_id(user_id)` | ID로 사용자 조회 |
| `find_all()` | 전체 사용자 조회 |
| `create(user_id, password)` | 사용자 생성 |
| `update(user_id, data)` | 사용자 수정 |
| `delete(user_id)` | 사용자 삭제 |

## SQL 의존성

- `user/find_by_id.sql`

## 관련 문서

- [dao/README.md](README.md) - DAO 개요
- [services/auth-service.md](../services/auth-service.md) - 인증 서비스