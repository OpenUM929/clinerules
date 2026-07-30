# 기본 시간 처리 규칙

## DB 저장 규칙

- KST (UTC+9) 기준
- `TIMESTAMP WITHOUT TIME ZONE`

## DAO SQL 조회 (필수)

```sql
-- ✅ 올바름
SELECT TO_CHAR(created_at, 'YYYY-MM-DD HH24:MI:SS') as created_at
FROM TB_TABLE;

-- ❌ 금지
SELECT created_at FROM TB_TABLE;
```

## Python

- 생성: `utils.datetime_utils.get_kst_now()`
- 금지: `datetime.now()`, `datetime.utcnow()`

## JavaScript (static/js/modules/common/dateUtils.js)

- 생성: `getKSTNow()`
- 표시: `formatDBDateTime()`
- 금지: `new Date()`, `Date.now()`
