# UI Routes (UI 페이지 라우트)

**문서 위치**: `.clinerules/docs/msys/routes/ui-routes.md`

## 파일 위치

`routes/ui/` - 페이지 렌더링용 Flask 라우트

## 역할

HTML 템플릿을 렌더링하는 페이지 라우트 (템플릿 기반)

## 파일 목록

| 파일 | 역할 |
|------|------|
| dashboard_routes.py | 대시보드 페이지 (59줄) |
| card_summary_routes.py | 카드 요약 페이지 |
| api_key_mngr_routes.py | API 키 관리 페이지 |
| collection_schedule_routes.py | 수집 일정 페이지 |

## 각 파일별 엔드포인트

### dashboard_routes.py

| 엔드포인트 | 메서드 | 템플릿 | 기능 |
|------------|--------|--------|------|
| `/dashboard` | GET | dashboard.html | 대시보드 페이지 |

### card_summary_routes.py

| 엔드포인트 | 메서드 | 템플릿 | 기능 |
|------------|--------|--------|------|
| `/card/summary` | GET | card_summary.html | 카드 요약 페이지 |

### api_key_mngr_routes.py

| 엔드포인트 | 메서드 | 템플릿 | 기능 |
|------------|--------|--------|------|
| `/api-key` | GET | api_key_mngr.html | API 키 관리 페이지 |

### collection_schedule_routes.py

| 엔드포인트 | 메서드 | 템플릿 | 기능 |
|------------|--------|--------|------|
| `/schedule` | GET | collection_schedule.html | 수집 일정 페이지 |

## 관련 문서

- [routes/README.md](README.md) - routes 개요
- [templates/screen-domain.md](../templates/screen-domain.md) - 화면-템플릿 매핑
- [services/dashboard-service.md](../services/dashboard-service.md) - 대시보드 서비스