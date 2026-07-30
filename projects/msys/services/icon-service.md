# Icon Service (icon_service.py)

## 파일 위치

`service/icon_service.py` (146줄)

## 역할

아이콘 관리 - 아이콘 코드 매핑, CSV 내보내기/가져오기

## 주요 함수

| 함수 | 기능 |
|------|------|
| `get_icon_mappings()` | emoji ↔ int 매핑 반환 |
| `get_all_icons_data()` | 전체 아이콘 데이터 |
| `export_icons_csv()` | 아이콘 CSV 내보내기 |
| `import_icons_csv(file)` | 아이콘 CSV 가져오기 |

## 의존성

- `mapper/icon_mapper.py` - 아이콘 매퍼

## 관련 문서

- [services/README.md](README.md) - services 개요
- [routes/mngr-sett-routes.md](../routes/mngr-sett-routes.md) - 관리자 설정 라우트