# Trbl Hist DAO (trbl_hist_dao.py)

## 파일 위치

`dao/trbl_hist_dao.py` (232줄)

## 역할

장애 이력 접근 - TB_CON_HIST에서 장애 상태 조회

## 주요 함수

| 함수 | 기능 |
|------|------|
| `get_all_troubles(start_date, end_date)` | 장애 상태별 카운트 조회 |
| `get_trouble_details(trbl_status, start_date, end_date)` | 장애 상세 조회 |

## SQL 의존성

- `sql/trbl/trbl_sql.py` - TrblSQL 클래스

## 관련 문서

- [dao/README.md](README.md) - DAO 개요
- [services/trbl-service.md](../services/trbl-service.md) - 장애 서비스