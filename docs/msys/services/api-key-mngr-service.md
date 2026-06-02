# ApiKey Mngr Service (api_key_mngr_service.py)

## 파일 위치

`service/api_key_mngr_service.py` (405줄)

## 역할

API 키 관리 - CRUD, 만료일 계산, CD 동기화

## 주요 함수

| 함수 | 기능 |
|------|------|
| `get_all_api_key_mngr()` | 전체 API 키 목록 조회 |
| `get_api_key_mngr(cd)` | 단일 API 키 조회 |
| `insert(data)` | API 키 추가 |
| `update(data)` | API 키 수정 |
| `delete(cd)` | API 키 삭제 |
| `update_cd_from_mngr_sett()` | TB_MNGR_SETT에서 CD 동기화 |

## 데이터 처리

1. 만료일 계산: `start_dt + due(년)`
2. 남은 일수: `expiry_dt - today`
3. 만료 임박 판단: `days_remaining <= 30`
4. 정렬: 시작일 기준 내림차순

## 의존성

- `dao/api_key_mngr_dao.py` - API 키 DAO
- `dao/con_mst_dao.py` - 연결 마스터 DAO
- `msys/mail_send.py` - 메일 발송

## 관련 문서

- [services/README.md](README.md) - services 개요
- [services/mail-scheduler-service.md](mail-scheduler-service.md) - 메일 스케줄러