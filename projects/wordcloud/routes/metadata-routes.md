# Metadata Routes (metadata_routes.py)

## 파일 위치
`wordcloud_project/src/routes/metadata_routes.py`

## 역할
메타데이터 조회, 저장, 업데이트 관련 REST API 엔드포인트 제공

## 주요 엔드포인트

| 엔드포인트 | 메서드 | 기능 |
|------------|--------|------|
| `/metadata` | GET | 메타데이터 페이지 렌더링 |
| `/metadata/save` | POST | 메타데이터 저장 |
| `/metadata/load/<employee_id>` | GET | 특정 직원 메타데이터 로드 |
| `/metadata/list` | GET | 메타데이터 목록 조회 |

## 의존성

- `src/services/metadata_service.py` - 메타데이터 관리 로직

## 관련 문서

- [project_wordcloud/services/metadata-service.md](../services/metadata-service.md)
- `project_wordcloud/models/metadata-manager.md` (문서 미작성)