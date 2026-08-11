# UI Routes (ui_routes.py)

## 파일 위치
`wordcloud_project/src/routes/ui_routes.py`

## 역할
웹 페이지 렌더링 엔드포인트 제공 - 메인 페이지, 결과 페이지 등

## 주요 엔드포인트

| 엔드포인트 | 메서드 | 기능 |
|------------|--------|------|
| `/` | GET | 메인 페이지 (감정 분석 입력) |
| `/results` | GET | 결과 보기 페이지 |
| `/wordcloud` | GET | 워드클라우드 페이지 |

## 템플릿 연동

- `web/templates/index.html` - 메인 페이지
- `web/templates/results.html` - 결과 페이지
- `web/templates/wordcloud.html` - 워드클라우드 페이지

## 의존성

- `web/templates/base.html` - 베이스 템플릿

## 관련 문서

- [project_wordcloud/templates/screen-domain.md](../templates/screen-domain.md)