# Analysis Routes (analysis_routes.py)

## 파일 위치

`routes/analysis_routes.py` (44줄)

## 역할

분석 페이지 - 차트 분석, 데이터 분석

## 주요 엔드포인트

| 엔드포인트 | 메서드 | 템플릿 | 기능 |
|------------|--------|--------|------|
| `/chart_analysis` | GET | chart_analysis.html | 차트 분석 페이지 |
| `/data_analysis` | GET | data_analysis.html | 데이터 분석 페이지 |

## 권한

- `login_required` - 로그인 필수
- `analysis_required` - analysis 권한
- `data_analysis_required` - data_analysis 권한

## 의존성

- `dao/analytics_dao.py` - 분석 DAO

## 관련 문서

- [routes/README.md](README.md) - routes 개요
- [services/analysis-service.md](../services/analysis-service.md) - 분석 서비스