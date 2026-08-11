# 설정값 참조표

## .env 설정 항목

| 변수명 | 설명 | 기본값 | 예시 |
|--------|------|--------|------|
| DB_HOST | DB 서버 주소 | localhost | 100.1.28.73 |
| DB_NAME | DB 이름 | - | etl_db_dev |
| DB_USER | DB 사용자 | - | etl_user |
| DB_PASSWORD | DB 비밀번호 | - | [비밀번호] |
| DB_PORT | DB 포트 | 5432 | 5432 |
| FLASK_HOST | 서버 바인드 주소 | 0.0.0.0 | 0.0.0.0 |
| FLASK_PORT | 서버 포트 | 18080 | 18080 |
| FLASK_DEBUG | 디버그 모드 | False | False |
| ADMIN_SESSION_LIFETIME_DAYS | 관리자 세션 유지 일수 | 7 | 7 |
| DEFAULT_SESSION_LIFETIME_MINUTES | 일반 사용자 세션 유지 분 | 20 | 20 |
| MAIL_SERVER | 메일 서버 주소 | - | 100.1.28.73 |
| MAIL_PORT | 메일 서버 포트 | 25 | 25 |

## 사용자 상태 코드

| 상태 | 설명 |
|------|------|
| PENDING | 가입 신청 대기 |
| APPROVED | 승인 완료 |
| DORMANT | 휴면 |
| INACTIVE | 비활성 |
| PENDING_RESET | 비밀번호 초기화 대기 |

---

> 메뉴얼 끝
