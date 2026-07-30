# data_analysis

## 파일
- Template: `D:\dev\msys\templates\data_analysis.html`
- Route: `D:\dev\msys\routes\analysis_routes.py`

## 도메인
데이터 분석 - 수집 이력 분석, 장애 추적, 통계

## 확장
- `base.html`
- `collapsible_controls.html`

## 엔드포인트
| 용도 | URL | 메서드 |
|------|-----|--------|
| 데이터 분석 | GET /data_analysis | 페이지 렌더링 |
| 필터 옵션 | GET /api/analytics/job_ids | JSON |
| 요약 데이터 | GET /api/analytics/summary | JSON |
| 상세 데이터 | GET /api/analytics/raw_data | JSON |

## UI 구성
### 필터
- 시작일, 종료일
- Job ID 선택
- 장애코드 선택
- 실 존재 데이터 기간 표시

### 요약/통계 카드 (3개 그리드)
1. 최대/최소 소요 시간
2. 실패 호출 건수
3. 중단 횟수

### Job ID 상세정보 테이블
- Job ID, 데이터명, 주기(cron), 설명
- 검색, 페이징

### 수집 및 가공 데이터 테이블
| 컬럼 | 설명 |
|------|------|
| 날짜 | 수집 날짜 |
| Job ID | 작업 ID |
| 장애코드 | 에러 코드 |
| 요일 | 요일 |
| 수집시간(hr) | 소요 시간 |
| 예측 수집시간(hr) | 예측 값 |
| 완전성(%) | 완전성 비율 |
| 평균소요시간(hr) | 평균 |
| 최근3회평균(hr) | |
| 연속실패 | 연속 실패 횟수 |
| 이상치 | 이상치 표시 |

## JS 파일
- `/static/js/pages/data_analysis.js`

## 연관 문서
- Service: [../services/analysis-service.md](../services/analysis-service.md)
- DAO: [../dao/analytics-dao.md](../dao/analytics-dao.md)
- Route: [../routes/analysis-routes.md](../routes/analysis-routes.md)
