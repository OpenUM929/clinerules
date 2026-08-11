# 04. User Statistics Menu Scenario

사용자 통계 메뉴 추가 및 접속 통계 작업 시나리오

---

## 시나리오 개요

**목적**: 사용자 통계 메뉴 추가 요청 시 AI가 올바른 문서를 참조하는지 검증

**사전 조건**:
- 00-core.md에 작업 유형 분류표 존재
- docs/msys/templates/mngr_sett.md (관리자설정 템플릿) 존재
- docs/development/time-handling-rules.md (시간 처리 규칙) 존재
- docs/development/field-naming-convention.md (필드명 규칙) 존재
- docs/development/database-naming-standard.md (DB 명명 규칙) 존재

---

## 사용자 요구사항

> 관리자 설정에 사용자 통계 메뉴를 추가하고 싶습니다.
> 
> 1. 사용자별 (ID별로) 일/주/월 접속 현황을 보고 싶습니다.
> 2. 메뉴별 접속 통계도 함께 보고 싶습니다.
> 3. 표과 차트 등으로 다양하게 보고 싶습니다.
> 4. 접속일 수가 없을 경우, 1~3단계로 구분해서 3단계에서는 삭제를 권하고 싶습니다.

---

## 시나리오 1: 사용자 통계 메뉴 추가

**상황**: 관리자 설정에 새 메뉴 "사용자 통계" 추가 요청

**진행 경로**:
1. 00-core.md 확인 → "공통 모듈 수정/추가" 또는 해당 문서 찾기
2. docs/msys/core/admin-page-rules.md → 관리 페이지 규칙 확인
3. docs/msys/templates/mngr_sett.md → 관리자설정 탭 구조 확인
4. docs/msys/screens.md → 화면 목록 확인
5. docs/development/field-naming-convention.md → 필드명 규칙 확인

**참조 문서**:
- [00-core.md](../../00-core.md)
- [docs/msys/core/admin-page-rules.md](../msys/core/admin-page-rules.md)
- [docs/msys/templates/mngr_sett.md](../msys/templates/mngr_sett.md)
- [docs/msys/screens.md](../msys/screens.md)
- [docs/development/field-naming-convention.md](../development/field-naming-convention.md)
- [docs/development/database-naming-standard.md](../development/database-naming-standard.md)

**검토 결과**: ✅ 관리 페이지 패턴 + 필드명 규칙 적용 가능

---

## 시나리오 2: 일/주/월 접속 현황 조회

**상황**: 사용자별 접속 빈도 조회 기능 추가 요청

**진행 경로**:
1. 00-core.md → "시간 문제" 규칙 확인
2. docs/development/time-handling-rules.md → 시간 처리 규칙 확인
3. docs/development/field-naming-convention.md → 필드명 규칙 확인
4. docs/development/database-naming-standard.md → DB 명명 규칙 확인

**데이터 요구사항**:
- 일간 접속 횟수
- 주간 접속 횟수
- 월간 접속 횟수
- 최종 접속일

**시간 기준**:
- 일/주/월 정의: docs/development/time-handling-rules.md 참조

**참조 문서**:
- [docs/development/time-handling-rules.md](../development/time-handling-rules.md)
- [docs/development/field-naming-convention.md](../development/field-naming-convention.md)
- [docs/development/database-naming-standard.md](../development/database-naming-standard.md)

**검토 결과**: ✅ 시간 처리 규칙 적용 가능

---

## 시나리오 3: 메뉴별 접속 통계

**상황**: 메뉴별 접근 통계 표시 요청

**진행 경로**:
1. docs/msys/templates/mngr_sett.md → 통계 탭 구조 확인
2. docs/msys/core/admin-page-rules.md → 관리 페이지 패턴 확인

**데이터 요구사항**:
- 메뉴별 접근 횟수
- 사용자별 메뉴 접근 기록
- 기간별 통계

**참조 문서**:
- [docs/msys/templates/mngr_sett.md](../msys/templates/mngr_sett.md)
- [docs/msys/core/admin-page-rules.md](../msys/core/admin-page-rules.md)

**검토 결과**: ✅ 관리 페이지 패턴 적용 가능

---

## 시나리오 4: 미접속 사용자 계정 관리 (1~3단계 구분)

**상황**: 장기간 미접속 사용자 계정 관리 기능 추가

**단계 구분 기준**:

| 단계 | 조건 | 조치 |
|------|------|------|
| 1단계 | 30일 미접속 | 안내 알림 |
| 2단계 | 60일 미접속 | 경고 알림 |
| 3단계 | 90일 미접속 | 삭제 권고 |

**진행 경로**:
1. docs/development/time-handling-rules.md → 시간 계산 규칙 확인
2. docs/msys/templates/mngr_sett.md → 관리 페이지 패턴 확인

**기능 요구사항**:
- 접근 빈도에 따른 사용자 분류
- 알림/경고/삭제 권고 UI
- 배치 또는 수동 실행 옵션

**참조 문서**:
- [docs/development/time-handling-rules.md](../development/time-handling-rules.md)
- [docs/msys/templates/mngr_sett.md](../msys/templates/mngr_sett.md)
- [docs/msys/core/admin-page-rules.md](../msys/core/admin-page-rules.md)

**검토 결과**: ✅ 시간 기준 + 관리 페이지 패턴 적용 가능

---

## 시나리오 5: 표/차트 시각화

**상황**: 데이터를 표와 차트로 다양하게 표시 요청

**진행 경로**:
1. docs/msys/screens.md → 화면 구성 확인
2. 04.design-change.md → UI 변경 규칙 확인 (차트 라이브러리 등)

**시각화 유형**:
- 테이블 (DataTables)
- 막대 차트
- 라인 차트
- 히트맵

**참조 문서**:
- [docs/msys/screens.md](../msys/screens.md)
- [04.design-change.md](../../04.design-change.md)

**검토 결과**: ✅ UI 변경 규칙 적용 가능

---

## 검증 체크리스트

- [ ] 00-core.md 작업 유형 분류 확인
- [ ] docs/msys/core/admin-page-rules.md 관리 페이지 규칙 확인
- [ ] docs/msys/templates/mngr_sett.md 템플릿 구조 확인
- [ ] docs/development/time-handling-rules.md 시간 처리 규칙 확인
- [ ] docs/development/field-naming-convention.md 필드명 규칙 확인
- [ ] docs/development/database-naming-standard.md DB 명명 규칙 확인

---

## 참조 문서 요약

| 구분 | 문서 | 용도 |
|------|------|------|
| 코어 | [00-core.md](../../00-core.md) | 작업 유형 분류 |
| 관리 페이지 | [docs/msys/core/admin-page-rules.md](../msys/core/admin-page-rules.md) | 관리 페이지 규칙 |
| 템플릿 | [docs/msys/templates/mngr_sett.md](../msys/templates/mngr_sett.md) | 관리자설정 구조 |
| 화면 | [docs/msys/screens.md](../msys/screens.md) | 화면 목록 |
| 시간 규칙 | [docs/development/time-handling-rules.md](../development/time-handling-rules.md) | 시간 처리 |
| 필드명 | [docs/development/field-naming-convention.md](../development/field-naming-convention.md) | 네이밍 규칙 |
| DB 명명 | [docs/development/database-naming-standard.md](../development/database-naming-standard.md) | DB 명명 |
| UI 변경 | [04.design-change.md](../../04.design-change.md) | UI 변경 |

---

**생성일**: 2026-04-21