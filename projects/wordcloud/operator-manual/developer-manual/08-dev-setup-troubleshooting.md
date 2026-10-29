---
reportTheme: technical
---

# 개발 환경·테스트·트러블슈팅

↑ [목록으로](00-index.md)

> **핵심**: Python 3.10 + Flask, 로컬 실행은 `python -m web.app`. 모델(`model/`)은 `wordcloud_project`의 형제 폴더에 둔다. **서버는 사용자 허락 없이 실행하지 않는다**(안내만).
> **기준 버전 / 최종 확인일**: v1.1.0 · 2026-07-22 (commit `7b106b5`)
> 최종 개정 2026-10-29 (당일 제1차) — rev-261029-01

---

## 런타임·의존성

| 항목 | 값 | 근거 |
|------|-----|------|
| Python | 3.10 (`.pyc` cpython-310 확인) | `pyproject.toml`, `__pycache__/*.cpython-310` |
| 웹 | Flask (블루프린트 12개) | `web/app.py` |
| ML | `torch`, `transformers`, `accelerate` 등 | `requirements.txt` |
| 형태소 | Kiwi / Okt | `src/modules/nlp_analysis.py` |
| 의존성 설치 | `pip install -r requirements.txt` (오프라인은 `vendor_python_pkgs/`) | `requirements.txt` |

- 모델 디렉터리(둘 다 `wordcloud_project`의 형제 `model/` 아래):
  - 베이스 KoTE: `../../model/kote_for_easygoing_people`(`settings.py:20`)
  - HR 파인튜닝: `../../model/hr_sentiment_finetuned`(`settings.py:26`)

---

## 로컬 구동 (안내 — 직접 실행 금지)

> ⚠️ **서버 무단 실행 금지.** 아래는 개발자가 **직접** 실행할 절차 안내이며, 문서 저자(AI)는 서버를 띄우지 않는다. 실행이 필요하면 사용자에게 `! python -m web.app` 형태로 요청한다. [[feedback_no_server_start]]

```
# (1) 가상환경·의존성
python -m venv venv && venv\Scripts\activate
pip install -r requirements.txt
# (2) 실행 (기본 127.0.0.1:5001)
python -m web.app
```

주요 환경변수(`src/config/settings.py`):

| 변수 | 기본 | 의미 |
|------|------|------|
| `FLASK_HOST` / `FLASK_PORT` | `127.0.0.1` / `5001` | 바인드(`:48-49`) |
| `FLASK_DEBUG` | `True` | 디버그(`:47`) |
| `USE_HR_SENTIMENT_MODEL` | `1`(on) | HR 파인튜닝 모델 사용(`:27`) |
| `SECRET_KEY` | (없음 — 기동마다 무작위 생성) | 세션 서명 키. 지정 불필요, 재시작하면 관리자 로그인이 풀린다(`:59`) |
| `ADMIN_PASSWORD` | `admin1234` | 가명 매핑 암호키(원래 배포본과 같은 코드 기본값) — 내부망 매핑이 이 값으로 암호화돼 있으므로 **바꾸지 않는다**. 환경변수가 남아 있으면 매핑을 실제로 여는 값을 자동 선택(`:64-83`). 로그인 비밀번호 분실은 로그인 화면에서 재설정(`admin_auth.json`, 매핑 암호키와 분리) |
| `PLANS_DIR` | `plans/2026` | Plans 보드 소스(`:61`) |

> `.env`는 배포 제외 목록(`build_deploy.ps1:41`)에 있으므로 비밀값이 패키지에 들어가지 않는다. 내부망 데스크톱 전용이므로 UI에 모바일/반응형은 고려하지 않는다. [[project_desktop_only_no_mobile]]

---
---pb---

## 자주 겪는 함정

| 증상 | 원인 | 대응 |
|------|------|------|
| 감정이 전부 규칙 폴백 | 모델 디렉터리 부재/로드 실패 → `predict_sentiments`가 `None` | `model_status()`(`hr_sentiment.py:136`)로 `dir_exists`·`load_failed` 확인 |
| 버전 모달에 무결성 경고 | 모델 파일 교체 후 **서버 미재시작**(디스크≠메모리 지문) | `gen_version.py` 재생성 + 서버 재시작. [[project_version_json_deploy_gap]] |
| `.bak` 파일 수정해도 반영 안 됨 | `*.py.bak`는 **임포트 경로에 없는 잔재** | 실제 로드되는 `.py`를 수정([02 모듈 지도](02-module-map.md) §1 주의) |
| 재추론이 배포본과 불일치 | 필드 프리픽스 누락 | `f'{field} 평가: {text}'` 규약 준수. [[project_batch_260709_model_gap]] |
| 특정 연/월 필터 시 전건 탈락 | `evaluation_date`가 int | `_get_eval_field_value` str 정규화. [[project_eval_date_int_filter_bug]] |
| 배포에 구버전 소스 | `build/`·옛 소스 사본 반입 | 새로 빌드한 zip이 정본. [[project_deploy_gap_worktree_stale_source]] |

---

## 디버깅 원칙

- 버그는 **증상 → 로그 → 재현**부터. 코드 존재는 원인이 아니며, 실제 파라미터로 재현해 게이트를 통과하기 전엔 수정하지 않는다(가설서 출발 금지). [[feedback_diagnose_from_symptom_not_hypothesis]]
- 로그 진단은 `STAGE`(예: `DB_LOAD`, `DB_LOAD_ALL`)부터 — `perspective_service.py`가 `request_id`·`stage`를 구조화 로깅한다(`:1763` 등).
- 테스트로 **완료(DN) 선언 금지**: 단위 테스트가 아니라 **실동작 검증** 후에만 DN, 그 전엔 PND + 체크리스트. [[feedback_dn_after_runtime_verify]]

---
## 개정 이력

| 판 | 날짜 | 무엇을·왜 |
|----|------|-----------|
| rev-261029-01 | 2026-10-29 | SECRET_KEY·ADMIN_PASSWORD 행을 현행 코드에 맞게 정정(SECRET_KEY 자동 생성, ADMIN_PASSWORD 코드 기본값·자동 선택, 분실 시 로그인 화면 재설정), '배포 전 교체' 안내 폐기 — 근거 common 01-global-rules 규칙 6 |

↑ [목록으로](00-index.md) · [← 이전: 07. 파인튜닝 데이터 파이프라인](07-finetune-pipeline.md) · [다음: 09. 확장 포인트/주의 →](09-extension-points.md)
