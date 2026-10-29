# 내부망 배포 (Deployment)

> 최초 작성 2026-06-11 · 최종 개정 2026-10-29 (당일 제2차) — rev-261029-02

## ⚠️ AI 수정 금지 파일

아래 파일은 **사용자가 명시적으로 수정을 요청하지 않는 한 절대 수정 금지**:

| 파일 | 이유 |
|------|------|
| `start.bat` (루트 및 `wordcloud-internal/`) | 내부망 실행 진입점, 런타임 경로 하드코딩 |
| `wordcloud_project/deploy/build_deploy.ps1` | 배포 자동화 스크립트, start.bat·update.bat 생성 로직 포함 |
| `wordcloud-internal/` 전체 | 빌드된 배포 패키지 — 소스 수정과 무관 |

소스 업데이트 작업 시 이 파일들은 절대 건드리지 않는다.

> `wordcloud_project/deploy/preserve_manifest.json`(운영 데이터 보존 목록 단일 정본)은 금지 대상이 **아니다** — 보존 대상을 추가·변경할 때 **고쳐야 하는** 파일이다(§운영 데이터 보존).

---

## 배포 유형

| 유형 | 명령어 | 출력 | 용도 |
|------|--------|------|------|
| **일반 배포 (소스 전용)** | `.\deploy\build_deploy.ps1` | 저장소 루트의 `wordcloud-project.zip` + `update.bat` | **기본값.** 내부망 기존 패키지의 코드만 교체, 운영 데이터는 보존 |
| **패키지 배포 (전체)** | `.\deploy\build_deploy.ps1 -Package` | `wordcloud-internal/` | **첫 설치용.** Python runtime + pip 패키지 + 모델 + 소스 포함 (7.7GB) |

> 🔴 **요청 해석 (고정 규칙):** 사용자가 「배포」「배포 파일 만들어줘」「배포 준비」처럼 **업무 연속성을 말하지 않아도** 배포 요청은 **항상 일반 배포**다 — 무인자 실행으로 매니페스트 `exclude` 항목(운영 DB `.sessions`·가명 매핑 등)을 zip 에 싣지 않고, 내부망의 것은 `update.bat` 이 보존한다. `-Package` 는 사용자가 「첫 설치」「전체 패키지」를 명시할 때만 만든다. 운영 DB·매핑을 덮어쓰거나 초기화하는 배포는 사용자가 명시하고 확인한 뒤에만 만든다. 빌드 뒤에는 zip 안의 `.db`·`.enc`·`.env`·`exclude` 항목이 0건인지 검사해 결과를 보고한다.

## 일반 배포 (소스 전용)

```powershell
cd wordcloud_project
.\deploy\build_deploy.ps1
```

**출력** (2026-10-29 rev-261029-02 재빌드 실측): `../wordcloud-project.zip` 947,870 바이트(약 0.9MB, 압축 전 `wordcloud_project` 본체 2,931KB) · `../update.bat`(preserve_manifest.json 으로 생성한 업데이터, 보존 21항목)
빌드 중간 폴더 `_source_staging/` 은 빌드 끝에 삭제된다. `wordcloud-source/` 는 현 스크립트가 만들지 않는다 — 남아 있다면 잔재다.

**내부망 업데이트 (원칙 — update.bat 사용):**
1. `wordcloud-project.zip` **과 `update.bat` 을 함께** 내부망 패키지 폴더(`start.bat` 이 있는 곳)에 복사한다. 내부망의 구 `update.bat` 은 보존 단계가 없거나 `.sessions`·매핑만 보존하는 판이므로 **반드시 새 것으로 덮어쓴다.**
2. 서버를 중지한다.
3. `update.bat` 을 실행한다.
4. `start.bat` 으로 재시작한다.

**update.bat 동작** (정본: `build_deploy.ps1` 의 `New-UpdateBat`):

| 상황 | 동작 |
|------|------|
| 정상 | 보존 항목을 `_update_backup_tmp` 로 이동 → `wordcloud_project/`·`.clinerules/` 삭제 → zip 해제 → 보존 항목 복원 → 백업 폴더 삭제 |
| zip 없음 / 포트 5001 LISTENING | 아무것도 하지 않고 중단 |
| `_update_backup_tmp` 가 이미 있음 | 중단. 직전 실패분이 운영 데이터의 **유일 사본**일 수 있다 — 내용을 `wordcloud_project` 로 되돌린 뒤 폴더를 지우고 재실행 |
| zip 해제 실패 | 운영 데이터를 복원한 뒤 오류로 종료(프로그램 파일은 비어 있음) — zip 을 확인하고 재실행 |
| 백업 이동 실패(파일 잠금 등) | **아무것도 지우지 않고** 롤백 후 중단 |
| 복원 실패 | `_update_backup_tmp` 를 남기고 오류 — 수동으로 되돌린다 |

2026-10-22 개발 PC 모의 내부망 폴더 실측(산출물 미보관): 정상 경로의 코드 교체·운영 데이터 보존, DB 파일 잠금 시 무삭제 롤백, 잔존 백업 폴더 시 거부, 손상 zip 시 운영 데이터 복원 후 오류 종료를 확인했다(매니페스트 20항목 판, 운영 데이터 표본 12종).

**수동 업데이트 (update.bat 을 쓸 수 없을 때만):** `wordcloud_project/` 를 지우고 압축을 풀면 **운영 DB·가명 매핑·화면 저장 설정이 함께 사라진다.** 부득이하면 `preserve_manifest.json` 의 **모든 항목을 먼저 패키지 밖으로 옮겨 두고**, 압축 해제 후 같은 경로로 되돌린다.

**ZIP 구조 (압축 풀면):**
```
wordcloud_project/
├── src/              (src/configs/ 의 seed 항목은 첫 설치 초기값)
├── web/
├── utils/
├── VERSION.json
└── requirements.txt
.clinerules/docs/cr/
```
`.env`·`.sessions/`·가명 매핑·실명 불용어 등 매니페스트 `exclude` 항목은 zip 에 **들어가지 않는다**(빌드가 누출을 검사한다).

## 운영 데이터 보존

**원칙: 내부망이 정본이다.** 일반 배포는 코드만 바꾸고, 내부망이 실행 중에 만들거나 고친 데이터는 덮어쓰지 않는다.

**정본은 `wordcloud_project/deploy/preserve_manifest.json` 하나다.** 항목(`path`·`type`·`mode`·`why`)은 그 파일에서만 본다 — 이 문서에 목록을 옮겨 적지 않는다. `build_deploy.ps1` 이 이 파일을 읽어 ① zip 제외 ② `update.bat` 백업·복원 단계 생성 ③ `exclude` 항목 누출 시 빌드 중단(throw)을 수행한다(일반 배포 기준, `-Package` 는 §패키지 배포 경고 참조).

| mode | zip | update 시 |
|------|-----|-----------|
| `exclude` | 싣지 않는다 | 내부망에 있으면 빼뒀다 되돌린다 |
| `seed` | 개발본을 첫 설치 초기값으로 싣는다 | 내부망에 있으면 내부망 것으로 되돌린다 |

**왜 보존하는가 (범주 요약):**

| 범주 | mode | 이유 |
|------|------|------|
| 운영 DB(`.sessions`) | exclude | 평가·배치 작업서·사용자 등 내부망에서만 자란다 |
| 가명 매핑·직전 백업·복호화 실패 시 밀려난 원본 | exclude | 덮으면 매핑이 되돌아가거나 소실된다. 밀려난 원본은 매핑 복구의 유일 사본 |
| 실명 불용어 | exclude | PII — 배포 금지([domain-locks.md](domain-locks.md) DL-9) |
| 비밀값(`.env`)·재설정한 로그인 비밀번호 해시(`admin_auth.json`) | exclude | 비밀값은 배포물에 싣지 않는다. 로그인 비밀번호 해시를 덮으면 재설정 전 비밀번호로 되돌아간다 |
| 산출물·업로드·반입 원데이터·로그·배치 실패 기록·내부망 배치가 쓰는 `plans/`(판정 패킷 등) | exclude | 운영 결과·원데이터 파생·장애 추적 이력 |
| 화면에서 저장되는 설정·테스트 케이스(`src/configs/` 의 json·하위 폴더) | seed | 첫 설치엔 기본값이 필요하고, 이후엔 관리자가 저장한 값이 정본 |

**규칙:**
1. 내부망에서 실행 중 생성·수정되는 파일/폴더를 새로 만드는 기능을 추가하거나 그 경로를 바꾸면 **같은 변경에서** `preserve_manifest.json` 에 항목을 추가한다. 판단 기준은 앱이 런타임에 쓰는 경로다 — sqlite connect 대상, `open(..., 'w')`·`'a'` 대상, `json.dump` 대상, 업로드 저장 위치, 로그 출력 위치.
2. 경로를 바꿨다면 구 경로 항목은 내부망 데이터 이관 방법을 사용자와 정하기 전에는 지우지 않는다.
3. mode 선택: 개발본 기본값이 있어야 앱이 첫 설치에서 동작하면 `seed`, 아니면 `exclude`. PII·비밀값·운영 데이터는 항상 `exclude`.
4. `seed` 의 한계: 개발본 seed 파일을 고쳐도 **내부망에 이미 있는 파일이 이긴다 — 자동 반영되지 않는다.** 내부망 반영이 필요하면 그 절차를 사용자와 별도로 정한다(현재 자동 반영 절차는 없다).
5. 항목 형식: `path` 는 `wordcloud_project` 기준 ASCII 상대경로(`..` 금지), `type` 은 `file|dir`, `mode` 는 `exclude|seed`. 어기면 빌드가 중단된다(`Get-PreserveEntries`).
6. 항목을 바꾸면 빌드를 다시 돌려 새 `update.bat` 을 만들고, **zip 과 함께 반입**한다. 보존 목록은 `update.bat` 안에 실려 가기 때문이다.

## 비밀번호·환경변수

**환경변수 없이 기동한다.** 내부망에서 환경변수를 새로 넣거나 `.env` 를 만들 일은 없다 — 운영 중인 배포본에 그런 조건을 더하는 변경 자체가 금지다([01-global-rules.md](../../common/core/00-core/01-global-rules.md) 규칙 6).
- **가명 매핑 암호키**(`settings.ADMIN_PASSWORD`): 원래 배포본과 같은 **코드 기본값**을 쓴다 — 내부망의 기존 `pseudonym_mappings.enc` 가 이 값으로 암호화돼 있다. 예전에 넣은 환경변수가 남아 있어도 `_mapping_key()` 가 매핑을 실제로 여는 값(환경변수 값 또는 기본값)을 자동으로 고르고, 둘 다 못 열면 `web/app.py` 의 `_assert_mapping_decryptable` 가 기동을 멈춘다(빈 매핑 덮어쓰기 방지). 기본값을 바꾸거나 없애지 않는다(규칙 6-2). 정본: `src/config/settings.py`
- **세션 서명 키**(`SECRET_KEY`): 없으면 기동마다 무작위로 만든다 — 재시작하면 관리자 로그인이 풀린다(`src/config/settings.py`). **기동 시 입력은 없다** — 비밀번호를 묻지 않는다(구 `src/config/admin_password.py` 삭제).
- **관리자 로그인 비밀번호 분실**: 로그인 화면 「비밀번호를 잊으셨나요?」(`/admin/reset-password`) → 마스터 비밀번호 확인 → 새 로그인 비밀번호 저장. 해시로만 `src/configs/admin_auth.json` 에 남고 update 시 보존된다(매니페스트 exclude). 이 파일이 없으면 매핑 암호키 값으로 로그인한다(기존 동작). 로그인 비밀번호와 매핑 암호키는 **분리돼 있어** 재설정해도 가명 매핑은 그대로 열린다. 마스터 비밀번호는 코드에 해시로만 있으며 **값은 어떤 문서에도 적지 않는다.** 정본: `src/services/admin_auth_service.py` · `src/routes/admin_routes.py` · `web/templates/admin_reset_password.html`

## 패키지 배포 (전체) — `wordcloud-internal/`

```powershell
cd wordcloud_project
.\deploy\build_deploy.ps1 -Package
```

인자: `-OutputDir`(출력 경로, 기본 `../wordcloud-internal`) · `-SkipDriver`(NVIDIA Driver 다운로드 생략) · `-DriverUrl`(다운로드 URL 변경)

```
wordcloud-internal/
├── runtime/python/       Python 3.10 실행 파일 + 표준 라이브러리 + site-packages
├── model/                감정 분석 모델 (kote, sarcasm)
├── wordcloud_project/    소스 코드 (venv, logs, .sessions, 캐시 제외)
├── .clinerules/docs/cr/
├── install_driver/       NVIDIA CUDA Driver (선택)
├── start.bat             [더블클릭 실행]
├── update.bat            [일반 배포와 같은 생성기 — preserve_manifest.json]
└── README.txt            설치/실행 안내
```

> ⚠️ `-Package` 의 소스 복사는 매니페스트 `exclude` 와 누출 검사를 적용하지 않는다. 반입 전에 `preserve_manifest.json` 의 `exclude` 항목 전부가 `wordcloud-internal/wordcloud_project/` 에 들어가지 않았는지 확인한다.

**내부망 실행 순서:** ① `install_driver/` 로 CUDA Driver 설치(관리자 권한, 재부팅) ② `wordcloud-internal/` 을 내부망 PC로 복사 ③ `start.bat` 실행 ④ 브라우저 `http://127.0.0.1:5001`

**이후 업데이트:** 일반 배포 산출물(zip + update.bat)을 쓴다. `-Package` 가 함께 만드는 `wordcloud-project.zip` 은 `wordcloud-internal/` 전체(runtime·model 포함)를 압축한 것이다.

**의존성 용량:** Python 3.10 ~80MB · torch + CUDA ~5.2GB(GPU 추론) · transformers ~45MB · kiwipiepy ~95MB(형태소) · 모델(kote, sarcasm) ~1GB. 번역 모델(nllb, opus-mt)은 미사용으로 제외.

## build_deploy.ps1 단계

**공통:** VERSION.json 재생성·모델 해시 확인(`Sync-Version`).

**소스 전용 모드 (기본, `Build-SourceOnly`):** ① 매니페스트 읽기·형식 검사 ② `_source_staging/` 로 복사(고정 제외 목록 + `exclude` 항목) ③ `exclude` 누출 검사 ④ `.clinerules/outputs/cr` → zip 안 `.clinerules/docs/cr` ⑤ zip 압축 ⑥ staging 삭제 ⑦ `update.bat` 생성

**전체 패키지 모드 (`-Package`):** ① 출력 디렉토리 ② Python 런타임 ③ pip 패키지 ④ 모델 ⑤ 소스코드 ⑥ NVIDIA Driver(선택) ⑦ start.bat + README ⑧ wordcloud-project.zip ⑨ `update.bat` 생성

---

## 개정 이력

| 판 | 날짜 | 무엇을·왜 |
|----|------|-----------|
| rev-261029-02 | 2026-10-29 | 사용자 요청(업무 연속성을 말하지 않는 일반 배포도 반드시 DB 를 업데이트하지 않게). §배포 유형에 **요청 해석 고정 규칙** 추가 — 배포 요청 기본은 일반 배포(보존), `-Package` 는 첫 설치 명시 시만, DB·매핑 덮어쓰기는 명시·확인 시만, 빌드 뒤 zip 의 `.db`·`.enc`·`.env`·`exclude` 0건 검사·보고. §일반 배포 출력 블록을 재빌드 실측 1줄로 압축(줄 상한 160 유지) |
| rev-261029-01 | 2026-10-29 | 사용자 지시(배포본에 환경변수를 넣게 만들지 말 것)와 코드 원복에 맞춰 정정. §내부망 필수 환경변수를 **§비밀번호·환경변수로 교체** — rev-261022-02~04 의 `ADMIN_PASSWORD` 필수화·기동 시 숨김 입력·마스터 비밀번호 복구 파일(`admin_recovery.json`)·환경변수 지정 권장·교체 절차서 안내는 **전부 폐기**(코드에서 삭제됨). 현재 사실: 환경변수 없이 기동, 매핑 암호키는 원래 코드 기본값·`_mapping_key()` 자동 선택, `SECRET_KEY` 무작위 생성, 로그인 화면 마스터 비밀번호 재설정(`admin_auth.json`, 매핑 암호키와 분리). 보존 범주 표 비밀값 행에 `admin_auth.json` 추가(매니페스트 21항목 판). 줄 상한(160) 유지를 위해 §배포 유형·§일반 배포 뒤 구분선 2개 삭제(내용 변경 없음). 근거: 기본값 제거로 운영본 기동 불가·4일 손실 → [01-global-rules.md](../../common/core/00-core/01-global-rules.md) 규칙 6 신설 |
| rev-261022-04 | 2026-10-22 | 사용자 요청(비밀번호 분실 대비 마스터 비밀번호). 환경변수 절에 마스터 비밀번호 복구 파일 동작·교체 시 재설정 추가, 매니페스트에 `admin_recovery.json`(exclude) 추가. 요청된 고정값을 코드에 넣지 않은 이유(소스 공개) 명시 |
| rev-261022-03 | 2026-10-22 | 사용자 요청(기동 시 비밀번호 입력). 환경변수 절에 `ADMIN_PASSWORD` 미설정 시 콘솔 숨김 입력·매핑 복호화 검증·3회 실패 거부 동작 추가 |
| rev-261022-02 | 2026-10-22 | 검토(guideline-reviewer) 조건부 통과 지적 반영 + 같은 날 코드 변경 반영. 이번 배포본부터 `ADMIN_PASSWORD` 코드 기본값 제거(06_01 P1)·`SECRET_KEY` 무작위 생성(`settings.py`) — 환경변수 절에 기존 매핑 암호키와 같은 값 지정 의무·불일치 시 결과·교체 절차서 추가. update.bat 의 zip 해제 실패 시 복원 후 오류 종료 행 추가. 매니페스트 항목 추가(복호화 실패 원본·배치 실패 기록·`plans/`·테스트 케이스)를 범주 표에 반영. 가명 매핑 행의 무관한 DL-1 표기 제거. `-Package` 경고를 매니페스트 정본 지목으로 교체. 모의 실측 문장의 근거 수준(산출물 미보관) 표기, 구 항목 수(16)를 재실측 판 표기(20항목)로 교체. ExcludeFiles 에 `*.bak`·`*.bak_*`·`flask_*.txt` 추가 후 재빌드 실측으로 크기 갱신(944,325 바이트)·모의 실측에 손상 zip 시나리오 추가 |
| rev-261022-01 | 2026-10-22 | 사용자 요청(운영 연속성 — 일반 배포 시 DB·가명 매핑 등 덮어쓰지 않을 데이터를 지침으로 관리). §운영 데이터 보존·§내부망 필수 환경변수 신설, 일반 배포 산출물에 `update.bat` 추가, 업데이트 절차를 zip+update.bat 동시 반입으로 교체, 수동 절차를 경고로 교체. 같은 요청으로 `build_deploy.ps1` 에 보존 매니페스트 연동 수정(AI 수정 금지 파일이나 사용자 명시 요청). 낡은 사실 정정: ZIP 구조의 `.env`·존재하지 않는 `configs/` 삭제, 크기 ~400KB → 실측 961,215 바이트, `wordcloud-source/` 출력 삭제, `-Package` 출력의 `.env` 행 삭제·소스 복사 경고 추가 |
