# API Key Mngr API (api_key_mngr_routes.py)

## 파일 위치

`routes/api/api_key_mngr_routes.py` (562줄)

## 역할

API 키 관리 REST API - CRUD, 메일 발송, CD 동기화

## 주요 엔드포인트

| 엔드포인트 | 메서드 | 기능 |
|------------|--------|------|
| `/api/api_key_mngr` | GET | 전체 API 키 목록 |
| `/api/api_key_mngr/paged` | GET | 페이징 + 검색 API 키 목록 |
| `/api/api_key_mngr/<cd>` | GET | 단일 API 키 조회 |
| `/api/api_key_mngr` | POST | API 키 추가 |
| `/api/api_key_mngr/<cd>` | PUT | API 키 수정 |
| `/api/api_key_mngr/<cd>` | DELETE | API 키 삭제 |
| `/api/api_key_mngr/sync-cd` | POST | CD 동기화 (TB_MNGR_SETT → TB_API_KEY_MNGR) |
| `/api/api_key_mngr/mail/send` | POST | 메일 수동 발송 |
| `/api/api_key_mngr/mail/test` | GET | 메일 전송 테스트 |

## 권한

- `login_required` - 로그인 필수
- `check_password_change_required` - 비밀번호 변경 강제
- `api_key_mngr_required` - api_key_mngr 권한

## 의존성

- `service/api_key_mngr_service.py` - API 키 서비스
- `service/mail_scheduler_service.py` - 메일 스케줄러 서비스

## 관련 문서

- [routes/README.md](README.md) - routes 개요
- [services/api-key-mngr-service.md](../services/api-key-mngr-service.md) - API 키 서비스