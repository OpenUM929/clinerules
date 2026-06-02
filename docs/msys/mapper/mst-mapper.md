# Mst Mapper (mst_mapper.py)

## 파일 위치

`mapper/mst_mapper.py` (155줄)

## 역할

마스터 데이터 SQL - TB_CON_MST 조회

## 주요 함수

| 함수 | 기능 |
|------|------|
| `get_all_mst()` | 전체 마스터 조회 |
| `get_all_mst_for_schedule(job_ids)` | 일정용 전체 조회 |
| `get_mst_data_by_cd(cd)` | cd로 조회 |
| `update_mst(data)` | 마스터 수정 |
| `insert_mst(data)` | 마스터 추가 |

## SQL 의존성

- `sql/mst/mst_sql.py` - MstSQL 클래스

## 관련 문서

- [mapper/README.md](README.md) - mapper 개요
- [services/mst-service.md](../services/mst-service.md) - 마스터 서비스