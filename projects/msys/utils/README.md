# Utils (공통 유틸리티)

**문서 위치**: `.clinerules/projects/msys/utils/README.md`

## 파일 위치

`D:\dev\msys\utils/`

## 역할

모든 계층에서 공유하는 횡단 관심사(인증/권한, 시간/KST, 로깅, SQL 로드, 작업/모니터링) 처리

## 계층 구조

```
요청 → auth_middleware(인증/권한) → routes → service → dao → mapper → db
                                  ↑ datetime_utils/kst_utils 로 시간 처리
```

## 파일 목록

| 파일 | 역할 | 주요 export |
|------|------|------------|
| `auth_middleware.py` | 인증/권한 검증 미들웨어 (login_required 등 데코레이터) | `login_required`, `admin_required` 등 |
| `datetime_utils.py` | KST 시간 변환/계산 | `to_kst()`, `to_utc()` |
| `kst_utils.py` | KST 포맷팅 유틸 | `format_kst()` |
| `sql_loader.py` | `sql/` 디렉토리의 `.sql` 파일 로드 | `load_sql()` |
| `logging_config.py` | 로깅 설정 | `setup_logging()` |
| `job_utils.py` | 수집 Job 유틸리티 | `run_job()` |
| `cpu_monitor.py` | CPU 모니터링 | `get_cpu_usage()` |

## 관련 문서

- [../README.md](../README.md) - 프로젝트 개요
- [../file-structure.md](../file-structure.md) - 파일 구조
- [../data-handling/timezone.md](../data-handling/timezone.md) - KST 처리 규칙 (공통)
