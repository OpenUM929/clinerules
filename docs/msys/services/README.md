# Services (서비스)

**문서 위치**: `.clinerules/docs/msys/services/README.md`

## 파일 위치

`D:\dev\msys\service/`

## 역할

라우트와 DAO 사이에서 데이터 처리, 비즈니스 로직, 트랜잭션 관리

## 계층 구조

```
routes → service → dao → mapper → database
```

## 파일 목록

| 파일 | 설명 | 연관 DAO |
|------|------|----------|
| `analysis_service.py` | 데이터 분석 | analytics_dao.py |
| `api_key_mngr_service.py` | API 키 관리 | api_key_mngr_dao.py |
| `auth_service.py` | 인증 | user_dao.py |
| `card_summary_service.py` | 카드 요약 | - |
| `collection_schedule_service.py` | 수집 일정 | - |
| `dashboard_service.py` | 대시보드 | analytics_dao.py, con_hist_dao.py |
| `data_definition_service.py` | 데이터 정의 | - |
| `data_spec_service.py` | 데이터 사양 | data_spec_dao.py |
| `icon_service.py` | 아이콘 관리 | icon_dao.py |
| `jandi_service.py` | 잔디 모니터링 | con_hist_dao.py |
| `mail_scheduler_service.py` | 메일 스케줄링 | - |
| `mapping_service.py` | 매핑 관리 | mapping_dao.py |
| `mngr_sett_service.py` | 메뉴 설정 | mngr_sett_dao.py |
| `mst_service.py` | 마스터 데이터 | mst_mapper.py |
| `password_service.py` | 비밀번호 검증 | - |
| `popup_service.py` | 팝업 관리 | popup_dao.py |
| `spec_scraper_service.py` | URL 스펙 분석 | - |
| `status_code_service.py` | 상태 코드 | sts_cd_dao.py |
| `trbl_service.py` | 장애 | trbl_hist_dao.py |
| `url_analyzer_service.py` | URL 분석 | - |
| `user_service.py` | 사용자 관리 | user_dao.py |

## 문서 목록

| 문서 | 대상 파일 |
|------|----------|
| [analysis-service.md](analysis-service.md) | analysis_service.py |
| [api-key-mngr-service.md](api-key-mngr-service.md) | api_key_mngr_service.py |
| [auth-service.md](auth-service.md) | auth_service.py |
| [card-summary-service.md](card-summary-service.md) | card_summary_service.py |
| [collection-schedule-service.md](collection-schedule-service.md) | collection_schedule_service.py |
| [dashboard-service.md](dashboard-service.md) | dashboard_service.py |
| [data-definition-service.md](data-definition-service.md) | data_definition_service.py |
| [data-spec-service.md](data-spec-service.md) | data_spec_service.py |
| [icon-service.md](icon-service.md) | icon_service.py |
| [jandi-service.md](jandi-service.md) | jandi_service.py |
| [mail-scheduler-service.md](mail-scheduler-service.md) | mail_scheduler_service.py |
| [mapping-service.md](mapping-service.md) | mapping_service.py |
| [mngr-sett-service.md](mngr-sett-service.md) | mngr_sett_service.py |
| [mst-service.md](mst-service.md) | mst_service.py |
| [password-service.md](password-service.md) | password_service.py |
| [status-code-service.md](status-code-service.md) | status_code_service.py |
| [trbl-service.md](trbl-service.md) | trbl_service.py |
| [url-analyzer-service.md](url-analyzer-service.md) | url_analyzer_service.py |
| [user-service.md](user-service.md) | user_service.py |

## 관련 문서

- [../README.md](../README.md) - 프로젝트 개요
- [../routes/README.md](../routes/README.md) - 라우트 계층
- [../dao/README.md](../dao/README.md) - DAO 계층
