# 시간/날짜 처리 규칙 (Time Handling Rules)

> **모든 프로젝트에서 시간/날짜 처리 시 준수해야 할 공통 규칙입니다.**

---

## 1. 타임존 기준

- **프로젝트 표준 시간대 지정 필수** (예: KST, UTC, EST 등)
- 모든 서버 시간, DB 저장, API 응답은 **동일한 시간대 기준**으로 처리
- 문서화: 프로젝트 `README.md` 또는 별도 설정 파일에 표준 시간대 명시

---

## 2. 날짜/시간 형식

### 표준 형식

| 용도 | 형식 | 예시 |
|------|------|------|
| 날짜만 | `YYYY-MM-DD` | `2026-04-20` |
| 날짜+시간 | `YYYY-MM-DD HH:mm:ss` | `2026-04-20 14:30:00` |
| ISO 8601 | `YYYY-MM-DDTHH:mm:ss±HH:mm` | `2026-04-20T14:30:00+09:00` |
| UTC | `YYYY-MM-DDTHH:mm:ssZ` | `2026-04-20T05:30:00Z` |

### 권장사항
- API 응답: **ISO 8601 형식** 사용 권장
- DB 저장: 타임존 정보 포함 권장 (PostgreSQL: `TIMESTAMP WITH TIME ZONE`)

---

## 3. 언어별 처리 방식

### Python

```python
from datetime import datetime, timezone

# 표준 시간대 지정 (예시: KST)
KST = timezone(timedelta(hours=9))

# 현재 시간 (표준 시간대 포함)
now = datetime.now(KST)

# UTC 변환
utc_time = now.astimezone(timezone.utc)

# ISO 형식 문자열
iso_str = now.isoformat()  # "2026-04-20T14:30:00+09:00"
```

### JavaScript/TypeScript

```javascript
// 현재 시간 (로컬)
const now = new Date();

// ISO 형식
const isoStr = now.toISOString();  // "2026-04-20T05:30:00.000Z" (UTC)

// 로컬 시간 문자열
const localStr = now.toLocaleString('ko-KR', { timeZone: 'Asia/Seoul' });
```

---

## 4. 데이터베이스

### 저장 형식

| DBMS | 권장 타입 | 설명 |
|------|----------|------|
| PostgreSQL | `TIMESTAMP WITH TIME ZONE` | 타임존 정보 포함 |
| MySQL | `DATETIME` 또는 `TIMESTAMP` | `TIMESTAMP`는 UTC로 자동 변환 |
| SQLite | `TEXT` (ISO 8601) | `"2026-04-20T14:30:00+09:00"` |

### 쿼리 시 주의사항
- 시간대 변환 함수 사용: PostgreSQL (`AT TIME ZONE`), MySQL (`CONVERT_TZ`)
- 저장 시에는 UTC 권장, 조회 시 표준 시간대로 변환

---

## 5. 주의사항

1. **서버 타임존 의존 금지**
   - `datetime.now()` 대신 `datetime.now(timezone)` 사용
   - 서버 환경 설정에 관계없이 일관된 시간 처리

2. **Naive Datetime 금지**
   - 항상 timezone 정보 포함 (aware datetime)
   - Python: `pytz` 또는 `zoneinfo` (Python 3.9+) 사용

3. **DB 저장 시**
   - UTC로 변환 후 저장 권장
   - 조회 시 표준 시간대로 변환하여 표시

4. **API 응답 시**
   - ISO 8601 형식 문자열로 변환 후 전달
   - 타임존 오프셋 포함 (`+09:00` 등)

5. **프론트엔드 표시 시**
   - 사용자 로컬 시간대로 변환하여 표시
   - Intl API 사용 권장

---

## 6. 프로젝트별 설정

프로젝트 시작 시 아래 사항을 문서화하세요:

- [ ] 표준 시간대 지정 (예: KST, UTC)
- [ ] DB 시간 타입 선택
- [ ] API 응답 형식 (ISO 8601 권장)
- [ ] 유틸리티 모듈 경로 (프로젝트별 설정)

---

## 7. 관련 문서

- [field-naming-convention.md](field-naming-convention.md) - 필드명 및 변수명 규칙
- [database-naming-standard.md](database-naming-standard.md) - DB 테이블/컬럼 명명 규칙

---

> 📌 이 문서는 공통 표준입니다. 프로젝트별 특화 내용은 해당 프로젝트 문서에 추가하세요.
