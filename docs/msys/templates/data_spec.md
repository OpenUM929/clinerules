# data_spec

## 파일
- Template: `D:\dev\msys\templates\data_spec.html`
- Route: `D:\dev\msys\routes\data_spec_routes.py`

## 도메인
데이터 명세서 관리 - API 스펙, 요청/응답 파라미터

## 확장
- `base.html`
- `collapsible_controls.html`

## 엔드포인트
| 용도 | URL | 메서드 |
|------|-----|--------|
| 명세서 목록 | GET /data_spec | 페이지 렌더링 |
| 명세 목록 | GET /api/data-spec | JSON |
| 명세 저장 | POST /api/data-spec | JSON |
| 명세 삭제 | DELETE /api/data-spec/{id} | JSON |

## UI 구성
### 메타데이터로 명세서 채우기
- 파일로 불러오기 (JSON/XML/RDF)
- 붙여넣기로 불러오기

### 명세서 목록
- 테이블: ID, 데이터 명칭, 제공 기관, 키워드, 등록일, 참조문서
- 검색, 페이징, 수동 등록

## Modal: 명세 상세 정보
### 필드
| 필드 | ID | 설명 |
|------|-----|------|
| 데이터 명칭 | data_name | |
| 제공 기관 | provider | |
| API URL | api_url | |
| 참고 문서 URL | reference_doc_url | |
| 키워드 | keywords | |
| 상세 설명 | description | |

### 하위 섹션
- 요청 파라미터 테이블
- 응답 파라미터 테이블

## 비밀번호 보호
- 저장/삭제 시 비밀번호 확인 Modal

## JS 파일
- `/static/js/pages/data_spec.js`

## 연관 문서
- Service: [../services/data-spec-service.md](../services/data-spec-service.md)
- DAO: [../dao/data-spec-dao.md](../dao/data-spec-dao.md)
- Route: [../routes/data-spec-routes.md](../routes/data-spec-routes.md)
