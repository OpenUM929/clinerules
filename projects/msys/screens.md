# 화면/페이지 목록

> 프로젝트의 화면과 페이지 엔드포인트

---

## 화면 목록

| 페이지 | 템플릿 | 엔드포인트 | 설명 |
|--------|--------|-----------|------|
| 로그인 | `login.html` | `/login` | 사용자 인증 |
| 대시보드 | `dashboard.html` | `/dashboard` | 수집 현황 (Job별 성공률, 이벤트 로그) |
| Jandi | `jandi.html` | `/jandi` | 히트맵 시각화 |
| 수집일정 | `collection_schedule.html` | `/collection_schedule` | 주간/월간 수집 일정 |
| 관리자설정 | `mngr_sett.html` | `/admin/mngr_sett` | 메뉴/설정 관리 |
| 컬럼매핑 | `mapping_management.html` | `/mapping/` | DB 컬럼 매핑 관리 |
| 데이터Specs | `data_spec.html` | `/data_spec` | 데이터 명세서 |
| 카드요약 | `card_summary.html` | `/card_summary` | 요약 카드 |
| 데이터리포트 | `data_report.html` | `/data_report` | 데이터 리포트 |
| 분석 | `chart_analysis.html` | `/chart_analysis` | 차트 분석 |
| 데이터분석 | `data_analysis.html` | `/data_analysis` | 데이터 분석 |
| API 키관리 | `api_key_mngr.html` | `/api_key_mngr` | API 키 관리 |
| 관리자설정(테스트) | `mngr_sett_test.html` | `/mngr_sett_test` | 관리자 설정 테스트 |

---

## 화면별 기능 정의

### 대시보드 (/dashboard)
- Job별 수집 성공률 표시
- 이벤트 로그 조회 (최대/최소 날짜 범위)
- 일별 수집 결과 요약

### Jandi (/jandi)
- 히트맵 시각화 (Job × 날짜)
- Job 선택 및 필터링
- Job 마스터 상세정보 조회

### 수집일정 (/collection_schedule)
- 주간/월간 수집 일정 표시
- 그룹 메모 CRUD
- 배치 메모 조회

### 관리자설정 (/admin/mngr_sett)
- 메뉴 접근 통계
- 엑셀 템플릿 업로드/다운로드
- 아이콘 목록 및 업로드

### 컬럼매핑 (/mapping/)
- 전체 컬럼 매핑 조회
- 미매핑 컬럼 표시
- 매핑 추가/수정/삭제

### 데이터Specs (/data_spec)
- 데이터 명세서 목록
- 명세서 생성/편집/삭제
- 파라미터 관리

### 카드요약 (/card_summary)
- 요약 카드 표시
- 카드별 데이터 구성

### 데이터리포트 (/data_report)
- 리포트 요약 및 상세
- 데이터 내보내기 (export)

### 분석 (/chart_analysis, /data_analysis)
- 차트 분석 (차트 유형 선택)
- 데이터 분석 (테이블 뷰)
- 관리자/일반 사용자 권한 분리

### API 키관리 (/api_key_mngr)
- API 키 생성
- 키 상태 관리 (활성/비활성)
- 사용량 모니터링

---

## 관련 문서

- [overview.md](overview.md) - 프로젝트 개요
- [api-endpoints.md](api-endpoints.md) - API 엔드포인트