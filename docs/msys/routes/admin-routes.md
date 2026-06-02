# admin_routes

**문서 위치**: `.clinerules/docs/msys/routes/admin-routes.md`

## 파일
- `D:\dev\msys\routes\admin_routes.py` (603줄)

## 역할
관리자 설정 - 메뉴 설정, 통계, 엑셀 템플릿 관리

## Blueprint
```python
admin_bp = Blueprint('admin', __name__)
```

## 엔드포인트

### 페이지
| 경로 | 메서드 | 함수 | 설명 |
|------|--------|------|------|
| `/admin/mngr_sett` | GET | `mngr_sett_page()` | 관리자 설정 페이지 |

### API
| 경로 | 메서드 | 함수 | 설명 |
|------|--------|------|------|
| `/api/statistics/config` | GET | `get_statistics_config()` | 통계 설정 (연도, 메뉴 목록) |
| `/api/statistics/recent_date` | GET | `get_recent_data_date()` | 최근 데이터 날짜 |
| `/api/statistics` | GET | `get_statistics()` | 통계 데이터 (일별/주별/월별/비교) |
| `/api/statistics/monthly_excel_download` | GET | `download_monthly_statistics_excel()` | 월별 통계 엑셀 다운로드 |
| `/api/excel_template/upload` | POST | `upload_excel_template()` | 엑셀 템플릿 업로드 |
| `/api/excel_template/info` | GET | `get_excel_template_info()` | 엑셀 템플릿 정보 |
| `/api/excel_template/download` | GET | `download_excel_template()` | 엑셀 템플릿 다운로드 |
| `/api/excel_template/delete` | DELETE | `delete_excel_template()` | 엑셀 템플릿 삭제 |

## 데코레이터
- `@login_required`: 로그인 필요
- `@log_menu_access`: 메뉴 접근 로그 기록

## 권한
- `mngr_sett` 권한 필요

## 의존성
- DAO: `dao/analytics_dao.py`, `dao/mngr_sett_dao.py`
- Service: `service/dashboard_service.py`

## 연관 문서
- [../services/dashboard-service.md](../services/dashboard-service.md)
- [../services/mngr-sett-service.md](../services/mngr-sett-service.md)
- [../dao/analytics-dao.md](../dao/analytics-dao.md)
- [../dao/mngr-sett-dao.md](../dao/mngr-sett-dao.md)
- [../templates/mngr_sett.md](../templates/mngr_sett.md)
