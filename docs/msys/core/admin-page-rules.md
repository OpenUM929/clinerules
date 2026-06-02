# 관리 페이지 규칙 (Admin Page Rules)

> 이 문서는 00-core.md에서 참조합니다.

## 관리 페이지 규칙 (CRITICAL)
- 새 관리 페이지 작업 시: **mngr_sett.md 먼저 읽기**
- 기존 관리 페이지 수정 시: 해당 페이지 문서 + mngr_sett.md 동시 참조

## 기준 패턴 문서 위치
- `docs/msys/templates/mngr_sett.md` - 관리 페이지 패턴 예시

## 관리 페이지 개발 체크리스트
- [ ] mngr_sett.md 읽기
- [ ] 대상 페이지 문서 읽기
- [ ] 기준 패턴과 비교하여 차이점 확인
- [ ] 일관성 있는 UI/UX 적용
- [ ] 서버 사이드 페이징 구현
- [ ] 검색 기능 구현 (디바운스 적용)
- [ ] 테스트 실행

## 관리 페이지 공통 패턴
- 테이블: DataTables 기반 서버 사이드 페이징
- 검색: 디바운스 적용 (300ms)
- CRUD: Modal 또는 별도 페이지
- 권한: mngr_sett 권한 필요

## 관련 문서
- [mngr_sett.md](../msys/templates/mngr_sett.md) - 관리 페이지 패턴
- [04.design-change.md](../../04.design-change.md) - UI 변경 규칙
