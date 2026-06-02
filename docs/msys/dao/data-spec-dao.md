# Data Spec DAO (data_spec_dao.py)

## 파일 위치

`dao/data_spec_dao.py` (153줄)

## 역할

데이터 사양 접근 - TB_DATA_SPEC, TB_DATA_SPEC_PARM 조회/수정

## 주요 함수

| 함수 | 기능 |
|------|------|
| `get_all_specs()` | 전체 사양 조회 |
| `get_spec_by_id(spec_id)` | 단일 사양 조회 |
| `insert_spec(data)` | 사양 추가 |
| `update_spec(data)` | 사양 수정 |
| `delete_spec(spec_id)` | 사양 삭제 |
| `insert_params(params)` | 파라미터 추가 |
| `delete_params(spec_id)` | 파라미터 삭제 |

## SQL 의존성

- `data_spec/select_all_specs.sql`

## 관련 문서

- [dao/README.md](README.md) - DAO 개요
- [services/data-spec-service.md](../services/data-spec-service.md) - 데이터 사양 서비스