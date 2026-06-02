# Analysis Service (analysis_service.py)

## 파일 위치

`service/analysis_service.py` (52줄)

## 역할

분석 데이터 조회 - 동적 차트 데이터, 권한 기반 필터링

## 주요 함수

| 함수 | 기능 |
|------|------|
| `get_dynamic_chart_data(params, user)` | 동적 차트 데이터 조회 |
| `_get_allowed_job_ids(user, job_ids)` | 권한 기반 Job 필터링 |

## 데이터 흐름

1. `_get_allowed_job_ids()` - 관리자/일반 사용자 권한 확인
2. `mapper.get_dynamic_chart_data()` - 차트 데이터 조회
3. 권한 필터링 적용

## 의존성

- `mapper/analysis_mapper.py` - 분석 매퍼

## 관련 문서

- [services/README.md](README.md) - services 개요
- [routes/analysis-routes.md](../routes/analysis-routes.md) - 분석 라우트