# 내부망 배포 (Deployment)

## ⚠️ AI 수정 금지 파일

아래 파일은 **사용자가 명시적으로 수정을 요청하지 않는 한 절대 수정 금지**:

| 파일 | 이유 |
|------|------|
| `start.bat` (루트 및 `wordcloud-internal/`) | 내부망 실행 진입점, 런타임 경로 하드코딩 |
| `wordcloud_project/deploy/build_deploy.ps1` | 배포 자동화 스크립트, start.bat 생성 로직 포함 |
| `wordcloud-internal/` 전체 | 빌드된 배포 패키지 — 소스 수정과 무관 |

소스 업데이트 작업 시 이 파일들은 절대 건드리지 않는다.

---

## 파일 위치
`wordcloud_project/deploy/build_deploy.ps1`

## 배포 유형

| 유형 | 명령어 | 출력 | 용도 |
|------|--------|------|------|
| **일반 배포 (소스 전용)** | `.\deploy\build_deploy.ps1` | `wordcloud-project.zip` + `wordcloud-source/` | **기본값.** 소스코드만 배포. 기존 패키지의 `wordcloud_project/`를 교체할 때 |
| **패키지 배포 (전체)** | `.\deploy\build_deploy.ps1 -Package` | `wordcloud-internal/` | **첫 설치용.** Python runtime + pip 패키지 + 모델 + 소스 포함 (7.7GB) |

---

## 일반 배포 (소스 전용) — `wordcloud-project.zip`

```powershell
cd wordcloud_project
.\deploy\build_deploy.ps1
```

**출력:**
```
../wordcloud-project.zip     ← 압축 파일 (소스만 ~400KB)
../wordcloud-source/         ← 압축 풀기 전 폴더
```

**내부망 업데이트 방법 (간편):**
1. `wordcloud-project.zip`을 내부망 PC의 패키지 폴더(`wordcloud-internal/` 등)에 복사
2. `update.bat` 더블클릭 → 자동으로 교체 완료
3. `start.bat`으로 재시작

**내부망 업데이트 방법 (수동):**
1. `wordcloud-project.zip`을 USB로 내부망 PC에 복사
2. 기존 패키지에서 `wordcloud_project/` 폴더 **삭제**
3. `wordcloud-project.zip` 압축 해제 → `wordcloud_project/` 폴더 생성됨
4. 해제된 `wordcloud_project/` 폴더를 패키지 폴더 안으로 이동
5. 끝. 재시작하면 새 소스로 동작

**ZIP의 구조 (압축 풀면):**
```
wordcloud_project/     ← 이 폴더 전체를 패키지 폴더 안에 넣으면 됨
├── .env
├── src/
├── web/
├── configs/
├── utils/
└── requirements.txt
```

## 패키지 배포 (전체) — `wordcloud-internal/`

```powershell
cd wordcloud_project
.\deploy\build_deploy.ps1 -Package
```

### 옵션
| 인자 | 설명 |
|------|------|
| `-OutputDir` | 출력 경로 지정 (기본: `../wordcloud-internal`) |
| `-SkipDriver` | NVIDIA Driver 다운로드 생략 |
| `-DriverUrl` | NVIDIA Driver 다운로드 URL 변경 |

### 출력 구조
```
wordcloud-internal/
├── runtime/              Python 3.10 실행 파일 + pip 패키지
│   └── python/
│       ├── python.exe
│       ├── Lib/          표준 라이브러리 + site-packages
│       └── DLLs/
├── model/                감정 분석 모델 (kote, sarcasm)
│   └── kote_for_easygoing_people/
├── wordcloud_project/    소스 코드 (venv, logs, 캐시 제외)
│   ├── .env              (BASE_ROOT=.. 상대경로)
│   ├── src/              백엔드
│   ├── web/              Flask + 템플릿
│   └── .sessions/        SQLite DB (자동 생성)
├── install_driver/       NVIDIA CUDA Driver (선택)
├── start.bat             [더블클릭 실행]
├── update.bat            [소스 업데이트용 — ZIP 교체 자동화]
└── README.txt            설치/실행 안내
```

### 내부망 실행 순서
1. `install_driver/` → CUDA Driver 설치 (관리자 권한, 재부팅)
2. `wordcloud-internal/` 폴더를 내부망 PC로 복사
3. `start.bat` 더블클릭
4. 브라우저 자동 열림 → `http://127.0.0.1:5001`

### 소스 업데이트
`-Package` 모드로 전체 패키지를 만들면 `wordcloud-project.zip`도 함께 생성됩니다.
업데이트 시에는 이 ZIP만 교체하면 됩니다.

## 의존성
| 의존성 | 용량 | 비고 |
|--------|------|------|
| Python 3.10 | ~80 MB | 표준 라이브러리 |
| torch + CUDA | ~5.2 GB | GPU 추론용 |
| transformers | ~45 MB | KoTE 모델 로딩 |
| kiwipiepy | ~95 MB | 형태소 분석기 |
| 모델 (kote, sarcasm) | ~1 GB | 감정/반어법 분석 |

> 번역 모델 (nllb, opus-mt)은 미사용으로 제외되었습니다.

## build_deploy.ps1 스크립트
`wordcloud_project/deploy/build_deploy.ps1` 에서 모든 과정을 자동화합니다:

**소스 전용 모드 (기본):**
1. 출력 디렉토리 생성
2. 소스코드 복사 (logs, venv, 캐시 제외)
3. wordcloud-project.zip 압축

**전체 패키지 모드 (`-Package`):**
1. 출력 디렉토리 생성
2. Python 런타임 복사 (표준 라이브러리 + DLLs)
3. pip 패키지 복사 (venv site-packages)
4. 모델 파일 복사
5. 소스코드 복사 (logs, venv, 캐시 제외)
6. NVIDIA Driver 다운로드 (선택)
7. start.bat + README 생성
8. wordcloud-project.zip 함께 생성
