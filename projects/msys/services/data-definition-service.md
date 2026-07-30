# Data Definition Service (data_definition_service.py)

## 파일 위치

`service/data_definition_service.py` (300줄)

## 역할

데이터 정의 관리 - CRUD, 내보내기/가져오기

## 주요 함수

| 함수 | 기능 |
|------|------|
| `get_data_list()` | 데이터 목록 조회 |
| `get_data_groups()` | 데이터 그룹 조회 |
| `save_data(data)` | 데이터 저장 |
| `update_data(data)` | 데이터 수정 |
| `delete_data(cd)` | 데이터 삭제 |
| `export_data()` | 데이터 내보내기 (CSV) |
| `import_data(file)` | 데이터 가져오기 |

## 의존성

- `dao/con_mst_dao.py` - 연결 마스터 DAO
- `dao/mngr_sett_dao.py` - 메뉴 설정 DAO

## 관련 문서

- [services/README.md](README.md) - services 개요
- [routes/api-data-definition.md](../routes/api-data-definition.md) - 데이터 정의 API