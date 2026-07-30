# NLP Analysis (형태소 분석)

## 파일 위치
`wordcloud_project/src/modules/nlp_analysis.py` (183줄)

## 역할
텍스트 형태소 분석 - Kiwi 및 Okt 형태소 분석기 사용

## 주요 클래스/함수

| 이름 | 기능 |
|------|------|
| `NLPAnalysis` | 형태소 분석기 클래스 |
| `analyze(text, output_path, context)` | 텍스트 분석 |
| `analyze_word_pos(word)` | 단어 품사 분석 |
| `_extract_sentence_boundaries(text)` | 문장 경계 추출 |

## 분석기

| 분석기 | 사용 | 기능 |
|--------|------|------|
| **Kiwi** | `kiwipiepy.Kiwi` | 의존 구문 분석, 형태소 분석 |
| **Okt** | `konlpy.tag.Okt` | 형태소 분석, 품사 태깅 |

## 주요 품사 태그

| 태그 | 설명 |
|------|------|
| `Noun` | 명사 |
| `Verb` | 동사 |
| `Adjective` | 형용사 |
| `Adverb` | 부사 |
| `Exclamation` | 감탄사 |

## 설정

- `configs/nlp_config.json` - 분석기 설정
- `wordcloud_pos` - 워드클라우드에 사용할 품사 선택

## 의존성

- `kiwipiepy` - Kiwi 형태소 분석
- `konlpy` - Okt 형태소 분석
- `src/modules/stopword_manager.py` - 불용어 관리

## 관련 문서

- [project_wordcloud/services/wordcloud-service.md](../services/wordcloud-service.md)
- `project_wordcloud/modules/stopword-manager.md` (문서 미작성)