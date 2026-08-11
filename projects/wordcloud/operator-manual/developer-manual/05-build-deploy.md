---
reportTheme: technical
---

# 빌드·배포

↑ [목록으로](00-index.md)

> **핵심**: 배포는 `deploy/build_deploy.ps1` 하나로 한다. 빌드 매 단계가 **VERSION.json을 현재 모델로 재생성**하는 것이 정본 규칙(모델 교체 후 미갱신 사고 방지). 잔재 소스(`build/`·`*.egg-info`)와 런타임 폴더는 반드시 제외한다.
> **기준 버전 / 최종 확인일**: v1.1.0 · 2026-07-22 (commit `7b106b5`)
> **절차 상세 정본**: [`project_wordcloud/deployment.md`](../../deployment.md)

---

## 두 가지 배포 모드 (`build_deploy.ps1`)

| 모드 | 실행 | 산출물 | 내용 |
|------|------|--------|------|
| 소스 전용(기본) | `.\deploy\build_deploy.ps1` | `wordcloud-project.zip` | 앱 소스만(제외 규칙 적용) |
| 패키지 전체 | `.\deploy\build_deploy.ps1 -Package` | `wordcloud-internal/` (+zip) | runtime(Python) + **model/** + driver + source + `start.bat` |

- `-Package`는 base Python `Lib`(site-packages 제외)를 복사하고(`:138`), `model/`을 동봉하며, 실행용 `start.bat`을 생성한다(`:192-212`). `start.bat`은 `python -m web.app`으로 서버를 띄운다.

---

## 배포 제외 목록 (`:34-41`) — 잔재·런타임·비밀 반입 방지

`$ExcludeDirs`:
```
venv, __pycache__, .git, .sessions, doc, vendor_python_pkgs, logs, temp,
node_modules, deploy, .pytest_cache, inputs, scripts, .opencode, .clinerules,
failed, plans, default, outputs, processed_data,
build, *.egg-info        ← setup.py 빌드 잔재(옛 소스 사본 반입 방지)
```
`$ExcludeFiles`:
```
*.pyc, .gitignore, CACHEDIR.TAG, README.md, mermaid.min.js,
.env, *.jsonl, *.zip, flask_err.txt, flask_out.txt
```

> ⚠️ **잔재 소스 트랩**: 과거 `build/`·`wordcloud-source/`(옛 사본)이 반입돼 구버전이 배포되는 사고가 있었다. 정본은 **이 스크립트가 새로 만든 zip**이며, 워킹트리에 미커밋 규칙이 남아 있지 않은지 확인한다. [[project_deploy_gap_worktree_stale_source]] · `.env`는 제외 목록에 있으므로 비밀키가 패키지에 들어가지 않는다.

---
---pb---

## VERSION.json 동기화 (배포 정본)

빌드 시작 시 스크립트가 `scripts/gen_version.py`를 실행해 VERSION.json을 **현재 `model/hr_sentiment_finetuned` 기준으로 재생성**한다(`:57-80`, "항상 이 빌드 단계가 정본으로 만든다").

`gen_version.py`(`scripts/gen_version.py`)가 기록하는 값:

| 필드 | 산출 | 근거 |
|------|------|------|
| `system_version` | 고정 `1.1.0` | `:71` |
| `model_version` | 고정 `hr-sentiment-v1.0` | `:72` |
| `model_sha256` | `model/hr_sentiment_finetuned/model.safetensors`의 SHA-256(없으면 `-`) | `:43-55` |
| `model_trained` | 위 파일 mtime 날짜 | `:58-66` |
| `source_commit` | `git rev-parse --short HEAD` | `:30-40` |
| `build_date` | UTC ISO8601 | `:76` |

- 무결성 대조: 런타임에 `hr_sentiment` 싱글톤이 로드 시 디스크 가중치 sha256을 기록(`hr_sentiment.py:57-59`)하고, `version_service`가 **선언(VERSION.json)·디스크·메모리 3자**를 대조해 "파일 교체 후 서버 미재시작"을 버전 모달에서 탐지한다.

> 🔴 **모델을 교체했다면**: 반드시 `gen_version.py` 재생성 + 패키지 동봉 + **서버 재시작**. 안 하면 모달 학습일·무결성이 불일치한다. [[project_version_json_deploy_gap]]

---

## 배포 후 확인 체크리스트

1. `-Package` zip 안에 `model/hr_sentiment_finetuned/`가 포함됐는가.
2. VERSION.json의 `model_sha256`·`model_trained`가 실제 모델과 일치하는가(빌드 로그 `VERSION.json OK …` 확인, `:80`).
3. 잔재 폴더(`build/`, `*.egg-info`, 옛 소스 사본)가 zip에 없는가.
4. `start.bat` 실행 → 서버 기동 후 버전 모달에 무결성 경고가 없는가.

> 배포 패키지 정합성 점검은 `deploy-verifier` 에이전트의 담당 영역이다(빌드 산출물 포함/제외 대사).

---
↑ [목록으로](00-index.md) · [← 이전: 04. 데이터 계층](04-data-layer.md) · [다음: 06. 배치 처리 →](06-batch.md)
