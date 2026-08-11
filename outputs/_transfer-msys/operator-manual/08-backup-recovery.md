---
reportTheme: report
---

# 백업 및 복구

> **기준 버전 / 최종 확인일**: v1.1.0 · 2026-07-22

↑ [목록으로](00-index.md)

> 백업·복구를 **Task 기반 시나리오**로 재현한다(작성 지침 `../common/operator-manual/DEVELOPMENT/05-composition-nav.md §1.5`). 각 단계에 실행 명령·확인지점을 명시한다.

---

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

## 운영 시나리오 (Task 기반)

### 일일 백업 점검

- **상황/목표**: 매일 정기 백업(설정·DB)이 정상 생성됐는지 확인한다.
- **단계**:
  1. 전일 백업 파일 존재·크기 확인(`ls -lh backup/`).
  2. `pg_dump` 로그에 오류 없는지 확인(§2.2).
  3. 보관 기간(§1) 초과분 정리.
- **완료 확인**: 당일자 `.env`·`*.sql` 백업 파일이 정상 크기로 존재.

### 배포 실패 → 소스 롤백

- **상황/목표**: 배포 후 서비스 이상 → 직전 백업으로 신속 롤백.
- **단계**:
  1. 서비스 중지(`./kill_data_moni.sh`).
  2. 직전 백업 복원(§3.1).
  3. 서비스 기동(`./start_moni.sh`) → [대시보드](04-common-menus/01-dashboard.md)·[장애 대응 §2.1](07-troubleshooting.md) 절차로 정상 확인.
- **완료 확인**: 대시보드 정상 표시 + 수집 재개. **미복구 시** DB 복구(§3.2) 병행.

---

↑ [목록으로](00-index.md) · [← 이전: 장애 대응](07-troubleshooting.md)
