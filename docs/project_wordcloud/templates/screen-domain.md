# 화면 도메인 (Screen Domain)

## 파일 위치
`wordcloud_project/web/templates/`

## 화면 목록

| 화면 | 템플릿 파일 | 설명 |
|------|-----------|------|
| 메인 (감정 분석) | `index.html` | 텍스트 입력, 감정 분석, 워드클라우드 |
| 결과 보기 | `results.html` | 분석 결과 표시 |
| 워드클라우드 | `wordcloud.html` | 워드클라우드 전용 페이지 |
| 메타데이터 | `metadata.html` | 메타데이터 관리 |
| 배치 처리 | `metadata_batch.html` | 배치 처리 페이지 |
| 데이터 전처리 | `preprocess.html` | 데이터 전처리 |
| 반어법 분석 | `sarcasm.html` | 반어법 감지 |
| 불용어 관리 | `stopwords.html` | 불용어 CRUD |
| 설정 | `settings.html` | 시스템 설정 |
| 베이스 | `base.html` | 공통 레이아웃 템플릿 |

## 관련 문서

- [project_wordcloud/routes/ui-routes.md](../routes/ui-routes.md) - 페이지 라우트
- [project_wordcloud/routes/batch-routes.md](../routes/batch-routes.md) - 배치 라우트