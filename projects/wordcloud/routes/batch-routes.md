# Batch Routes (batch_routes.py)

## 파일 위치
`wordcloud_project/src/routes/batch_routes.py`

## 역할
배치 처리 관련 REST API 엔드포인트 제공 - 파일 업로드, 배치 처리, 결과 조회/삭제

## 주요 엔드포인트

| 엔드포인트 | 메서드 | 기능 |
|------------|--------|------|
| `/api/batch/upload` | POST | 배치 파일 (CSV/Excel) 업로드 |
| `/api/batch/preprocess` | POST | 데이터 전처리 시작 |
| `/api/batch/process` | POST | 배치 메타데이터 처리 시작 |
| `/api/batch/list` | GET | 배치 목록 조회 |
| `/api/batch/delete` | POST | 배치 삭제 |
| `/api/batch/download` | GET | 배치 결과 ZIP 다운로드 |
| `/api/batch/sample` | GET | 샘플 메타데이터 조회 |
| `/api/batch/events` | GET | SSE 이벤트 스트리밍 |

## 의존성

- `src/services/batch_service.py` - 배치 처리 로직
- `src/services/batch_manager.py` - 배치 관리
- `src/services/batch_processor.py` - 배치 처리
- `src/services/batch_events.py` - SSE 이벤트

## 관련 문서

- [project_wordcloud/services/batch-service.md](../services/batch-service.md)
- [project_wordcloud/services/batch-manager.md](../services/batch-manager.md)
- [project_wordcloud/services/batch-processor.md](../services/batch-processor.md)