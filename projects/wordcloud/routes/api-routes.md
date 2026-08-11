# API Routes (api_routes.py)

## 파일 위치
`wordcloud_project/src/routes/api_routes.py`

## 역할
감정 분석, 반어법 감지, 워드클라우드 생성, 불용어管理等 REST API 엔드포인트 제공

## 주요 엔드포인트

| 엔드포인트 | 메서드 | 기능 |
|------------|--------|------|
| `/api/analyze` | POST | 텍스트 감정 분석 및 워드클라우드 생성 |
| `/api/analyze_sarcasm` | POST | 반어법 감지 분석 |
| `/api/upload_csv` | POST | CSV 파일 업로드 |
| `/api/health` | GET | 서버 상태 확인 |
| `/api/stopwords` | GET/POST | 불용어 조회/추가 |
| `/api/stopwords/categories` | GET | 불용어 카테고리 조회 |
| `/api/stopwords/<word>` | DELETE | 불용어 삭제 |
| `/api/stopwords/check` | POST | 단어 불용어 확인 |
| `/api/stopwords/classify` | POST | 단어 자동 분류 |
| `/api/stopwords/filter` | POST | 텍스트에서 불용어 제거 |

## 의존성

- `src/modules/emotion_analysis.py` - 감정 분석
- `src/modules/sarcasm_analysis.py` - 반어법 감지
- `src/modules/wordcloud_generator.py` - 워드클라우드 생성
- `src/modules/stopword_manager.py` - 불용어 관리
- `src/config/settings.py` - 설정

## 관련 문서

- [project_wordcloud/modules/emotion-analysis.md](../modules/emotion-analysis.md)
- [project_wordcloud/modules/sarcasm-analysis.md](../modules/sarcasm-analysis.md)
- [project_wordcloud/modules/wordcloud-generator.md](../modules/wordcloud-generator.md)
- `project_wordcloud/modules/stopword-manager.md` (문서 미작성)