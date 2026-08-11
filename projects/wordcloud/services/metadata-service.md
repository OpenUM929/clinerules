# Metadata Service

## 파일 위치
`wordcloud_project/src/services/metadata_service.py` (220줄)

## 역할
메타데이터 저장, 조회, 업데이트 관련 서비스 로직

## 주요 함수

| 함수 | 기능 |
|------|------|
| `create_metadata()` | 메타데이터 생성 |
| `save_metadata()` | 메타데이터 저장 |
| `load_metadata()` | 메타데이터 로드 |
| `update_metadata()` | 메타데이터 업데이트 |
| `verify_integrity()` | 데이터 무결성 검증 |
| `get_consolidated_analysis()` | 통합 분석 결과 조회 |

## 의존성

- `src/models/metadata_manager.py` - MetadataManager 클래스
- `src/modules/metadata_analysis.py` - 통합 분석 계산
- `src/modules/nlp_analysis.py` - 형태소 분석
- `src/modules/emotion_analysis.py` - 감정 분석
- `src/modules/profanity_filter.py` - 욕설 필터

## 관련 문서

- [project_wordcloud/routes/metadata-routes.md](../routes/metadata-routes.md)
- `project_wordcloud/models/metadata-manager.md` (문서 미작성)
- `project_wordcloud/modules/metadata-analysis.md` (문서 미작성)