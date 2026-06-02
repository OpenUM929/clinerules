# Card Summary API (card_summary_api.py)

## 파일 위치

`routes/api/card_summary_api.py` (20줄)

## 역할

카드 요약 REST API - 카드 데이터 조회

## 주요 엔드포인트

| 엔드포인트 | 메서드 | 기능 |
|------------|--------|------|
| `/api/card_summary` | GET | 카드 요약 데이터 조회 |

## 권한

- `login_required` - 로그인 필수
- `card_summary_required` - card_summary 권한

## 의존성

- `service/card_summary_service.py` - 카드 요약 서비스

## 관련 문서

- [routes/README.md](README.md) - routes 개요
- [routes/card-summary-routes.md](card-summary-routes.md) - 카드 요약 라우트
- [services/card-summary-service.md](../services/card-summary-service.md) - 카드 요약 서비스