# Analysis Mapper (analysis_mapper.py)

## 파일 위치

`mapper/analysis_mapper.py` (24줄)

## 역할

분석 SQL 매핑 - 동적 차트 데이터 조회

## 주요 함수

| 함수 | 기능 |
|------|------|
| `get_dynamic_chart_data(params)` | 동적 쿼리로 분석 데이터 조회 |

## SQL 의존성

- `sql/analytics/analytics_sql.py` - AnalyticsSQL 클래스

## 관련 문서

- [mapper/README.md](README.md) - mapper 개요
- [services/analysis-service.md](../services/analysis-service.md) - 분석 서비스