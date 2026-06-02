# API Routes (REST API)

**문서 위치**: `.clinerules/docs/msys/routes/api-routes.md`

## 파일 위치

`routes/api/` - REST API 엔드포인트

## 역할

JSON 기반 REST API 제공 (DataTables, Ajax 등)

## 파일 목록

| 파일 | 역할 |
|------|------|
| auth_api.py | 인증 REST API (49줄) |
| dashboard_api.py | 대시보드 REST API |
| data_definition_api.py | 데이터 정의 REST API |
| card_summary_api.py | 카드 요약 REST API |
| api_key_mngr_routes.py | API 키 관리 REST API |
| analysis_api.py | 분석 REST API |

## 각 파일별 엔드포인트

### auth_api.py

| 엔드포인트 | 메서드 | 기능 |
|------------|--------|------|
| `/api/auth/status` | GET | 로그인 상태 확인 |
| `/api/auth/validate-password` | POST | 비밀번호 정책 검증 |

### dashboard_api.py

| 엔드포인트 | 메서드 | 기능 |
|------------|--------|------|
| `/api/dashboard/stats` | GET | 대시보드 통계 |
| `/api/dashboard/data` | GET | 대시보드 데이터 |

### data_definition_api.py

| 엔드포인트 | 메서드 | 기능 |
|------------|--------|------|
| `/api/data/definition` | GET | 데이터 정의 조회 |
| `/api/data/definition` | POST | 데이터 정의 저장 |

### card_summary_api.py

| 엔드포인트 | 메서드 | 기능 |
|------------|--------|------|
| `/api/card/summary` | GET | 카드 요약 데이터 |

### api_key_mngr_routes.py

| 엔드포인트 | 메서드 | 기능 |
|------------|--------|------|
| `/api/key/mngr` | GET | API 키 목록 |
| `/api/key/mngr` | POST | API 키 추가 |
| `/api/key/mngr/<id>` | PUT | API 키 수정 |
| `/api/key/mngr/<id>` | DELETE | API 키 삭제 |

### analysis_api.py

| 엔드포인트 | 메서드 | 기능 |
|------------|--------|------|
| `/api/analysis` | GET/POST | 분석 데이터 |

## 관련 문서

- [routes/README.md](README.md) - routes 개요
- [services/README.md](../services/README.md) - 비즈니스 로직
- [00-core.md](../../00-core.md) - 나침반