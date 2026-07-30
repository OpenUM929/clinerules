**Cline 필수 읽기 문서** — Python + Flask

## 1. 기본 규칙 (PEP 8 + Best Practices)
- Black 또는 Ruff로 포맷팅
- Type Hint everywhere (`from __future__ import annotations`)
- Google 스타일 Docstring
- 의미 있는 변수/함수명 사용
- Early return, Guard Clause 적극 활용

## 2. Flask 전용 규칙
- Blueprint 이름은 snake_case
- Route 함수는 명확한 이름 (`get_users`, `create_post` 등)
- Configuration은 `Config` 클래스 상속
- Error handling: try/except 최소화하고 Flask errorhandler 활용

## 3. 관리 페이지 데이터 호출 방식 선택 가이드

새로운 관리 페이지 개발 시 다음 두 가지 버전 중 선택한다.

### 버전 A: 페이징 + 검색 기능 (대용량 데이터용)
- 서버 사이드 페이징 구현 (page, page_size 파라미터)
- 서버 사이드 검색 기능 (디바운스 적용)
- 페이지당 10~20건 표시
- **선택 기준**: 데이터가 100건 이상 예상되거나 검색 기능이 필요한 경우

### 버전 B: 전체 데이터 호출 (소용량 데이터용)
- 한 번에 모든 데이터 로드
- 클라이언트 사이드 정렬/필터링
- **선택 기준**: 데이터가 50건 이하이고 검색이 불필요한 경우

### 선택 방법
1. 사용자에게 데이터 예상 건수 확인
2. 검색 기능 필요 여부 확인
3. 위 기준에 따라 버전 A 또는 B 선택
4. 데이터 양을 정확히 모르면 **버전 A(페이징+검색)**를 기본으로 선택
