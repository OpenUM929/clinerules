# Mngr Sett Routes (mngr_sett_routes.py)

## 파일 위치

`routes/mngr_sett_routes.py` (859줄)

## 역할

관리자 설정 - 메뉴 설정, 사용자 권한 관리, 데이터 내보내기

## 주요 엔드포인트

### 페이지 렌더링

| 엔드포인트 | 메서드 | 템플릿 | 기능 |
|------------|--------|--------|------|
| `/mngr_sett` | GET | mngr_sett.html | 관리자 설정 페이지 |
| `/mngr_sett_test` | GET | mngr_sett_test.html | 관리자 설정 테스트 페이지 |

### REST API

| 엔드포인트 | 메서드 | 기능 |
|------------|--------|------|
| `/api/mngr_sett/settings/all` | GET | 전체 설정 조회 (페이징 지원) |
| `/api/mngr_sett/settings/save` | POST | 설정 저장 (Job ID별 + 권한) |
| `/api/mngr_sett/settings/<cd>` | GET | 단일 설정 조회 |
| `/api/mngr_sett/settings/<cd>` | PUT | 설정 수정 |
| `/api/mngr_sett/settings/<cd>` | DELETE | 설정 삭제 |
| `/api/mngr_sett/users` | GET | 사용자 목록 조회 |
| `/api/mngr_sett/users/permissions` | POST | 사용자 권한 저장 |
| `/api/mngr_sett/export` | GET | 설정 내보내기 (CSV) |
| `/api/mngr_sett/import` | POST | 설정 가져오기 (CSV) |

## 권한

- `login_required` - 로그인 필수
- `admin_required` - mngr_sett 권한
- `mngr_sett_required` - 관리자 설정 권한

## 의존성

- `service/mngr_sett_service.py` - 메뉴 설정 서비스
- `service/icon_service.py` - 아이콘 서비스
- `service/user_service.py` - 사용자 서비스
- `dao/sts_cd_dao.py` - 상태 코드 DAO

## 관련 문서

- [routes/README.md](README.md) - routes 개요
- [services/mngr-sett-service.md](../services/mngr-sett-service.md) - 메뉴 설정 서비스
- [templates/screen-domain.md](../templates/screen-domain.md) - 화면-템플릿 매핑