# 파일 구조

> 프로젝트의 파일 및 디렉토리 구조

---

## 디렉토리 구조

```
msys/
├── msys_app.py              # Flask 메인 앱 (진입점, Blueprint 등록)
├── routes/                 # 라우트 (Blueprint)
│   ├── *.py                #   최상위 UI 라우트 (auth, admin, analysis, ...)
│   ├── api/                #   JSON API 라우트 (url_prefix=/api/...)
│   └── ui/                 #   UI 전용 라우트 (dashboard, collection_schedule, api_key_mngr)
├── service/                # 비즈니스 로직 (도메인별 22개)
├── dao/                    # Data Access Object (도메인별 15개 + sql_loader)
├── mapper/                 # SQL 쿼리 정의/실행 (도메인별 11개)
├── models/                 # ORM 모델 (user.py)
├── utils/                 # 공통 유틸 (인증/시간/로깅/SQL로더/작업/모니터)
├── templates/             # HTML 템플릿 (Jinja2)
├── static/js/modules/     # JavaScript (jQuery, 도메인별 모듈)
├── my_setting/            # 환경별 설정
├── scripts/               # 운영/배치 스크립트
├── DDL/                   # 데이터베이스 DDL
└── sql/                   # SQL 쿼리 파일 (sql_loader로 로드)
```

---

## routes/

### 최상위 UI 라우트
| 파일 | 설명 |
|------|------|
| `auth_routes.py` | 인증 + 권한 데코레이터 (`login_required` 등) |
| `admin_routes.py` | 관리자 |
| `dashboard_routes.py` | 대시보드 |
| `jandi_routes.py` | Jandi 히트맵 |
| `collection_schedule_routes.py` | 수집 일정 |
| `mapping_routes.py` | 컬럼 매핑 |
| `mngr_sett_routes.py` | 관리자 설정 |
| `data_spec_routes.py` | 데이터 스펙 |
| `data_report_routes.py` | 데이터 리포트 |
| `card_summary_routes.py` | 카드 요약 |
| `analysis_routes.py` | 분석 |
| `today_routes.py` | 오늘 날짜 |

### `routes/api/` (JSON API, `url_prefix=/api/...`)
| 파일 | Blueprint |
|------|-----------|
| `auth_api.py` | `auth_api` (`/api/auth`) |
| `dashboard_api.py` | `dashboard_api` (`/api/dashboard`) |
| `data_definition_api.py` | `data_definition_api` (`/api/data_definition`) |
| `card_summary_api.py` | `card_summary_api` (`/api/card_summary`) |
| `api_key_mngr_routes.py` | `api_key_mngr_api` (`/api`) |
| `analysis_api.py` | `analysis_api` (`/api/analytics`) |
| `popup_routes.py` | `popup_api` (`/api/popups`) |

### `routes/ui/` (UI 전용 라우트)
| 파일 | 설명 |
|------|------|
| `dashboard_routes.py` | 대시보드 UI |
| `collection_schedule_routes.py` | 수집 일정 UI |
| `api_key_mngr_routes.py` | API 키 관리 UI |

---

## 공통 유틸리티 (utils/)

| 파일 | 역할 |
|------|------|
| `datetime_utils.py` | KST 시간 변환 |
| `kst_utils.py` | KST 포맷팅 |
| `sql_loader.py` | SQL 파일 로드 |
| `auth_middleware.py` | 인증/권한 미들웨어 |
| `logging_config.py` | 로깅 설정 |
| `job_utils.py` | Job 유틸리티 |
| `cpu_monitor.py` | CPU 모니터링 |

---

## 공통 JavaScript (static/js/modules/common/)

| 파일 | 역할 |
|------|------|
| `dateUtils.js` | 날짜 처리 |
| `api/auth.js` | 인증 API |
| `api/dashboard.js` | 대시보드 API |
| `api/sts_cd.js` | 상태코드 API |
| `apiConfig.js` | API 설정 |
| `utils.js` | 범용 유틸리티 |
| `ui.js` | UI 조작 |
| `dataManager.js` | 데이터 관리 |

---

## 권한 데코레이터 (routes/auth_routes.py)

| 데코레이터 | 설명 |
|-----------|------|
| `login_required` | 로그인 필수 |
| `admin_required` | 관리자 권한 필요 |
| `analysis_required` | 분석 권한 필요 |
| `data_analysis_required` | 데이터 분석 권한 필요 |
| `collection_schedule_required` | 수집 일정 권한 필요 |
| `card_summary_required` | 카드 요약 권한 필요 |

---

## 관련 문서

- [overview.md](overview.md) - 프로젝트 개요
- [screens.md](screens.md) - 화면/페이지
- [api-endpoints.md](api-endpoints.md) - API 엔드포인트