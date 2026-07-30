# 백업 및 복구

## 백업 전략

| 대상 | 주기 | 방법 | 보관 기간 |
|------|------|------|----------|
| 소스 코드 | 배포 시 | ZIP 백업 | 최근 5개 |
| 설정 파일 | 매일 | `.env` 복사 | 30일 |
| DB 스키마 | 변경 시 | DDL 저장 | 영구 |
| DB 데이터 | 매일 | pg_dump | 7일 |

## 백업 절차

### 소스 코드 백업

```bash
# 배포 전 백업
cp -r /data/external_data_monitoring/msys /data/external_data_monitoring/msys_backup_$(date +%Y%m%d)
```

### DB 백업

```bash
# 전체 DB 백업
pg_dump -h [DB_HOST] -U [DB_USER] -d [DB_NAME] > backup_$(date +%Y%m%d_%H%M%S).sql

# 특정 테이블 백업
pg_dump -h [DB_HOST] -U [DB_USER] -d [DB_NAME] -t tb_user > tb_user_backup.sql
```

### 설정 백업

```bash
cp /data/external_data_monitoring/msys/.env /data/external_data_monitoring/backup/env_backup_$(date +%Y%m%d)
```

## 복구 절차

### 소스 코드 복구

```bash
# 1. 서비스 중지
./kill_data_moni.sh

# 2. 백업 복원
cp -r /data/external_data_monitoring/msys_backup_YYYYMMDD/* /data/external_data_monitoring/msys/

# 3. 서비스 기동
./start_moni.sh
```

### DB 복구

```bash
# 1. DB 연결
psql -h [DB_HOST] -U [DB_USER] -d [DB_NAME]

# 2. 복원
\i backup_YYYYMMDD_HHMMSS.sql
```

---

> 메뉴얼 끝

---

> ↑ [목록으로](README.md) · [← 이전: 장애 대응](07-troubleshooting.md) · [다음: 부록 · 명령어 모음 →](appendix/command-cheatsheet.md)
