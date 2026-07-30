# Trbl Service (trbl_service.py)

## 파일 위치

`service/trbl_service.py` (70줄)

## 역할

장애 이력 -故障 리스트 조회

## 주요 함수

| 함수 | 기능 |
|------|------|
| `get_trouble_list(start_date, end_date)` | 장애 이력 조회 |

## 의존성

- `mapper/trbl_mapper.py` - 장애 매퍼

## 관련 문서

- [services/README.md](README.md) - services 개요
- [routes/admin-routes.md](../routes/admin-routes.md) - 관리자 라우트