# 검증 체크리스트

> 시간 문제 디버깅 및 검증 체크리스트

## 시간 문제 디버깅 체크리스트

### 1. 저장 단계 검증

- [ ] Backend에서 `get_kst_now()`로 생성했는가?
- [ ] DB에 `YYYY-MM-DD HH:mm:ss` 형식으로 저장되었는가?
- [ ] `TIMESTAMP WITHOUT TIME ZONE` 타입을 사용했는가?

### 2. 조회 단계 검증

- [ ] DAO SQL에서 TO_CHAR로 변환했는가?
- [ ] API 응답이 문자열 형식인가? (`2026-04-16 15:30:00`)
- [ ] datetime 객체가 jsonify에 직접 전달되지 않았는가?

### 3. 표시 단계 검증

- [ ] Frontend에서 `formatDBDateTime()`을 사용했는가?
- [ ] `new Date()`로 시간을 생성/파싱하지 않았는가?
- [ ] 표시된 시간이 `YY.MM.DD HH:mm` 형식인가?

## SQL 검증 쿼리

### 저장된 시간 확인

```sql
-- 저장된 시간이 KST인지 확인
SELECT 
    created_at,
    TO_CHAR(created_at, 'YYYY-MM-DD HH24:MI:SS') as formatted
FROM TB_MEMO 
WHERE id = {memo_id};
-- 결과: "2026-04-16 15:30:00" (KST 기준)
```

### 시간대 변환 테스트

```sql
-- 현재 DB 서버 시간 확인 (KST 기준)
SELECT TO_CHAR(CURRENT_TIMESTAMP, 'YYYY-MM-DD HH24:MI:SS') as now;
SELECT TO_CHAR(NOW(), 'YYYY-MM-DD HH24:MI:SS') as now;
```

## Python 검증 코드

```python
from utils.datetime_utils import get_kst_now

# KST 시간 생성 검증
kst_now = get_kst_now()
print(f"KST Now: {kst_now.strftime('%Y-%m-%d %H:%M:%S')}")

# DB 저장 후 검증
def verify_memo_time(memo_id):
    query = """
        SELECT TO_CHAR(created_at, 'YYYY-MM-DD HH24:MI:SS') as created_at
        FROM TB_MEMO WHERE id = :memo_id
    """
    result = db.execute(query, {'memo_id': memo_id}).fetchone()
    print(f"DB Stored Time: {result['created_at']}")
    return result['created_at']
```

## JavaScript 검증 코드

```javascript
import { formatDBDateTime, getKSTNow } from '../modules/common/dateUtils.js';

// DB 시간 표시 검증
function verifyDBTime(dbDateTime) {
    console.log('DB Time:', dbDateTime);  // "2026-04-16 15:30:00"
    console.log('Formatted:', formatDBDateTime(dbDateTime));  // "26.04.16 15:30"
    return formatDBDateTime(dbDateTime);
}

// 현재 KST 시간 생성 검증
function verifyKSTNow() {
    const kstNow = getKSTNow();
    console.log('KST Now:', kstNow);  // Date 객체 (KST 기준)
    return kstNow;
}
```
