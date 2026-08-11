# Batch Manager

## 파일 위치
`wordcloud_project/src/services/batch_manager.py` (175줄)

## 역할
배치 디렉토리 관리 - 배치 목록 조회, 삭제, 메타데이터 로드

## 주요 함수

| 함수 | 기능 |
|------|------|
| `get_batch_list(processed_data_dir)` | 배치 목록 조회 (날짜순 정렬) |
| `delete_batch_directory(batch_path)` | 배치 디렉토리 삭제 |
| `load_batch_metadata(processed_data_dir, batch_dir)` | 배치 내 모든 메타데이터 로드 |
| `get_batch_summary(processed_data_dir, batch_path)` | 배치 요약 정보 조회 |
| `get_sample_metadata_from_results(session_results, batch_dir, processed_data_dir)` | 세션 결과에서 샘플 메타데이터 조회 |

## 매개변수

- `processed_data_dir`: 처리된 데이터 기본 디렉토리 경로

## 관련 문서

- [project_wordcloud/routes/batch-routes.md](../routes/batch-routes.md)
- [project_wordcloud/services/batch-service.md](batch-service.md)
- `project_wordcloud/models/metadata-manager.md` (문서 미작성)