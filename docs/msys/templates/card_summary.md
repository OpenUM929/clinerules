# card_summary

## 파일
- Template: `templates/card_summary.html`
- Route: `routes/card_summary_routes.py`

## 도메인
수집 현황 카드 형태 요약 - Job ID별 상태를 카드로 표시

## 확장
- `base.html`

## UI 구성
### 옵션
- 표시 모드: 명칭 / 코드 / 명칭+코드

### 카드 그리드
- Job ID별 수집 상태 카드
- 성공/실패 건수
- 동적 생성

### 기능
- 수집 요청서 양식 다운로드

## JS 파일
- `/static/js/pages/card_summary.js`
- CSS: `/static/css/card_summary.css`

## 연관 문서
- Service: `service/card_summary_service.py`
- Route: `.clinerules/docs/msys/routes/card-summary-routes.md`
