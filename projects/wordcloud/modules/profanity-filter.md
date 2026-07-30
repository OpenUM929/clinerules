# Profanity Filter (욕설 필터)

## 파일 위치
`wordcloud_project/src/modules/profanity_filter.py` (269줄)

## 역할
텍스트에서 욕설 단어 检测 및 필터링

## 주요 함수

| 함수 | 기능 |
|------|------|
| `check_profanity(text)` | 욕설 检测 |
| `filter_profanity(text)` | 욕설 제거 |
| `get_profanity_list()` | 욕설 목록 조회 |

## 필터링 방식

1. 사전 기반 매칭
2. 정규식 패턴 매칭
3. 노이즈 처리 (특수문자, 띄어쓰기 우회)

## 관련 문서

- [project_wordcloud/services/wordcloud-service.md](../services/wordcloud-service.md)
- [project_wordcloud/services/batch-processor.md](../services/batch-processor.md)