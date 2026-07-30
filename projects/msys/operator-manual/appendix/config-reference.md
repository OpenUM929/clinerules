# 설정값 참조표

## .env 설정 항목

> 🔒 **값 표기 원칙**: 비밀번호·마스터 패스워드·API 키의 **실제 값은 본 메뉴얼에 적지 않습니다.** 아래 표에는 **변수 이름과 용도만** 적고, 값 자리는 `<설정값>` 으로 둡니다. 실제 값은 운영 서버의 `.env` 파일에만 두고, 인수인계 시 별도 경로로 전달하십시오.
> 아래 목록은 프로젝트 소스(`config`·`msys_app.py`·`routes`·`service`·`msys`·`utils`)에서 `os.getenv` / `os.environ.get` 로 읽는 변수명을 직접 추출해 만든 것입니다(2026-07-29, 총 26개).

### 접속·기동

| 변수명 | 설명 | 기본값 | 값 |
|--------|------|--------|------|
| `DB_HOST` | DB 서버 주소 | localhost | 운영 서버 설정값 참조 |
| `DB_NAME` | DB 이름 | - | `etl_db_dev` (개발) |
| `DB_USER` | DB 사용자 | - | `etl_user` |
| `DB_PASSWORD` | DB 비밀번호 | - | `<설정값>` 🔒 |
| `DB_PORT` | DB 포트 | 5432 | 5432 |
| `FLASK_HOST` | 서버 바인드 주소 | 0.0.0.0 | 0.0.0.0 |
| `FLASK_PORT` | 서버 포트 | 18080 | 18080 |
| `FLASK_DEBUG` | 디버그 모드 | False | 운영은 반드시 False |
| `FLASK_SECRET_KEY` | 세션 서명 키 | - | `<설정값>` 🔒 |
| `BASE_URL` | 메일 본문 등에 쓰이는 시스템 기본 주소 | - | 운영 서버 주소 |
| `LOG_DIR` | 로그 파일 경로 | - | `/data/external_data_monitoring/log/` |

### 세션·계정

| 변수명 | 설명 | 기본값 | 값 |
|--------|------|--------|------|
| `ADMIN_SESSION_LIFETIME_DAYS` | 관리자 세션 유지 일수 | 7 | 7 |
| `DEFAULT_SESSION_LIFETIME_MINUTES` | 일반 사용자 세션 유지 분 | 20 | 20 |
| `ADMIN_USER_ID` | 초기 관리자 계정 ID | - | `<설정값>` |
| `ADMIN_USER_PASSWORD` | 초기 관리자 계정 비밀번호 | - | `<설정값>` 🔒 |
| `MASTER_PASSWORD` | 마스터 패스워드 | - | `<설정값>` 🔒 |
| `TEST_USER_ID` | 시험 계정 ID | - | `<설정값>` |
| `TEST_USER_PASSWORD` | 시험 계정 비밀번호 | - | `<설정값>` 🔒 |

### 메일·외부 연동

| 변수명 | 설명 | 기본값 | 값 |
|--------|------|--------|------|
| `MAIL_SERVER` | 메일(SMTP) 서버 주소 | - | 사내 메일 릴레이 |
| `MAIL_PORT` | 메일 서버 포트 | 25 | 25 |
| `MAIL_USE_TLS` | TLS 사용 여부 | - | 운영 설정 확인 |
| `MAIL_USERNAME` | SMTP 인증 계정 | - | `<설정값>` |
| `MAIL_PASSWORD` | SMTP 인증 비밀번호 | - | `<설정값>` 🔒 |
| `MAIL_SENDER` | 발신자 주소 | - | 운영 설정 확인 |
| `CONTACT_INFO` | 안내 메일에 넣는 담당자 연락처 | - | 운영 설정 확인 |
| `GEMINI_API_KEY` | 데이터 명세서 자동 채우기용 외부 API 키 | - | `<설정값>` 🔒 |

> 🔒 표시 항목은 **유출 시 즉시 교체**가 필요한 값입니다. 화면 캡처·메일·메신저에 붙여 넣지 마십시오.

## 사용자 상태 코드

| 상태 | 설명 |
|------|------|
| PENDING | 가입 신청 대기 |
| APPROVED | 승인 완료 |
| DORMANT | 휴면 |
| INACTIVE | 비활성 |
| PENDING_RESET | 비밀번호 초기화 대기 |

---

> ↑ [목록으로](../README.md) · [← 이전: 부록 · 명령어 모음](command-cheatsheet.md)
