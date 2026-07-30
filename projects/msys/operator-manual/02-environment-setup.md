# 환경 설정

## .env 파일 설정

`.env` 파일은 환경별 설정을 관리합니다.

> 🔒 아래 예시에서 **비밀번호·키의 실제 값은 적지 않고 `<설정값>` 으로 표기**합니다. 전체 변수 목록은 부록 «설정 항목 레퍼런스» 를 보십시오.

### 필수 설정 항목

```env
# Database
DB_HOST=localhost
DB_NAME=etl_db_dev
DB_USER=<설정값>
DB_PASSWORD=<설정값>          # 🔒 실제 값은 문서에 적지 않는다
DB_PORT=5432

# Flask
FLASK_HOST=0.0.0.0
FLASK_PORT=18080
FLASK_DEBUG=False

# Session
ADMIN_SESSION_LIFETIME_DAYS=7
DEFAULT_SESSION_LIFETIME_MINUTES=20

# Mail
MAIL_SERVER=<사내 메일 릴레이 주소>
MAIL_PORT=25
```

## 로컬 개발 환경 구축

```bash
# 1. 가상환경 생성
python -m venv msys_venv

# 2. 가상환경 활성화
# Windows
msys_venv\Scripts\activate
# Linux
source msys_venv/bin/activate

# 3. 의존성 설치
pip install -r requirements.txt

# 4. .env 파일 설정

# 5. 서비스 기동
python msys_app.py
```

## 운영 환경 설정

| 항목 | 경로/값 |
|------|---------|
| 배포 경로 | `/data/external_data_monitoring/msys/` |
| Python 환경 | `/data/external_data_monitoring/.web/bin/activate` |
| 로그 경로 | `/data/external_data_monitoring/log/` |

---

> ↑ [목록으로](README.md) · [← 이전: MSYS 시스템 개요](01-system-overview.md) · [다음: 배포 절차 →](03-deployment.md)
