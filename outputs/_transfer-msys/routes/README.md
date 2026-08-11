# Routes (라우트)

**문서 위치**: `.clinerules/docs/msys/routes/README.md`

## 파일 위치

`D:\dev\msys\routes/`

## 역할

HTTP 요청을 받아 service를 호출하고, JSON 또는 HTML 응답을 반환합니다.

## 계층 구조

```
request → routes → service → dao → mapper → database
```

## 파일 목록

### 최상위 Routes
| 파일 | 설명 | 템플릿 |
|------|------|--------|
| `auth_routes.py` | 인증 (로그인/로그아웃) | login.html |
| `admin_routes.py` | 관리자 페이지 | mngr_sett.html |
| `analysis_routes.py` | 분석/차트 | data_analysis.html, chart_analysis.html |
| `card_summary_routes.py` | 카드 요약 | card_summary.html |
| `collection_schedule_routes.py` | 수집 일정 | collection_schedule.html |
| `data_report_routes.py` | 데이터 리포트 | data_report.html |
| `data_spec_routes.py` | 데이터 사양 | data_spec.html |
| `jandi_routes.py` | 잔디 모니터링 | jandi.html |
| `mapping_routes.py` | 매핑 관리 | mapping_management.html |
| `mngr_sett_routes.py` | 메뉴 설정 테스트 | mngr_sett_test.html |
| `today_routes.py` | 오늘의 일정 | - |

### UI Routes
| 파일 | 설명 |
|------|------|
| `ui/dashboard_routes.py` | 대시보드 |
| `ui/card_summary_routes.py` | 카드 요약 |
| `ui/api_key_mngr_routes.py` | API 키 관리 |
| `ui/collection_schedule_routes.py` | 수집 일정 |

### API Routes
| 파일 | 설명 |
|------|------|
| `api/auth_api.py` | 인증 API |
| `api/dashboard_api.py` | 대시보드 API |
| `api/data_definition_api.py` | 데이터 정의 API |
| `api/data_definition_api.py` | 데이터 정의 API |
| `api/card_summary_api.py` | 카드 요약 API |
| `api/api_key_mngr_api.py` | API 키 관리 API |
| `api/analysis_api.py` | 분석 API |

## 문서 목록

| 문서 | 대상 파일 |
|------|----------|
| [auth-routes.md](auth-routes.md) | auth_routes.py |
| [admin-routes.md](admin-routes.md) | admin_routes.py |
| [analysis-routes.md](analysis-routes.md) | analysis_routes.py |
| [api-analysis.md](api-analysis.md) | api/analysis_api.py |
| [api-api-key-mngr.md](api-api-key-mngr.md) | api/api_key_mngr_api.py |
| [api-card-summary.md](api-card-summary.md) | api/card_summary_api.py |
| [api-dashboard.md](api-dashboard.md) | api/dashboard_api.py |
| [api-data-definition.md](api-data-definition.md) | api/data_definition_api.py |
| [api-routes.md](api-routes.md) | api/* 공통 |
| [card-summary-routes.md](card-summary-routes.md) | card_summary_routes.py, ui/card_summary_routes.py |
| [collection-schedule-routes.md](collection-schedule-routes.md) | collection_schedule_routes.py |
| [data-report-routes.md](data-report-routes.md) | data_report_routes.py |
| [data-spec-routes.md](data-spec-routes.md) | data_spec_routes.py |
| [jandi-routes.md](jandi-routes.md) | jandi_routes.py |
| [mapping-routes.md](mapping-routes.md) | mapping_routes.py |
| [mngr-sett-routes.md](mngr-sett-routes.md) | mngr_sett_routes.py |
| [today-routes.md](today-routes.md) | today_routes.py |
| [ui-dashboard-routes.md](ui-dashboard-routes.md) | ui/dashboard_routes.py |
| [ui-routes.md](ui-routes.md) | ui/* 공통 |

## 관련 문서

- [../README.md](../README.md) - 프로젝트 개요
- [../services/README.md](../services/README.md) - 서비스 계층
- [../templates/screen-domain.md](../templates/screen-domain.md) - 화면 매핑
