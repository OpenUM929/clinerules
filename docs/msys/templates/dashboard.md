# dashboard

## 파일
- Template: `D:\dev\msys\templates\dashboard.html`
- Route: `D:\dev\msys\routes\ui\dashboard_routes.py`

## 도메인
실시간 수집 현황 대시보드 - Job ID별 성공률, 이벤트 로그

## 확장
- `base.html`
- `collapsible_controls.html`

## 엔드포인트
| 용도 | URL | 메서드 |
|------|-----|--------|
| 대시보드 | GET /, /dashboard | 페이지 렌더링 |
| 요약 데이터 | GET /api/dashboard/summary | JSON |
| 상세 데이터 | GET /api/dashboard/details | JSON |
| 이벤트 로그 | GET /api/dashboard/event-log | JSON |

## UI 구성
### 날짜 선택
- 시작일, 종료일, 전체 데이터 체크박스, 조회 버튼

### 주요 지표 (상단 6개 그리드)
1. 총 Job ID 개수
2. 총 호출 건수
3. 기간별 수집 현황 (일간/주간/월간/연간 성공률)

### Job ID별 상세 현황 테이블
- Job ID, 데이터명, 주기(cron), 총 호출 건수
- 일간/주간/월간/반기/연간 성공률
- 검색, 페이징

### 이벤트 로그
- 일별 이벤트 목록
- 검색, 페이징
- 저장 버튼

## JS 파일
- `/static/js/pages/dashboard.js`

## 연관 문서
- Service: [../services/dashboard-service.md](../services/dashboard-service.md)
- DAO: [../dao/analytics-dao.md](../dao/analytics-dao.md), [../dao/con-hist-dao.md](../dao/con-hist-dao.md)
- Mapper: [../mapper/dashboard-mapper.md](../mapper/dashboard-mapper.md)
- Route: [../routes/ui-dashboard-routes.md](../routes/ui-dashboard-routes.md)
