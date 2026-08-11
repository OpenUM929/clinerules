# data_spec_routes

**문서 위치**: `.clinerules/docs/msys/routes/data-spec-routes.md`

## 파일
- `D:\dev\msys\routes\data_spec_routes.py` (159줄)

## 역할
데이터 명세서 관리 - CRUD, URL 스크래핑

## Blueprint
```python
bp = Blueprint('data_spec', __name__, url_prefix='/')
```

## 엔드포인트

| 경로 | 메서드 | 함수 | 설명 |
|------|--------|------|------|
| `/data_spec` | GET | `data_spec_page()` | 명세서 페이지 |
| `/api/data-spec` | GET, POST | `handle_data_specs()` | 목록 조회/생성 |
| `/api/scrape-spec` | POST | `scrape_spec_from_url()` | URL 스크래핑 |
| `/api/data-spec/check-name` | GET | `check_data_spec_name()` | 이름 중복 확인 |
| `/api/data-spec/<id>` | GET, PUT, DELETE | `handle_data_spec_by_id()` | 상세/수정/삭제 |

## 데코레이터
- `@log_menu_access`: 메뉴 접근 로그 기록

## 의존성
- Service: `service/data_spec_service.py`
- DAO: `dao/analytics_dao.py`

## 연관 문서
- [../services/data-spec-service.md](../services/data-spec-service.md)
- [../templates/data_spec.md](../templates/data_spec.md)
