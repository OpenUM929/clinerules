# Mapper (SQL 매핑)

**문서 위치**: `.clinerules/docs/msys/mapper/README.md`

## 파일 위치

`D:\dev\msys\mapper/`

## 역할

DAO에서 호출되는 SQL 쿼리 정의 및 실행

## 계층 구조

```
service → dao → mapper → database
```

## 파일 목록

| 파일 | 설명 | 연관 테이블 |
|------|------|-----------|
| `analysis_mapper.py` | 분석 SQL | tb_con_hist |
| `dashboard_mapper.py` | 대시보드 SQL | tb_con_hist, tb_con_mst |
| `data_spec_mapper.py` | 데이터 사양 SQL | tb_data_spec_parm |
| `grp_memo_mapper.py` | 그룹 메모 SQL | - |
| `icon_mapper.py` | 아이콘 SQL | tb_icon |
| `jandi_mapper.py` | 잔디 SQL | tb_con_hist |
| `mapping_mapper.py` | 매핑 SQL | tb_mapping |
| `mngr_sett_mapper.py` | 메뉴 설정 SQL | tb_mngr_sett |
| `mst_mapper.py` | 마스터 SQL | tb_con_mst |
| `trbl_mapper.py` | 장애 SQL | tb_trbl_hist |
| `user_mapper.py` | 사용자 SQL | tb_user |

## 문서 목록

| 문서 | 대상 파일 |
|------|----------|
| [analysis-mapper.md](analysis-mapper.md) | analysis_mapper.py |
| [dashboard-mapper.md](dashboard-mapper.md) | dashboard_mapper.py |
| [data-spec-mapper.md](data-spec-mapper.md) | data_spec_mapper.py |
| [icon-mapper.md](icon-mapper.md) | icon_mapper.py |
| [jandi-mapper.md](jandi-mapper.md) | jandi_mapper.py |
| [mapping-mapper.md](mapping-mapper.md) | mapping_mapper.py |
| [mst-mapper.md](mst-mapper.md) | mst_mapper.py |
| [trbl-mapper.md](trbl-mapper.md) | trbl_mapper.py |
| [user-mapper.md](user-mapper.md) | user_mapper.py |

## 관련 문서

- [../README.md](../README.md) - 프로젝트 개요
- [../dao/README.md](../dao/README.md) - DAO 계층
- [../services/README.md](../services/README.md) - 서비스 계층
