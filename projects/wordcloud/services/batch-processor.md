# Batch Processor

## 파일 위치
`wordcloud_project/src/services/batch_processor.py` (402줄)

## 역할
배치 메타데이터 처리 및 워드클라우드 생성 핵심 로직

## 주요 함수

| 함수 | 기능 |
|------|------|
| `initialize_batch_directory(processed_data_dir)` | 배치 디렉토리 생성 |
| `group_data_by_employee(df, target_id_column, mappings)` | employee_id별 데이터 그룹화 |
| `process_employee_metadata()` | 개별 직원 메타데이터 처리 |
| `check_profanity_in_metadata()` | 욕설 检测 및 추적 |
| `generate_employee_wordcloud()` | 직원별 워드클라우드 생성 |
| `calculate_word_scores()` | 감정 기반 단어 점수 계산 |
| `create_batch_summary()` | 배치 요약 JSON 생성 |
| `process_batch()` | 메인 배치 처리 함수 |

## 워드클라우드 옵션

| 옵션 | 변수명 | 기본값 |
|------|--------|--------|
| 형태소 선택 | `wordcloud_pos` | `['Noun']` |
| 배경색 | `background_color` | `'white'` |
| 감정 색상 | `apply_emotion_colors` | `True` |
| 욕설 제거 | `remove_profanity` | `False` |
| 최대 단어 수 | `max_words` | `100` |
| 너비 | `width` | `800` |
| 높이 | `height` | `600` |

## 의존성

- `src/models/metadata_manager.py` - 메타데이터 관리
- `src/modules/wordcloud_generator.py` - 워드클라우드 생성

## 관련 문서

- [project_wordcloud/modules/wordcloud-generator.md](../modules/wordcloud-generator.md)
- `project_wordcloud/models/metadata-manager.md` (문서 미작성)