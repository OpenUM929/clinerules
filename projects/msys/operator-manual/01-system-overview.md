# MSYS 시스템 개요

## 시스템 정의

MSYS(Monitoring System)는 **외부 데이터 수집 현황을 모니터링하고 관리하는 웹 기반 대시보드 시스템**입니다.

## 주요 기능

| 기능 | 설명 |
|------|------|
| 수집 현황 모니터링 | 실시간 수집 작업 상태 확인 |
| 스케줄 관리 | 수집 작업 스케줄 조회 및 관리 |
| API 키 관리 | API 키 등록, 만료 알림, 메일 발송 |
| 데이터 분석 | 차트/리포트 기반 데이터 분석 |
| 사용자 관리 | 계정 승인, 권한 설정, 데이터 접근 제어 |
| 시스템 설정 | 상태 코드, 아이콘, 스케줄 표시 설정 |

## 시스템 아키텍처

```
[사용자] → [Flask Web Server] → [PostgreSQL]
                ↓
            [Redis Cache]
                ↓
            [SMTP Mail]
```

| 구성 요소 | 기술 |
|-----------|------|
| Backend | Python 3 + Flask 3.1.1 |
| Frontend | HTML/Jinja2 + jQuery + JavaScript |
| Database | PostgreSQL |
| Cache | Redis |
| Mail | SMTP |

## 운영 환경

| 환경 | 설명 |
|------|------|
| 운영 서버 | CIB040L5 (Linux) |
| 배포 경로 | `/data/external_data_monitoring/msys/` |
| 로그 경로 | `/data/external_data_monitoring/log/` |
| 타임존 | KST (Asia/Seoul, UTC+9) |

## 주요 테이블

| 테이블 | 설명 |
|--------|------|
| tb_user | 사용자 계정 |
| tb_con_mst | 수집 작업 마스터 |
| tb_con_hist | 수집 이력 |
| tb_api_key_mngr | API 키 관리 |
| tb_mngr_sett | 관리자 설정 |
| tb_menu | 메뉴 정의 |

## 메뉴 목록 (실측)

아래 표는 `DDL/data/tb_menu.csv`(상단 메뉴 정의 시드) 12행과 `routes/` 의 화면 라우트를 **직접 대조해 만든 것**입니다(2026-07-29 확인).

| 표시 순서 | 상단 메뉴 이름 | `menu_id` | URL | 본 메뉴얼 |
|:--:|------|------|------|------|
| 0 | 데이터 수집 일정 | `collection_schedule` | `/collection_schedule` | 데이터 수집 일정 |
| 1 | 실시간 현황 | `card_summary` | `/card_summary` | 실시간 현황(카드 요약) |
| 2 | 대시보드 | `dashboard` | `/dashboard` | 대시보드 |
| 3 | 잔디 | `jandi` | `/jandi` | 잔디 |
| 4 | 데이터분석 | `data_analysis` | `/data_analysis` | 데이터분석 |
| 5 | 차트분석 | `chart_analysis` | `/chart_analysis` | 차트분석 |
| 6 | 상세데이터 | `raw_data` | `/raw_data` | 상세데이터 |
| 7 | 데이터 명세서 | `data_spec` | `/data_spec` | 데이터 명세서 |
| 8 | 관리자 설정 | `mngr_sett` | `/mngr_sett` | 관리자 설정 |
| 9 | API 테스트 | `api_test` | `/api_test` | API 테스트 |
| 10 | Airflow | `airflow` | `http://10.200.153.136:180` (외부) | 외부 연동 |
| 11 | Kafka UI | `kafka_ui` | `http://10.200.153.136:28080/` (외부) | 외부 연동 |

**시드 정의와 실제 화면의 차이 (확인된 것만 기재)**

| 항목 | 상태 | 설명 |
|------|------|------|
| API 키 관리 (`/api_key_mngr`) | 화면·라우트 **있음**, `tb_menu.csv` 시드에 **없음** | 2026-05-11 캡처의 상단 메뉴에는 «API 키 관리» 가 보입니다. 운영 DB의 `tb_menu` 에는 등록되어 있고 CSV 시드만 오래된 것으로 보입니다. |
| 컬럼 매핑 (`/mapping/`) | 화면·라우트 **있음**, 상단 메뉴 **없음** | URL 직접 입력으로만 접근합니다. |
| «관리자» 메뉴 (`/admin`) | **없음** | 화면 라우트가 없습니다. 통계·엑셀 양식 관리는 «관리자 설정» 안의 탭입니다. |

> ⚠️ 위 표의 근거는 **저장소의 시드 CSV와 소스 코드**입니다. 운영 DB의 `tb_menu` 를 직접 조회한 것이 아니므로, 실제 상단 메뉴와 다르면 DB 값이 우선입니다.

## 권한 체계

| 권한(`menu_id`) | 설명 |
|------|------|
| `mngr_sett` | 관리자 설정 메뉴 접근. 이 권한 보유 여부가 곧 **관리자 판정** 기준입니다(`is_admin = 'mngr_sett' in user_permissions`) |
| `api_key_mngr` | API 키 관리 메뉴 접근 |
| `collection_schedule` / `dashboard` / `card_summary` / `jandi` | 각 모니터링 화면 접근 |
| `analysis` / `data_analysis` | 차트분석 / 데이터분석 접근 |
| `data_spec` | 데이터 명세서 접근 |
| `raw_data` / `api_test` | 상세데이터 / API 테스트 접근 |

> ℹ️ **권한이 실제로 하는 일**: 권한 값은 **상단 메뉴에 그 항목을 보여줄지**를 정합니다(`templates/navbar.html` — `item.menu_id in g.user.permissions`).
> 페이지 URL 자체를 막는 것은 **API 키 관리(`@api_key_mngr_required`)** 등 일부 화면뿐이며, 나머지 화면은 로그인만 되어 있으면 URL 직접 입력으로 열립니다. 다만 **표시되는 데이터는 사용자별 데이터 접근 권한(`tb_user_data_perm_auth_ctrl`)으로 걸러집니다.**

## 공통 화면 동작 (2026-05 반영)

| 항목 | 내용 | 반영 |
|------|------|------|
| 로딩 표시 | 모든 화면이 **같은 로딩 오버레이 하나**를 씁니다. 화면 전체(상단 메뉴 포함)를 덮으며 기본 문구는 «데이터 로딩 중...» 입니다. | REQ-2605-009 (2026-05-13) |
| 화면 전환 시 요청 취소 | 데이터를 불러오는 중에 다른 메뉴로 이동하면 진행 중이던 요청이 **취소**됩니다. 이전에는 잔디 화면에서 이 처리가 없어 이동 후에도 로딩이 남아 있었습니다. | REQ-2605-009 |
| 상단 메뉴 크기 | 상단 메뉴 영역이 `nav-container` 라는 전용 규칙(최대 폭 1600px)으로 고정되어, 화면 안쪽 내용 폭을 바꿔도 메뉴 크기가 따라 변하지 않습니다. | REQ-2605-007 (2026-05-13) |

> 근거: `static/js/components/loading.js`, `templates/base.html`(`#global-loading`·`#loading-message`), `static/css/common.css`(`.nav-container`), `templates/navbar.html`.

---

> ↑ [목록으로](README.md) · [← 이전: 빠른 시작 가이드](00-getting-started.md) · [다음: 환경 설정 →](02-environment-setup.md)
