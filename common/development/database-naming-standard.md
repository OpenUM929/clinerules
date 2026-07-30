# 데이터베이스 명명 표준 (Database Naming Standard)

> ✅ **모든 DDL / 테이블 / 컬럼 작업시 가장 먼저 참조**
> ✅ 이 문서의 규칙은 절대적이다. 예외 없이 100% 준수
> ✅ 00-core.md 작업 유형 분류표에 등록됨

---

## 1. 기본 원칙
✅ 모든 이름은 전체 대문자만 사용한다. 소문자 절대 금지
✅ 언더스코어(`_`)만 구분자로 사용
✅ 표준 약어만 사용. 풀네임 절대 금지
✅ 모든 프로젝트, 모든 테이블 일관성 유지

---

## 2. 표준 약어 사전 (MANDATORY)

| 원문 | 표준 약어 | 비고 |
|------|----------|------|
| status | sts | |
| code | cd | |
| master | mst | |
| date | dt | |
| name | nm | |
| description | desc | |
| order | ord | |
| color | colr | |
| use | use | |
| register / create | reg | |
| update | upd | |
| delete | del | |
| history | hist | |
| log | log | |
| schedule | schd | |
| setting | sett | |

---

## 3. 테이블 명명 규칙
```
TB_ + [도메인] + _ + [유형]
```
✅ 예시(**중립 예시 — 등록 프로젝트에 실재하지 않는 이름을 쓴다**, [`../core/21-project-isolation.md`](../core/21-project-isolation.md) ISO-7):
- `TB_CODE_MST` 코드 마스터
- `TB_ITEM_MST` 항목 마스터
- `TB_JOB_HIST` 작업 이력

---

## 4. 컬럼 명명 규칙
✅ 기본 컬럼 표준:
| 컬럼명 | 타입 | 기본값 | 설명 |
|--------|------|--------|------|
| CD | VARCHAR | | 기본키 코드 |
| NM | VARCHAR | | 이름 |
| DESC | VARCHAR | | 설명 |
| ORD | INT | 999 | 표시순서 |
| COLR | VARCHAR(7) | | 색상코드 |
| USE_YN | CHAR(1) | 'Y' | 사용여부 |
| REG_DT | DATETIME | CURRENT_TIMESTAMP | 등록일 |
| UPD_DT | DATETIME | CURRENT_TIMESTAMP | 수정일 |
| DEL_YN | CHAR(1) | 'N' | 삭제여부 |

---

## 5. 인덱스 명명 규칙
```
IDX_ + [테이블명] + _ + [컬럼명]
```
✅ 예시(중립 예시):
- `IDX_TB_CODE_MST_USE`
- `IDX_TB_CODE_MST_ORD`

---

## 6. 관련 문서
✅ 모든 DDL/SQL 작업시 반드시 아래 문서도 함께 읽으시오:
- `common/development/sql-error-prevention-guide.md`

## 7. 위반시 조치
- 이 규칙을 위반한 모든 코드는 무조건 리젝
- 재작성 요청
- 규칙 준수 확인후 진행

---

> 📌 이 문서는 영구 지침이다. 절대 변경 금지
