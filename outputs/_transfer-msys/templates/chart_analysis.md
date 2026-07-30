# chart_analysis

## 파일
- Template: `D:\dev\msys\templates\chart_analysis.html`
- Route: `D:\dev\msys\routes\analysis_routes.py`

## 도메인
수집 현황 분석 차트 - 성공률/장애 코드 시각화

## 확장
- `base.html`
- `collapsible_controls.html`

## 엔드포인트
| 용도 | URL | 메서드 |
|------|-----|--------|
| 차트 분석 | GET /chart_analysis | 페이지 렌더링 |
| 성공률 추이 | GET /api/analytics/success_rate_trend | JSON |
| 장애 비율 | GET /api/analytics/trouble_by_code | JSON |

## UI 구성
### 날짜 선택
- 시작일, 종료일

### 차트 표시 옵션
- 라벨 표시 방식: 명칭 / 코드

### Job ID 선택
- 전체 선택 / 전체 해제
- 체크박스 목록

### 차트 (2개)
1. **기간별 수집 성공률**
   - 라인 차트 / 바 차트

2. **장애 코드별 비율**
   - 도넛 차트 / 바 차트

## JS 파일
- `/static/js/pages/chart_analysis.js`

## 연관 문서
- Service: [../services/analysis-service.md](../services/analysis-service.md)
- Route: [../routes/api-analysis.md](../routes/api-analysis.md)
