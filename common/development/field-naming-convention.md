# 필드명 및 변수명 네이밍 규칙 (Field Naming Convention)

> **모든 프로젝트에서 사용하는 공통命名 규칙입니다.**

---

## 1. 기본 원칙

### 명명법 (Case Styles)

| 스타일 | 설명 | 사용처 |
|--------|------|--------|
| **snake_case** | 소문자 + 언더스코어 | Python, DB 컬럼, JSON 키 |
| **camelCase** | 소문자 시작 + 대문자 구분 | JavaScript 변수/함수 |
| **PascalCase** | 대문자 시작 + 대문자 구분 | 클래스명, 타입명 |
| **UPPER_SNAKE_CASE** | 대문자 + 언더스코어 | 상수, 환경변수 |
| **kebab-case** | 소문자 + 하이픈 | URL, 파일명, CSS 클래스 |

---

## 2. 언어별 규칙

### Python

| 구분 | 규칙 | 예시 |
|------|------|------|
| 변수명 | snake_case | `user_id`, `created_at` |
| 함수명 | snake_case | `get_user()`, `find_by_id()` |
| 클래스명 | PascalCase | `UserMapper`, `DashboardService` |
| 상수 | UPPER_SNAKE_CASE | `MAX_RETRY_COUNT`, `DEFAULT_TIMEOUT` |
| 모듈명 | snake_case | `user_mapper.py`, `datetime_utils.py` |
| 패키지명 | snake_case | `my_package` |

```python
from typing import Dict, List, Any, Optional

class UserService:
    DEFAULT_PAGE_SIZE = 20  # 상수
    
    def find_by_id(self, user_id: str) -> Optional[Dict[str, Any]]:
        current_time = datetime.now(timezone.utc)  # 변수
        pass
```

### JavaScript / TypeScript

| 구분 | 규칙 | 예시 |
|------|------|------|
| 변수명 | camelCase | `userId`, `createdAt` |
| 함수명 | camelCase | `getUser()`, `formatDate()` |
| 클래스명 | PascalCase | `UserMapper`, `DashboardService` |
| 상수 | UPPER_SNAKE_CASE | `API_BASE_URL`, `MAX_ITEMS` |
| 인터페이스 | PascalCase | `UserInterface`, `ApiResponse` |
| 타입 별칭 | PascalCase | `UserType`, `Nullable` |

```javascript
const API_BASE_URL = 'https://api.example.com';  // 상수

class UserService {  // 클래스
    getUserById(userId) {  // 메서드, 변수
        return fetch(`${API_BASE_URL}/users/${userId}`);
    }
}
```

---

## 3. 데이터베이스

> 자세한 DB 명명 규칙은 [database-naming-standard.md](database-naming-standard.md) 참조

| 구분 | 권장 규칙 | 예시 |
|------|----------|------|
| 테이블명 | 프로젝트 표준 (대문자/소문자 일관성) | `TB_USER`, `users` |
| 컬럼명 | snake_case | `user_id`, `created_at` |
| 인덱스명 | 프로젝트 표준 | `IDX_USER_EMAIL` |

---

## 4. JSON / API

### 키 명명 규칙

| 상황 | 권장 규칙 | 예시 |
|------|----------|------|
| API 요청/응답 | snake_case (권장) | `{ "user_id": "abc" }` |
| 프론트엔드 전용 | camelCase 가능 | `{ "userId": "abc" }` |
| 외부 API 연동 | 해당 API 명세 따름 | - |

### 일관성 원칙
- **백엔드 ↔ 프론트엔드**: 프로젝트 표준에 따른 일관된 규칙 적용
- **DB ↔ JSON**: 필요 시 매퍼/직렬화 계층에서 변환

---

## 5. 파일/폴더명

| 구분 | 규칙 | 예시 |
|------|------|------|
| 파이썬 파일 | snake_case | `user_mapper.py`, `datetime_utils.py` |
| 자바스크립트 파일 | camelCase 또는 kebab-case | `userService.js`, `user-service.js` |
| 컴포넌트 파일 | PascalCase | `UserCard.tsx`, `Dashboard.vue` |
| 폴명 | kebab-case 또는 snake_case | `user-management/`, `user_management/` |
| 테스트 파일 | 원본명 + `_test` 또는 `.test.` | `user_mapper_test.py`, `userService.test.js` |

---

## 6. 약어 사용 규칙

### 일반적인 약어 (Common Abbreviations)

| 원문 | 약어 | 사용처 |
|------|------|--------|
| identifier | `id` | 범용 |
| password | `pwd` 또는 `password` | 범용 |
| timestamp | `ts` | 시간 관련 |
| number | `num` 또는 `no` | 순서/번호 |
| configuration | `config` | 설정 관련 |
| application | `app` | 앱 관련 |
| database | `db` | DB 관련 |
| api | `api` | API 관련 |

### 약어 사용 원칙
1. **일관성**: 프로젝트 내에서 동일한 약어 사용
2. **명확성**: 모호한 약어는 피하기 (`usr` 대신 `user`)
3. **문서화**: 프로젝트별 약어 사전 작성 권장

---

## 7. 금지 사항

| 항목 | 금지 예시 | 권장 |
|------|----------|------|
| 한글 변수명 | `사용자이름` | `user_name` |
| 특수문자 | `user@name`, `user-name` (변수) | `user_name` |
| 숫자 시작 | `1st_user` | `first_user`, `user_1` |
| 예약어 | `class`, `def`, `if` | `user_class`, `class_name` |
| 모호한 이름 | `data`, `info`, `tmp` | `user_data`, `user_info` |

---

## 8. 프로젝트별 설정

프로젝트 시작 시 아래 사항을 문서화하세요:

- [ ] 주요 Case Style 선택 (snake_case vs camelCase)
- [ ] DB 테이블명 규칙 (접두사 사용 여부)
- [ ] JSON 키 규칙
- [ ] 프로젝트별 약어 사전

---

## 9. 관련 문서

- [database-naming-standard.md](database-naming-standard.md) - DB 테이블/컬럼 명명 규칙
- [time-handling-rules.md](time-handling-rules.md) - 시간/날짜 처리 규칙

---

> 📌 이 문서는 공통 표준입니다. 프로젝트별 특화 내용은 해당 프로젝트 문서에 추가하세요.
