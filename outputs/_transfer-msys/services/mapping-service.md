# Mapping Service (mapping_service.py)

## 파일 위치

`service/mapping_service.py` (56줄)

## 역할

매핑 관리 - CRUD (Job ID, URL, 아이콘 등)

## 주요 함수

| 함수 | 기능 |
|------|------|
| `get_all_mappings()` | 전체 매핑 조회 |
| `add_mapping(mapping_data)` | 매핑 추가 |
| `update_mapping(mapping_data)` | 매핑 수정 |
| `delete_mapping(mapp_id)` | 매핑 삭제 |

## 의존성

- `mapper/mapping_mapper.py` - 매핑 매퍼

## 관련 문서

- [services/README.md](README.md) - services 개요
- [routes/mapping-routes.md](../routes/mapping-routes.md) - 매핑 라우트