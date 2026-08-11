# Batch Events

## 파일 위치
`wordcloud_project/src/services/batch_events.py` (103줄)

## 역할
SSE (Server-Sent Events) 이벤트 스트리밍 및 배치 결과 ZIP 파일 생성

## 주요 함수

| 함수 | 기능 |
|------|------|
| `stream_batch_events(global_state)` | SSE 이벤트 스트림 생성 (제너레이터) |
| `create_batch_zip(batch_dir, session_results)` | 배치 결과 ZIP 파일 생성 |
| `create_sse_response(global_state)` | Flask SSE Response 생성 |

## 사용처

- `/api/batch/events` 엔드포인트에서 실시간 진행률 전달
- `/api/batch/download` 엔드포인트에서 결과 파일 제공

## 관련 문서

- [project_wordcloud/routes/batch-routes.md](../routes/batch-routes.md)
- [project_wordcloud/services/batch-service.md](batch-service.md)