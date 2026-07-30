# Icon Mapper (icon_mapper.py)

## 파일 위치

`mapper/icon_mapper.py` (38줄)

## 역할

아이콘 SQL 매핑 - TB_ICON 조회/수정 (DAO 래퍼)

## 주요 함수

| 함수 | 기능 |
|------|------|
| `get_all_icons()` | 전체 아이콘 |
| `get_icon_by_code(icon_code)` | 코드로 조회 |
| `insert_icon(icon_data)` | 추가 |
| `update_icon(icon_data)` | 수정 |
| `insert_or_update_icon(icon_data)` | 추가 또는 수정 |
| `delete_icon(icon_id)` | 삭제 |

## 관련 문서

- [mapper/README.md](README.md) - mapper 개요
- [dao/icon-dao.md](../dao/icon-dao.md) - 아이콘 DAO