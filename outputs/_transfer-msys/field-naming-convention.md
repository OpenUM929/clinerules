# 필드명 Naming 규칙

> **프로젝트 전체에서 사용할命名 규칙입니다.**

---

## 데이터베이스

### 테이블명

| 규칙 | 예시 |
|------|------|
| 대문자 + 접두사 | `TB_USER`, `TB_CON_MST`, `TB_COL_MAPP` |
| 의미: `TB_{기능}` | `TB_USER` (사용자), `TB_CON_MST` (수집マスター) |

### 컬럼명

| 규칙 | 예시 |
|------|------|
| 소문자 + snake_case | `user_id`, `user_pwd`, `acc_cre_dt` |
| 약어 사용 | `dt` (date), `cd` (code), `sts` (status) |
| 동사 금지 | `acc_cre_dt` (생성일), not `create_date` |

###常见 약어

| 약어 | 원어 |
|------|------|
| `dt` | date, datetime |
| `cd` | code |
| `sts` | status |
| `mngr` | manager |
| `mst` | master |
| `hist` | history |
| `schd` | schedule |
| `clt` | collection |
| `apr` | approve |
| `acc` | account |

---

## JSON 응답 (API)

### 규칙

- **基本原则**: DB와 동일 (snake_case)
- ** camelCase 필요시**: 프론트엔트 요구에 따라 선택적 적용

### 예시

```json
{
  "user_id": "admin",
  "acc_sts": "ACTIVE",
  "acc_cre_dt": "2026-04-20T14:30:00+09:00"
}
```

---

## Python (백엔드)

### 변수명

| 규칙 | 예시 |
|------|------|
| snake_case | `user_id`, `acc_cre_dt` |
| 클래스명 | `UserMapper`, `DashboardService` |
| 함수명 | `get_user()`, `find_by_id()` |

### 타입 힌트

```python
from typing import Dict, List, Any

def find_by_id(self, user_id: str) -> Dict[str, Any]:
    pass
```

---

## JavaScript (프론트엔드)

### 변수명

| 규칙 | 예시 |
|------|------|
| camelCase | `userId`, `accCreDt` |
| 함수명 | `getUser()`, `formatDate()` |

### 예시

```javascript
const userId = data.user_id;
const accCreDt = data.acc_cre_dt;
```

---

## 파일/폴더명

| 구분 | 규칙 | 예시 |
|------|------|------|
| 파이썬 파일 | snake_case | `user_mapper.py`, `datetime_utils.py` |
| 라우트 | snake_case | `auth_routes.py`, `jandi_routes.py` |
| 서비스 | snake_case | `auth_service.py`, `dashboard_service.py` |
| DAO | snake_case | `analytics_dao.py`, `sts_cd_dao.py` |
| SQL 파일 | snake_case | `user_sql.py`, `find_by_id.sql` |
| HTML 템플릿 | snake_case | `login.html`, `dashboard.html` |

---

## 매핑 규칙

### DB → Python

- `UserMapper`가 `convert_to_new_columns()` 통해 변환
- 대소문자 혼용 → snake_case統一

### Python → JSON

- `flask` `jsonify()` 또는 커스텀 인코더가 자동 처리
- `datetime` → ISO 형식 문자열

---

## 주의사항

1. **새 컬럼 추가 시**: 기존 명명 패턴 준수
2. **약어 사용**: 프로젝트 내 기존 약어 우선
3. **외부 API**: 명세에 따름 (변경 불가)

---

## 관련 파일

- `mapper/` - DB 쿼리 매퍼
- `service/` - 비즈니스 로직
- `dao/` - Data Access Object
- `routes/` - FlaskBlueprint 라우트
- `msys/column_mapper.py` - 컬럼명 변환
- `DDL/` - 테이블 정의