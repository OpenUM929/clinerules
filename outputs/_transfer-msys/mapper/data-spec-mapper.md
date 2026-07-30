# Data Spec Mapper (data_spec_mapper.py)

## 파일 위치

`mapper/data_spec_mapper.py` (52줄)

## 역할

데이터 사양 SQL 매핑 - TB_DATA_SPEC, TB_DATA_SPEC_PARM (DAO 래퍼)

## 주요 함수

| 함수 | 기능 |
|------|------|
| `get_all_specs()` | 전체 사양 조회 |
| `get_spec_by_id(spec_id)` | 단일 사양 조회 |
| `create_spec(spec_data, params_data)` | 사양 생성 |
| `update_spec(spec_data, params_data)` | 사양 수정 |
| `delete_spec(spec_id)` | 사양 삭제 |

## 관련 문서

- [mapper/README.md](README.md) - mapper 개요
- [dao/data-spec-dao.md](../dao/data-spec-dao.md) - 데이터 사양 DAO