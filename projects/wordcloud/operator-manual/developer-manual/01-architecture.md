---
reportTheme: technical
---

# 아키텍처 개요

↑ [목록으로](00-index.md)

> **핵심**: Flask 팩토리(`web/app.py`) → 12개 블루프린트 → 서비스 계층 → SQLite(`.sessions`) + 파일 산출물.
> **기준 버전 / 최종 확인일**: v1.1.0 · 2026-07-22 (commit `7b106b5`)

---

## 실행 진입점

| 항목 | 값 | 근거 |
|------|-----|------|
| 앱 팩토리 | `create_app()` | `web/app.py:53` |
| 실행 함수 | `main()` → `app.run(...)` | `web/app.py:121-141` |
| 모듈 실행 | `python -m web.app` | `web/app.py:144-145` (`if __name__ == '__main__': main()`) |
| 기본 포트/호스트 | `127.0.0.1:5001` | `src/config/settings.py:48-49`, `.env` |
| Debug 플래그 | `FLASK_DEBUG`(기본 True) | `src/config/settings.py:47` |
| 리로더 | `use_reloader=False`, `threaded=True` | `web/app.py:139-140` |

- Windows 인코딩 강제: `web/app.py:9-15`에서 `stdout/stderr`를 UTF-8로 재구성하고 로케일을 `ko_KR`로 고정한다.
- 프로젝트 루트를 `sys.path`에 추가: `web/app.py:18`.
- 배포 패키지의 `start.bat`도 동일하게 `python -m web.app`을 호출한다(`deploy/build_deploy.ps1:195-211`).

> ⚠️ **서버 실행은 안내만**: 이 문서는 기동 방법을 설명할 뿐, 저자는 서버를 직접 띄우지 않는다. 로컬 구동은 [08 문서](08-dev-setup-troubleshooting.md) 참조.

---

## 앱 부팅 시퀀스

`main()`(`web/app.py:121`) 실행 순서:

1. `create_app()` — Flask 인스턴스 생성, `template_folder`/`static_folder`를 절대경로로 지정(`web/app.py:55-57`).
2. 앱 설정: `SECRET_KEY`, `JSON_AS_ASCII=False`(한글 JSON 유지), 업로드 한도 `MAX_CONTENT_LENGTH=100MB`(`web/app.py:60-63`).
3. 블루프린트 12개 등록(`web/app.py:66-77`).
4. 컨텍스트 프로세서 2개 주입: 관리자 세션 상태(`inject_auth_state`)·버전 정보(`inject_version_info` → `version_service.get_version_info()`)(`web/app.py:79-86`).
5. 404/500 에러 핸들러 등록(`web/app.py:89-100`).
6. `/outputs/...` 정적 산출물 서빙 라우트 3종(`web/app.py:103-116`).
7. **부팅 마이그레이션**: `main()`이 `deploy_session_service._auto_migrate_evaluations()`를 호출(`web/app.py:125-126`) — DB가 비어 있으면 `users/*.json`을 `evaluations` 테이블로 1회 이전.

---

## 블루프린트(라우트) 지도

`web/app.py:40-51`에서 임포트하여 `web/app.py:66-77`에서 등록한다.

| 블루프린트 | URL prefix | 파일 | 책임 |
|-----------|-----------|------|------|
| `ui_bp` | (없음) | `src/routes/ui_routes.py` | HTML 페이지 렌더(대시보드·워드클라우드·설정 등) |
| `integrated_bp` (`metadata`) | `/api/integrated` | `src/routes/integrated_data_routes.py` | 통합 수집 데이터 API |
| `batch_bp` | `/api/batch` | `src/routes/batch_routes.py` | 배치 실행·진행·Resume API |
| `wordcloud_bp` | `/api/wordcloud` | `src/routes/wordcloud_routes.py` | 워드클라우드 생성 API |
| `api_bp` | `/api` | `src/routes/api_routes.py` | 공통/기타 API |
| `perspective_bp` | `/api/perspective` | `src/routes/perspective_routes.py` | 감정·관점(그룹) 분석 API |
| `test_bp` | (없음) | `src/routes/test_routes.py` | 감정/욕설/비꼬임 테스트 UI·API |
| `admin_bp` | `/admin` | `src/routes/admin_routes.py` | 관리자 로그인·설정 |
| `wordcloud_data_bp` | `/api/wordcloud` | `src/routes/wordcloud_data_routes.py` | 워드클라우드용 데이터 조회 |
| `wordcloud_preview_bp` | (없음) | `src/routes/wordcloud_preview_routes.py` | 미리보기 |
| `plans_bp` | `/admin` | `src/routes/plans_routes.py` | Plans 칸반보드·CR |
| `version_bp` | `/api/version` | `src/routes/version_routes.py` | 버전·무결성 정보 |

> 확인 필요: `wordcloud_bp`와 `wordcloud_data_bp`가 동일 prefix `/api/wordcloud`를 공유한다(`src/routes/wordcloud_routes.py:11`, `wordcloud_data_routes.py:10`). 엔드포인트 경로가 겹치지 않는지는 라우트 추가 시 반드시 확인하라.

---
---pb---

## 요청 흐름 (라우트 → 서비스 → DAO → DB)

계층 경계가 명확하다. 대표 예로 감정/단어 집계 흐름:

```
[HTTP 요청]
   ↓  src/routes/perspective_routes.py (Blueprint 핸들러: 파라미터 파싱·검증)
   ↓  src/services/perspective_service.py (도메인 로직: 문장→감정 override, 단어 점수 집계)
   ↓  src/modules/*.py (엔진: KoTE 추론·HR 감정모델·전처리·워드클라우드 렌더)
   ↓  src/services/deploy_session_service._get_conn() (DAO: SQLite 연결 헬퍼)
   ↓  .sessions/deploy_sessions.db (SQLite, WAL)
   ↑  응답(JSON) 또는 산출 이미지(/outputs/... 서빙)
```

- **DAO 계층**은 별도 ORM 없이 `deploy_session_service._get_conn()`(`src/services/deploy_session_service.py:12-17`)을 공유하는 얇은 SQLite 접근이다. `batch_work_order_service`도 이 헬퍼를 재사용해 순환 임포트·중복 초기화를 피한다(`src/services/batch_work_order_service.py:12`).
- **모듈(엔진)**은 상태를 갖는 싱글톤(KoTE·HR 감정모델)이라 프로세스 1회 로드 후 재사용된다([03 문서](03-emotion-engine.md)).
- **산출물**(워드클라우드 PNG 등)은 DB가 아니라 `outputs/` 하위에 저장되고 `/outputs/<path>` 라우트로 서빙된다(`web/app.py:103-116`).

---

## 디렉터리 지도 (`wordcloud_project/`)

| 폴더 | 역할 |
|------|------|
| `web/` | Flask 진입점(`app.py`)·`templates/`(Jinja HTML)·`static/`·`configs/` |
| `src/routes/` | 블루프린트(HTTP 계층) |
| `src/services/` | 도메인 서비스·DAO(감정 집계·배치·수집·판정패킷·갤러리 등) |
| `src/modules/` | 분석 엔진(KoTE·HR 감정·전처리·워드클라우드·욕설·리더십·비꼬임) |
| `src/models/` | 통합 데이터 매니저(`integrated_data_manager.py`) |
| `src/config/` | `settings.py`(경로·플래그 정본) |
| `src/configs/` | 런타임 설정 JSON·매핑(`mappings/`)·가명 매핑(`pseudonym_mappings.enc`)·불용어 등 |
| `scripts/` | 유지보수 스크립트(`gen_version.py`·`migrate_evaluations.py`·벤치) |
| `utils/` | 로거·날짜 정규화 공용 유틸 |
| `deploy/` | `build_deploy.ps1`(배포 빌더) |
| `.sessions/` | SQLite DB(`deploy_sessions.db`) — 배포 제외 |
| `outputs/` · `processed_data/` · `inputs/` | 산출·중간·입력 데이터 — 배포 제외 |
| `plans/` | 계획·데이터셋(`_datasets/kote_finetune/`) — 배포 제외 |
| `venv/` · `vendor_python_pkgs/` | 로컬 런타임 — 배포 제외 |

> 배포 제외 목록의 정확한 근거는 [05 빌드·배포](05-build-deploy.md) `$ExcludeDirs`/`$ExcludeFiles` 절 참조.

---
↑ [목록으로](00-index.md) · [← 이전: 00. 색인](00-index.md) · [다음: 02. 모듈 지도 →](02-module-map.md)
