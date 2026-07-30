# Jandi Mapper (jandi_mapper.py)

## 파일 위치

`mapper/jandi_mapper.py` (16줄)

## 역할

지정 데이터 SQL 매핑 - 일별 Job 실행 통계

## 주요 함수

| 함수 | 기능 |
|------|------|
| `get_daily_job_counts(job_id, start_date, end_date, all_data, job_ids)` | 일별 Job 통계 |

## SQL 의존성

- `sql/jandi/jandi_sql.py` - get_daily_job_counts 함수

## 관련 문서

- [mapper/README.md](README.md) - mapper 개요
- [services/jandi-service.md](../services/jandi-service.md) - 지정 데이터 서비스