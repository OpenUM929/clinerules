# data_report

## 파일
- Template: `templates/data_report.html`
- Route: `routes/data_report_routes.py`

## 도메인
수집 현황 보고서 - 주간/월간 보고서

## 확장
- `base.html`

## UI 구성
### 뷰 전환
- 주간 / 월간 토글

### 보고서 테이블
| 컬럼 | 설명 |
|------|------|
| 날짜 | 수집 날짜 |
| Job ID | 작업 ID |
| 예정 시간 | 스케줄된 시간 |
| 상태 | 성공/실패 |
| 상세 정보 | 오류 메시지 등 |

## JS 파일
- `/static/js/pages/data_report.js`

## 연관 문서
- Route: `.clinerules/docs/msys/routes/data-report-routes.md`
