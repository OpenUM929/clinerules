# Batch Service

## 파일 위치
`wordcloud_project/src/services/batch_service.py` (150줄)

## 역할
배치 처리 관련 기능을 조정(coordination)하는 메인 서비스 - 파일 업로드, 배치 목록 조회, 메타데이터 처리 조정

## 주요 함수

| 함수 | 기능 |
|------|------|
| `upload_batch_file()` | CSV/Excel 파일 업로드 및 검증 |
| `upload_csv()` | CSV 파일 업로드 (단일) |
| `start_preprocessing()` | 데이터 전처리 시작 |
| `get_batch_list()` | 배치 목록 조회 |
| `delete_batch()` | 배치 삭제 |
| `process_batch_metadata()` | 배치 메타데이터 처리 조율 |
| `get_sample_metadata()` | 샘플 메타데이터 조회 |
| `download_batch_results()` | 배치 결과 ZIP 다운로드 |
| `get_processing_events()` | SSE 이벤트 스트리밍 |

## 의존성

- `src/services/file_parser.py` - 파일 파싱
- `src/services/batch_manager.py` - 배치 관리
- `src/services/batch_processor.py` - 배치 처리
- `src/services/batch_events.py` - 이벤트 처리
- `src/models/metadata_manager.py` - 메타데이터 관리

## 관련 문서

- [project_wordcloud/routes/batch-routes.md](../routes/batch-routes.md)
- [project_wordcloud/services/batch-manager.md](batch-manager.md)
- [project_wordcloud/services/batch-processor.md](batch-processor.md)
- [project_wordcloud/services/batch-events.md](batch-events.md)