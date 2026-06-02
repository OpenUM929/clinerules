# Mapping DAO (mapping_dao.py)

## 파일 위치

`dao/mapping_dao.py` (35줄)

## 역할

매핑 데이터 접근 - TB_MAPPING 조회/수정

## 주요 함수

| 함수 | 기능 |
|------|------|
| `get_all_mappings()` | 전체 매핑 조회 |
| `add_mapping(mapping_data)` | 매핑 추가 |
| `update_mapping(mapping_data)` | 매핑 수정 |
| `delete_mapping(mapp_id)` | 매핑 삭제 |
| `get_all_schema_columns()` | 스키마 컬럼 조회 |

## SQL 의존성

- `mapping/get_all_mappings.sql`
- `mapping/add_mapping.sql`

## 관련 문서

- [dao/README.md](README.md) - DAO 개요
- [services/mapping-service.md](../services/mapping-service.md) - 매핑 서비스