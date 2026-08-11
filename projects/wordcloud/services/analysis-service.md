# Analysis Service

## 파일 위치
`wordcloud_project/src/services/analysis_service.py` (144줄)

## 역할
텍스트 분석 조율 - 감정 분석, 형태소 분석, 워드클라우드 생성 통합 조정

## 주요 함수

| 함수 | 기능 |
|------|------|
| `analyze_text(data)` | 텍스트 분석 (감정 + 형태소) |
| `get_analysis_result(analysis_id)` | 분석 결과 조회 |
| `batch_analyze(data)` | 배치 분석 |

## 분석 파이프라인

1. 텍스트 입력
2. 형태소 분석 (NLP) - 단어 추출
3. 감정 분석 (Emotion) - 감정 점수 계산
4. 워드클라우드 생성

## 의존성

- `src/modules/nlp_analysis.py` - 형태소 분석
- `src/modules/emotion_analysis.py` - 감정 분석
- `src/modules/wordcloud_generator.py` - 워드클라우드 생성

## 관련 문서

- [project_wordcloud/modules/nlp-analysis.md](../modules/nlp-analysis.md)
- [project_wordcloud/modules/emotion-analysis.md](../modules/emotion-analysis.md)
- [project_wordcloud/modules/wordcloud-generator.md](../modules/wordcloud-generator.md)