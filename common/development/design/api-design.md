# API 설계 (API Design)

**Cline 필수 읽기 문서**

## 1. API 디자인 원칙
- RESTful 원칙 준수 (Resource 중심 URL)
- JSON 응답 표준화 (`{"status": "success", "data": {...}}` 또는 error 형식)
- 에러 처리: Flask errorhandler 사용, 명확한 에러 메시지
- Pagination, Filtering 필요 시 명세
