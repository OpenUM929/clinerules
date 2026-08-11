# WordCloud Generator (워드클라우드 생성)

## 파일 위치
`wordcloud_project/src/modules/wordcloud_generator.py` (351줄)

## 역할
텍스트/단어빈도에서 워드클라우드 이미지 생성 - 감정 기반 색상 지원

## 클래스

| 이름 | 기능 |
|------|------|
| `WordCloudConfig` | 워드클라우드 설정 관리 |
| `WordCloudGenerator` | 워드클라우드 생성기 |

## 주요 메서드

| 메서드 | 기능 |
|--------|------|
| `generate(text, output_path)` | 기본 워드클라우드 생성 |
| `generate_wordcloud_with_options()` | 옵션 적용 워드클라우드 생성 |
| `generate_with_colors_and_options()` | 감정 기반 색상 워드클라우드 생성 |

## 옵션

| 옵션 | 설명 | 기본값 |
|------|------|--------|
| `background_color` | 배경색 | `white` |
| `max_words` | 최대 단어 수 | `100` |
| `width` | 너비 | `800` |
| `height` | 높이 | `600` |
| `remove_stopwords` | 불용어 제거 | `True` |

## 감정 기반 색상

- `word_scores` 딕셔너리로 단어별 감정 점수 전달
- 양수(긍정):暖色系
- 음수(부정):寒色系
- 0(중립):중립 색상

## 의존성

- `wordcloud` - wordcloud 라이브러리
- `matplotlib` - 이미지 생성
- `src/modules/stopword_manager.py` - 불용어

## 관련 문서

- [project_wordcloud/services/wordcloud-service.md](../services/wordcloud-service.md)
- [project_wordcloud/services/batch-processor.md](../services/batch-processor.md)