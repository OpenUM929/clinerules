# Collection Schedule Service (collection_schedule_service.py)

## 파일 위치

`service/collection_schedule_service.py` (200줄)

## 역할

데이터 수집 일정 - cron 기반 스케줄 생성, 히스토리 매칭, 상태 계산

## 주요 함수

| 함수 | 기능 |
|------|------|
| `get_schedule_only(start_date, end_date, user)` | 스케줄 데이터 조회 |
| `get_schedule_and_history(start_date, end_date, user)` | 스케줄 + 이력 데이터 |
| `_generate_scheduled_tasks(start_date, end_date, job_ids)` | cron 기반 스케줄 생성 |
| `_fetch_and_group_history_data(start_date, end_date, job_ids, user)` | 이력 데이터 조회 |
| `_match_schedule_with_history(scheduled_tasks, history_by_date_job)` | 스케줄-이력 매칭 |

## 데이터 구조

### 그룹 계층

| 구분 | 예시 | 설명 |
|------|------|------|
| 상위 그룹 | CD100 | job_id 100단위 (CD1xx 전체) |
| 하위 그룹 | CD101, CD102, CD103 | 개별 job_id |

### 스케줄 객체 (Cron 반복 적용)

- Cron 기반으로 스케줄 생성 시, 같은 job_id도 **반복 횟수만큼 별도 객체**로 생성
- 예: job_id=CD101, repeat=2 → CD101 객체 2개 생성

### Jobs 수 계산 (중요)

- **Jobs 수 = 하위 그룹 수 = 고유 job_id 수**
- `array.length` 사용 시 Chron 반복 횟수 포함됨
- 올바른 방법: `new Set(array.map(i => i.job_id)).size`

## 데이터 흐름

1. `_get_allowed_job_ids_for_schedule()` - 사용자 권한별 Job 필터링
2. `_generate_scheduled_tasks()` - cron 표현식으로 스케줄 생성
3. `_fetch_and_group_history_data()` - TB_CON_HIST에서 이력 조회
4. `_match_schedule_with_history()` - 상태 계산 (성공/실패/대기/미실행)

## 의존성

- `mapper/mst_mapper.py` - 마스터 데이터 매퍼
- `mapper/user_mapper.py` - 사용자 매퍼
- `mapper/dashboard_mapper.py` - 대시보드 매퍼

## 관련 문서

- [services/README.md](README.md) - services 개요
- [routes/collection-schedule-routes.md](../routes/collection-schedule-routes.md) - 수집 일정 라우트