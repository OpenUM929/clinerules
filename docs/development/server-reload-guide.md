# 소스 수정 시 서버 재시작 vs F5 판단 가이드

## 적용 대상
`wordcloud_project` Flask 개발 서버 — `web/app.py`의
`app.run(debug=FLASK_DEBUG, use_reloader=False, ...)`.

## 핵심 팩트 (실제 설정, 추측 금지)
- `FLASK_DEBUG` 기본 `True` (`src/config/settings.py:47`).
- **`use_reloader=False`** → Werkzeug 자동 리로더 꺼짐. `.py` 코드 변경이 자동 반영되지 않음.
- Jinja `TEMPLATES_AUTO_RELOAD` = `app.debug` → 기본 `True` →
  서버사이드 렌더 템플릿(`render_template`, `{{ }}` 포함)은 요청마다 재로딩.

## 판단 매트릭스
| 수정 대상 | 예시 | 재시작 | 브라우저 |
|------|--------|---------|----------|
| Python 백엔드 | `src/routes/*.py`, `src/services/*.py`, `src/config/*.py` | **무조건 필요** (reloader off) | F5만으론 구형 유지 |
| Blueprint/import-time | `web/app.py` register_blueprint | **필요** | — |
| 설정/환경 | `.env`, config 상수 | **필요** | — |
| 설치 패키지 | `pip install` (requirements 변경) | **필요** (venv 재기동) | — |
| 서버사이드 템플릿 | `web/templates/*.html` (`{{ }}` 포함) | **불필요** (debug Auto-Reload) | **F5** |
| 정적 자산 | `static/**`, JS/CSS | **불필요** | **F5** (보류 시 Ctrl+Shift+R) |

## 완료 보고 의무 (AI 행동 규칙)
소스 수정 작업 종료 시, **반드시 "재시작 필요 / F5로 충분"을 명시**해
사용자에게 안내한다. 다중 파일 혼합 시 대상별로 구분 안내.

## 예외/주의
- `.py` 수정 후 F5만 누르면 서버는 기존 적재 코드로 응답 → 변경 미반영(최빈실수).
- 템플릿 자동 리로드는 `FLASK_DEBUG=true`일 때만. `.env`에서 `false`로 기동 시 템플릿도 재시작 필요.
- 정적 파일은 브라우저 캐시로 가끔 하드 리로드(Ctrl+Shift+R) 필요.
