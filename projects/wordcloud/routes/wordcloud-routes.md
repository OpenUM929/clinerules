# WordCloud Routes (wordcloud_routes.py)

## 파일 위치
`wordcloud_project/src/routes/wordcloud_routes.py`

## 역할
워드클라우드 생성 및 관리 관련 REST API 엔드포인트 제공

## 주요 엔드포인트

| 엔드포인트 | 메서드 | 기능 |
|------------|--------|------|
| `/api/wordcloud/create` | POST | 워드클라우드 생성 |
| `/api/wordcloud/options` | POST | 워드클라우드 옵션 업데이트 |

## 의존성

- `src/modules/wordcloud_generator.py` - 워드클라우드 생성
- `src/services/wordcloud_service.py` - 워드클라우드 서비스

## 관련 문서

- [project_wordcloud/modules/wordcloud-generator.md](../modules/wordcloud-generator.md)
- [project_wordcloud/services/wordcloud-service.md](../services/wordcloud-service.md)