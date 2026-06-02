# Data Spec Service (data_spec_service.py)

## 파일 위치

`service/data_spec_service.py` (99줄)

## 역할

데이터 사양 관리 - CRUD, URL 분석, 스펙 스크래핑

## 주요 함수

| 함수 | 기능 |
|------|------|
| `get_all_specs()` | 전체 사양 조회 |
| `get_spec_by_id(spec_id)` | 단일 사양 조회 |
| `create_spec(spec_data, params_data)` | 사양 생성 |
| `update_spec(spec_data, params_data)` | 사양 수정 |
| `delete_spec(spec_id)` | 사양 삭제 |
| `check_name_exists(data_name)` | 이름 중복 확인 |
| `analyze_url(url)` | URL 분석 |
| `scrape_spec(url)` | 스펙 스크래핑 |

## 의존성

- `mapper/data_spec_mapper.py` - 데이터 사양 매퍼
- `service/spec_scraper_service.py` - 스펙 스크래퍼
- `service/url_analyzer_service.py` - URL 분석기
- `service/password_service.py` - 비밀번호 서비스

## 관련 문서

- [services/README.md](README.md) - services 개요
- [routes/data-spec-routes.md](../routes/data-spec-routes.md) - 데이터 사양 라우트