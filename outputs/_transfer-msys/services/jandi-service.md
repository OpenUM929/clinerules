# Jandi Service (jandi_service.py)

## 파일 위치

`service/jandi_service.py` (28줄)

## 역할

지정 데이터 (Jandi) - 일별 작업 성공 실행 건수 조회

## 주요 함수

| 함수 | 기능 |
|------|------|
| `get_daily_job_counts(job_id, start_date, end_date, all_data, user)` | 일별 Job 실행 통계 |

## 데이터 필터링

- 관리자: 전체 데이터 조회
- 일반 사용자: data_permissions 기반 필터링

## 의존성

- `mapper/jandi_mapper.py` - 지정 데이터 매퍼

## 관련 문서

- [services/README.md](README.md) - services 개요
- [routes/jandi-routes.md](../routes/jandi-routes.md) - 지정 데이터 라우트