# jandi

## 파일
- Template: `D:\dev\msys\templates\jandi.html`
- Route: `D:\dev\msys\routes\jandi_routes.py`

## 도메인
Job ID별 수집 잔디(Heatmap) 모니터링

## 확장
- `base.html`
- `collapsible_controls.html`

## 엔드포인트
| 용도 | URL | 메서드 |
|------|-----|--------|
| 잔디 현황 | GET /jandi | 페이지 렌더링 |
| Job ID 목록 | GET /api/job-list | JSON |
| 잔디 데이터 | GET /api/jandi-data | JSON |

## UI 구성
### 날짜 선택
- 시작일, 종료일, 전체 데이터 체크박스, 조회 버튼

### Job ID 상세정보 테이블
- Job ID, 데이터명, 주기(cron), 설명
- 검색, 페이징

### Job ID별 잔디 모니터링
- Heatmap 차트
- 정렬 (Job ID 오름차순/내림차순)
- 검색, 페이징

## JS 파일
- `/static/js/pages/jandi.js`

## 연관 문서
- Service: [../services/jandi-service.md](../services/jandi-service.md)
- DAO: [../dao/con-hist-dao.md](../dao/con-hist-dao.md)
- Mapper: [../mapper/jandi-mapper.md](../mapper/jandi-mapper.md)
- Route: [../routes/jandi-routes.md](../routes/jandi-routes.md)
