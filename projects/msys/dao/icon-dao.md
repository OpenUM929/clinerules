# Icon DAO (icon_dao.py)

## 파일 위치

`dao/icon_dao.py` (136줄)

## 역할

아이콘 데이터 접근 - TB_ICON 조회/수정

## 주요 함수

| 함수 | 기능 |
|------|------|
| `get_all_icons()` | 전체 아이콘 조회 |
| `get_icon_by_id(icon_id)` | 아이콘 조회 |
| `insert_icon(data)` | 아이콘 추가 |
| `update_icon(data)` | 아이콘 수정 |
| `delete_icon(icon_id)` | 아이콘 삭제 |

## SQL 의존성

- `icon/get_all_icons.sql`

## 관련 문서

- [dao/README.md](README.md) - DAO 개요
- [services/icon-service.md](../services/icon-service.md) - 아이콘 서비스