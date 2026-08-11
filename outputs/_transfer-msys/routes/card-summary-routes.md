# card_summary_routes

**문서 위치**: `.clinerules/docs/msys/routes/card-summary-routes.md`

## 파일
- `D:\dev\msys\routes\card_summary_routes.py` (18줄)

## 역할
카드 요약 페이지 렌더링

## Blueprint
```python
card_summary_bp = Blueprint('card_summary', __name__)
```

## 엔드포인트

| 경로 | 메서드 | 함수 | 설명 |
|------|--------|------|------|
| `/card_summary` | GET | `card_summary_page()` | 카드 요약 페이지 |

## 데코레이터
- `@login_required`: 로그인 필요
- `@log_menu_access`: 메뉴 접근 로그 기록
- `@card_summary_required`: card_summary 권한

## 템플릿
- `card_summary.html`

## 의존성
- Service: `service/card_summary_service.py`

## 연관 문서
- [../services/card-summary-service.md](../services/card-summary-service.md)
- [../templates/card_summary.md](../templates/card_summary.md)
