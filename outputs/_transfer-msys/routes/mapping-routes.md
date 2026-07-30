# mapping_routes

**문서 위치**: `.clinerules/docs/msys/routes/mapping-routes.md`

## 파일
- `D:\dev\msys\routes\mapping_routes.py` (108줄)

## 역할
컬럼 매핑 관리 - 레거시 ↔ 신규 컬럼명 매핑 CRUD

## Blueprint
```python
mapping_bp = Blueprint('mapping', __name__, url_prefix='/mapping')
```

## 엔드포인트

| 경로 | 메서드 | 함수 | 설명 |
|------|--------|------|------|
| `/mapping/` | GET | `index()` | 매핑 관리 페이지 |
| `/mapping/api/all` | GET | `get_all_mappings()` | 모든 매핑 조회 |
| `/mapping/api/unmapped` | GET | `get_unmapped_columns()` | 매핑되지 않은 컬럼 |
| `/mapping/api/add` | POST | `add_mapping()` | 매핑 추가 |
| `/mapping/api/update` | POST | `update_mapping()` | 매핑 수정 |
| `/mapping/api/delete/<id>` | DELETE | `delete_mapping()` | 매핑 삭제 |

## 데코레이터
- `@login_required`: 로그인 필요
- `@log_menu_access`: 메뉴 접근 로그 기록

## 의존성
- Service: `service/mapping_service.py`
- DAO: `dao/analytics_dao.py`

## 연관 문서
- [../services/mapping-service.md](../services/mapping-service.md)
- [../dao/mapping-dao.md](../dao/mapping-dao.md)
- [../templates/mapping.md](../templates/mapping.md)
