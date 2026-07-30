# DAO (Data Access Object)

**문서 위치**: `.clinerules/docs/msys/dao/README.md`

## 파일 위치

`D:\dev\msys\dao/`

## 역할

SQL 실행, 트랜잭션 관리, 데이터 조회/수정

## 계층 구조

```
service → dao → mapper → database
```

## 파일 목록

| 파일 | 설명 | 연관 Mapper |
|------|------|------------|
| `analytics_dao.py` | 분석 데이터 | dashboard_mapper.py, analysis_mapper.py |
| `api_key_mngr_dao.py` | API 키 관리 | - |
| `con_hist_dao.py` | 수집 이력 | dashboard_mapper.py, jandi_mapper.py |
| `con_mst_dao.py` | 수집 마스터 | mst_mapper.py |
| `data_spec_dao.py` | 데이터 사양 | data_spec_mapper.py |
| `grp_memo_dao.py` | 그룹 메모 | - |
| `icon_dao.py` | 아이콘 | icon_mapper.py |
| `mapping_dao.py` | 매핑 | mapping_mapper.py |
| `mngr_sett_dao.py` | 메뉴 설정 | mngr_sett_mapper.py |
| `popup_dao.py` | 팝업 | - |
| `schedule_settings_dao.py` | 일정 설정 | - |
| `sql_loader.py` | SQL 로더 유틸리티 | - |
| `sts_cd_dao.py` | 상태 코드 | - |
| `trbl_hist_dao.py` | 장애 이력 | trbl_mapper.py |
| `user_dao.py` | 사용자 | user_mapper.py |

## 문서 목록

| 문서 | 대상 파일 |
|------|----------|
| [analytics-dao.md](analytics-dao.md) | analytics_dao.py |
| [con-hist-dao.md](con-hist-dao.md) | con_hist_dao.py |
| [con-mst-dao.md](con-mst-dao.md) | con_mst_dao.py |
| [data-spec-dao.md](data-spec-dao.md) | data_spec_dao.py |
| [grp-memo-dao.md](grp-memo-dao.md) | grp_memo_dao.py |
| [icon-dao.md](icon-dao.md) | icon_dao.py |
| [mapping-dao.md](mapping-dao.md) | mapping_dao.py |
| [mngr-sett-dao.md](mngr-sett-dao.md) | mngr_sett_dao.py |
| [schedule-settings-dao.md](schedule-settings-dao.md) | schedule_settings_dao.py |
| [sts-cd-dao.md](sts-cd-dao.md) | sts_cd_dao.py |
| [trbl-hist-dao.md](trbl-hist-dao.md) | trbl_hist_dao.py |
| [user-dao.md](user-dao.md) | user_dao.py |

## 관련 문서

- [../README.md](../README.md) - 프로젝트 개요
- [../services/README.md](../services/README.md) - 서비스 계층
- [../mapper/README.md](../mapper/README.md) - SQL 매핑
