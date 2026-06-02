# Card Summary Service (card_summary_service.py)

## 파일 위치

`service/card_summary_service.py` (89줄)

## 역할

카드 요약 - 오늘의 Job 상태 요약 데이터

## 주요 함수

| 함수 | 기능 |
|------|------|
| `get_card_summary(user)` | 오늘의 Job 상태 요약 |

## 데이터 흐름

1. `collection_schedule_service.get_schedule_only()` - 오늘 스케줄 조회
2. 권한 필터링 (data_permissions)
3. 상태별 분류 (성공, 실패, 경고, 미실행)
4. 카드 형식으로 반환

## 의존성

- `service/dashboard_service.py` - 대시보드 서비스
- `service/collection_schedule_service.py` - 수집 일정 서비스

## 관련 문서

- [services/README.md](README.md) - services 개요
- [routes/card-summary-routes.md](../routes/card-summary-routes.md) - 카드 요약 라우트