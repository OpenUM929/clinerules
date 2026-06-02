# Mst Service (mst_service.py)

## 파일 위치

`service/mst_service.py` (51줄)

## 역할

마스터 데이터 (TB_CON_MST) - Job ID별 정보 조회

## 주요 함수

| 함수 | 기능 |
|------|------|
| `fetch_mst_list()` | 전체 마스터 목록 조회 |
| `get_cd_nm_item2(cd)` | cd로 cd_nm, item2 조회 |
| `get_job_mst_info(job_ids)` | Job ID 목록의 상세정보 조회 |
| `get_paged_jobs(start, length, search_value, start_date, end_date, all_data, user)` | 페이징 + 검색 조회 |

## 의존성

- `mapper/mst_mapper.py` - 마스터 매퍼

## 관련 문서

- [services/README.md](README.md) - services 개요
- [routes/jandi-routes.md](../routes/jandi-routes.md) - 지정 데이터 라우트