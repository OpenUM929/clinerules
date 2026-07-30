# Data Definition API (data_definition_api.py)

## 파일 위치

`routes/api/data_definition_api.py` (191줄)

## 역할

데이터 정의 REST API - 데이터 목록, 그룹, 저장, 삭제

## 주요 엔드포인트

| 엔드포인트 | 메서드 | 기능 |
|------------|--------|------|
| `/api/data_definition/list` | GET | 데이터 목록 조회 |
| `/api/data_definition/groups` | GET | 데이터 그룹 조회 |
| `/api/data_definition/save` | POST | 데이터 저장 |
| `/api/data_definition/<id>` | PUT | 데이터 수정 |
| `/api/data_definition/<id>` | DELETE | 데이터 삭제 |
| `/api/data_definition/export` | GET | 데이터 내보내기 |
| `/api/data_definition/import` | POST | 데이터 가져오기 |

## 권한

- `login_required` - 로그인 필수
- `check_password_change_required` - 비밀번호 변경 강제

## 의존성

- `service/data_definition_service.py` - 데이터 정의 서비스

## 관련 문서

- [routes/README.md](README.md) - routes 개요
- [routes/data-spec-routes.md](data-spec-routes.md) - 데이터 사양 라우트
- [services/data-definition-service.md](../services/data-definition-service.md) - 데이터 정의 서비스