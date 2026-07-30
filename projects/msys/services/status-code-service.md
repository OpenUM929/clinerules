# Status Code Service (status_code_service.py)

## 파일 위치

`service/status_code_service.py` (125줄)

## 역할

상태 코드 관리 - DB에서 동적 로드 및 캐싱 (Singleton)

## 주요 함수

| 함수 | 기능 |
|------|------|
| `get_status_codes()` | 상태 코드 조회 |
| `get_status_description(code)` | 상태 코드 설명 조회 |
| `refresh()` | 캐시 새로고침 |

## 캐싱

- Singleton 패턴으로 메모리 캐싱
- DB 변경 시 `refresh()`로 갱신

## 의존성

- `service/mst_service.py` - 마스터 서비스

## 관련 문서

- [services/README.md](README.md) - services 개요
- [routes/api-analysis.md](../routes/api-analysis.md) - 분석 API