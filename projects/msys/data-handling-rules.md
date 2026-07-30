# 데이터 시간 처리 규칙

> **시간/날짜 처리 시 반드시 준수해야 할 규칙입니다.**

---

## 타임존 기준

- **표준 시간**: KST (Asia/Seoul, UTC+9)
- 모든 서버 시간, DB 저장, API 응답은 **KST 기준**으로 처리

---

## 날짜/시간 형식

| 용도 | 형식 | 예시 |
|------|------|------|
| 날짜만 | `YYYY-MM-DD` | `2026-04-20` |
| 날짜+시간 | `YYYY-MM-DD HH:mm:ss` | `2026-04-20 14:30:00` |
| ISO 형식 (응답) | `YYYY-MM-DDTHH:mm:SS+09:00` | `2026-04-20T14:30:00+09:00` |

---

## Python (백엔드)

### 유틸리티 모듈

| 모듈 | 제공 함수 |
|------|----------|
| `utils/datetime_utils.py` | `get_kst_now()`, `utc_to_kst()`, `kst_to_utc()` |
| `utils/kst_utils.py` | `get_kst_now()`, `utc_to_kst()`, `format_date()` |

### 사용 예시

```python
from utils.datetime_utils import get_kst_now, utc_to_kst

# 현재 KST 시간
now = get_kst_now()

# UTC → KST 변환
kst_time = utc_to_kst(utc_datetime)

# KST 문자열로 변환
kst_str = utc_to_kst_str(utc_datetime)  # "2026-04-20 14:30:00+09:00"
```

---

## JavaScript (프론트엔드)

### dateUtils.js 사용

```javascript
// 현재 KST 시간
const now = getKSTNow();

// 날짜 형식화
const formatted = formatDate(dateObj);

// UTC → KST
const kst = utcToKST(utcDate);
```

---

## 데이터베이스 (PostgreSQL)

- **저장 형식**: `YYYY-MM-DD HH24:MI:SS` (timezone 포함 가능)
- **쿼리 시**: KST 기준으로 변환하여 저장/조회
- **비교 연산**: 타임존 고려 (`AT TIME ZONE 'Asia/Seoul'` 사용)

---

## JSON 응답

- Flask `CustomJSONEncoder`가 `datetime` 객체를 자동으로 ISO 형식으로 변환
- 형식: `"2026-04-20T14:30:00"` (시간대 포함)

---

## 주의사항

1. **서버 timezone에 의존 금지**: `datetime.now()` 대신 `get_kst_now()` 사용
2. **naive datetime 금지**: 항상 timezone 정보 포함
3. **DB 저장 시**: UTC로 변환 후 저장, 조회 시 KST로 변환
4. **프론트엔드 전달**: 반드시 KST 기준 문자열로 변환 후 전달

---

## 관련 파일

- `utils/datetime_utils.py` - KST 시간 변환 유틸리티
- `utils/kst_utils.py` - KST 포맷팅
- `routes/today_routes.py` - 오늘 날짜 API (`/api/today_date`)
- `static/js/modules/common/dateUtils.js` - 프론트엔드 날짜 처리