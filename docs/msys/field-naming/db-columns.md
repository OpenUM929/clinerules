# DB 컬럼명 기준

## 1. DB 컬럼명 기준

- **기준**: `information_schema.columns` 또는 DDL 정의의 컬럼명
- **형식**: 대문자 + 언더스코어 (예: `START_DT`, `HIDE_OPT_YN`)
- **변환**: Frontend/Backend에서는 소문자로 사용 (예: `start_dt`, `hide_opt_yn`)

## 2. 계층별 적용

| 계층 | 명명 규칙 | 예시 |
|------|----------|------|
| **Database** | 대문자 스네이크 | `TITL`, `CONT`, `START_DT` |
| **Backend (Python)** | 소문자 스네이크 | `titl`, `cont`, `start_dt` |
| **Frontend (JS)** | 소문자 스네이크 | `titl`, `cont`, `start_dt` |
| **FormData** | 소문자 스네이크 | `titl`, `cont`, `start_dt` |
| **JSON** | 소문자 스네이크 | `titl`, `cont`, `start_dt` |
