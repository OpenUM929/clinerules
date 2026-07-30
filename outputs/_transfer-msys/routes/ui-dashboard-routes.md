# ui/dashboard_routes

**문서 위치**: `.clinerules/docs/msys/routes/ui-dashboard-routes.md`

## 파일
- `D:\dev\msys\routes\ui\dashboard_routes.py` (59줄)

## 역할
대시보드 페이지 렌더링

## Blueprint
```python
dashboard_bp = Blueprint('dashboard', __name__)
```

## 엔드포인트

| 경로 | 메서드 | 함수 | 설명 |
|------|--------|------|------|
| `/dashboard` | GET | `dashboard()` | 대시보드 페이지 |

## 데코레이터
- `@login_required`: 로그인 필요
- `@check_password_change_required`: 비밀번호 변경 필요 시 체크
- `@log_menu_access`: 메뉴 접근 로그 기록

## 권한
- `dashboard` 권한 필요

## 템플릿
- `dashboard.html`

## 연관 문서
- [../services/dashboard-service.md](../services/dashboard-service.md)
- [../dao/analytics-dao.md](../dao/analytics-dao.md)
- [../templates/dashboard.md](../templates/dashboard.md)
