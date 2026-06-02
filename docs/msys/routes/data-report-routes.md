# data_report_routes

**문서 위치**: `.clinerules/docs/msys/routes/data-report-routes.md`

## 파일
- `D:\dev\msys\routes\data_report_routes.py` (13줄)

## 역할
데이터 리포트 페이지

## Blueprint
```python
data_report_bp = Blueprint('data_report', __name__)
```

## 템플릿
- `data_report.html`

## 의존성
- Service: `service/dashboard_service.py`
- Mapper: `mapper/mst_mapper.py`, `mapper/user_mapper.py`

## 연관 문서
- [../services/dashboard-service.md](../services/dashboard-service.md)
- [../templates/data_report.md](../templates/data_report.md)
