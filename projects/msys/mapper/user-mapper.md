# User Mapper (user_mapper.py)

## 파일 위치

`mapper/user_mapper.py` (134줄)

## 역할

사용자 데이터 SQL 매핑 - 조회, 삽입, 수정, 삭제

## 주요 함수

| 함수 | 기능 |
|------|------|
| `find_by_id(user_id)` | ID로 사용자 조회 |
| `find_all()` | 전체 사용자 조회 |
| `delete_by_id(user_id)` | 사용자 삭제 |
| `save(user_id, hashed_password)` | 사용자 저장 |
| `find_user_permissions(user_id)` | 사용자 권한 조회 |
| `find_user_data_permissions(user_id)` | 사용자 데이터 권한 조회 |

## SQL 의존성

- `sql/user/user_sql.py` - 사용자 SQL 정의

## 관련 문서

- [mapper/README.md](README.md) - mapper 개요
- [services/auth-service.md](../services/auth-service.md) - 인증 서비스
- [dao/user-dao.md](user-dao.md) - 사용자 DAO