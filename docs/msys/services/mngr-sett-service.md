# Mngr Sett Service (mngr_sett_service.py)

## 파일 위치

`service/mngr_sett_service.py` (663줄)

## 역할

관리자 설정 - Job별 설정, 사용자 권한 관리, 아이콘 매핑

## 주요 함수

| 함수 | 기능 |
|------|------|
| `get_all_settings()` | 전체 설정 조회 |
| `get_all_settings_paged(page, per_page, search_term)` | 페이징 + 검색 조회 |
| `get_settings_by_cd(cd)` | 단일 설정 조회 |
| `insert_or_update_settings(data)` | 설정 저장/수정 |
| `delete_settings(cd)` | 설정 삭제 |
| `get_all_users_with_permissions()` | 사용자별 권한 조회 |
| `update_user_permissions(user_id, permissions)` | 권한 업데이트 |
| `get_icon_menu_mapping()` | 아이콘-메뉴 매핑 |

## 기본 설정 (DEFAULT_ADMIN_SETTINGS)

| 설정 | 기본값 | 설명 |
|------|--------|------|
| CNN_FAILR_THRS_VAL | 5 | 연결 실패 임계값 |
| CNN_WARN_THRS_VAL | 3 | 연결 경고 임계값 |
| DLY_SUCS_RT_THRS_VAL | 95.0 | 일별 성공률 임계값 |
| DD7_SUCS_RT_THRS_VAL | 90.0 | 7일 성공률 임계값 |
| MTHL_SUCS_RT_THRS_VAL | 85.0 | 월간 성공률 임계값 |

## 의존성

- `mapper/mst_mapper.py` - 마스터 매퍼
- `mapper/mngr_sett_mapper.py` - 설정 매퍼
- `dao/schedule_settings_dao.py` - 일정 설정 DAO
- `mapper/user_mapper.py` - 사용자 매퍼

## 관련 문서

- [services/README.md](README.md) - services 개요
- [routes/mngr-sett-routes.md](../routes/mngr-sett-routes.md) - 관리자 설정 라우트