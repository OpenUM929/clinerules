# Trbl Mapper (trbl_mapper.py)

## 파일 위치

`mapper/trbl_mapper.py` (92줄)

## 역할

장애 SQL 매핑 - TB_CON_HIST에서 장애 데이터 조회

## 주요 함수

| 함수 | 기능 |
|------|------|
| `get_all_troubles(start_date, end_date)` | 장애 이력 조회 |

## SQL 의존성

- `sql/trbl/trbl_sql.py` - TrblSQL 클래스
- `sql/dashboard/dashboard_sql.py` - DashboardSQL 클래스

## 관련 문서

- [mapper/README.md](README.md) - mapper 개요
- [services/trbl-service.md](../services/trbl-service.md) - 장애 서비스