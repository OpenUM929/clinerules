# Mapping Mapper (mapping_mapper.py)

## 파일 위치

`mapper/mapping_mapper.py` (41줄)

## 역할

매핑 SQL - TB_COL_MAPP 조회/수정

## 주요 함수

| 함수 | 기능 |
|------|------|
| `get_all_mappings()` | 전체 매핑 조회 |
| `add_mapping(mapping_data)` | 매핑 추가 |
| `update_mapping(mapping_data)` | 매핑 수정 |
| `delete_mapping(mapp_id)` | 매핑 삭제 |

## SQL 의존성

- `sql.mapping.mapping_sql.py` - MappingSQL 클래스

## 관련 문서

- [mapper/README.md](README.md) - mapper 개요
- [services/mapping-service.md](../services/mapping-service.md) - 매핑 서비스