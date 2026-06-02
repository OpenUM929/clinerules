# Screen Domain Map

**문서 위치**: `.clinerules/docs/msys/templates/screen-domain.md`

## 개요

화면(URL)과 템플릿 파일 매핑. UI 변경 시 참조.

## 화면-템플릿 매핑

| 화면명 | 템플릿 | URL | Route | 도메인 |
|--------|--------|-----|-------|--------|
| base | base.html | - | - | 기본 레이아웃 (navbar, CSS/JS) |
| login | login.html | /login | auth_routes.py | 인증 (로그인/회원가입/비밀번호초기화) |
| dashboard | dashboard.html | /, /dashboard | dashboard_routes.py | 실시간 수집 현황 |
| api_key_mngr | api_key_mngr.html | /api_key_mngr | api_key_mngr_routes.py | API 키 만료 관리 |
| mngr_sett | mngr_sett.html | /admin/mngr_sett | admin_routes.py | 메뉴/설정 관리 |
| jandi | jandi.html | /jandi | jandi_routes.py | 지연 데이터 현황 |
| card_summary | card_summary.html | /card/summary | card_summary_routes.py | 카드 요약 |
| mapping | mapping_management.html | /mapping | mapping_routes.py | 컬럼 매핑 관리 |
| data_spec | data_spec.html | /data/spec | data_spec_routes.py | 데이터 사양 |
| data_report | data_report.html | /data/report | data_report_routes.py | 데이터 리포트 |
| data_analysis | data_analysis.html | /data_analysis | analysis_routes.py | 데이터 분석 |
| chart_analysis | chart_analysis.html | /chart_analysis | analysis_routes.py | 차트 분석 |
| collection_schedule | collection_schedule.html | /collection_schedule | collection_schedule_routes.py | 수집 일정 |
| change_password | change_password.html | /change-password | auth_routes.py | 비밀번호 변경 |
| navbar | navbar.html | - | - | 네비게이션 바 |
| collapsible_controls | collapsible_controls.html | - | - | 접이식 컨트롤 (dashboard 포함) |
| unauthorized | unauthorized.html | - | - | 권한 없음 |
| empty_base | empty_base.html | - | - | 빈 기본 레이아웃 |
| api_test | api_test.html | - | - | API 테스트 |
| raw_data | raw_data.html | - | - | 원시 데이터 |
| test_css | test_css.html | - | - | CSS 테스트 |
| mngr_sett_test | mngr_sett_test.html | /mngr_sett_test | mngr_sett_routes.py | 메뉴 설정 테스트 |

## 계층 구조

```
base.html (최상위 레이아웃)
├── navbar.html (네비게이션)
├── collapsible_controls.html (접이식 컨트롤)
└── {화면명}.html (base.html 확장)
    ├── dashboard.html
    ├── api_key_mngr.html
    ├── mngr_sett.html
    └── ...
```

## 개별 문서

| 화면명 | 문서 |
|--------|------|
| base | - |
| login | [login.md](login.md) |
| dashboard | [dashboard.md](dashboard.md) |
| api_key_mngr | [api_key_mngr.md](api_key_mngr.md) |
| mngr_sett | [mngr_sett.md](mngr_sett.md) |
| jandi | [jandi.md](jandi.md) |
| card_summary | [card_summary.md](card_summary.md) |
| mapping | [mapping.md](mapping.md) |
| data_spec | [data_spec.md](data_spec.md) |
| data_report | [data_report.md](data_report.md) |
| data_analysis | [data_analysis.md](data_analysis.md) |
| chart_analysis | [chart_analysis.md](chart_analysis.md) |
| collection_schedule | [collection_schedule.md](collection_schedule.md) |
| change_password | [change_password.md](change_password.md) |
