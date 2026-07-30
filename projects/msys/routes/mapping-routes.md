# mapping_routes

**문서 ?�치**: `.clinerules/projects/msys/routes/mapping-routes.md`

## ?�일
- `D:\dev\msys\routes\mapping_routes.py` (108�?

## ??��
컬럼 매핑 관�?- ?�거?????�규 컬럼�?매핑 CRUD

## Blueprint
```python
mapping_bp = Blueprint('mapping', __name__, url_prefix='/mapping')
```

## ?�드?�인??
| 경로 | 메서??| ?�수 | ?�명 |
|------|--------|------|------|
| `/mapping/` | GET | `index()` | 매핑 관�??�이지 |
| `/mapping/api/all` | GET | `get_all_mappings()` | 모든 매핑 조회 |
| `/mapping/api/unmapped` | GET | `get_unmapped_columns()` | 매핑?��? ?��? 컬럼 |
| `/mapping/api/add` | POST | `add_mapping()` | 매핑 추�? |
| `/mapping/api/update` | POST | `update_mapping()` | 매핑 ?�정 |
| `/mapping/api/delete/<id>` | DELETE | `delete_mapping()` | 매핑 ??�� |

## ?�코?�이??- `@login_required`: 로그???�요
- `@log_menu_access`: 메뉴 ?�근 로그 기록

## ?�존??- Service: `service/mapping_service.py`
- DAO: `dao/analytics_dao.py`

## ?��? 문서
- [../services/mapping-service.md](../services/mapping-service.md)
- [../dao/mapping-dao.md](../dao/mapping-dao.md)
- [../templates/mapping.md](../templates/mapping.md)
