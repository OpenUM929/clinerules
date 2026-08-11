# WordCloud Service

## 파일 위치
`wordcloud_project/src/services/wordcloud_service.py` (222줄)

## 역할
워드클라우드 생성 관련 서비스 로직 - 텍스트 처리, 단어 빈도 계산, 워드클라우드 생성 옵션 관리

## 주요 함수

| 함수 | 기능 |
|------|------|
| `create_wordcloud(data)` | 워드클라우드 생성 |
| `get_wordcloud_list()` | 워드클라우드 목록 조회 |
| `get_wordcloud_detail(wordcloud_id)` | 워드클라우드 상세 정보 |
| `update_wordcloud_options(data)` | 워드클라우드 옵션 업데이트 |
| `update_wordcloud_pos(data)` | 형태소 유형 업데이트 |

## 워드클라우드 옵션

| 옵션 | 변수명 | 기본값 |
|------|--------|--------|
| 형태소 선택 | `wordcloud_pos` | `['Noun']` |
| 배경색 | `background_color` | `'white'` |
| 감정 색상 | `apply_emotion_colors` | `True` |
| 욕설 제거 | `remove_profanity` | `False` |
| 최대 단어 수 | `max_words` | `100` |

## 의존성

- `src/modules/wordcloud_generator.py` - 워드클라우드 생성
- `src/modules/nlp_analysis.py` - 형태소 분석
- `src/modules/profanity_filter.py` - 욕설 필터

## 관련 문서

- [project_wordcloud/routes/wordcloud-routes.md](../routes/wordcloud-routes.md)
- [project_wordcloud/modules/wordcloud-generator.md](../modules/wordcloud-generator.md)