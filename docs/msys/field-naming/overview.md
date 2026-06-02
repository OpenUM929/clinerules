# 필드명 네이밍 규칙

> **원칙: 모든 계층은 DB 테이블 컬럼명과 일치하는 필드명을 사용한다**

## 개요

msys 프로젝트에서 Frontend, Backend, Database 간 데이터 교환 시 **필드명 일관성**을 유지하기 위한 규칙입니다.

## 핵심 원칙

```
Frontend (JS)  ←→  Backend (Python)  ←→  Database (PostgreSQL)
     titl     ←→       titl         ←→      TITL
     cont     ←→       cont         ←→      CONT
   start_dt   ←→     start_dt       ←→    START_DT
```

**모든 계층에서 동일한 명명법 사용** - 변환/매핑 로직 최소화

## 명명 규칙 요약

| 계층 | 명명 규칙 | 예시 |
|------|----------|------|
| **Database** | 대문자 스네이크 | `START_DT`, `HIDE_OPT_YN` |
| **Backend (Python)** | 소문자 스네이크 | `start_dt`, `hide_opt_yn` |
| **Frontend (JS)** | 소문자 스네이크 | `start_dt`, `hide_opt_yn` |
| **FormData** | 소문자 스네이크 | `start_dt`, `hide_opt_yn` |

## 사용 금지

❌ **절대 사용하지 말 것**:
- 풀네임 (예: `title`, `content`, `start_time`) 
- 칵케이스 (예: `startDt`, `hideOptYn`)
- 축약형 변형 (예: `ttl`, `cnt`, `sdt`)

## 관련 문서

- [naming.md](naming.md) - 네이밍 규칙 상세
- [db-columns.md](db-columns.md) - DB 컬럼명 기준
- [formdata.md](formdata.md) - FormData 처리 규칙
