# api/analysis_api

**문서 위치**: `.clinerules/docs/msys/routes/api-analysis.md`

## 파일
- `D:\dev\msys\routes\api\analysis_api.py` (371줄)

## 역할
데이터 분석 REST API

## Blueprint
```python
analysis_api_bp = Blueprint('analysis_api', __name__, url_prefix='/api/analytics')
```

## 엔드포인트

| 경로 | 메서드 | 함수 | 설명 |
|------|--------|------|------|
| `/api/analytics/success_rate_trend` | GET | `get_analytics_success_rate_trend_api()` | 기간별 성공률 추이 |
| `/api/analytics/trouble_by_code` | GET | `get_analytics_trouble_by_code_api()` | 장애 코드별 비율 |
| `/api/analytics/summary` | GET | `api_analysis_summary()` | 분석 요약 |
| `/api/analytics/trend` | GET | `api_analysis_trend()` | 추이/경향 데이터 |
| `/api/analytics/raw_data` | GET | `api_analysis_raw_data()` | 원시 데이터 |
| `/api/analytics/job_ids` | GET | `api_analysis_job_ids()` | Job ID 목록 |
| `/api/analytics/error_codes` | GET | `api_analysis_error_codes()` | 장애코드 목록 |
| `/api/analytics/error_code_map` | GET | `api_analysis_error_code_map()` | 장애코드 매핑 |
| `/api/analytics/dynamic-chart` | GET | `get_dynamic_chart_data()` | 동적 차트 데이터 |

## 파라미터
| 파라미터 | 타입 | 필수 | 설명 |
|----------|------|------|------|
| start_date | string | 일부 | 시작 날짜 |
| end_date | string | 일부 | 종료 날짜 |
| job_ids | array | 아니오 | Job ID 목록 |
| x_axis | string | 동적차트 | X축 차원 (date, job_id, status) |
| y_axis | string | 동적차트 | Y축 측정항목 |

## 의존성
- Service: `service/dashboard_service.py`, `service/analysis_service.py`, `service/mst_service.py`

## 연관 문서
- [../services/analysis-service.md](../services/analysis-service.md)
- [../services/dashboard-service.md](../services/dashboard-service.md)
