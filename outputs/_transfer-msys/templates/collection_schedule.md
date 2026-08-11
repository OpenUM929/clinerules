# collection_schedule

## 파일
- Template: `D:\dev\msys\templates\collection_schedule.html`
- Route: `D:\dev\msys\routes\ui\collection_schedule_routes.py`

## 도메인
데이터 수집 일정 - 주간/월간 히트맵, 그룹별 수집 현황

## 확장
- `base.html`

## 엔드포인트
| 용도 | URL | 메서드 |
|------|-----|--------|
| 수집 일정 | GET /collection_schedule | 페이지 렌더링 |
| 일정 데이터 | GET /api/collection_schedule | JSON |
| 그룹 메모 | GET/POST/PUT/DELETE /api/group-memo | JSON |
| 메모 일괄 조회 | GET /api/memos-batch | JSON |

## UI 구성
### 요약 통계
- 전체 예정 / 성공 / 실패 / 미수집

### 보기 옵션
- 주간 / 월간 토글
- 표시 모드: 명칭 / 코드 / 설명

### 히트맵 (캘린더 그리드)
- 일별 Job ID별 수집 현황
- 상태별 색상: 성공(초록), 실패(빨강), 미수집(주황), 진행중(노랑), 예정(회색)
- 그룹화 및 팝업

### 메모 기능
- 그룹별 날짜별 메모

## 상태
| 상태 | 색상 | 설명 |
|------|------|------|
| success | 초록 | 수집 성공 |
| fail | 빨강 | 수집 실패 |
| nodata | 주황 | 미수집 |
| inprogress | 노랑 | 진행 중 |
| scheduled | 회색 | 예정 |

## JS 파일
- `/static/js/pages/collection_schedule.js`

## 연관 문서
- Service: [../services/collection-schedule-service.md](../services/collection-schedule-service.md)
- Mapper: [../mapper/grp-memo-mapper.md](../mapper/grp-memo-mapper.md)
- Route: [../routes/collection-schedule-routes.md](../routes/collection-schedule-routes.md)
