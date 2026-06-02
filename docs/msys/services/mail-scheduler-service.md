# Mail Scheduler Service (mail_scheduler_service.py)

## 파일 위치

`service/mail_scheduler_service.py` (395줄)

## 역할

API 키 만료 알림 메일 스케줄링 - 만료 30일 전부터，每日 발송

## 주요 함수

| 함수 | 기능 |
|------|------|
| `check_and_send_scheduled_mails(target_cds, exclude_cds)` | 스케줄 기반 메일 발송 |
| `_check_and_send_mail_for_cd(cd, today)` | 개별 CD 메일 발송 |
| `send_manual_mail(cd)` | 수동 메일 발송 |
| `get_mail_history(cd)` | 발송 이력 조회 |

## 발송 규칙

| 만료 전 기간 | 발송 규칙 |
|--------------|----------|
| 30일 전 | 1회만 발송 |
| 29~8일 전 | 발송 안 함 |
| 7일 전 ~ 1일 전 | 매일 발송 |
| 당일 (0일) | 1회만 발송 |
| 당일 이후 | 발송 안 함 |

## 의존성

- `dao/api_key_mngr_dao.py` - API 키 DAO
- `service/api_key_mngr_service.py` - API 키 서비스
- `msys/mail_send.py` - 메일 발송

## 관련 문서

- [services/README.md](README.md) - services 개요
- [services/api-key-mngr-service.md](api-key-mngr-service.md) - API 키 서비스