# Collection Schedule Routes (collection_schedule_routes.py)

## 파일 위치

`routes/ui/collection_schedule_routes.py` (223줄)

## 역할

데이터 수집 일정 - 스케줄 조회, 그룹 메모 (메모장) 관리

## 주요 엔드포인트

### 페이지 렌더링

| 엔드포인트 | 메서드 | 템플릿 | 기능 |
|------------|--------|--------|------|
| `/collection_schedule` | GET | collection_schedule.html | 수집 일정 페이지 |

### REST API

| 엔드포인트 | 메서드 | 기능 |
|------------|--------|------|
| `/api/collection_schedule` | GET | 일정 + 이력 데이터 조회 |
| `/api/group-memo` | GET | 그룹 메모 조회 |
| `/api/group-memo` | POST | 그룹 메모 생성 (관리자) |
| `/api/group-memo` | PUT | 그룹 메모 수정 (관리자) |
| `/api/group-memo` | DELETE | 그룹 메모 삭제 (관리자) |
| `/api/memos-batch` | GET | 배치 메모 조회 |

## 그룹 메모 (메모장) 기본 내용

메모장 생성 시 기본 내용:
- **빈 내용으로 시작** (사용자가 직접 입력)
- `TB_GRP_MEMO` 테이블에 저장
- 필드: `grp_id`, `depth`, `memo_date`, `content`, `writer_id`

## 권한

- `login_required` - 로그인 필수
- `collection_schedule_required` - collection_schedule 권한

## 의존성

- `service/collection_schedule_service.py` - 일정 서비스
- `mapper/grp_memo_mapper.py` - 그룹 메모 매퍼
- `dao/analytics_dao.py` - 분석 DAO

## 관련 문서

- [routes/README.md](README.md) - routes 개요
- [services/collection-schedule-service.md](../services/collection-schedule-service.md) - 수집 일정 서비스
- [templates/screen-domain.md](../templates/screen-domain.md) - 화면-템플릿 매핑