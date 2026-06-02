# 03. Setting Popup (Settings) Scenario

설정 팝업 (모달리스) 작업 시나리오

---

## 시나리오 개요

**목적**: 설정 팝업 관련 작업 요청 시 AI가 올바른 문서를 참조하는지 검증

**사전 조건**:
- 00-core.md에 작업 유형 분류 존재
- docs/msys/templates/ 문서 존재

---

## 시나리오 1: 새 설정 팝업 추가

**상황**: 관리 페이지에 새 설정 팝업 추가 요청

**진행 경로**:
1. 00-core.md 확인 → 작업 유형 분류 확인
2. 04.design-change.md → 표준 절차 적용
3. docs/msys/templates/screen-domain.md에서 관리 페이지 확인
4. docs/msys/core/admin-page-rules.md → 관리 페이지 패턴 확인
5. templates/mngr_sett.html 분석
6. templates/setting_popup.html (새 파일) 생성

**결과**: 관리 페이지에 새 설정 팝업 추가

**검토 결과**: ✅ 올바른 문서 참조로 진행 가능

---

## 시나리오 2: 설정 팝업 시간 표시 수정

**상황**: 설정 팝업의 생성 시간이 잘못 표시됨

**진행 경로**:
1. 00-core.md 확인 → 시간 관련 문서 확인
2. docs/msys/data-handling/modal-time.md 이동
3. formatDBDateTime() 사용 확인
4. templates/setting_popup.html 수정

**결과**: 시간이 YY.MM.DD HH:mm 형식으로 정상 표시

**검토 결과**: ✅ 팝업 시간 표시 규칙 적용 가능

---

## 시나리오 3: 설정 팝업 필드명 변경

**상황**: 설정 팝업의 필드명을 DB 컬럼명과 일치시키도록 요청

**진행 경로**:
1. 00-core.md 확인 → 필드명 관련 문서 확인
2. docs/msys/field-naming/overview.md 이동
3. TB_POPUP_MST 테이블 컬럼명 기준 확인
4. service/popup_service.py, templates/setting_popup.html 수정

**결과**: 모든 계층에서 필드명 일치

**검토 결과**: ✅ 필드명 네이밍 규칙 적용 가능

---

## 검증 체크리스트

- [ ] 00-core.md 작업 유형 분류 확인
- [ ] 04.design-change.md 절차 확인
- [ ] docs/msys/core/admin-page-rules.md 관리 페이지 패턴 확인
- [ ] docs/msys/data-handling/modal-time.md 팝업 시간 규칙 확인
- [ ] docs/msys/field-naming/ 필드명 규칙 확인

---

**생성일**: 2026-04-16
