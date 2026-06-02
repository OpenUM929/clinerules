# 02. Time Handling Workflow Scenario

시간/날짜 처리 작업 시나리오

---

## 시나리오 개요

**목적**: 시간/날짜 관련 작업 요청 시 AI가 `00-core.md` → `docs/msys/data-handling/` 또는 `docs/development/time-handling-rules.md` 경로를 올바르게 따르는지 검증

**사전 조건**:
- 00-core.md에 "시간 문제" 작업 유형 등록됨
- docs/msys/data-handling/ 또는 docs/development/time-handling-rules.md 문서 존재

---

## 시나리오 1: 메모 시간 표시 오류 수정

**상황**: 사용자가 "스케줄 메모 저장 후 시간이 이상하게 표시돼"

**진행 경로**:
1. 00-core.md 확인 → "시간 문제" 행 찾기
2. docs/development/time-handling-rules.md 또는 docs/msys/data-handling/timezone.md 이동
3. SQL TO_CHAR 규칙 확인 (docs/msys/data-handling/basic-rules.md)
4. DAO 쿼리에서 `SELECT created_at` → `SELECT TO_CHAR(created_at, 'YYYY-MM-DD HH24:MI:SS')` 수정
5. 또는 프론트엔드에서 `formatDBDateTime()` 사용 확인

**결과**: 시간이 `26.04.14 19:15` 형식으로 정상 표시

**검토 결과**: ✅ docs/development/time-handling-rules.md 또는 docs/msys/data-handling/ 경로로 정확한 해결책 도출 가능

---

## 시나리오 2: 새 메모 시간 생성

**상황**: 사용자가 "새 메모 추가할 때 현재 시간 자동 입력되게 해줘"

**진행 경로**:
1. 00-core.md 확인 → "시간 문제" 행 찾기
2. docs/msys/data-handling/basic-rules.md 이동
3. JavaScript: `getKSTNow()` 사용 권장
4. Python: `get_kst_now()` 사용 권장
5. `new Date()` 사용 시 → 경고 후 사용자 확인

**결과**: 브라우저 시간대와 관계없이 정확한 KST 시간 생성

**검토 결과**: ✅ 공통함수 사용으로 일관된 시간 생성 가능

---

## 시나리오 3: 작성 시간 표시 포맷 변경

**상황**: 사용자가 "메모 작성 시간을 '2024년 1월 15일' 형식으로 표시해줘"

**진행 경로**:
1. 00-core.md 확인 → "시간 문제" 행 찾기
2. docs/msys/data-handling/time-display.md 이동 (시간 표시 체계 3단계)
3. `formatDBDateTime()` 사용 확인
4. 공통함수 수정 또는 새 포맷 함수 추가 검토
5. SQL `TO_CHAR` 포맷 변경 검토

**결과**: 원하는 포맷으로 시간 표시 (공통함수 사용)

**검토 결과**: ✅ 중앙화된 공통함수로 유지보수 용이

---

## 시나리오 4: 시간대 변환 기능 (위반 케이스)

**상황**: 사용자가 "UTC 시간을 KST로 변환하는 함수 만들어줘"

**진행 경로**:
1. 00-core.md 확인 → "시간 문제" 행 찾기
2. docs/msys/data-handling/timezone.md 이동
3. 프로젝트 규칙 확인: KST만 사용, UTC 변환 불필요
4. 위반 사항 명시:
   - "프로젝트는 KST(UTC+9)만 사용"
   - "UTC 변환은 docs/msys/data-handling/ 또는 docs/development/ 규칙 위반"
5. 사용자 확인: "진행하시겠습니까?"

**결과**: 위반 사항 경고 후 사용자 의사에 따라 진행/취소

**검토 결과**: ✅ 규칙 위반 시 경고 및 사용자 확인 절차 정상 작동

---

## 검증 체크리스트

- [ ] 00-core.md에서 "시간 문제" 행 확인
- [ ] docs/development/time-handling-rules.md 또는 docs/msys/data-handling/ 정상 접근
- [ ] SQL TO_CHAR 규칙 준수 확인
- [ ] JavaScript 공통함수 사용 권장
- [ ] 위반 사항 시 경고 및 사용자 확인

---

**생성일**: 2026-04-15  
**수정일**: 2026-04-16 (경로 업데이트: msys → core)
