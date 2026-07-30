# User Service (user_service.py)

## 파일 위치

`service/user_service.py` (139줄)

## 역할

사용자 관리 - 사용자 목록, 권한 조회/수정

## 주요 함수

| 함수 | 기능 |
|------|------|
| `get_all_users_with_permissions(search_term)` | 전체 사용자 + 권한 조회 |
| `create_user(user_id, password)` | 사용자 생성 |
| `update_user(user_id, data)` | 사용자 수정 |
| `delete_user(user_id)` | 사용자 삭제 |

## 의존성

- `mapper/user_mapper.py` - 사용자 매퍼
- `service/dashboard_service.py` - 대시보드 서비스
- `service/password_service.py` - 비밀번호 서비스

## 관련 문서

- [services/README.md](README.md) - services 개요
- [routes/mngr-sett-routes.md](../routes/mngr-sett-routes.md) - 관리자 설정 라우트