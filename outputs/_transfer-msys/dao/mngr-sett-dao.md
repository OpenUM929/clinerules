# Mngr Sett DAO (mngr_sett_dao.py)

## 파일 위치

`dao/mngr_sett_dao.py` (195줄)

## 역할

관리자 설정 데이터 접근 - TB_MNGR_SETT 조회/저장

## 주요 함수

| 함수 | 기능 |
|------|------|
| `get_settings_by_cd(cd)` | 단일 설정 조회 |
| `get_all_menu_settings()` | 전체 메뉴 설정 조회 |
| `insert_or_update(settings_data)` | 설정 저장/수정 |
| `delete_settings(cd)` | 설정 삭제 |
| `get_menu_by_url(url)` | URL로 메뉴 조회 |

## SQL 의존성

- `mngr_sett/get_mngr_sett.sql`

## 관련 문서

- [dao/README.md](README.md) - DAO 개요
- [services/mngr-sett-service.md](../services/mngr-sett-service.md) - 관리자 설정 서비스