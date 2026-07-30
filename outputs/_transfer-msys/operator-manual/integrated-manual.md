# MSYS 운영자 메뉴얼

> **대상**: MSYS(수집 현황 대시보드) 시스템 운영자 · 인수인계자 · 관리자(admin)
> **목적**: 시스템 운영에 필요한 메뉴별 조작 절차, 모니터링, 장애 대응을 한곳에서 안내
> **구성**: 본 진입점(목록) + 메뉴별 파일 + 부록. 각 메뉴 파일은 하단의 "이전/다음" 링크로 이동 가능.

---

## 목차 (목록)

### 시작하기
- [빠른 시작 가이드](00-getting-started.md)
- [시스템 개요](01-system-overview.md)
- [환경 설정](02-environment-setup.md)
- [배포 절차](03-deployment.md)

### 일반 메뉴
- [대시보드](04-common-menus/01-dashboard.md)
- [수집 스케줄](04-common-menus/02-collection-schedule.md)
- [차트 분석](04-common-menus/03-chart-analysis.md)
- [데이터 분석](04-common-menus/04-data-analysis.md)
- [데이터 스펙](04-common-menus/05-data-spec.md)
- [카드 요약](04-common-menus/06-card-summary.md)
- [매핑](04-common-menus/07-mapping.md)
- [API 키 관리](04-common-menus/08-api-key-mngr.md)
- [잔디(Jandi)](04-common-menus/09-jandi.md)
- [원시 데이터](04-common-menus/10-raw-data.md)
- [관리자](04-common-menus/11-admin.md)
- [API 테스트](04-common-menus/12-api-test.md)
- [외부 링크](04-common-menus/13-external-links.md)

### 관리/운영
- [관리자 설정](05-mngr-sett.md)
- [일상 운영](06-daily-operations.md)
- [장애 대응](07-troubleshooting.md)
- [백업/복구](08-backup-recovery.md)
- [구성·설정 시나리오 (신규 데이터/코드/키 추가)](09-provisioning-scenarios.md)

### 부록
- [명령어 치트시트](appendix/command-cheatsheet.md)
- [설정 참조](appendix/config-reference.md)

---

> 💡 **인쇄용 통합본**: `integrated-manual.html`을 브라우저에서 열고 "인쇄 → PDF 저장"(용지 A4)으로 전체 메뉴얼을 한 번에 출력하세요. 생성 방법은 `DEVELOPMENT.md` §9 참조.

---pb---


---pb---

# 1 빠른 시작 가이드

> **기준 버전 / 최종 확인일**: v1.1.0 · 2026-07-22

## 1.1 시스템 접속

1. 브라우저에서 `http://[서버주소]:18080` 접속
2. 로그인 화면에서 ID/PW 입력
3. 관리자 계정으로 접속 시 전체 메뉴 확인 가능

## 1.2 필수 확인 사항

| 항목 | 확인 방법 |
|------|----------|
| 서비스 기동 상태 | `ps -ef \| grep msys` |
| DB 연결 상태 | 대시보드 데이터 로드 여부 |
| 로그 확인 | `/data/external_data_monitoring/log/` |

## 1.3 기본 조작 순서

### 1.3.1 일일 업무
1. 대시보드 접속 → 수집 현황 확인
2. 수집 스케줄 → 이상 작업 확인
3. API 키 관리 → 만료 임박 키 확인

### 1.3.2 주간 업무
1. 관리자 설정 → 사용자 승인 대기 확인
2. 통계 → 메뉴 접근 현황 확인

---

> 다음 문서: [01-system-overview.md](01-system-overview.md)


---pb---

# 2 MSYS 시스템 개요

> **기준 버전 / 최종 확인일**: v1.1.0 · 2026-07-22

## 2.1 시스템 정의

MSYS(Monitoring System)는 **외부 데이터 수집 현황을 모니터링하고 관리하는 웹 기반 대시보드 시스템**입니다.

## 2.2 주요 기능

| 기능 | 설명 |
|------|------|
| 수집 현황 모니터링 | 실시간 수집 작업 상태 확인 |
| 스케줄 관리 | 수집 작업 스케줄 조회 및 관리 |
| API 키 관리 | API 키 등록, 만료 알림, 메일 발송 |
| 데이터 분석 | 차트/리포트 기반 데이터 분석 |
| 사용자 관리 | 계정 승인, 권한 설정, 데이터 접근 제어 |
| 시스템 설정 | 상태 코드, 아이콘, 스케줄 표시 설정 |

## 2.3 시스템 아키텍처

```
[사용자] → [Flask Web Server] → [PostgreSQL]
                ↓
            [Redis Cache]
                ↓
            [SMTP Mail]
```

| 구성 요소 | 기술 |
|-----------|------|
| Backend | Python 3 + Flask 3.1.1 |
| Frontend | HTML/Jinja2 + jQuery + JavaScript |
| Database | PostgreSQL |
| Cache | Redis |
| Mail | SMTP |

## 2.4 운영 환경

| 환경 | 설명 |
|------|------|
| 운영 서버 | CIB040L5 (Linux) |
| 배포 경로 | `/data/external_data_monitoring/msys/` |
| 로그 경로 | `/data/external_data_monitoring/log/` |
| 타임존 | KST (Asia/Seoul, UTC+9) |

## 2.5 주요 테이블

| 테이블 | 설명 |
|--------|------|
| tb_user | 사용자 계정 |
| tb_con_mst | 수집 작업 마스터 |
| tb_con_hist | 수집 이력 |
| tb_api_key_mngr | API 키 관리 |
| tb_mngr_sett | 관리자 설정 |
| tb_menu | 메뉴 정의 |

## 2.6 권한 체계

| 권한 | 설명 |
|------|------|
| admin | 전체 관리자 권한 |
| mngr_sett | 관리자 설정 메뉴 접근 |
| api_key_mngr | API 키 관리 메뉴 접근 |
| analysis | 분석 메뉴 접근 |
| data_spec | 데이터 스펙 메뉴 접근 |

---

> 다음 문서: [02-environment-setup.md](02-environment-setup.md)


---pb---

# 3 환경 설정

> **기준 버전 / 최종 확인일**: v1.1.0 · 2026-07-22

## 3.1 .env 파일 설정

`.env` 파일은 환경별 설정을 관리합니다.

### 3.1.1 필수 설정 항목

```env
# Database
DB_HOST=localhost
DB_NAME=etl_db_dev
DB_USER=[사용자명]
DB_PASSWORD=[비밀번호]
DB_PORT=5432

# Flask
FLASK_HOST=0.0.0.0
FLASK_PORT=18080
FLASK_DEBUG=False

# Session
ADMIN_SESSION_LIFETIME_DAYS=7
DEFAULT_SESSION_LIFETIME_MINUTES=20

# Mail
MAIL_SERVER=100.1.28.73
MAIL_PORT=25
```

## 3.2 로컬 개발 환경 구축

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

## 3.3 운영 환경 설정

| 항목 | 경로/값 |
|------|---------|
| 배포 경로 | `/data/external_data_monitoring/msys/` |
| Python 환경 | `/data/external_data_monitoring/.web/bin/activate` |
| 로그 경로 | `/data/external_data_monitoring/log/` |

---

> 다음 문서: [03-deployment.md](03-deployment.md)


---pb---

# 4 배포 절차

> **기준 버전 / 최종 확인일**: v1.1.0 · 2026-07-22

## 4.1 배포 전 체크리스트

- [ ] 소스 코드 최신화 (git pull)
- [ ] `.env` 파일 백업
- [ ] DB 마이그레이션 필요 여부 확인
- [ ] 의존성 변경 여부 확인 (`requirements.txt`)

## 4.2 배포 절차

```bash
# 1. 기존 프로세스 중지
./kill_data_moni.sh

# 2. 백업 생성
cp -r /data/external_data_monitoring/msys /data/external_data_monitoring/msys_backup_$(date +%Y%m%d)

# 3. 소스 배포
# ZIP 파일을 scp로 전송 후 압축 해제
unzip msys.zip -d /data/external_data_monitoring/msys/

# 4. 권한 설정
chown -R etl_user:etl_user /data/external_data_monitoring/msys

# 5. 가상환경 활성화
source /data/external_data_monitoring/.web/bin/activate

# 6. 의존성 설치 (변경 시)
pip install -r requirements.txt

# 7. 서비스 기동
./start_moni.sh

# 8. 기동 확인
ps -ef | grep msys
tail -f /data/external_data_monitoring/log/external_data_monitoring.log
```

## 4.3 롤백 절차

```bash
# 1. 기존 프로세스 중지
./kill_data_moni.sh

# 2. 백업 복원
cp -r /data/external_data_monitoring/msys_backup_YYYYMMDD/* /data/external_data_monitoring/msys/

# 3. 서비스 기동
./start_moni.sh
```

---

> 다음 문서: [04-common-menus/](04-common-menus/)


---pb---

# 5.1 대시보드

> **기준 버전 / 최종 확인일**: v1.1.0 · 2026-07-22


> **핵심 기능**: 수집 작업의 전반적인 현황을 한눈에 모니터링하고, Job ID별 상세 성공률 및 이벤트 로그를 조회합니다.

---

## 5.1.1 메뉴 접속 방법

- **경로**: 상단 메뉴 → 대시보드 (또는 `/` 루트 URL)
- **URL**: `/dashboard`
- **필요 권한**: `dashboard`
- **로그**: 메뉴 접근 시 `tb_user_acs_log` 테이블에 접근 이력이 기록됩니다.

---

## 5.1.2 화면 구성

### 5.1.2.1 전체 화면 구조

![대시보드 전체 화면](images/dashboard-full.png)

### 5.1.2.2 각 영역 상세 설명

#### ① 날짜 선택 카드 (`date-selection-card`)

| 요소 | ID | 설명 |
|------|-----|------|
| 시작일 | `startDate` | 조회 시작 날짜 (기본값: 올해 1월 1일) |
| 종료일 | `endDate` | 조회 종료 날짜 (기본값: 오늘) |
| 전체 데이터 조회 | `allDataCheckbox` | 체크 시 날짜 선택 없이 전체 기간 조회 |
| 조회 버튼 | - | 데이터를 다시 로드합니다 |
| 실 존재 데이터 기간 | `minDateDisplay` ~ `maxDateDisplay` | DB에 실제로 존재하는 데이터의 최소/최대 날짜 |

**동작 로직:**
- 페이지 진입 시 자동으로 올해 1월 1일 ~ 오늘(KST 기준)로 설정됩니다.
- `전체 데이터 조회` 체크 시 시작일/종료일 입력 필드가 비활성화되고, 전체 기간 데이터를 조회합니다.
- 날짜 변경 또는 체크박스 변경 시 자동으로 `loadDashboardSummary()`가 호출되어 데이터가 갱신됩니다.
- 조회 버튼 클릭 시에도 동일하게 데이터가 갱신됩니다.

**주의사항:**
- 시작일이 종료일보다 늦을 수 없습니다 (백엔드에서 400 에러 반환).
- 종료일은 실제로 `end_date + 1일`로 처리되어 해당 종료일까지의 데이터가 포함됩니다.

---

#### ② 요약 패널 (`dashboard-main-grid`)

##### 2.2.1 총 Job ID 개수 (`totalJobsCount`)

- **표시 내용**: 현재 조회된 데이터에서 활성화된 Job ID의 총 개수
- **계산 로직**: `summaryData.length` (CHRT_DSP_YN='N'으로 숨겨진 Job은 제외)
- **아이콘**: ⚙️ (톱니바퀴)

![요약 패널](images/dashboard-summary-panel.png)

##### 2.2.2 총 호출 건수 (`totalCollectionsCount`)

- **표시 내용**: 전체 Job의 총 호출(수집 시도) 건수
- **계산 로직**: 모든 Job의 `(성공 + 실패 + 미수집)` 건수 합계
- **포맷**: 한글 단위 변환 (예: 12,345 → 1.2만)
- **아이콘**: 📊 (차트)

##### 2.2.3 기간별 수집 현황

일간/주간/월간/연간 성공률을 표시합니다.

| 기간 | ID | 계산식 | 기본 임계값 |
|------|-----|--------|------------|
| 일간 | `daySuccessRate` | 일간 성공 / (일간 성공 + 일간 실패 + 일간 미수집) × 100 | 95% |
| 주간 | `weekSuccessRate` | 주간 성공 / (주간 성공 + 주간 실패 + 주간 미수집) × 100 | 90% |
| 월간 | `monthSuccessRate` | 월간 성공 / (월간 성공 + 월간 실패 + 월간 미수집) × 100 | 85% |
| 반기 | `halfSuccessRate` | 반기 성공 / (반기 성공 + 반기 실패 + 반기 미수집) × 100 | 80% |
| 연간 | `yearSuccessRate` | 연간 성공 / (연간 성공 + 연간 실패 + 연간 미수집) × 100 | 75% |

**색상 기준:**
- 임계값 이상: `srSuccessColor` (기본 녹색 #28a745)
- 임계값 미만: `srWarningColor` (기본 노란색 #ffc107)

---

#### ③ Job ID별 상세 현황 테이블 (`job-details-card`)

**접이식 동작:** 카드 헤더를 클릭하면 내용이 접히거나 펼쳐집니다.

##### 테이블 컬럼 상세

| 컬럼 | 데이터 | 설명 |
|------|--------|------|
| **Job ID** | `job_id` | 수집 작업 고유 ID. 관리자는 Airflow 링크로 이동 가능 |
| **데이터명** | `cd_nm` | `tb_con_mst`의 코드명 |
| **주기(cron)** | `frequency` | 수집 주기 (cron 표현식). 하단에 해석된 텍스트 표시 |
| **총 호출 건수** | `overall_total` | 성공 + 실패 + 미수집 + 기타 건수 |
| **일간 성공률** | `day_success / day_total` | 오늘 기준 성공률. 아이콘 + 색상 + 툴팁 |
| **주간 성공률** | `week_success / week_total` | 최근 7일 기준 |
| **월간 성공률** | `month_success / month_total` | 최근 30일 기준 |
| **반기 성공률** | `half_success / half_total` | 최근 6개월 기준 |
| **연간 성공률** | `year_success / year_total` | 최근 1년 기준 |

![Job ID별 상세 현황 테이블](images/dashboard-job-details.png)

##### Job ID 표시 로직

**아이콘 및 색상:**
- `cnn_failr_icon_id` + `cnn_failr_wrd_colr`: 연속 실패(임계값 초과) 시
- `cnn_warn_icon_id` + `cnn_warn_wrd_colr`: 연속 실패(경고 임계값) 시  
- `cnn_sucs_icon_id` + `cnn_sucs_wrd_colr`: 정상 시

**연속 실패 (`fail_streak`):**
- 최근 10회 실행 중 `CD902`(장애) 또는 `CD903`(미수집) 상태인 횟수
- 계산 쿼리: `SELECT COUNT(*) FROM (SELECT status FROM TB_CON_HIST WHERE job_id = ? ORDER BY start_dt DESC LIMIT 10) WHERE status IN ('CD902', 'CD903')`

**임계값 비교:**
- `fail_streak >= cnn_failr_thrs_val` (기본 3회): 위험(빨간색)
- `fail_streak >= cnn_warn_thrs_val` (기본 1회): 경고(노란색)
- 그 외: 정상(녹색)

##### 성공률 표시 로직

**성공률 계산:**
```
성공률 = success / (success + fail + no_data) × 100
```
- `no_data`(CD904, 진행중)는 분모에 포함되지 않음

**아이콘:**
- 임계값 이상: `sucs_rt_sucs_icon_id` (기본 없음)
- 임계값 미만: `sucs_rt_warn_icon_id` (기본 없음)

**하단 툴팁:**
```
(성공건수, 진행중건수, 실패건수/미수집건수/기타건수)
```

##### 검색 및 필터링

- **검색 (`detailTableSearch`)**: Job ID, 데이터명(`cd_nm`), 주기(`frequency`)로 실시간 필터링
- **행 수 (`detailTablePageSize`)**: 5/10/20/50/100개 선택 가능
- **페이징**: 하단 페이지네이션 버튼으로 이동

**필터링 로직:**
```javascript
filteredData = allData.filter(item => 
  item.job_id.toLowerCase().includes(searchTerm) ||
  item.cd_nm.toLowerCase().includes(searchTerm) ||
  item.frequency.toLowerCase().includes(searchTerm)
)
```

![실시간 검색 결과](images/dashboard-job-details-search.png)

---

#### ④ 이벤트 로그 (`event-log-card`)

**접이식 동작:** 카드 헤더를 클릭하면 내용이 접히거나 펼쳐집니다.

##### 데이터 출처

- **테이블**: `tb_con_hist_evnt_log`
- **컬럼**: `EVNT_CHG_ROW` (JSONB)에서 추출
  - `con_id`: 수집 ID
  - `start_dt`: 시작 시간
  - `end_dt`: 종료 시간
  - `job_id`: Job ID
  - `rqs_info`: 요청 정보
  - `status`: 상태 코드

##### 상태 코드 정의

| 코드 | 의미 | 설명 | 아이콘 |
|------|------|------|--------|
| CD901 | 정상 수집 | 수집 완료 | 관리자 설정 아이콘 또는 🔔 |
| CD902 | 장애 발생 | 실패 | 관리자 설정 아이콘 또는 🔔 |
| CD903 | 미수집 | 데이터 없음 | 관리자 설정 아이콘 또는 🟠 |
| CD904 | 수집중 | 진행 중 | 관리자 설정 아이콘 또는 🔔 |
| AUTH_LOGIN_SUCCESS | 로그인 성공 | 시스템 이벤트 | - |
| AUTH_REGISTER | 가입 신청 | 시스템 이벤트 | - |
| AUTH_APPROVE | 가입 승인 | 시스템 이벤트 | - |
| AUTH_REJECT | 가입 거절 | 시스템 이벤트 | - |
| AUTH_DELETE | 사용자 삭제 | 시스템 이벤트 | - |
| AUTH_RESET_PW | 비밀번호 초기화 | 시스템 이벤트 | - |
| AUTH_CHANGE_PW | 비밀번호 변경 | 시스템 이벤트 | - |

![이벤트 로그 (펼침)](images/dashboard-event-log.png)

##### 표시 컬럼

| 컬럼 | 내용 | 설명 |
|------|------|------|
| 시간 | `start_dt` | 이벤트 발생 시간 (KST) |
| 아이콘 | 상태별 아이콘 | 관리자 설정 또는 기본 아이콘 |
| Job ID | `job_id` | 작업 ID (시스템 이벤트는 'System') |
| 상태 | `status` → 해석 | CD901 → '정상 수집' 등 |
| 수집 건수 | `rqs_info` 파싱 | "총 요청 수: N, 실패: M"에서 추출 |
| 성공률 | 계산 | 성공 / 총 × 100 |
| 설명 | `status` → 해석 | '수집완료', '실패', '미수집', '진행중' |
| 수집 시간 | `end_dt - start_dt` | 소요 시간 (시간 단위, 소수점 1자리) |

##### 조작 기능

- **시작일/종료일 필터**: 날짜 변경 시 자동 조회
- **검색 (`eventLogSearch`)**: Job ID, 상태, 설명으로 실시간 필터링
- **행 수 (`eventLogPageSize`)**: 5/10/20/50/100개 선택
- **페이징**: 하단 페이지네이션
- **이벤트 로그 저장 버튼** (`save-event-log-btn`):
  - 현재 조회된 전체 이벤트 로그를 서버에 JSON으로 저장
  - API: `POST /api/save-event-log`
  - 저장 완료 시 파일 경로 표시 (2초 후 원래 텍스트로 복귀)

---

## 5.1.3 데이터 흐름 및 처리 로직

### 5.1.3.1 전체 데이터 흐름도

![전체 데이터 흐름도](images/01-dashboard-data-flow.png)

### 5.1.3.2 오늘 데이터 처리 상세

**CollectionScheduleService.get_schedule_only():**
- 오늘(KST 기준)의 수집 스케줄을 조회
- 상태 코드 분류:
  - `CD901`: 성공
  - `CD902`, `CD903`: 실패
  - `CD904`: 진행 중
  - 기타: 미수집
  - `CD907`: 스케줄 제외 (total_scheduled에서 제외)

**병합 로직:**
- 과거 데이터(`TB_CON_HIST`)와 오늘 데이터를 Job ID 기준으로 병합
- 오늘 데이터는 `day_*` 필드에 저장 (day_success, day_fail_count, day_ing_count, day_no_data_count, day_total_scheduled)
- 과거 데이터는 `week_*`, `month_*`, `half_*`, `year_*` 필드에 저장

### 5.1.3.3 관리자 설정 적용

**`tb_mngr_sett` 설정 항목:**

| 설정 항목 | 컬럼명 | 기본값 | 설명 |
|-----------|--------|--------|------|
| 대시보드 표시 여부 | `CHRT_DSP_YN` | Y | N인 경우 대시보드에서 제외 |
| 연속 실패 임계값(위험) | `cnn_failr_thrs_val` | 3 | 이 횟수 이상 연속 실패 시 빨간색 |
| 연속 실패 임계값(경고) | `cnn_warn_thrs_val` | 1 | 이 횟수 이상 연속 실패 시 노란색 |
| 연속 실패 성공 아이콘 | `cnn_sucs_icon_id` | - | 정상 상태 아이콘 |
| 연속 실패 경고 아이콘 | `cnn_warn_icon_id` | - | 경고 상태 아이콘 |
| 연속 실패 위험 아이콘 | `cnn_failr_icon_id` | - | 위험 상태 아이콘 |
| 일간 성공률 임계값 | `dly_sucs_rt_thrs_val` | 95 | % |
| 주간 성공률 임계값 | `dd7_sucs_rt_thrs_val` | 90 | % |
| 월간 성공률 임계값 | `mthl_sucs_rt_thrs_val` | 85 | % |
| 반기 성공률 임계값 | `mc6_sucs_rt_thrs_val` | 80 | % |
| 연간 성공률 임계값 | `yy1_sucs_rt_thrs_val` | 75 | % |
| 성공률 성공 아이콘 | `sucs_rt_sucs_icon_id` | - | 임계값 이상 아이콘 |
| 성공률 경고 아이콘 | `sucs_rt_warn_icon_id` | - | 임계값 미만 아이콘 |

---

## 5.1.4 조작 방법

### 5.1.4.1 날짜 범위 변경하여 조회

**조작 절차:**
1. `시작일` 입력 필드 클릭 → 날짜 선택
2. `종료일` 입력 필드 클릭 → 날짜 선택
3. `조회` 버튼 클릭 (또는 Enter)
4. 요약 패널과 상세 테이블이 자동 갱신됨

**확인 방법:**
- 요약 패널의 숫자가 변경되는지 확인
- 상세 테이블의 데이터가 갱신되는지 확인
- 상단에 초록색 토스트 메시지 "대시보드 요약 업데이트 완료" 표시

### 5.1.4.2 전체 기간 조회

**조작 절차:**
1. `전체 데이터 조회` 체크박스 클릭
2. 시작일/종료일 필드가 비활성화됨
3. 데이터가 자동으로 갱신됨

### 5.1.4.3 Job ID 검색

**조작 절차:**
1. 상세 테이블 우측 상단 `검색` 입력 필드에 텍스트 입력
2. 입력 즉시(Job ID, 데이터명, 주기 중 하나라도 포함) 필터링됨

### 5.1.4.4 이벤트 로그 조회

**조작 절차:**
1. `이벤트 로그` 카드 펼치기 (헤더 클릭)
2. 시작일/종료일 설정
3. `조회` 버튼 클릭
4. 이벤트 로그 목록 확인

### 5.1.4.5 이벤트 로그 저장

**조작 절차:**
1. 이벤트 로그 조회
2. 좌측 하단 `이벤트 로그 저장` 버튼 클릭
3. `저장 완료: [파일경로]` 메시지 확인

**주의사항:**
- 저장할 데이터가 없으면 "저장할 이벤트 로그 데이터가 없습니다" 경고 표시
- 저장 실패 시 "저장 실패" 표시 (2초 후 원래 텍스트로 복귀)

![이벤트 로그 (접힘)](images/dashboard-event-log-collapsed.png)

---

## 5.1.5 운영 시나리오

> 실제 운영 업무를 순서대로 재현한다. 각 단계에는 조작하는 **요소만 캡처한 이미지**를 붙인다(§2 캡처 규칙). 이미지는 `images/`에 아래 파일명으로 저장.

### 5.1.5.1 아침 점검 — 야간 수집 결과 확인 및 실패 Job 대응

- **상황/목표**: 매일 오전, 전일 야간 수집이 정상 완료됐는지 확인하고 실패한 Job을 조기에 발견·조치한다.
- **사전 조건**: `dashboard` 권한 보유, 로그인 상태.
- **단계**:
  1. 상단 메뉴 → **대시보드** 진입. 요약 패널에서 **일간 성공률**을 확인한다.
     ![요약 패널 일간 성공률](images/dashboard-summary-panel.png)
     - 임계값(기본 95%) 미만이면 노란색 → 상세 확인 필요.
  2. **Job ID별 상세 현황** 카드를 펼치고, **연속 실패(빨간색)** Job이 있는지 훑는다.
     ![연속 실패 Job 행](images/dashboard-job-details.png)
  3. 해당 Job ID를 상세 테이블 **검색(`detailTableSearch`)** 에 입력해 좁힌다.
     ![Job ID 검색](images/dashboard-job-details-search.png)
  4. **이벤트 로그** 카드를 펼쳐 그 Job의 최근 상태(CD902 장애/CD903 미수집)를 확인한다.
     ![이벤트 로그 상태 확인](images/dashboard-event-log.png)
  5. 필요 시 **이벤트 로그 저장(`save-event-log-btn`)** 으로 근거를 파일로 남긴다.
- **완료 확인**: 실패 Job의 원인(상태 코드·시간)을 파악하고, 조치 대상 목록을 확보. 저장 시 `저장 완료: [파일경로]` 토스트 확인.
- **실패 시 대응**: 성공률 0%·데이터 없음 등은 §7 자주 발생하는 문제 표 참조(수집 스케줄/에이전트 상태 점검은 [02-collection-schedule.md](02-collection-schedule.md) 연계).

### 5.1.5.2 기간 지정 리포트 — 특정 구간 성공률 확인

- **상황/목표**: 주간 보고를 위해 특정 기간의 수집 성공률을 확인한다.
- **단계**:
  1. **시작일(`startDate`)·종료일(`endDate`)** 을 지정하고 **조회** 클릭.
     ![기간 지정 조회](images/dashboard-date-selection.png)
  2. 요약 패널의 주간/월간 성공률과 총 호출 건수를 캡처해 보고에 사용.
- **완료 확인**: "대시보드 요약 업데이트 완료" 토스트 + 숫자 갱신.

---

## 5.1.6 모니터링 체크리스트

- [ ] **총 Job ID 개수**가 예상 범위 내인지 확인 (보통 100~200개)
- [ ] **총 호출 건수**가 0이 아닌지 확인
- [ ] **일간 성공률**이 95% 이상인지 확인
- [ ] **주간 성공률**이 90% 이상인지 확인
- [ ] **연속 실패**가 3회 이상인 Job(빨간색)이 있는지 확인
- [ ] **이벤트 로그**에 비정상적인 에러가 없는지 확인
- [ ] `전체 데이터 조회` 시에도 데이터가 로드되는지 확인

---

## 5.1.7 자주 발생하는 문제

| 증상 | 원인 | 해결 방법 |
|------|------|-----------|
| 대시보드가 비어있음 (데이터 없음) | 날짜 범위 내 데이터 없음 | 전체 데이터 조회 체크 또는 날짜 범위 확대 |
| 특정 Job이 표시되지 않음 | `CHRT_DSP_YN='N'` 설정됨 | 관리자 설정 → 해당 Job의 대시보드 표시 여부 확인 |
| 성공률이 0%로 표시됨 | 해당 기간 내 수집 이력 없음 | 데이터 수집 스케줄/에이전트 상태 확인 |
| 연속 실패 횟수가 이상함 | 상태 코드 분류 오류 | `tb_sts_cd_mst`의 성공/실패 코드 설정 확인 |
| 이벤트 로그에 AUTH_ 이벤트만 있음 | 비관리자 계정으로 조회 | 관리자 권한 확인 (비관리자는 시스템 이벤트 필터링됨) |
| 이벤트 로그 저장 실패 | 서버 디스크 공간 부족 | 서버 디스크 여유 공간 확인 |

---

## 5.1.8 관련 DB 테이블 및 쿼리

### 5.1.8.1 주요 테이블

| 테이블 | 설명 |
|--------|------|
| `tb_con_hist` | 수집 실행 이력 (Job ID별 성공/실패 상태) |
| `tb_con_hist_evnt_log` | 이벤트 로그 (JSONB 형태로 변경 전/후 데이터 저장) |
| `tb_con_mst` | 수집 작업 마스터 (Job ID, 주기, 데이터명) |
| `tb_mngr_sett` | 관리자 설정 (성공률 임계값, 색상, 아이콘) |
| `tb_icon` | 아이콘 마스터 |
| `tb_user_data_perm_auth_ctrl` | 사용자별 데이터 접근 권한 |

### 5.1.8.2 연속 실패 계산 쿼리

```sql
SELECT COUNT(*) as fail_count
FROM (
    SELECT status
    FROM TB_CON_HIST
    WHERE job_id = ?
    ORDER BY start_dt DESC
    LIMIT 10
) recent_runs
WHERE status IN ('CD902', 'CD903')
```

### 5.1.8.3 이벤트 로그 조회 쿼리

```sql
SELECT
    (EVNT_CHG_ROW ->> 'con_id')::text AS con_id,
    EVNT_OCCR_TIME AS start_dt,
    (EVNT_CHG_ROW ->> 'end_dt')::timestamptz AS end_dt,
    (EVNT_CHG_ROW ->> 'job_id')::text AS job_id,
    (EVNT_CHG_ROW ->> 'rqs_info')::text AS rqs_info,
    (EVNT_CHG_ROW ->> 'status')::text AS status
FROM TB_CON_HIST_EVNT_LOG
WHERE EVNT_OCCR_TIME >= ? AND EVNT_OCCR_TIME <= ?
ORDER BY EVNT_OCCR_TIME DESC
```

---

---



---pb---

# 5.2 데이터 수집 일정

> **기준 버전 / 최종 확인일**: v1.1.0 · 2026-07-22


> **핵심 기능**: 주간/월간 단위로 데이터 수집 작업의 예정 및 실제 실행 상태를 히트맵 형태로 모니터링하고, 그룹별/Job별 상세 현황과 메모를 관리합니다.

---

## 5.2.1 메뉴 접속 방법

- **경로**: 상단 메뉴 → 수집 스케줄
- **URL**: `/collection_schedule`
- **필요 권한**: `collection_schedule`
- **로그**: 메뉴 접근 시 `tb_user_acs_log` 테이블에 접근 이력이 기록됩니다.

---

## 5.2.2 화면 구성

### 5.2.2.1 전체 화면 구조

![수집 스케줄 전체 화면](images/collection-schedule-full.png)

### 5.2.2.2 각 영역 상세 설명

#### ① 히트맵 컨테이너 (`.heatmap-container`)

| 요소 | 선택자 | 설명 |
|------|--------|------|
| 제목 | `.card-title` | "주간 수집 현황 히트맵" 또는 "월간 수집 현황 히트맵" |
| 요약 통계 | `.summary-stats` | 전체 예정 / 성공 / 실패 / 미수집 건수 |
| 캘린더 그리드 | `#calendar-grid` | 7열(주간) 또는 N열(월간) 그리드 |
| 설정 패널 | `#settings-container` | 그룹화 임계값, 색상 기준 (기본 접힘) |

#### ② 컨트롤 영역 (`.controls`)

| 요소 | ID | 설명 |
|------|-----|------|
| 주간 버튼 | `#weekly-btn` | 주간 뷰로 전환 (기본값) |
| 월간 버튼 | `#monthly-btn` | 월간 뷰로 전환 |
| 이전 주 | `#prev-week-btn` | 한 주 이전으로 이동 |
| 다음 주 | `#next-week-btn` | 한 주 이후로 이동 |
| 이전 달 | `#prev-month-btn` | 한 달 이전으로 이동 |
| 다음 달 | `#next-month-btn` | 한 달 이후로 이동 |

**동작 로직:**
- 버튼 클릭 시 `week_offset` 또는 `month_offset` 값이 증감
- `/api/collection_schedule?week_offset=N` API 호출
- 응답 데이터로 캘린더 그리드 재렌더링

![컨트롤 영역](images/collection-schedule-controls.png)

#### ③ 캘린더 그리드 (`#calendar-grid`)

**Day 열 구조:**
```
┌──────────────┐
│ 월 01/13     │  ← .day-header (요일 + 날짜)
├──────────────┤
│ [CD101]      │  ← .job-pill (단일 Job)
│ [CD102]      │     상태별 색상: 초록(성공), 빨강(실패), 주황(미수집)
│ [그룹A ▶]    │  ← .group-pill-summary (그룹화된 Job)
│  진행률 ████ │     마우스 오버 시 팝업으로 상세 Job 목록 표시
└──────────────┘
```

**Job 상태별 색상:**
| 상태 | 클래스 | 색상 | 의미 |
|------|--------|------|------|
| 성공 | `.status-success` | 배경: #dcfce7, 글자: #166534 | 수집 완료 |
| 실패 | `.status-fail` | 배경: #fee2e2, 글자: #991b1b | 수집 실패 |
| 미수집 | `.status-nodata` | 배경: #ffedd5, 글자: #9a3412 | 데이터 없음 |
| 진행중 | `.status-inprogress` | 배경: #fef9c3, 글자: #854d0e | 수집 진행 중 |
| 예정 | `.status-scheduled` | 배경: #e5e7eb, 글자: #4b5563 | 아직 실행 전 |

![캘린더 그리드](images/collection-schedule-calendar.png)

#### ④ 그룹 팝업 (`.popup`)

![그룹 팝업](images/collection-schedule-group-popup.png)

**표시 조건:** 그룹화된 Job 셀 클릭
**표시 내용:**
- 그룹 내 개별 Job 목록 (페이징 지원)
- 각 Job의 상태별 색상 유지
- 페이지네이션: ← 1 / 3 →

#### ⑤ 표시 모드 선택 (`#display-mode-selector`)

| 모드 | 값 | 표시 내용 |
|------|-----|----------|
| 명칭 | `name` | Job의 한글 이름 (`cd_nm`) |
| 코드 | `code` | Job ID (예: CD101) |
| 설명 | `desc` | Job 상세 설명 |

#### ⑥ 그룹 메모 팝업 (`#memo-popup`)

![그룹 메모 팝업](images/collection-schedule-memo-popup.png)

**표시 조건:** 그룹 셀의 `+` 버튼 클릭 (관리자만)
**기능:**
- 메모 작성/수정/삭제
- 작성자, 작성일시 표시
- 그룹 ID, 날짜 자동 매핑

#### ⑦ 가이드 버튼 (`#guide-toggle-btn`)

**위치:** 화면 우측 하단 고정 (원형 `?` 버튼)
**표시 내용:**
- 그룹 항목 색상 가이드 (상태별 색상 코드)
- 상세 데이터 상태 가이드

![설정 패널 (펼침)](images/collection-schedule-settings-expanded.png)

---

## 5.2.3 데이터 흐름 및 처리 로직

### 5.2.3.1 전체 데이터 흐름도

![전체 데이터 흐름도](images/02-collection-schedule-data-flow.png)

### 5.2.3.2 주요 처리 단계

**1단계: 스케줄 생성 (`_generate_scheduled_tasks`)**
- `tb_con_mst`의 cron 표현식 기반
- 시작일~종료일 범위 내 예정된 실행 시간 계산
- 사용자 권한에 따른 Job 필터링

**2단계: 히스토리 조회 (`_fetch_and_group_history_data`)**
- `tb_con_hist`에서 실제 수집 기록 조회
- KST 기준 날짜로 그룹화 (`date_key + job_id`)
- 상태 코드: CD901(성공), CD902(실패), CD903(미수집), CD904(진행중)

**3단계: 매칭 (`_match_schedule_with_history`)**
- 날짜별로 스케줄과 히스토리를 시간순 정렬
- 순차 매칭: 예정 시간과 실제 실행 시간 비교
- 5분 허용 시간(Grace Period) 내 실행 → 성공으로 처리
- 자정 경계 문제 해결: 날짜 비교 제거, 시간 차이만 비교

**4단계: 그룹화**
- 관리자 설정의 `grouping_threshold` 기준
- 일정 개수 이상인 Job ID 접두사로 그룹화
- 그룹 진행률 = (성공+진행중) / 전체 × 100

---

## 5.2.4 조작 방법

### 5.2.4.1 주간/월간 뷰 전환

**조작 절차:**
1. `주간` 또는 `월간` 버튼 클릭
2. 캘린더 그리드가 즉시 전환됨

**확인 방법:**
- 버튼 활성화 상태(파란색) 변경
- 제목이 "주간 수집 현황 히트맵" → "월간 수집 현황 히트맵"으로 변경
- 캘린더 열 개수 변경 (7열 → 월 전체)

### 5.2.4.2 날짜 이동

**조작 절차:**
1. `← 지난 주` / `다음 주 →` 버튼 클릭
2. 또는 `← 지난달` / `다음달 →` 버튼 클릭

**확인 방법:**
- Day 헤더의 날짜가 변경됨
- 캘린더 그리드 데이터 갱신

### 5.2.4.3 표시 모드 변경

**조작 절차:**
1. 하단 `표시:` 라디오 버튼 그룹에서 선택
2. 명칭 / 코드 / 설명 중 선택

**확인 방법:**
- Job 셀의 텍스트가 즉시 변경됨

### 5.2.4.4 그룹 상세 보기

**조작 절차:**
1. 그룹화된 셀(예: `[그룹A ▶]`)에 마우스 오버
2. 팝업으로 개별 Job 목록 표시
3. 팝업 내 페이지네이션으로 추가 Job 확인

### 5.2.4.5 그룹 메모 작성 (관리자 전용)

**조작 절차:**
1. 그룹 셀 더블클릭
2. 메모 작성 팝업 표시
3. 텍스트 입력 후 `저장` 버튼 클릭

**확인 방법:**
- 저장 완료 시 토스트 메시지 "메모가 저장되었습니다"
- 메모가 있는 그룹 셀에 시각적 표시

### 5.2.4.6 수집 요청서 양식 다운로드

**조작 절차:**
1. 우측 상단 `수집 요청서 양식 다운로드` 버튼 클릭
2. Excel 파일(.xlsx) 다운로드

---

## 5.2.5 운영 시나리오

> 각 단계에는 조작하는 **요소만 캡처한 이미지**를 붙인다(작성 지침 `../../common/operator-manual/DEVELOPMENT/02-image-capture.md`). 이미지는 `images/`에 저장.

### 5.2.5.1 주간 수집 현황 점검 → 미수집 급증 대응

- **상황/목표**: 주간 히트맵에서 미수집이 급증한 구간을 찾아 원인(스케줄/에이전트)을 조치한다.
- **사전 조건**: `collection_schedule` 권한.
- **단계**:
  1. **주간 뷰(`#weekly-btn`)** 로 이번 주 현황 확인, 요약 통계에서 미수집 건수 확인.
     ![주간 히트맵 요약](images/collection-schedule-weekly-view.png)
  2. 주황색(`.status-nodata`) 셀이 몰린 날짜를 찾는다.
     ![미수집 셀 집중 구간](images/collection-schedule-weekly-view.png)
  3. 그룹 셀이면 클릭해 **그룹 팝업(`.popup`)** 에서 실패 Job을 특정.
  4. 해당 Job의 원인을 [대시보드 이벤트 로그](01-dashboard.md)·에이전트 로그로 확인, 필요 시 `tb_con_mst` cron 점검.
- **완료 확인**: 미수집 원인(스케줄 미등록/에이전트 장애)을 확정하고 조치 대상 확보.
- **실패 시**: §7 자주 발생하는 문제 표 참조.

### 5.2.5.2 그룹 메모로 인수인계 (관리자)

- **상황/목표**: 특정 그룹의 이슈를 메모로 남겨 다음 담당자에게 인계.
- **단계**: 그룹 셀 더블클릭 → **메모 팝업(`#memo-popup`)** 에 내용 입력 → 저장.
  ![그룹 메모 작성](images/collection-schedule-memo-popup.png)
- **완료 확인**: "메모가 저장되었습니다" 토스트 + 해당 그룹 셀에 메모 표시.

---

## 5.2.6 모니터링 체크리스트

- [ ] **전체 예정 건수**가 0이 아닌지 확인
- [ ] **성공률**이 90% 이상인지 확인
- [ ] **미수집 건수**가 급증하지 않는지 확인
- [ ] **특정 Job/그룹**이 연속 실패하는지 확인
- [ ] **그룹 메모**가 최신 상태인지 확인
- [ ] **캘린더 이동** 시 데이터가 정상 로드되는지 확인

---

## 5.2.7 자주 발생하는 문제

| 증상 | 원인 | 해결 방법 |
|------|------|-----------|
| 히트맵이 비어있음 | 데이터 수집 기록 없음 | 날짜 범위 확대 또는 데이터 수집 에이전트 상태 확인 |
| Job이 표시되지 않음 | 사용자 데이터 권한 없음 | 관리자에게 데이터 접근 권한 요청 |
| 그룹 진행률이 이상함 | 그룹화 임계값 부적절 | 관리자 설정에서 `grouping_threshold` 조정 |
| 미수집이 과다함 | 수집 에이전트 장애 또는 스케줄 미등록 | `tb_con_mst`의 cron 설정 및 에이전트 로그 확인 |
| 팝업이 표시되지 않음 | 그룹화되지 않은 단일 Job | 단일 Job은 팝업 없이 직접 상태 표시 |
| 메모 저장 실패 | 관리자 권한 없음 | 관리자 계정으로 로그인 확인 |

---

## 5.2.8 관련 DB 테이블 및 쿼리

### 5.2.8.1 주요 테이블

| 테이블 | 설명 |
|--------|------|
| `tb_con_hist` | 수집 실행 이력 (실제 성공/실패 상태) |
| `tb_con_mst` | 수집 작업 마스터 (Job ID, cron 주기, 그룹 정보) |
| `tb_mngr_sett` | 관리자 설정 (그룹화 임계값, 색상 기준) |
| `tb_grp_memo` | 그룹 메모 (그룹 ID, 날짜, 내용, 작성자) |
| `tb_user_data_perm_auth_ctrl` | 사용자별 데이터 접근 권한 |

### 5.2.8.2 스케줄 조회 API

```
GET /api/collection_schedule?view=weekly&week_offset=0
GET /api/collection_schedule?view=monthly&month_offset=0
```

**응답 구조:**
```json
[
  {
    "job_id": "CD101",
    "date": "2025-12-18",
    "status": "success",
    "scheduled_time": "06:30",
    "is_grouped": false
  },
  {
    "group_id": "GRP_A",
    "date": "2025-12-18",
    "progress": 85,
    "jobs": ["CD201", "CD202"],
    "is_grouped": true
  }
]
```

---

---



---pb---

# 5.3 차트 분석

> **기준 버전 / 최종 확인일**: v1.1.0 · 2026-07-22

> **핵심 기능**: 선택한 기간과 Job ID를 기준으로 수집 성공률 추이와 장애 코드별 비율을 차트로 시각화하여 분석합니다.

---

## 5.3.1 메뉴 접속 방법

- **경로**: 상단 메뉴 → 차트 분석
- **URL**: `/chart_analysis`
- **필요 권한**: `analysis`
- **로그**: 메뉴 접근 시 `tb_user_acs_log` 테이블에 접근 이력이 기록됩니다.

---

## 5.3.2 화면 구성

### 5.3.2.1 전체 화면 구조

![차트 분석 전체 화면](images/chart-analysis-full.png)

### 5.3.2.2 각 영역 상세 설명

#### ① 날짜 선택 카드 (`#date-selection-card-chart`)

| 요소 | ID | 설명 |
|------|-----|------|
| 시작일 | `#startDate` | 조회 시작 날짜 |
| 종료일 | `#endDate` | 조회 종료 날짜 |
| 실 존재 데이터 기간 | `#chart-min-date` ~ `#chart-max-date` | DB에 실제로 존재하는 데이터의 최소/최대 날짜 |

**동작 로직:**
- 페이지 진입 시 자동으로 올해 1월 1일 ~ 오늘(KST 기준)로 설정됩니다.
- 날짜 변경 시 차트 데이터가 자동으로 갱신됩니다.
- `collapsible_controls.html` 공통 모듈을 사용하여 접이식 동작을 제공합니다.

#### ② 차트 표시 옵션 카드 (`#chart-options-card`)

| 옵션 | 값 | 설명 |
|------|-----|------|
| 라벨 표시 방식 | `name` | Job의 한글 이름 (`cd_nm`) 표시 |
| 라벨 표시 방식 | `code` | Job ID (예: CD101) 표시 |

**동작 로직:**
- 라디오 버튼 변경 시 모든 차트의 범례와 툴팁 라벨이 즉시 변경됩니다.
- `chart_analysis.js`의 `labelDisplayType` 이벤트 리스너에서 처리합니다.

#### ③ Job ID 선택 카드 (`#job-selection-card-chart`)

| 요소 | 설명 |
|------|------|
| 모두 선택 버튼 | 모든 Job ID 체크박스 선택 |
| 모두 해제 버튼 | 모든 Job ID 체크박스 해제 |
| 개별 체크박스 | `#jobCheckboxes` 낸 각 Job ID별 체크박스 |

**동작 로직:**
- 페이지 진입 시 `tb_con_mst`의 모든 Job ID를 체크박스로 로드합니다.
- 사용자 권한(`data_permissions`)에 따라 표시되는 Job이 필터링됩니다.
- 체크박스 변경 시 차트 데이터가 자동으로 갱신됩니다.

![Job ID 선택 및 필터 패널](images/chart-analysis-filter-panel.png)

#### ④ 기간별 수집 성공률 차트 (`#success-rate-chart-card`)

| 요소 | 설명 |
|------|------|
| 차트 유형 선택 | 라인 차트 / 바 차트 전환 |
| 차트 캔버스 | `#successRateChart` (Chart.js) |
| 범례 영역 | `#successRateLegend` (세로 스크롤 지원, 최대 높이 180px) |

**데이터 출처:**
- API: `GET /api/chart_data` (또는 `/api/analysis/chart`)
- Service: `AnalysisService.get_dynamic_chart_data()`
- Mapper: `AnalysisMapper.get_dynamic_chart_data()`
- SQL: `sql/analytics/analytics_sql.py`

**차트 데이터 구조:**
```json
[
  {
    "job_id": "CD101",
    "date": "2025-01",
    "success_rate": 95.5,
    "success_count": 100,
    "fail_count": 5,
    "total_count": 105
  }
]
```

**색상 및 스타일:**
- 각 Job ID별 고유 색상 자동 할당
- 라인 차트: `tension: 0.3` (부드러운 곡선)
- 바 차트: `barPercentage: 0.7`
- 범례: 하단 세로 스크롤, 가로 배치 (`flex-wrap: wrap`)

#### ⑤ 장애 코드별 비율 차트 (`#trouble-code-chart-card`)

| 요소 | 설명 |
|------|------|
| 차트 유형 선택 | 도넛 차트 / 바 차트 전환 |
| 차트 캔버스 | `#troublePieChart` (Chart.js) |

**데이터 출처:**
- `tb_con_hist`의 `status` 컬럼 집계
- 선택된 기간 및 Job ID 필터 적용

**표시 데이터:**
| 상태 코드 | 의미 | 색상 |
|-----------|------|------|
| CD901 | 정상 수집 | 녹색 계열 |
| CD902 | 장애 발생 | 빨간색 계열 |
| CD903 | 미수집 | 주황색 계열 |
| CD904 | 수집중 | 노란색 계열 |
| 기타 | 기타 상태 | 회색 계열 |

---

## 5.3.3 데이터 흐름 및 처리 로직

### 5.3.3.1 전체 데이터 흐름도

![전체 데이터 흐름도](images/03-chart-analysis-data-flow.png)

### 5.3.3.2 성공률 계산 로직

```
성공률 = (성공 건수 / (성공 건수 + 실패 건수 + 미수집 건수)) × 100
```
- `CD904`(진행중)은 분모에 포함되지 않음
- 기간별(월간/주간/일간) 그룹화는 SQL의 `GROUP BY`로 처리

### 5.3.3.3 권한 필터링

**관리자(`mngr_sett`):**
- 모든 Job ID 조회 가능
- 요청된 `job_ids` 파라미터 그대로 사용

**일반 사용자:**
- `TB_USER_DATA_PERM_AUTH_CTRL`에서 허용된 Job ID만 조회
- 요청된 `job_ids`와 교집합(intersection)으로 필터링

---

## 5.3.4 조작 방법

### 5.3.4.1 날짜 범위 변경

**조작 절차:**
1. `시작일` 입력 필드 클릭 → 날짜 선택
2. `종료일` 입력 필드 클릭 → 날짜 선택
3. 차트가 자동으로 갱신됨

**확인 방법:**
- 차트의 X축(날짜 범위)이 변경되는지 확인
- 데이터 포인트 개수가 변경되는지 확인

### 5.3.4.2 Job ID 필터링

**조작 절차:**
1. `Job ID 선택` 카드 펼치기 (헤더 클릭)
2. 체크박스로 표시할 Job ID 선택/해제
3. 또는 `모두 선택` / `모두 해제` 버튼 사용

**확인 방법:**
- 차트에 표시되는 선/막대 개수가 변경됨
- 범례 목록이 변경됨

### 5.3.4.3 차트 유형 전환

**조작 절차:**
1. `기간별 수집 성공률` 또는 `장애 코드별 비율` 카드 펼치기
2. `라인 차트` / `바 차트` 또는 `도넛 차트` / `바 차트` 라디오 버튼 선택

**확인 방법:**
- 차트가 즉시 해당 유형으로 변경됨
- 라인 차트 → 선 그래프, 바 차트 → 막대 그래프, 도넛 차트 → 원형 그래프

### 5.3.4.4 라벨 표시 방식 변경

**조작 절차:**
1. `차트 표시 옵션` 카드 펼치기
2. `명칭` 또는 `코드` 라디오 버튼 선택

**확인 방법:**
- 차트 범례의 Job 이름이 변경됨 (예: "CD101" → "기상청예보")
- 툴팁의 라벨도 동일하게 변경됨

---

## 5.3.5 모니터링 체크리스트

- [ ] **성공률 추이**가 안정적인지 확인 (급격한 하락 여부)
- [ ] **특정 Job**의 성공률이 지속적으로 낮은지 확인
- [ ] **장애 코드 비율**에서 CD902(장애) 비율이 높지 않은지 확인
- [ ] **데이터 기간**이 충분히 넓은지 확인 (최소 3개월 이상 권장)
- [ ] **Job ID 선택**이 너무 많아 차트가 복잡하지 않은지 확인
- [ ] **범례**가 정상적으로 표시되는지 확인 (세로 스크롤 필요 시)

---

## 5.3.6 자주 발생하는 문제

| 증상 | 원인 | 해결 방법 |
|------|------|-----------|
| 차트가 비어있음 | 선택된 Job ID 없음 또는 데이터 없음 | Job ID 선택 확인, 날짜 범위 확대 |
| 성공률이 0%로 표시됨 | 해당 기간 내 수집 이력 없음 | 데이터 수집 스케줄/에이전트 상태 확인 |
| 특정 Job이 보이지 않음 | 사용자 데이터 권한 없음 | 관리자에게 데이터 접근 권한 요청 |
| 범례가 짤려서 보임 | 선택 Job ID가 너무 많음 | 일부 Job만 선택하거나 차트 카드 확대 |
| 차트 로딩이 느림 | 조회 기간이 너무 김 | 시작일/종료일 범위를 좁혀서 조회 |
| 장애 코드가 부정확함 | 상태 코드 분류 오류 | `tb_sts_cd_mst`의 성공/실패 코드 설정 확인 |

---

## 5.3.7 관련 DB 테이블 및 쿼리

### 5.3.7.1 주요 테이블

| 테이블 | 설명 |
|--------|------|
| `tb_con_hist` | 수집 실행 이력 (성공/실패 상태, 시간) |
| `tb_con_mst` | 수집 작업 마스터 (Job ID, 데이터명) |
| `tb_sts_cd_mst` | 상태 코드 마스터 (CD901~CD904 정의) |
| `tb_user_data_perm_auth_ctrl` | 사용자별 데이터 접근 권한 |

### 5.3.7.2 차트 데이터 조회 API

```
GET /api/chart_data?start_date=2025-01-01&end_date=2025-12-31&job_ids=CD101,CD102
```

**응답 구조:**
```json
[
  {
    "job_id": "CD101",
    "cd_nm": "기상청예보",
    "date": "2025-01",
    "success_rate": 95.5,
    "success_count": 100,
    "fail_count": 5,
    "no_data_count": 0,
    "total_count": 105
  }
]
```

---

> 다음 문서: [04-data-analysis.md](04-data-analysis.md)


---pb---

# 5.4 데이터 분석

> **기준 버전 / 최종 확인일**: v1.1.0 · 2026-07-22

> **핵심 기능**: 수집 데이터의 소요 시간, 성공률, 연속 실패 등 다양한 지표를 분석하여 데이터 품질과 수집 안정성을 평가합니다.

---

## 5.4.1 메뉴 접속 방법

- **경로**: 상단 메뉴 → 데이터 분석
- **URL**: `/data_analysis`
- **필요 권한**: `analysis`
- **로그**: 메뉴 접근 시 `tb_user_acs_log` 테이블에 접근 이력이 기록됩니다.

---

## 5.4.2 화면 구성

### 5.4.2.1 전체 화면 구조

![데이터 분석 전체 화면](images/data-analysis-full.png)

### 5.4.2.2 각 영역 상세 설명

#### ① 필터 카드 (`#filter-card`)

| 요소 | ID | 설명 |
|------|-----|------|
| 시작일 | `#startDate` | 조회 시작 날짜 |
| 종료일 | `#endDate` | 조회 종료 날짜 |
| Job ID | `#jobIdSelect` | 특정 Job ID 필터 (기본: 전체) |
| 장애코드 | `#errorCodeSelect` | 특정 장애 코드 필터 (기본: 전체) |
| 실 존재 데이터 기간 | `#data-min-date` ~ `#data-max-date` | DB에 실제로 존재하는 데이터의 최소/최대 날짜 |

**동작 로직:**
- 페이지 진입 시 자동으로 올해 1월 1일 ~ 오늘(KST 기준)로 설정됩니다.
- 필터 변경 시 상단 요약 카드와 하단 테이블이 자동으로 갱신됩니다.
- Job ID와 장애코드 드롭다운은 `tb_con_mst` 및 `tb_sts_cd_mst`에서 동적으로 로드됩니다.

#### ② 요약 카드 (3개)

| 카드 | ID | 내용 | 색상 |
|------|-----|------|------|
| 최대/최소 소요 시간 | `#durationRangeCard` | 선택 기간 내 수집 소요 시간의 최대/최소값 | 파란색 |
| 실패 호출 건수 | `#failCountCard` | 상태 코드가 CD902(장애)인 건수 | 빨간색 |
| 중단 횟수 | `#stopCountCard` | 수집이 중단된 건수 | 볼색 |

**계산 로직:**
- 최대/최소 소요 시간: `MAX(end_dt - start_dt)`, `MIN(end_dt - start_dt)`
- 실패 호출 건수: `COUNT(*) WHERE status = 'CD902'`
- 중단 횟수: `COUNT(*) WHERE status IN ('CD903', 'CD905')` (미수집, 중단)

#### ③ Job ID 상세정보 카드 (`#job-info-card`)

| 기능 | 설명 |
|------|------|
| 검색 | `#jobInfoSearch` - Job ID 또는 한글명으로 실시간 필터링 |
| 행 수 | `#jobInfoPageSize` - 5/10/20/50/100개 선택 |
| 테이블 | `#jobInfoTable` - Job ID, 데이터명, 주기(cron), 설명 |
| 페이징 | `#jobInfoPagination` - 페이지 이동 버튼 |

**데이터 출처:**
- `tb_con_mst` - Job 기본 정보
- `tb_mngr_sett` - 추가 설정 정보 (있는 경우)

#### ④ 수집 및 가공 데이터 카드 (`#raw-data-card`)

| 컬럼 | 데이터 | 설명 |
|------|--------|------|
| 날짜 | `start_dt` | 수집 시작 날짜 (KST) |
| Job ID | `job_id` | 수집 작업 ID |
| 장애코드 | `status` | 상태 코드 (CD901~CD904 등) |
| 요일 | `DAYOFWEEK(start_dt)` | 일~토 요일 표시 |
| 수집시간(hr) | `end_dt - start_dt` | 실제 소요 시간 (시간 단위) |
| 예측 수집시간(hr) | `predicted_duration` | ML 또는 통계 기반 예측 소요 시간 |
| 완전성(%) | `completeness` | (실제 수집 건수 / 예상 건수) × 100 |
| 평균소요시간(hr) | `avg_duration` | 전체 기간 평균 소요 시간 |
| 최대/최소 제외 평균(hr) | `trimmed_avg` | 최대/최소값 제외 평균 |
| 최근3회평균(hr) | `recent_3avg` | 최근 3회 실행의 평균 소요 시간 |
| 연속실패 | `fail_streak` | 현재까지 연속 실패 횟수 |
| 이상치 | `is_outlier` | 평균 대비 2표준편차 이상 여부 |
| 성공률변화(%) | `success_rate_change` | 전 기간 대비 성공률 변화량 |
| 누적수집 | `cumulative_count` | 해당 Job의 누적 수집 건수 |

**검색 및 필터링:**
- **검색 (`#rawDataSearch`)**: Job ID 또는 장애코드로 실시간 필터링
- **행 수 (`#rawDataPageSize`)**: 10/20/50/100개 선택
- **페이징 (`#rawPagination`)**: 페이지 이동

**데이터 출처:**
- API: `GET /api/data_analysis` (또는 `/api/analysis/data`)
- Service: `AnalysisService.get_dynamic_chart_data()` 또는 별도 분석 메소드
- Mapper: `AnalysisMapper`
- SQL: `sql/analytics/analytics_sql.py`

---

## 5.4.3 데이터 흐름 및 처리 로직

### 5.4.3.1 전체 데이터 흐름도

![전체 데이터 흐름도](images/04-data-analysis-data-flow.png)

### 5.4.3.2 주요 지표 계산 로직

**소요 시간 (Duration):**
```
수집시간(hr) = (end_dt - start_dt)의 시간 단위 변환
```

**완전성 (Completeness):**
```
완전성(%) = (실제 수집 건수 / 예상 수집 건수) × 100
```

**최대/최소 제외 평균 (Trimmed Average):**
```
값이 3개 이상: (전체 합계 - 최대값 - 최소값) / (개수 - 2)
값이 2개 이하: 일반 평균
```

**최근 3회 평균 (Recent 3 Average):**
```
최근 3회 실행의 소요 시간 산술평균
```

**연속 실패 (Fail Streak):**
```
현재까지 연속된 CD902(장애) 또는 CD903(미수집) 횟수
```

**이상치 (Outlier):**
```
|현재값 - 평균값| > 2 × 표준편차 → 이상치(True)
```

**성공률 변화:**
```
성공률변화(%) = (현재 기간 성공률 - 이전 기간 성공률)
```

---

## 5.4.4 조작 방법

### 5.4.4.1 필터 변경하여 조회

**조작 절차:**
1. `시작일` / `종료일` 입력 필드에서 날짜 선택
2. `Job ID` 또는 `장애코드` 드롭다운에서 선택 (선택 사항)
3. 상단 요약 카드와 하단 테이블이 자동 갱신됨

**확인 방법:**
- 요약 카드의 숫자가 변경되는지 확인
- 테이블 데이터가 갱신되는지 확인

### 5.4.4.2 Job ID 상세정보 조회

**조작 절차:**
1. `Job ID 상세정보` 카드 펼치기 (헤더 클릭)
2. 검색어 입력 또는 행 수 변경
3. 페이지네이션으로 추가 항목 확인

### 5.4.4.3 수집 데이터 테이블 조회

**조작 절차:**
1. `수집 및 가공 데이터` 카드 펼치기
2. 검색어 입력 (Job ID 또는 장애코드)
3. 행 수 변경 (10/20/50/100개)
4. 페이지네이션으로 이동

**확인 방법:**
- 총 건수 표시 (`총 1,234건`)
- 각 컬럼 값이 정상적으로 표시되는지 확인
- 이상치 표시 여부 확인

---

## 5.4.5 모니터링 체크리스트

- [ ] **최대/최소 소요 시간**이 예상 범위 내인지 확인
- [ ] **실패 호출 건수**가 급증하지 않는지 확인
- [ ] **중단 횟수**가 0에 가까운지 확인
- [ ] **연속 실패**가 3회 이상인 Job이 있는지 확인
- [ ] **이상치**가 발생한 Job이 있는지 확인
- [ ] **성공률 변화**가 큰 폭으로 하락한 Job이 있는지 확인
- [ ] **완전성**이 100%에 가까운지 확인

---

## 5.4.6 자주 발생하는 문제

| 증상 | 원인 | 해결 방법 |
|------|------|-----------|
| 테이블이 비어있음 | 날짜 범위 내 데이터 없음 | 날짜 범위 확대 또는 필터 초기화 |
| 소요 시간이 0으로 표시됨 | `end_dt`가 `start_dt`와 동일 | 데이터 품질 문제, `tb_con_hist` 확인 |
| 이상치가 너무 많음 | 데이터 품질 저하 또는 기준값 부적절 | 관리자 설정에서 이상치 임계값 조정 |
| 예측 수집시간이 부정확함 | 예측 모델 미학습 또는 데이터 부족 | 충분한 학습 데이터 확보 후 모델 재학습 |
| 완전성이 낮음 | 데이터 유실 또는 수집 누락 | 수집 에이전트 로그 확인 |
| 특정 Job이 보이지 않음 | 사용자 데이터 권한 없음 | 관리자에게 데이터 접근 권한 요청 |

---

## 5.4.7 관련 DB 테이블 및 쿼리

### 5.4.7.1 주요 테이블

| 테이블 | 설명 |
|--------|------|
| `tb_con_hist` | 수집 실행 이력 (소요 시간, 상태, 시간) |
| `tb_con_mst` | 수집 작업 마스터 (Job ID, 데이터명, 주기) |
| `tb_sts_cd_mst` | 상태 코드 마스터 (CD901~CD904 정의) |
| `tb_user_data_perm_auth_ctrl` | 사용자별 데이터 접근 권한 |

### 5.4.7.2 데이터 분석 조회 API

```
GET /api/data_analysis?start_date=2025-01-01&end_date=2025-12-31&job_id=CD101&error_code=CD902
```

**응답 구조:**
```json
[
  {
    "date": "2025-01-15",
    "job_id": "CD101",
    "status": "CD901",
    "day_of_week": "월",
    "duration": 2.5,
    "predicted_duration": 2.3,
    "completeness": 98.5,
    "avg_duration": 2.4,
    "trimmed_avg": 2.35,
    "recent_3avg": 2.45,
    "fail_streak": 0,
    "is_outlier": false,
    "success_rate_change": 0.5,
    "cumulative_count": 1250
  }
]
```

---

> 다음 문서: [05-data-spec.md](05-data-spec.md)


---pb---

# 5.5 데이터 명세서

> **기준 버전 / 최종 확인일**: v1.1.0 · 2026-07-22

> **핵심 기능**: 수집 대상 데이터의 명세서를 등록, 조회, 수정, 삭제하고, 메타데이터를 자동으로 채워 넣어 데이터 관리의 효율성을 높입니다.

---

## 5.5.1 메뉴 접속 방법

- **경로**: 상단 메뉴 → 데이터 명세서
- **URL**: `/data_spec`
- **필요 권한**: `data_spec`
- **로그**: 메뉴 접근 시 `tb_user_acs_log` 테이블에 접근 이력이 기록됩니다.

---

## 5.5.2 화면 구성

### 5.5.2.1 전체 화면 구조

![데이터 명세서 전체 화면](images/data-spec-full.png)

### 5.5.2.2 각 영역 상세 설명

#### ① 메타데이터로 명세서 채우기 카드 (`#metadata-import-card`)

**지원 형식:**
| 형식 | 파일 확장자 | 설명 |
|------|------------|------|
| schema.org(JSON) | `.json` | 공공데이터 포털 메타데이터 JSON |
| DCAT(RDF) | `.xml`, `.rdf` | DCAT 표준 RDF/XML 메타데이터 |

**입력 방법:**
| 방법 | 요소 | 설명 |
|------|------|------|
| 파일로 불러오기 | `#metadata-file-input` | 파일 선택 후 `파일에서 채우기` 버튼 클릭 |
| 붙여넣기로 불러오기 | `#metadata-text-input` | 텍스트 직접 입력 후 `텍스트에서 채우기` 버튼 클릭 |

**동작 로직:**
- 파일 또는 텍스트 입력 후 버튼 클릭
- `data_spec.js`의 파서가 JSON/XML을 파싱
- 파싱된 데이터로 명세서 등록 모달의 폼 필드 자동 채움
- API URL, 데이터 명칭, 제공 기관, 키워드 등 추출

#### ② 명세서 목록 카드 (`#spec-list-card`)

| 기능 | 요소 | 설명 |
|------|------|------|
| 총 건수 | `#spec-total-count` | 전체 명세서 개수 표시 |
| 검색 | `#specSearch` | 데이터명, 기관, 키워드로 실시간 필터링 |
| 행 수 | `#specPageSize` | 10/20/50/100개 선택 |
| 새로 등록 | `#add-new-btn` | 빈 명세서 등록 모달 열기 |
| 테이블 | `#spec-list-body` | 명세서 목록 테이블 |
| 페이징 | `#specPagination` | 페이지 이동 버튼 |

**테이블 컬럼:**
| 컬럼 | 데이터 | 설명 |
|------|--------|------|
| ID | `id` | 명세서 고유 ID |
| 데이터 명칭 | `data_name` | 데이터의 한글 이름 |
| 제공 기관 | `provider` | 데이터 제공 기관명 |
| 키워드 | `keywords` | 검색용 키워드 (쉼표 구분) |
| 등록일 | `created_at` | 명세서 최초 등록일 |
| 참조문서 | `reference_doc_url` | 참고 문서 링크 (있는 경우 아이콘 표시) |

**동작 로직:**
- 행 클릭 시 `#spec-modal` 모달 열림 (상세 조회/수정)
- 검색 입력 시 실시간 필터링
- 페이지네이션으로 대량 데이터 처리

#### ③ 명세서 상세/등록 모달 (`#spec-modal`)

**기본 정보:**
| 필드 | ID | 설명 | 필수 |
|------|-----|------|------|
| 데이터 명칭 | `#data_name` | 데이터의 한글 이름 | ✅ |
| 제공 기관 | `#provider` | 데이터 제공 기관명 | - |
| API URL | `#api_url` | 데이터 수집 API 엔드포인트 | - |
| 참고 문서 URL | `#reference_doc_url` | 참고 문서 링크 | - |
| 비밀번호 | `#password` | 수정/삭제 시 필요한 비밀번호 | ✅ (신규) |
| 키워드 | `#keywords` | 검색용 키워드 | - |
| 상세 설명 | `#description` | 데이터에 대한 상세 설명 | - |

**동적 섹션:**
| 섹션 | 컨테이너 | 설명 |
|------|----------|------|
| 요청 파라미터 | `#request-params-container` | API 호출 시 필요한 파라미터 목록 |
| 응답 파라미터 | `#response-params-container` | API 응답의 파라미터 목록 |

**동작 로직:**
- `저장 후 닫기` 클릭 시 `#save-password-confirm-modal` 열림 (신규 또는 비밀번호 미설정 시)
- `삭제` 클릭 시 `#password-confirm-modal` 열림
- 비밀번호는 4자리 이상 입력 필요
- API URL 입력 후 자동 분석 기능으로 요청/응답 파라미터 추출 가능

#### ④ URL 분석 결과 모달 (`#url-analysis-modal`)

**표시 조건:** API URL 입력 후 자동 분석 또는 수동 분석 버튼 클릭
**표시 내용:**
- URL 유효성 검사 결과
- 요청 파라미터 자동 추출 (query string, path variable)
- 응답 파라미터 자동 추출 (JSON 응답 샘플 기반)
- 데이터 매핑 테이블

**동작:**
- `선택한 정보로 명세서 채우기` 버튼 클릭 시 모달 닫히고 폼 필드 업데이트

---

## 5.5.3 데이터 흐름 및 처리 로직

### 5.5.3.1 전체 데이터 흐름도

![전체 데이터 흐름도](images/05-data-spec-data-flow.png)

### 5.5.3.2 명세서 저장 절차

**신규 등록:**
1. `수동으로 새로 등록` 또는 메타데이터 채우기
2. 모달 폼에 데이터 입력
3. `저장 후 닫기` 클릭
4. 비밀번호 설정 모달 표시 (4자리 이상)
5. `POST /api/data_spec` API 호출
6. 목록 자동 갱신

**수정:**
1. 목록에서 대상 행 클릭
2. 모달 폼에서 데이터 수정
3. `저장 후 닫기` 클릭
4. `PUT /api/data_spec/{id}` API 호출

**삭제:**
1. 목록에서 대상 행 클릭
2. `삭제` 버튼 클릭
3. 비밀번호 확인 모달 표시
4. 비밀번호 입력 후 `확인`
5. `DELETE /api/data_spec/{id}` API 호출
6. 목록 자동 갱신

### 5.5.3.3 메타데이터 파싱 로직

**schema.org(JSON):**
```json
{
  "@context": "https://schema.org",
  "@type": "Dataset",
  "name": "데이터 명칭",
  "publisher": {"name": "제공 기관"},
  "keyword": ["키워드1", "키워드2"],
  "distribution": {"contentUrl": "API URL"}
}
```

**DCAT(RDF/XML):**
```xml
<dcat:Dataset>
  <dct:title>데이터 명칭</dct:title>
  <dct:publisher>제공 기관</dct:publisher>
  <dcat:keyword>키워드1</dcat:keyword>
  <dcat:distribution rdf:resource="API URL"/>
</dcat:Dataset>
```

---

## 5.5.4 조작 방법

### 5.5.4.1 메타데이터로 명세서 자동 채우기

**조작 절차 (파일):**
1. `메타데이터로 명세서 채우기` 카드 펼치기
2. `파일로 불러오기` 영역에서 파일 선택 (`.json`, `.xml`, `.rdf`)
3. `파일에서 채우기` 버튼 클릭
4. 명세서 등록 모달이 열리며 필드가 자동으로 채워짐

**조작 절차 (붙여넣기):**
1. `메타데이터로 명세서 채우기` 카드 펼치기
2. `붙여넣기로 불러오기` 텍스트 영역에 메타데이터 내용 입력
3. `텍스트에서 채우기` 버튼 클릭

**확인 방법:**
- 모달의 데이터 명칭, 제공 기관, API URL 등이 채워졌는지 확인

### 5.5.4.2 명세서 직접 등록

![명세서 등록 모달](images/data-spec-add-modal.png)

**조작 절차:**
1. `명세서 목록` 카드에서 `수동으로 새로 등록` 버튼 클릭
2. 모달 폼에 데이터 입력
3. `저장 후 닫기` 클릭
4. 비밀번호 설정 (4자리 이상)
5. `저장` 클릭

**확인 방법:**
- 목록에 신규 항목이 추가되었는지 확인
- 총 건수가 1 증가했는지 확인

### 5.5.4.3 명세서 조회 및 수정

**조작 절차:**
1. 목록에서 대상 행 클릭
2. 모달에서 내용 확인
3. 필요 시 필드 수정
4. `저장 후 닫기` 클릭

**확인 방법:**
- 목록의 해당 행 내용이 변경되었는지 확인

### 5.5.4.4 명세서 삭제

**조작 절차:**
1. 목록에서 대상 행 클릭
2. 모달 하단의 `삭제` 버튼 클릭
3. 비밀번호 확인 모달에서 등록 시 설정한 비밀번호 입력
4. `확인` 클릭

**확인 방법:**
- 목록에서 해당 행이 사라졌는지 확인
- 총 건수가 1 감소했는지 확인

---

## 5.5.5 모니터링 체크리스트

- [ ] **명세서 총 건수**가 증가하는지 확인 (신규 데이터 수집 시)
- [ ] **API URL**이 유효한지 확인 (404 오류 여부)
- [ ] **참고 문서 URL**이 정상적으로 연결되는지 확인
- [ ] **키워드**가 적절히 등록되어 검색이 용이한지 확인
- [ ] **비밀번호**가 분실되지 않도록 별도 관리
- [ ] **메타데이터 자동 채우기** 실패 시 수동으로 입력 가능한지 확인

---

## 5.5.6 자주 발생하는 문제

| 증상 | 원인 | 해결 방법 |
|------|------|-----------|
| 메타데이터 파싱 실패 | 지원하지 않는 형식 또는 잘못된 데이터 | schema.org 또는 DCAT 표준 형식 확인 |
| API URL이 유효하지 않음 | 잘못된 URL 또는 서비스 종료 | 브라우저에서 URL 직접 접속 테스트 |
| 저장 실패 | 필수 항목(데이터 명칭) 누락 | 데이터 명칭 입력 확인 |
| 삭제 실패 | 비밀번호 불일치 | 등록 시 설정한 비밀번호 확인 |
| 목록이 비어있음 | 등록된 명세서 없음 | 메타데이터 자동 채우기 또는 수동 등록 |
| 검색 결과 없음 | 검색어와 일치하는 항목 없음 | 검색어 변경 또는 키워드 확인 |
| URL 분석 실패 | CORS 오류 또는 서버 응답 없음 | 브라우저 개발자 도구에서 네트워크 오류 확인 |

---

## 5.5.7 관련 DB 테이블 및 쿼리

### 5.5.7.1 주요 테이블

| 테이블 | 설명 |
|--------|------|
| `tb_data_spec` | 데이터 명세서 기본 정보 (ID, 데이터명, 제공기관, API URL 등) |
| `tb_data_spec_parm` | 명세서 파라미터 정보 (요청/응답 파라미터명, 타입, 설명) |
| `tb_user_acs_log` | 메뉴 접근 이력 |

### 5.5.7.2 명세서 API

```
GET    /api/data_spec              # 명세서 목록 조회
POST   /api/data_spec              # 명세서 신규 등록
GET    /api/data_spec/{id}         # 명세서 상세 조회
PUT    /api/data_spec/{id}         # 명세서 수정
DELETE /api/data_spec/{id}         # 명세서 삭제 (비밀번호 필요)
POST   /api/data_spec/parse        # 메타데이터 파싱
POST   /api/data_spec/analyze-url  # URL 분석
```

---

> 다음 문서: [06-card-summary.md](06-card-summary.md)


---pb---

# 5.6 카드 요약

> **기준 버전 / 최종 확인일**: v1.1.0 · 2026-07-22

> **핵심 기능**: 수집 작업의 핵심 지표를 카드 형태로 요약하여 한눈에 현황을 파악하고, 표/카드 뷰 전환 및 다양한 표시 옵션을 제공합니다.

---

## 5.6.1 메뉴 접속 방법

- **경로**: 상단 메뉴 → 카드 요약
- **URL**: `/card_summary`
- **필요 권한**: `card_summary`
- **로그**: 메뉴 접근 시 `tb_user_acs_log` 테이블에 접근 이력이 기록됩니다.

---

## 5.6.2 화면 구성

### 5.6.2.1 전체 화면 구조

![카드 요약 전체 화면](images/card-summary-full.png)

### 5.6.2.2 각 영역 상세 설명

#### ① 수집 요청서 양식 다운로드 버튼

| 요소 | 설명 |
|------|------|
| 버튼 | 우측 상단 `수집 요청서 양식 다운로드` |
| 기능 | Excel 파일(.xlsx) 다운로드 |
| 스타일 | 녹색 배경(#10b981), 흰색 글자 |

#### ② 카드 요약 표시 옵션 (`#cardContainer` 상단)

| 기능 | 요소 | 설명 |
|------|------|------|
| 뷰 모드 토글 | `#viewModeToggle` | 표(테이블) ↔ 콩(카드) 뷰 전환 |
| 검색 | `#cardSearchInput` | Job ID, 데이터명, 상태 등으로 실시간 필터링 |
| 표시 모드 | `#display-mode-selector` | 명칭 / 코드 / 명칭+코드 / 설명 중 선택 |

**표시 모드 상세:**
| 모드 | 값 | 표시 내용 |
|------|-----|----------|
| 명칭 | `name` | Job의 한글 이름 (`cd_nm`)만 표시 |
| 코드 | `code` | Job ID (예: CD101)만 표시 |
| 명칭+코드 | `both` | `코드: 명칭` 형태로 표시 (예: CD101: 기상청예보) |
| 설명 | `desc` | Job 상세 설명 표시 |

#### ③ 카드 컨테이너 (`#cardContainer`)

**카드 구조:**
```
┌──────────────────┐
│ [CD101]          │  ← Job ID (표시 모드에 따라 코드/명칭/둘 다)
│ 기상청 예보 데이터 │  ← 데이터명
│                  │
│ 성공률: 95.5%    │  ← 기간별 성공률
│ 연속실패: 0회    │  ← 연속 실패 횟수
│ 상태: 정상       │  ← 상태 (정상/경고/위험)
│                  │
│ [상세 보기]      │  ← 상세 정보 링크 (있는 경우)
└──────────────────┘
```

**카드 상태별 스타일:**
| 상태 | 조건 | 색상 |
|------|------|------|
| 정상 | 성공률 ≥ 임계값, 연속실패 < 경고 임계값 | 녹색 계열 |
| 경고 | 성공률 < 임계값 또는 연속실패 ≥ 경고 임계값 | 노란색/주황색 계열 |
| 위험 | 연속실패 ≥ 위험 임계값 | 빨간색 계열 |

**데이터 출처:**
- API: `GET /api/card_summary`
- Service: `CardSummaryService.get_summary()`
- Mapper: `CardSummaryMapper`
- SQL: `sql/card_summary/card_summary_sql.py`

---

## 5.6.3 데이터 흐름 및 처리 로직

### 5.6.3.1 전체 데이터 흐름도

![전체 데이터 흐름도](images/06-card-summary-data-flow.png)

### 5.6.3.2 주요 지표 계산

**성공률:**
```
성공률 = (성공 건수 / (성공 건수 + 실패 건수 + 미수집 건수)) × 100
```

**연속 실패:**
```
최근 10회 실행 중 CD902(장애) 또는 CD903(미수집) 상태인 횟수
```

**상태 결정:**
- `tb_mngr_sett`의 임계값 기준
- 성공률 임계값 미만 또는 연속 실패 경고 임계값 이상 → 경고
- 연속 실패 위험 임계값 이상 → 위험

---

## 5.6.4 조작 방법

### 5.6.4.1 뷰 모드 전환

**조작 절차:**
1. `표` 또는 `콩` 토글 클릭

**확인 방법:**
- 카드 형태 ↔ 테이블 형태로 전환됨
- 카드: 직사각형 카드 그리드 배치
- 표: 행/열 테이블 배치

### 5.6.4.2 검색

**조작 절차:**
1. 검색 입력 필드에 텍스트 입력

**확인 방법:**
- 입력 즉시 카드/행이 필터링됨
- Job ID, 데이터명, 상태 등 모든 텍스트 필드 검색

### 5.6.4.3 표시 모드 변경

**조작 절차:**
1. 라디오 버튼 그룹에서 `명칭` / `코드` / `명칭+코드` / `설명` 선택

**확인 방법:**
- 카드/표의 제목 영역이 변경됨
- 예: "CD101" → "기상청예보" → "CD101: 기상청예보"

---

## 5.6.5 모니터링 체크리스트

- [ ] **위험 상태 카드**(빨간색)가 있는지 확인
- [ ] **경고 상태 카드**(노란색)가 과도하게 많지 않은지 확인
- [ ] **성공률**이 전반적으로 90% 이상인지 확인
- [ ] **연속 실패**가 3회 이상인 Job이 있는지 확인
- [ ] **검색**으로 특정 Job을 쉽게 찾을 수 있는지 확인

---

## 5.6.6 자주 발생하는 문제

| 증상 | 원인 | 해결 방법 |
|------|------|-----------|
| 카드가 비어있음 | 데이터 수집 기록 없음 | 날짜 범위 확대 또는 데이터 수집 에이전트 상태 확인 |
| 특정 Job이 보이지 않음 | 사용자 데이터 권한 없음 | 관리자에게 데이터 접근 권한 요청 |
| 성공률이 0%로 표시됨 | 해당 기간 내 수집 이력 없음 | 데이터 수집 스케줄/에이전트 상태 확인 |
| 상태가 모두 위험으로 표시됨 | 임계값 설정 부적절 | 관리자 설정에서 성공률/연속실패 임계값 조정 |
| 검색 결과 없음 | 검색어와 일치하는 Job 없음 | 검색어 변경 또는 전체 목록 확인 |

---

## 5.6.7 관련 DB 테이블 및 쿼리

### 5.6.7.1 주요 테이블

| 테이블 | 설명 |
|--------|------|
| `tb_con_hist` | 수집 실행 이력 (성공/실패 상태, 시간) |
| `tb_con_mst` | 수집 작업 마스터 (Job ID, 데이터명) |
| `tb_mngr_sett` | 관리자 설정 (성공률 임계값, 연속실패 임계값) |
| `tb_user_data_perm_auth_ctrl` | 사용자별 데이터 접근 권한 |

### 5.6.7.2 카드 요약 조회 API

```
GET /api/card_summary
```

**응답 구조:**
```json
[
  {
    "job_id": "CD101",
    "cd_nm": "기상청예보",
    "success_rate": 95.5,
    "fail_streak": 0,
    "status": "normal",
    "color": "#28a745"
  }
]
```

---

> 다음 문서: [07-mapping.md](07-mapping.md)


---pb---

# 5.7 매핑 관리

> **기준 버전 / 최종 확인일**: v1.1.0 · 2026-07-22

> **핵심 기능**: 데이터베이스 테이블 컬럼의 변경 이력을 관리하고, 레거시 코드와 신규 코드 간의 컬럼 매핑 정보를 유지하여 호환성을 보장합니다.

---

## 5.7.1 메뉴 접속 방법

- **경로**: 상단 메뉴 → 매핑 관리
- **URL**: `/mapping`
- **필요 권한**: `mapping`
- **로그**: 메뉴 접근 시 `tb_user_acs_log` 테이블에 접근 이력이 기록됩니다.

---

## 5.7.2 화면 구성

### 5.7.2.1 전체 화면 구조

> 📷 *화면 캡처 미보유 — 운영 환경에서 재캡처 필요. 아래는 구조 파악용 와이어프레임(실제 화면 배치와 세부 스타일은 다를 수 있음).*

![전체 화면 구조](images/07-mapping-layout.png)

### 5.7.2.2 각 영역 상세 설명

#### ① 매핑되지 않은 신규 컬럼

| 컬럼 | 설명 |
|------|------|
| 테이블명 | 신규 컬럼이 추가된 테이블 이름 |
| 컬럼명 | 매핑되지 않은 신규 컬럼 이름 |
| 작업 | 매핑 추가 버튼 |

**동작 로직:**
- 시스템 startup 시 또는 `새로고침` 버튼 클릭 시 DB 스키마 스캔
- `tb_col_mapp` 테이블에 등록되지 않은 컬럼을 자동으로 감지
- 매핑 추가 버튼 클릭 시 매핑 모달이 열리며 해당 테이블/컬럼명이 자동으로 채워짐

#### ② 매핑 관리 테이블

| 컬럼 | 설명 |
|------|------|
| ID | 매핑 고유 ID |
| 이전 테이블명 | 레거시(변경 전) 테이블 이름 |
| 이전 컬럼명 | 레거시(변경 전) 컬럼 이름 |
| 새 테이블명 | 신규(변경 후) 테이블 이름 |
| 새 컬럼명 | 신규(변경 후) 컬럼 이름 |
| 설명 | 매핑에 대한 부가 설명 |
| 수정일 | 마지막 수정 일시 |
| 작업 | 수정/삭제 버튼 |

**동작 로직:**
- `tb_col_mapp` 테이블의 모든 매핑 정보 표시
- 행 클릭 시 매핑 모달 열림 (수정 모드)
- `신규 매핑 추가` 버튼 클릭 시 빈 모달 열림 (등록 모드)

#### ③ 매핑 정보 모달 (`#mapping-modal`)

| 필드 | ID | 설명 | 필수 |
|------|-----|------|------|
| 이전 테이블명 | `#bf-tbl-nm` | 레거시 테이블 이름 | - |
| 이전 컬럼명 | `#bf-col-nm` | 레거시 컬럼 이름 | - |
| 새 테이블명 | `#new-tbl-nm` | 신규 테이블 이름 | ✅ |
| 새 컬럼명 | `#new-col-nm` | 신규 컬럼 이름 | ✅ |
| 설명 | `#expl` | 매핑 설명 | - |

---

## 5.7.3 데이터 흐름 및 처리 로직

### 5.7.3.1 전체 데이터 흐름도

![전체 데이터 흐름도](images/07-mapping-data-flow.png)

### 5.7.3.2 매핑 조회 절차

1. 페이지 진입 시 `GET /api/mappings` API 호출
2. `MappingService`가 `MappingMapper`를 통해 `TB_COL_MAPP` 조회
3. 응답 데이터를 테이블에 렌더링

### 5.7.3.3 매핑 저장 절차

**신규 등록:**
1. `신규 매핑 추가` 버튼 클릭
2. 모달 폼에 데이터 입력
3. `저장` 버튼 클릭
4. `POST /api/mappings` API 호출

**수정:**
1. 대상 행 클릭
2. 모달 폼에서 데이터 수정
3. `저장` 버튼 클릭
4. `PUT /api/mappings/{id}` API 호출

**삭제:**
1. 대상 행의 `삭제` 버튼 클릭
2. 확인 대화상자 표시
3. `DELETE /api/mappings/{id}` API 호출

### 5.7.3.4 신규 컬럼 감지 로직

```
1. DB 메타데이터 조회 (INFORMATION_SCHEMA.COLUMNS)
2. tb_col_mapp의 모든 (테이블명, 컬럼명) 집합 생성
3. DB 메타데이터와 비교하여 미등록 컬럼 식별
4. 미등록 컬럼을 "매핑되지 않은 신규 컬럼" 테이블에 표시
```

---

## 5.7.4 조작 방법

### 5.7.4.1 매핑 목록 조회

**조작 절차:**
1. 상단 메뉴 → 매핑 관리 클릭
2. 매핑 관리 테이블에서 목록 확인

**확인 방법:**
- 이전/새 테이블명과 컬럼명이 정상적으로 표시되는지 확인

### 5.7.4.2 신규 매핑 등록

**조작 절차:**
1. `신규 매핑 추가` 버튼 클릭
2. 모달 폼에 이전/새 테이블명, 컬럼명 입력
3. 설명 입력 (선택 사항)
4. `저장` 버튼 클릭

**확인 방법:**
- 목록에 신규 항목이 추가되었는지 확인

### 5.7.4.3 기존 매핑 수정

**조작 절차:**
1. 대상 행 클릭
2. 모달 폼에서 필요한 필드 수정
3. `저장` 버튼 클릭

**확인 방법:**
- 목록의 해당 행 내용이 변경되었는지 확인

### 5.7.4.4 매핑 삭제

**조작 절차:**
1. 대상 행의 `삭제` 버튼 클릭
2. 확인 대화상자에서 `확인` 클릭

**확인 방법:**
- 목록에서 해당 행이 사라졌는지 확인

### 5.7.4.5 신규 컬럼 매핑 추가

**조작 절차:**
1. `매핑되지 않은 신규 컬럼` 테이블 확인
2. 대상 행의 `매핑 추가` 버튼 클릭
3. 모달이 열리며 테이블명/컬럼명이 자동으로 채워짐
4. 이전 테이블명/컬럼명 입력 (있는 경우)
5. `저장` 버튼 클릭

**확인 방법:**
- 신규 컬럼 테이블에서 해당 행이 사라졌는지 확인
- 매핑 관리 테이블에 추가되었는지 확인

---

## 5.7.5 모니터링 체크리스트

- [ ] **매핑되지 않은 신규 컬럼**이 지속적으로 증가하지 않는지 확인
- [ ] **이전 테이블명/컬럼명**이 누락된 매핑이 없는지 확인
- [ ] **새 테이블명/컬럼명**이 실제 DB 스키마와 일치하는지 확인
- [ ] **설명**이 명확하게 작성되어 있는지 확인

---

## 5.7.6 자주 발생하는 문제

| 증상 | 원인 | 해결 방법 |
|------|------|-----------|
| 매핑 목록이 비어있음 | 등록된 매핑 정보 없음 | 신규 매핑 추가 또는 DB 스키마 변경 시 자동 감지 대기 |
| 신규 컬럼이 감지되지 않음 | DB 스키마 변경 후 새로고침 미실행 | `새로고침` 버튼 클릭 |
| 저장 실패 | 필수 항목(새 테이블명/컬럼명) 누락 | 필수 필드 입력 확인 |
| 중복 매핑 저장 | 동일한 (새 테이블명, 새 컬럼명)이 이미 존재 | 기존 매핑 수정 또는 중복 여부 확인 |
| 이전 코드 호환성 문제 | 매핑 정보 부정확 또는 누락 | 매핑 테이블의 이전/새 컬럼명 정확성 확인 |

---

## 5.7.7 관련 DB 테이블 및 쿼리

### 5.7.7.1 주요 테이블

| 테이블 | 설명 |
|--------|------|
| `tb_col_mapp` | 컬럼 매핑 정보 (ID, 이전 테이블명, 이전 컬럼명, 새 테이블명, 새 컬럼명, 설명, 수정일) |
| `INFORMATION_SCHEMA.COLUMNS` | DB 메타데이터 (테이블명, 컬럼명 등) |

### 5.7.7.2 매핑 API

```
GET    /api/mappings              # 매핑 목록 조회
POST   /api/mappings              # 매핑 신규 등록
GET    /api/mappings/{id}         # 매핑 상세 조회
PUT    /api/mappings/{id}         # 매핑 수정
DELETE /api/mappings/{id}         # 매핑 삭제
GET    /api/unmapped-columns      # 매핑되지 않은 신규 컬럼 조회
```

---

> 다음 문서: [08-api-key-mngr.md](08-api-key-mngr.md)


---pb---

# 5.8 API 키 관리

> **기준 버전 / 최종 확인일**: v1.1.0 · 2026-07-22

> **핵심 기능**: 데이터 수집에 사용되는 API 키의 등록, 조회, 수정, 삭제 및 만료 알림 메일 스케줄 관리를 수행합니다.
> **탭 하위파일**: 각 탭 상세는 `08-api-key-mngr.tabN.md`로 분리합니다 (작성 지침 §7.3).

---

## 5.8.1 메뉴 접속 방법

- **경로**: 상단 메뉴 → API 키 관리
- **URL**: `/api_key_mngr`
- **필요 권한**: `api_key_mngr`
- **로그**: 메뉴 접근 시 `tb_user_acs_log` 테이블에 접근 이력이 기록됩니다.

---

## 5.8.2 화면 구성 (탭 목록)

| 탭 | 파일 | 설명 |
|----|------|------|
| API 키 관리 | [08-api-key-mngr.tab1.md](08-api-key-mngr.tab1.md) | API 키 목록 조회/등록/수정/삭제, 메일 테스트 |
| 기간 차트 | [08-api-key-mngr.tab2.md](08-api-key-mngr.tab2.md) | API 키 유효기간 간트 차트 시각화 |
| 위험군 | [08-api-key-mngr.tab3.md](08-api-key-mngr.tab3.md) | 1개월 이내 만료 API 키 관리 |
| 설정 | [08-api-key-mngr.tab4.md](08-api-key-mngr.tab4.md) | 메일 알림 및 스케줄 설정 |

---

## 5.8.3 데이터 흐름 및 처리 로직

### 5.8.3.1 전체 데이터 흐름도

![전체 데이터 흐름도](images/08-api-key-mngr-data-flow.png)

### 5.8.3.2 API 키 상태 분류 기준

| 상태 | 조건 |
|------|------|
| 정상 | 만료일 - 오늘 > 30일 |
| 만료 임박(30일) | 7일 < 만료일 - 오늘 ≤ 30일 |
| 만료 임박(7일) | 0일 < 만료일 - 오늘 ≤ 7일 |
| 오버 | 만료일 - 오늘 ≤ 0일 |

### 5.8.3.3 메일 알림 스케줄

```
1. 스케줄러가 설정된 주기/시간에 실행
2. TB_API_KEY_MNGR에서 대상 키 조회 (30일/7일/당일 기준)
3. 메일 템플릿 변수 치환
4. SMTP 서버 통해 메일 발송
5. 발송 결과를 TB_API_KEY_MNGR_MAIL_LOG에 기록
```

---

## 5.8.4 모니터링 체크리스트

- [ ] **오버 상태 키**가 있는지 확인 (즉시 갱신 필요)
- [ ] **만료 임박(7일)** 키가 있는지 확인
- [ ] **메일 전송 상태**에서 실패 항목이 있는지 확인
- [ ] **위험군** 키에 대해 담당자가 조치했는지 확인
- [ ] **스케줄 설정**이 활성화되어 있는지 확인
- [ ] **메일 알림 템플릿**이 최신 상태인지 확인

---

## 5.8.5 자주 발생하는 문제

| 증상 | 원인 | 해결 방법 |
|------|------|-----------|
| API 키가 오버로 표시됨 | 만료일이 지남 | 즉시 API 키 갱신 후 등록일/기간 수정 |
| 메일 전송 실패 | SMTP 설정 오류 또는 잘못된 이메일 주소 | 설정 탭의 SMTP 설정 확인, 책임자 이메일 주소 확인 |
| 알림 메일이 가지 않음 | 스케줄 비활성화 또는 주기 설정 부적절 | 설정 탭에서 스케줄 활성화 및 주기 확인 |
| CD 업데이트 후 키가 사라짐 | TB_MNGR_SETT에서 CD가 삭제됨 | TB_CON_MST의 ITEM10 값 확인 |
| 간트 차트가 비어있음 | 등록된 API 키 없음 | API 키 등록 필요 |
| 일괄 수정이 안 됨 | 선택된 항목 없음 | 체크박스로 항목 선택 확인 |

---

## 5.8.6 관련 DB 테이블 및 쿼리

### 5.8.6.1 주요 테이블

| 테이블 | 설명 |
|--------|------|
| `tb_api_key_mngr` | API 키 기본 정보 (코드, 값, 책임자, 등록일, 기간) |
| `tb_api_key_mngr_mail_log` | 메일 발송 이력 (발송일, 상태, 결과) |
| `tb_api_key_mngr_mail_sett` | 메일 알림 설정 (템플릿, 스케줄) |
| `tb_api_key_mngr_mail_schd` | 메일 스케줄 정보 (주기, 시간, 활성화 여부) |
| `tb_con_mst` | 수집 작업 마스터 (CD, ITEM10, UDATE_DT) |
| `tb_mngr_sett` | 관리자 설정 (CD 목록) |

### 5.8.6.2 API 키 관리 API

```
GET    /api/api_key_mngr              # API 키 목록 조회
POST   /api/api_key_mngr              # API 키 신규 등록
PUT    /api/api_key_mngr/{id}         # API 키 수정
DELETE /api/api_key_mngr/{id}         # API 키 삭제
POST   /api/api_key_mngr/batch        # 일괄 수정
POST   /api/api_key_mngr/send-mail    # 테스트 메일 발송
POST   /api/api_key_mngr/sync-cd      # CD 동기화
GET    /api/api_key_mngr/gantt        # 간트 차트 데이터
GET    /api/api_key_mngr/risk         # 위험군 키 조회
POST   /api/api_key_mngr/settings     # 설정 저장
```

---



---pb---

# 5.8.7 API 키 관리 — API 키 관리 탭

> **기준 버전 / 최종 확인일**: v1.1.0 · 2026-07-22

> 소속 메뉴: [API 키 관리](08-api-key-mngr.md) · 탭 ① (`content0`)

---

## 5.8.7.1 화면 구성

**서브 탭:**
| 서브 탭 | 설명 |
|---------|------|
| 정상 API 키 관리 테이블 | 정상 상태의 API 키 목록 |
| 비정상 API 키 관리 테이블 | 만료 또는 오류 상태의 API 키 목록 |

**상태 필터 버튼:**
| 필터 | 설명 | 색상 |
|------|------|------|
| 전체키 | 모든 API 키 | 회색 |
| 정상 | 만료까지 30일 이상 남은 키 | 녹색 |
| 만료 임박(30일) | 30일 이내 만료 예정 | 노란색 |
| 만료 임박(7일) | 7일 이내 만료 예정 | 주황색 |
| 오버 | 이미 만료된 키 | 빨간색 |

**테이블 컬럼:**
| 컬럼 | 설명 |
|------|------|
| ✓ | 다중 선택 체크박스 |
| 코드명 | API 키 코드 (예: CD101) |
| 명칭 | API 키 한글 이름 |
| API값 | 실제 API 키 값 (마스킹 처리) |
| API책임자이메일 | 담당자 이메일 주소 |
| 기간 | 유효 기간 (년) |
| 등록일 | 최초 등록일 |
| 남은 기간 | 만료까지 남은 일수 |
| 알림 메일 전송 | 테스트 메일 발송 버튼 |
| 수정 | 개별 수정 버튼 |

**일괄 수정:**
- 체크박스로 다중 선택 후 `일괄 수정` 버튼 클릭
- 일괄 수정 모달에서 공통 필드 일괄 변경 가능

**CD 업데이트 동작:**
- `TB_MNGR_SETT`의 CD 값을 `TB_API_KEY_MNG`에 동기화
- `TB_CON_MST`의 ITEM10 값으로 업데이트
- `TB_CON_MST`의 UDATE_DT를 START_DT에 저장
- DUE 기본값: 1년

---

## 5.8.7.2 조작 방법

### 5.8.7.3 API 키 등록

1. `API 키 관리` 탭 선택
2. 테이블 내 `등록` 버튼 클릭 (또는 빈 행 더블클릭)
3. 코드명, 명칭, API값, 책임자 이메일, 기간 입력
4. `저장` 버튼 클릭

**확인 방법:**
- 목록에 신규 항목이 추가되었는지 확인
- 상태가 정상(녹색)으로 표시되는지 확인

### 5.8.7.4 API 키 수정

**개별:**
1. 대상 행의 `수정` 버튼 클릭
2. 필드 수정
3. `저장` 버튼 클릭

**일괄:**
1. 체크박스로 다중 선택
2. `일괄 수정` 버튼 클릭
3. 공통 수정 필드 입력
4. `저장` 버튼 클릭

### 5.8.7.5 만료 알림 메일 테스트

1. 대상 행의 `알림 메일 전송` 버튼 클릭
2. 테스트 메일 발송 확인

---



---pb---

# 5.8.8 API 키 관리 — 기간 차트 탭

> **기준 버전 / 최종 확인일**: v1.1.0 · 2026-07-22

> 소속 메뉴: [API 키 관리](08-api-key-mngr.md) · 탭 ② (`content1`)

---

## 5.8.8.1 간트 차트 (Gantt Chart)

- 각 API 키의 유효기간을 막대 그래프로 시각화
- X축: 시간 (등록일 ~ 만료일)
- Y축: API 키 코드명
- 오늘 날짜 기준 빨간색 세로선 표시
- 상태별 막대 색상: 녹색(정상), 주황(만료임박), 빨강(오버)
- 마우스 오버 시 툴팁으로 상세 정보 표시

---



---pb---

# 5.8.9 API 키 관리 — 위험군 탭

> **기준 버전 / 최종 확인일**: v1.1.0 · 2026-07-22

> 소속 메뉴: [API 키 관리](08-api-key-mngr.md) · 탭 ③ (`content2`)

---

## 5.8.9.1 정의

1개월 이내로 만료되는 API 키

**메일 전송 상태 필터:**
| 필터 | 설명 |
|------|------|
| 전체 | 모든 위험군 키 |
| ✅ 전송완료 | 알림 메일이 성공적으로 전송된 키 |
| ❌ 전송실패 | 알림 메일 전송에 실패한 키 |
| ⏳ 대기중 | 아직 알림 메일이 전송되지 않은 키 |

---



---pb---

# 5.8.10 API 키 관리 — 설정 탭

> **기준 버전 / 최종 확인일**: v1.1.0 · 2026-07-22

> 소속 메뉴: [API 키 관리](08-api-key-mngr.md) · 탭 ④ (`content3`)

---

## 5.8.10.1 메일 알림 설정

| 항목 | 템플릿 변수 | 설명 |
|------|------------|------|
| 30일 전 메일 | `{{cd}}`, `{{cd_nm}}`, `{{expiry_dt}}`, `{{days_remaining}}`, `{{start_dt}}`, `{{due}}`, `{{api_ownr_email_addr}}` | 만료 30일 전 발송 |
| 7일 전 메일 | 동일 | 만료 7일 전 발송 |
| 당일 메일 | 동일 | 만료 당일 발송 |

**메일 설정 항목:**
- 메일 제목
- 보내는 사람 Email
- 메일 내용
- 미리보기 (샘플: CD101 기준)
- 과거 버전 이력 (최대 3개)
- 기본값 복원 버튼

**스케줄 설정:**
| 항목 | 설정 내용 |
|------|----------|
| 주기 (일) | 1/3/5/7/10/15/30일 중 선택 |
| 실행 시간 | 00~23시 중 선택 |
| 활성화 | 체크박스로 ON/OFF |

---

## 5.8.10.2 조작 방법

### 5.8.10.3 메일 알림 설정 변경

1. `설정` 탭 선택
2. `메일 알림 설정` 서브 탭 선택
3. 30일 전 / 7일 전 / 당일 메일 제목/내용 수정
4. `설정 저장` 버튼 클릭

### 5.8.10.4 스케줄 설정 변경

1. `설정` 탭 선택
2. `스케줄 설정` 서브 탭 선택
3. 주기(일), 실행 시간, 활성화 여부 설정
4. `설정 저장` 버튼 클릭

---



---pb---

# 5.9 잔디 모니터링

> **기준 버전 / 최종 확인일**: v1.1.0 · 2026-07-22

> **핵심 기능**: 각 Job ID별 수집 활동을 GitHub 잔디(Contribution Graph) 형태의 히트맵으로 시각화하여, 데이터 수집 패턴과 이상 징후를 한눈에 파악합니다.

---

## 5.9.1 메뉴 접속 방법

- **경로**: 상단 메뉴 → 잔디
- **URL**: `/jandi`
- **필요 권한**: `jandi`
- **로그**: 메뉴 접근 시 `tb_user_acs_log` 테이블에 접근 이력이 기록됩니다.

---

## 5.9.2 화면 구성

### 5.9.2.1 전체 화면 구조

![잔디 모니터링 전체 화면](images/jandi-full.png)

### 5.9.2.2 각 영역 상세 설명

#### ① 날짜 선택 카드 (`#date-selection-card-jandi`)

| 요소 | ID | 설명 |
|------|-----|------|
| 시작일 | `#start-date` | 조회 시작 날짜 |
| 종료일 | `#end-date` | 조회 종료 날짜 |
| 전체 데이터 조회 | `#allDataCheckbox` | 체크 시 전체 기간 조회 |
| 조회 버튼 | `#filter-button` | 데이터 갱신 |

#### ② Job ID 상세정보 카드 (`#job-info-card-jandi`)

- 데이터 분석 메뉴얼의 Job ID 상세정보와 동일한 구조
- `tb_con_mst`의 Job 기본 정보 표시

#### ③ Job ID별 잔디 모니터링 카드 (`#jandi-monitoring-card`)

**정렬 기능:**
| 버튼 | ID | 설명 |
|------|-----|------|
| Job ID 오름차순 | `#sortAsc` | Job ID A→Z 정렬 |
| Job ID 내림차순 | `#sortDesc` | Job ID Z→A 정렬 |

**검색 및 페이징:**
| 기능 | ID | 설명 |
|------|-----|------|
| 검색 | `#jandiSearch` | Job ID 또는 한글명 필터링 |
| 행 수 | `#jandiPageSize` | 5/10/15/20개 선택 |
| 페이징 | `#jandiPagination` | 페이지 이동 |

**히트맵 (`#heatmap-container`):**
- 각 Job ID별로 가로로 펼쳐진 캘린더 히트맵
- X축: 날짜 (월 단위 표시)
- Y축: 요일 (생략 가능)
- 색상 밀도: 해당 날짜의 수집 성공률 또는 수집 횟수
  - 진한 녹색: 높은 성공률/많은 수집
  - 연한 녹색/회색: 낮은 성공률/적은 수집
  - 흰색/비어있음: 수집 없음

**데이터 출처:**
- API: `GET /api/jandi`
- Service: `JandiService`
- Mapper: `JandiMapper`
- SQL: `sql/jandi/jandi_sql.py`
- 테이블: `tb_con_hist`

---

## 5.9.3 데이터 흐름 및 처리 로직

### 5.9.3.1 전체 데이터 흐름도

![전체 데이터 흐름도](images/09-jandi-data-flow.png)

### 5.9.3.2 히트맵 데이터 집계

```
집계 단위: 일별 (date)
집계 대상: job_id별
집계 값: 
  - 성공률 = (성공 건수 / 전체 건수) × 100
  - 또는 수집 횟수 (count)

응답 구조:
[
  {
    "job_id": "CD101",
    "cd_nm": "기상청예보",
    "data": [
      {"date": "2025-01-01", "value": 95},
      {"date": "2025-01-02", "value": 100},
      ...
    ]
  }
]
```

### 5.9.3.3 색상 스케일

| 색상 | 조건 |
|------|------|
| 진한 녹색 | 성공률 ≥ 90% 또는 수집 횟수 ≥ 상위 25% |
| 중간 녹색 | 성공률 70~89% 또는 수집 횟수 중간 |
| 연한 녹색 | 성공률 50~69% 또는 수집 횟수 하위 |
| 연한 회색 | 성공률 1~49% 또는 수집 횟수 매우 적음 |
| 흰색/없음 | 수집 없음 (0%) |

---

## 5.9.4 조작 방법

### 5.9.4.1 날짜 범위 변경

**조작 절차:**
1. 시작일/종료일 선택
2. `조회` 버튼 클릭

**확인 방법:**
- 히트맵의 날짜 범위가 변경됨

### 5.9.4.2 Job ID 정렬

**조작 절차:**
1. `Job ID 오름차순` 또는 `Job ID 내림차순` 버튼 클릭

**확인 방법:**
- 히트맵 카드의 순서가 변경됨

### 5.9.4.3 히트맵 해석

**조작 절차:**
1. 히트맵의 특정 셀에 마우스 오버
2. 툴팁으로 해당 날짜의 상세 정보 확인

**확인 내용:**
- 날짜
- 수집 성공률 (%)
- 수집 횟수
- 상태 (성공/실패/미수집)

---

## 5.9.5 모니터링 체크리스트

- [ ] **히트맵에 흰색(비어있는) 구간**이 없는지 확인 (연속 미수집 여부)
- [ ] **특정 Job**의 색상이 전반적으로 연한지 확인 (지속적 낮은 성공률)
- [ ] **주기적 패턴**이 이상한지 확인 (예: 특정 요일마다 실패)
- [ ] **최근 날짜**의 색상이 정상인지 확인

---

## 5.9.6 자주 발생하는 문제

| 증상 | 원인 | 해결 방법 |
|------|------|-----------|
| 히트맵이 비어있음 | 날짜 범위 내 데이터 없음 | 날짜 범위 확대 |
| 특정 Job이 보이지 않음 | 사용자 데이터 권한 없음 | 관리자에게 데이터 접근 권한 요청 |
| 히트맵 색상이 모두 연함 | 해당 기간 내 지속적인 낮은 성공률 | 수집 에이전트 상태 확인 |
| 히트맵에 줄무늬 패턴 | 주기적 실패 (예: 주말) | 스케줄 설정 확인 |
| 툴팁이 표시되지 않음 | 해당 날짜에 데이터 없음 | 다른 날짜 확인 |

---

## 5.9.7 관련 DB 테이블 및 쿼리

### 5.9.7.1 주요 테이블

| 테이블 | 설명 |
|--------|------|
| `tb_con_hist` | 수집 실행 이력 (날짜, 성공/실패 상태) |
| `tb_con_mst` | 수집 작업 마스터 (Job ID, 데이터명) |
| `tb_user_data_perm_auth_ctrl` | 사용자별 데이터 접근 권한 |

### 5.9.7.2 잔디 조회 API

```
GET /api/jandi?start_date=2025-01-01&end_date=2025-12-31
```

**응답 구조:**
```json
[
  {
    "job_id": "CD101",
    "cd_nm": "기상청예보",
    "data": [
      {"date": "2025-01-01", "success_rate": 95, "count": 10},
      {"date": "2025-01-02", "success_rate": 100, "count": 12}
    ]
  }
]
```

---

> 다음 문서: [10-raw-data.md](10-raw-data.md)


---pb---

# 5.10 원본 데이터

> **기준 버전 / 최종 확인일**: v1.1.0 · 2026-07-22

> **핵심 기능**: 수집된 원본 데이터를 조회하고, 날짜/Job ID 등 다양한 필터로 검색하여 데이터 품질과 수집 상태를 확인합니다.

---

## 5.10.1 메뉴 접속 방법

- **경로**: 상단 메뉴 → 원본 데이터
- **URL**: `/raw_data`
- **필요 권한**: `raw_data`
- **로그**: 메뉴 접근 시 `tb_user_acs_log` 테이블에 접근 이력이 기록됩니다.

---

## 5.10.2 화면 구성

### 5.10.2.1 전체 화면 구조

> 📷 *화면 캡처 미보유 — 운영 환경에서 재캡처 필요. 아래는 구조 파악용 와이어프레임(실제 화면 배치와 세부 스타일은 다를 수 있음).*

![전체 화면 구조](images/10-raw-data-layout.png)

### 5.10.2.2 각 영역 상세 설명

#### ① 필터

| 요소 | 설명 |
|------|------|
| 시작일 | 조회 시작 날짜 |
| 종료일 | 조회 종료 날짜 |
| Job ID | 특정 Job ID 필터 |
| 조회 버튼 | 데이터 갱신 |

#### ② 원본 데이터 테이블

| 컬럼 | 설명 |
|------|------|
| 날짜 | 수집 실행 날짜/시간 |
| Job ID | 수집 작업 ID |
| 상태 | CD901(성공)/CD902(실패)/CD903(미수집) |
| 요청 정보 | API 요청 파라미터 또는 URL |
| 응답 정보 | API 응답 요약 또는 에러 메시지 |
| 소요 시간 | 수집 소요 시간 (ms) |
| 수집 건수 | 실제 수집된 데이터 건수 |

**데이터 출처:** `tb_con_hist`

---

## 5.10.3 조작 방법

### 5.10.3.1 원본 데이터 조회

**조작 절차:**
1. 시작일/종료일 선택
2. Job ID 선택 (선택 사항)
3. `조회` 버튼 클릭

**확인 방법:**
- 테이블에 데이터가 표시되는지 확인
- 총 건수 확인

### 5.10.3.2 상세 데이터 확인

**조작 절차:**
1. 대상 행 클릭
2. 상세 팝업 또는 확장 영역에서 전체 요청/응답 데이터 확인

---

## 5.10.4 모니터링 체크리스트

- [ ] **실패 상태** 데이터가 있는지 확인
- [ ] **소요 시간**이 비정상적으로 긴 경우가 있는지 확인
- [ ] **수집 건수**가 0인 경우가 있는지 확인
- [ ] **특정 기간**에 데이터가 누락되지 않았는지 확인

---

## 5.10.5 자주 발생하는 문제

| 증상 | 원인 | 해결 방법 |
|------|------|-----------|
| 테이블이 비어있음 | 날짜 범위 내 데이터 없음 | 날짜 범위 확대 |
| 상태가 모두 실패 | 수집 에이전트 장애 | 에이전트 로그 확인 |
| 소요 시간이 급증 | 네트워크 지연 또는 대상 서버 과부하 | 대상 서버 상태 확인 |

---

> 다음 문서: [11-admin.md](11-admin.md)


---pb---

# 5.11 관리자 (통계/템플릿)

> **기준 버전 / 최종 확인일**: v1.1.0 · 2026-07-22

> **핵심 기능**: 시스템 사용 현황 통계를 조회하고, 엑셀 템플릿 파일을 관리합니다.

---

## 5.11.1 메뉴 접속 방법

- **경로**: 상단 메뉴 → 관리자
- **URL**: `/admin`
- **필요 권한**: `admin`
- **로그**: 메뉴 접근 시 `tb_user_acs_log` 테이블에 접근 이력이 기록됩니다.

---

## 5.11.2 화면 구성

### 5.11.2.1 전체 화면 구조

> 📷 *화면 캡처 미보유 — 운영 환경에서 재캡처 필요. 아래는 구조 파악용 와이어프레임(실제 화면 배치와 세부 스타일은 다를 수 있음).*

![전체 화면 구조](images/11-admin-layout.png)

### 5.11.2.2 각 영역 상세 설명

#### ① 통계 탭

**필터:**
| 요소 | 설명 |
|------|------|
| 기간 | 조회 시작일/종료일 |
| 메뉴 | 특정 메뉴 필터 (전체/대시보드/수집스케줄 등) |
| 조회 | 데이터 갱신 |

**차트:**
- 메뉴 접근 횟수 추이 (막대/선 차트)
- 사용자별 접근 비율 (파이 차트)
- 시간대별 접근 분포 (히트맵)

**테이블:**
| 컬럼 | 설명 |
|------|------|
| 메뉴 | 메뉴 이름 |
| 접근횟수 | 해당 기간 내 접근 횟수 |
| 사용자수 | 고유 사용자 수 |
| 평균체류 | 평균 체류 시간 |

**데이터 출처:** `tb_user_acs_log`

#### ② 템플릿 탭

**파일 업로드:**
| 요소 | 설명 |
|------|------|
| 파일 선택 | 업로드할 엑셀 템플릿 파일 선택 |
| 업로드 | 선택된 파일 업로드 |

**파일 목록 테이블:**
| 컬럼 | 설명 |
|------|------|
| 파일명 | 템플릿 파일 이름 |
| 크기 | 파일 크기 |
| 등록일 | 업로드 일시 |
| 작업 | 다운로드/삭제 버튼 |

---

## 5.11.3 조작 방법

### 5.11.3.1 통계 조회

**조작 절차:**
1. `통계` 탭 선택
2. 기간/메뉴 선택
3. `조회` 버튼 클릭

### 5.11.3.2 엑셀 템플릿 업로드

**조작 절차:**
1. `템플릿` 탭 선택
2. `파일 선택` 버튼 클릭
3. 엑셀 파일(.xlsx) 선택
4. `업로드` 버튼 클릭

### 5.11.3.3 엑셀 템플릿 다운로드/삭제

**조작 절차:**
1. 대상 행의 `다운로드` 또는 `삭제` 버튼 클릭

---

## 5.11.4 모니터링 체크리스트

- [ ] **메뉴 접근 통계**에서 특정 메뉴의 접근이 급감하지 않았는지 확인
- [ ] **사용자별 접근**에서 비정상적인 접근 패턴이 없는지 확인
- [ ] **템플릿 파일**이 정상적으로 업로드/다운로드되는지 확인

---

## 5.11.5 자주 발생하는 문제

| 증상 | 원인 | 해결 방법 |
|------|------|-----------|
| 통계 데이터가 비어있음 | 접근 이력 없음 | 기간 확대 또는 메뉴 사용 유도 |
| 템플릿 업로드 실패 | 파일 형식 오류 | .xlsx 형식 확인 |
| 차트가 표시되지 않음 | 데이터 부족 | 충분한 기간 선택 |

---

> 다음 문서: [12-api-test.md](12-api-test.md)


---pb---

# 5.12 API 테스트

> **기준 버전 / 최종 확인일**: v1.1.0 · 2026-07-22

> **핵심 기능**: 데이터 수집에 사용되는 API를 직접 호출하여, 요청/응답을 테스트하고 유효성을 검증합니다.

---

## 5.12.1 메뉴 접속 방법

- **경로**: 상단 메뉴 → API 테스트
- **URL**: `/api_test`
- **필요 권한**: `api_test`
- **로그**: 메뉴 접근 시 `tb_user_acs_log` 테이블에 접근 이력이 기록됩니다.

---

## 5.12.2 화면 구성

### 5.12.2.1 전체 화면 구조

> 📷 *화면 캡처 미보유 — 운영 환경에서 재캡처 필요. 아래는 구조 파악용 와이어프레임(실제 화면 배치와 세부 스타일은 다를 수 있음).*

![전체 화면 구조](images/12-api-test-layout.png)

### 5.12.2.2 각 영역 상세 설명

#### ① 요청 패널

| 요소 | 설명 |
|------|------|
| URL | API 엔드포인트 주소 |
| 메서드 | HTTP 메서드 (GET/POST/PUT/DELETE) |
| Content-Type | 요청 본문 형식 (application/json 등) |
| 헤더 | 추가 HTTP 헤더 (키-값 쌍) |
| 바디 | 요청 본문 (JSON/XML/폼 데이터) |
| 실행 버튼 | API 호출 실행 |

#### ② 응답 패널

| 요소 | 설명 |
|------|------|
| 상태 | HTTP 상태 코드 (200, 404, 500 등) |
| 소요시간 | API 호출 소요 시간 (ms) |
| 응답 본문 | API 응답 데이터 (JSON/XML) |

---

## 5.12.3 조작 방법

### 5.12.3.1 API 테스트 실행

**조작 절차:**
1. URL 입력
2. 메서드 선택
3. 필요 시 헤더/바디 입력
4. `실행` 버튼 클릭

**확인 방법:**
- 상태 코드가 200번대인지 확인
- 응답 본문에 예상 데이터가 포함되어 있는지 확인
- 소요 시간이 정상 범위인지 확인

### 5.12.3.2 API 키 테스트

**조작 절차:**
1. URL에 API 키 파라미터 포함
2. `실행` 버튼 클릭
3. 응답 확인

---

## 5.12.4 모니터링 체크리스트

- [ ] **상태 코드**가 200번대인지 확인
- [ ] **응답 시간**이 5초 이내인지 확인
- [ ] **응답 데이터**가 정상적인 형식인지 확인
- [ ] **API 키**가 유효한지 확인

---

## 5.12.5 자주 발생하는 문제

| 증상 | 원인 | 해결 방법 |
|------|------|-----------|
| 404 Not Found | 잘못된 URL | API 명세서 확인 |
| 401 Unauthorized | 잘못된 API 키 | API 키 관리 메뉴에서 키 확인 |
| 500 Internal Server Error | 대상 서버 오류 | 대상 서버 상태 확인 |
| 응답 시간 초과 | 네트워크 지연 | 네트워크 상태 확인 또는 재시도 |
| 응답 데이터 파싱 실패 | 잘못된 JSON 형식 | 응답 본문의 따옴표, 쉼표 확인 |

---

> 다음 문서: [13-external-links.md](13-external-links.md)


---pb---

# 5.13 외부 연동

> **기준 버전 / 최종 확인일**: v1.1.0 · 2026-07-22

> **핵심 기능**: MSYS와 연동되는 외부 시스템(Airflow, Kafka UI 등)으로의 빠른 접근 링크를 제공합니다.

---

## 5.13.1 메뉴 접속 방법

- **경로**: 상단 메뉴 → Airflow / Kafka UI
- **URL**: 외부 URL (새 창으로 열림)
- **필요 권한**: 해당 메뉴 권한
- **로그**: 메뉴 접근 시 `tb_user_acs_log` 테이블에 접근 이력이 기록됩니다.

---

## 5.13.2 외부 시스템 목록

| 메뉴 | 설명 | URL 예시 | 로그인 필요 |
|------|------|----------|------------|
| Airflow | 데이터 수집 워크플로우 스케줄러 및 모니터링 | `http://airflow-server:8080` | 별도 계정 |
| Kafka UI | 메시지 브로커(Kafka) 관리 및 모니터링 | `http://kafka-ui-server:8080` | 별도 계정 |

---

## 5.13.3 주의사항

| 항목 | 설명 |
|------|------|
| 별도 로그인 | 외부 시스템은 MSYS 계정과 별도의 인증이 필요할 수 있습니다. |
| 네트워크 접근 | 외부 시스템 서버에 대한 네트워크 접근 권한이 필요합니다. |
| VPN | 일부 외부 시스템은 VPN 연결이 필요할 수 있습니다. |
| 보안 | 외부 시스템 URL 및 계정 정보는 유출되지 않도록 주의하세요. |

---

## 5.13.4 문제 해결

| 증상 | 원인 | 해결 방법 |
|------|------|-----------|
| 페이지가 열리지 않음 | 네트워크 접근 불가 또는 URL 변경 | 네트워크 상태 확인, 관리자에게 URL 변경 여부 확인 |
| 로그인 실패 | 잘못된 계정 정보 | 해당 시스템의 관리자에게 계정 확인 요청 |
| 403 Forbidden | 접근 권한 없음 | 해당 시스템의 관리자에게 권한 요청 |

---

> 메뉴얼 계속: [05-mngr-sett.md](../05-mngr-sett.md)


---pb---

# 6 관리자 설정 (mngr_sett)

> **기준 버전 / 최종 확인일**: v1.1.0 · 2026-07-22

> ⚠️ **별도 파일 + 탭 하위파일**: 본 메뉴는 탭이 6개로 방대하므로, **구성/탭 설명은 이 파일**에 두고 **각 탭 상세는 `05-mngr-sett.tabN.md` 하위파일**로 분리합니다 (작성 지침 §7.3).

---

## 6.1 메뉴 접속 방법

- **경로**: 상단 메뉴 → 관리자 설정
- **URL**: `/mngr_sett`
- **필요 권한**: `mngr_sett`
- **상세 권한**: 관리자 설정 페이지 접근 및 설정 변경 권한

---

## 6.2 화면 구성 (탭 목록)

> 📷 *화면 캡처 미보유 — 운영 환경에서 재캡처 필요(없는 자산 참조 금지 원칙에 따라 링크 제거).*

| 탭 | 파일 | 설명 |
|----|------|------|
| ① 설정 | [05-mngr-sett.tab1.md](05-mngr-sett.tab1.md) | Job ID별 설정, 임계값, 색상, 스케줄 표시, 백업/복원 |
| ② 사용자 | [05-mngr-sett.tab2.md](05-mngr-sett.tab2.md) | 사용자 승인/거절/삭제, 권한 설정, 대량 추가 |
| ③ 데이터 권한 | [05-mngr-sett.tab3.md](05-mngr-sett.tab3.md) | 사용자별 Job ID 접근 권한 설정 |
| ④ 상태 코드 | [05-mngr-sett.tab4.md](05-mngr-sett.tab4.md) | 상태 코드 동기화 및 커스터마이징 |
| ⑤ 아이콘 | [05-mngr-sett.tab5.md](05-mngr-sett.tab5.md) | 아이콘 등록/수정/삭제, 가져오기/내보내기 |
| ⑥ API 관리 | [05-mngr-sett.tab6.md](05-mngr-sett.tab6.md) | API 키 등록/수정/조회, 만료 알림, 메일 테스트 |

---

## 6.3 모니터링 체크리스트

- [ ] 사용자 승인 대기 목록 매일 확인
- [ ] API 키 만료 30일 이내 항목 주간 확인
- [ ] 상태 코드 동기화 월간 실행
- [ ] 설정 백업 월간 실행

---

## 6.4 자주 발생하는 문제

| 증상 | 원인 | 해결 방법 |
|------|------|-----------|
| 사용자 승인 후 로그인 불가 | 비밀번호 초기화 미반영 | 관리자가 비밀번호 재초기화 |
| API 키 알림 미발송 | SMTP 설정 오류 | `.env` 메일 서버 설정 확인 |
| 상태 코드 미동기화 | CD900 그룹 변경 | 수동 동기화 버튼 실행 |

---



---pb---

# 6.5 관리자 설정 — 설정 탭

> **기준 버전 / 최종 확인일**: v1.1.0 · 2026-07-22

> 소속 메뉴: [관리자 설정 (mngr_sett)](05-mngr-sett.md) · 탭 ①

---

## 6.5.1 조작 절차

### 6.5.1.1 Job ID별 설정

**목적:** 각 수집 작업(Job ID)별로 임계값, 색상, 아이콘을 설정합니다.

**조작 절차:**
1. 설정 탭 선택
2. Job ID 검색 또는 목록에서 선택
3. 임계값(Threshold) 입력
4. 색상 선택
5. 아이콘 선택
6. 저장 버튼 클릭

**확인 방법:** 설정 저장 후 목록에 반영 여부 확인

**주의사항:** 잘못된 임계값 설정 시 대시보드 상태 표시가 부정확해질 수 있습니다.

### 6.5.1.2 스케줄 표시 설정

**그룹 설정:** 수집 스케줄 화면에서 Job ID 그룹핑 기준을 설정합니다.

**진행률 임계값:** 진행률 표시 색상 변경 기준을 설정합니다.

### 6.5.1.3 설정 백업/복원

**설정 내보내기:**
1. 설정 탭 → 내보내기 버튼 클릭
2. `admin_settings.json` 파일 다운로드

**설정 가져오기:**
1. 설정 탭 → 가져오기 버튼 클릭
2. JSON 파일 선택
3. 확인 메시지 확인 후 업로드

---



---pb---

# 6.6 관리자 설정 — 사용자 탭

> **기준 버전 / 최종 확인일**: v1.1.0 · 2026-07-22

> 소속 메뉴: [관리자 설정 (mngr_sett)](05-mngr-sett.md) · 탭 ②

---

## 6.6.1 조작 절차

### 6.6.1.1 사용자 승인

**목적:** 가입 신청한 사용자를 승인합니다.

**조작 절차:**
1. 사용자 탭 선택
2. 상태가 `PENDING`인 사용자 검색
3. 승인 버튼 클릭
4. 확인 다이얼로그에서 확인

**확인 방법:** 사용자 상태가 `APPROVED`로 변경됨

**주의사항:** 승인 시 비밀번호가 ID와 동일하게 초기화됩니다.

### 6.6.1.2 사용자 권한 설정

**목적:** 사용자별 메뉴 접근 권한을 설정합니다.

**조작 절차:**
1. 사용자 탭 선택
2. 대상 사용자 선택
3. 권한 체크박스 그룹에서 메뉴 선택
4. 저장 버튼 클릭

### 6.6.1.3 대량 사용자 추가

**목적:** 여러 사용자를 한 번에 추가합니다.

**조작 절차:**
1. 사용자 탭 → 대량 추가 버튼 클릭
2. 사용자 ID 목록 입력 (쉼표 또는 줄바꿈 구분)
3. 유효성 검사 버튼 클릭
4. 추가 버튼 클릭

**주의사항:** 4-20자 영문, 숫자만 허용됩니다.

---



---pb---

# 6.7 관리자 설정 — 데이터 권한 탭

> **기준 버전 / 최종 확인일**: v1.1.0 · 2026-07-22

> 소속 메뉴: [관리자 설정 (mngr_sett)](05-mngr-sett.md) · 탭 ③

---

## 6.7.1 조작 절차

### 6.7.1.1 Job ID 접근 권한 설정

**목적:** 사용자별로 접근 가능한 Job ID를 제한합니다.

**조작 절차:**
1. 데이터 권한 탭 선택
2. 대상 사용자 선택
3. Job ID 체크박스 선택
4. 저장 버튼 클릭

**확인 방법:** 해당 사용자로 로그인 후 접근 가능한 Job ID만 표시되는지 확인

---



---pb---

# 6.8 관리자 설정 — 상태 코드 탭

> **기준 버전 / 최종 확인일**: v1.1.0 · 2026-07-22

> 소속 메뉴: [관리자 설정 (mngr_sett)](05-mngr-sett.md) · 탭 ④

---

## 6.8.1 조작 절차

### 6.8.1.1 상태 코드 동기화

**목적:** `tb_con_mst`의 CD900 그룹과 `tb_sts_cd_mst`를 동기화합니다.

**조작 절차:**
1. 상태 코드 탭 선택
2. 동기화 버튼 클릭
3. 결과 메시지 확인

### 6.8.1.2 상태 코드 커스터마이징

**목적:** 상태 코드별 색상, 아이콘, 배경/글자색을 설정합니다.

**조작 절차:**
1. 상태 코드 탭 선택
2. 대상 상태 코드 행 선택
3. 색상 선택기에서 색상 선택
4. 아이콘 드롭다운에서 선택
5. 저장 버튼 클릭

---



---pb---

# 6.9 관리자 설정 — 아이콘 탭

> **기준 버전 / 최종 확인일**: v1.1.0 · 2026-07-22

> 소속 메뉴: [관리자 설정 (mngr_sett)](05-mngr-sett.md) · 탭 ⑤

---

## 6.9.1 조작 절차

### 6.9.1.1 아이콘 등록/수정

**목적:** 시스템에서 사용할 아이콘을 관리합니다.

**조작 절차:**
1. 아이콘 탭 선택
2. 등록 버튼 클릭
3. 아이콘 코드, 이름, 설명 입력
4. 이미지 업로드
5. 저장 버튼 클릭

### 6.9.1.2 아이콘 가져오기/내보내기

**조작 절차:**
- 내보내기: CSV 버튼 클릭 → `icons.csv` 다운로드
- 가져오기: 파일 선택 → CSV 업로드 → 확인

---



---pb---

# 6.10 관리자 설정 — API 관리 탭

> **기준 버전 / 최종 확인일**: v1.1.0 · 2026-07-22

> 소속 메뉴: [관리자 설정 (mngr_sett)](05-mngr-sett.md) · 탭 ⑥

---

## 6.10.1 조작 절차

### 6.10.1.1 API 키 목록 조회

**목적:** 등록된 API 키 목록을 조회합니다.

**조작 절차:**
1. API 관리 탭 선택
2. 페이징 또는 검색어 입력
3. 목록 확인

**확인 항목:** 코드, 만료일, 담당자 이메일, 상태

### 6.10.1.2 API 키 등록/수정

**조작 절차:**
1. 등록 버튼 클릭
2. 코드, 만료일, 담당자 이메일 입력
3. 저장 버튼 클릭

**주의사항:** 만료일이 지난 API 키는 알림 대상이 됩니다.

### 6.10.1.3 API 키 삭제

**조작 절차:**
1. 대상 행 선택
2. 삭제 버튼 클릭
3. 확인 다이얼로그에서 확인

### 6.10.1.4 만료 알림 설정

**목적:** API 키 만료 전 메일 알림을 설정합니다.

**알림 기준:**

| 기간 | 발송 시점 |
|------|----------|
| 30일 전 | 1회 발송 |
| 7~1일 전 | 매일 발송 |
| 당일 | 1회 발송 |

### 6.10.1.5 메일 테스트

**조작 절차:**
1. 테스트 메일 발송 버튼 클릭
2. SMTP 연결 및 발송 결과 확인

---



---pb---

# 7 일상 운영

> **기준 버전 / 최종 확인일**: v1.1.0 · 2026-07-22


> 본 문서는 **여러 메뉴를 넘나드는 하루 운영 업무를 시나리오(Task)로** 재현한다(작성 지침 `DEVELOPMENT.md §7.5`). 각 단계는 해당 메뉴 문서로 링크하고, 조작하는 **요소만 캡처한 이미지**(§2 규칙)를 붙인다. 이미지는 이 문서와 같은 위치의 `images/`에 저장한다.

---

## 7.1 하루 운영 시나리오 (End-to-End)

### 7.1.1 오전 점검 루틴 — 야간 수집 결과 확인 → 실패 대응

- **상황/목표**: 매일 오전, 전일 야간 수집 정상 여부를 확인하고 실패 Job을 조치한다.
- **사전 조건**: 서비스 기동 상태(§2 일일 점검), `dashboard` 권한.
- **단계**:
  1. 서비스 기동 확인(§2) 후 **대시보드** 진입 → 일간 성공률 확인.
     > 📷 *화면 캡처 미보유 — 운영 환경에서 재캡처 필요(없는 자산 참조 금지 원칙에 따라 링크 제거).*
     - 상세는 [04-common-menus/01-dashboard.md](04-common-menus/01-dashboard.md) §5.1 참조.
  2. **연속 실패(빨간색) Job** 발견 시 Job ID로 검색 → 이벤트 로그에서 상태 코드(CD902/CD903) 확인.
     > 📷 *화면 캡처 미보유 — 운영 환경에서 재캡처 필요(없는 자산 참조 금지 원칙에 따라 링크 제거).*
  3. 원인이 **스케줄/주기** 문제로 의심되면 [02-collection-schedule.md](04-common-menus/02-collection-schedule.md)에서 해당 Job 스케줄 점검.
  4. 시스템 오류로 의심되면 §3 로그 확인 → 필요 시 [07-troubleshooting.md](07-troubleshooting.md) 절차 수행.
- **완료 확인**: 실패 Job의 원인 파악 및 조치/에스컬레이션 완료. 이벤트 로그 저장으로 근거 확보.

### 7.1.2 신규 수집 등록 → 정상 수집 확인

- **상황/목표**: 신규 수집 대상을 등록하고, 첫 수집이 정상 동작하는지 확인한다.
- **단계**:
  1. [02-collection-schedule.md](04-common-menus/02-collection-schedule.md)에서 수집 스케줄 등록/활성화.
     > 📷 *화면 캡처 미보유 — 운영 환경에서 재캡처 필요(없는 자산 참조 금지 원칙에 따라 링크 제거).*
  2. 예정 시각 경과 후 **대시보드**에서 해당 Job의 당일 성공 건수 확인.
     > 📷 *화면 캡처 미보유 — 운영 환경에서 재캡처 필요(없는 자산 참조 금지 원칙에 따라 링크 제거).*
- **완료 확인**: 대시보드 상세 테이블에 신규 Job이 나타나고 일간 성공률이 집계됨.

### 7.1.3 API 키 만료 대응

- **상황/목표**: 주간 점검에서 만료 임박 API 키를 발견해 갱신·알림 처리한다.
- **단계**:
  1. [08-api-key-mngr.md](04-common-menus/08-api-key-mngr.md)에서 만료 30일 이내 키 목록 확인.
     > 📷 *화면 캡처 미보유 — 운영 환경에서 재캡처 필요(없는 자산 참조 금지 원칙에 따라 링크 제거).*
  2. 갱신/메일 테스트 수행(해당 탭 문서 참조).
- **완료 확인**: 만료 임박 키가 갱신되거나 담당자 알림이 발송됨.

---

## 7.2 정기 점검 항목

### 7.2.1 일일 점검
| 시간 | 항목 | 방법 |
|------|------|------|
| 09:00 | 서비스 기동 상태 | `ps -ef \| grep msys` |
| 09:00 | 대시보드 정상 표시 | 웹 접속 확인 (§1.1) |
| 17:00 | 에러 로그 확인 | `tail -n 100 external_data_monitoring.log` |

### 7.2.2 주간 점검
| 요일 | 항목 |
|------|------|
| 월요일 | 사용자 승인 대기 목록 확인 |
| 월요일 | API 키 만료 30일 이내 목록 확인 (§1.3) |
| 금요일 | 디스크 사용량 확인 |

## 7.3 로그 확인 방법

```bash
# 실시간 로그 확인
tail -f /data/external_data_monitoring/log/external_data_monitoring.log

# 오늘 로그 확인
tail -n 500 /data/external_data_monitoring/log/external_data_monitoring.log

# 특정 날짜 로그 확인
cat /data/external_data_monitoring/log/external_data_monitoring.log.2026-05-11
```

## 7.4 세션 타임아웃

| 사용자 유형 | 세션 유지 시간 |
|------------|--------------|
| 관리자 | 7일 |
| 일반 사용자 | 20분 |

---



---pb---

# 8 장애 대응

> **기준 버전 / 최종 확인일**: v1.1.0 · 2026-07-22


> 증상 → 진단 → 조치를 **Task 기반 시나리오**로 재현한다(작성 지침 `../common/operator-manual/DEVELOPMENT/05-composition-nav.md §1.5`). 각 단계는 관련 메뉴로 링크하고 화면 근거 이미지를 붙인다(`images/`).

---

## 8.1 장애 등급 정의

| 등급 | 기준 | 대응 시간 |
|------|------|----------|
| P1 (심각) | 서비스 전체 중단 | 즉시 |
| P2 (경계) | 주요 기능 장애 | 2시간 이내 |
| P3 (주의) | 일부 기능 이상 | 4시간 이내 |
| P4 (정보) | 경미한 이슈 | 다음 영업일 |

## 8.2 장애 대응 시나리오 (Task 기반)

### 8.2.1 P1 — 서비스 접속 불가 긴급 대응

- **상황/목표**: 웹 접속이 안 됨(P1). 원인을 신속 진단하고 서비스를 복구한다.
- **단계**:
  1. **증상 확인**: 대시보드 URL 접속 실패 재현.
     > 📷 *화면 캡처 미보유 — 운영 환경에서 재캡처 필요(없는 자산 참조 금지 원칙에 따라 링크 제거).*
  2. **진단**: 프로세스(`ps -ef | grep msys`) → 없으면 중단, 있으면 로그 확인(§3.1).
     > 📷 *화면 캡처 미보유 — 운영 환경에서 재캡처 필요(없는 자산 참조 금지 원칙에 따라 링크 제거).*
  3. **조치**: `./start_moni.sh` 기동 → 로그로 정상 부팅 확인.
  4. **복구 확인**: [대시보드](04-common-menus/01-dashboard.md)가 정상 표시되고 요약 패널이 로드되는지 확인.
     > 📷 *화면 캡처 미보유 — 운영 환경에서 재캡처 필요(없는 자산 참조 금지 원칙에 따라 링크 제거).*
- **완료 확인**: 대시보드 정상 + 이벤트 로그에 신규 수집 기록. **미복구 시** DB 연결(§3.2)·인프라 담당(§4) 에스컬레이션.

### 8.2.2 P2 — 특정 수집 Job 연속 실패

- **상황/목표**: 대시보드에서 특정 Job이 연속 실패(빨간색). 원인 구분(스케줄 vs 시스템)해 조치.
- **단계**: [대시보드 §5.1](04-common-menus/01-dashboard.md)로 실패 Job 식별 → 이벤트 로그 상태코드(CD902/CD903) 확인 → [수집 스케줄](04-common-menus/02-collection-schedule.md) 점검 → 필요 시 재수집/담당자 통보.
- **완료 확인**: 실패 원인 확정 및 조치 티켓 생성.

---

## 8.3 자주 발생하는 문제

### 8.3.1 서비스 접속 불가

**증상:** 웹 페이지 로딩 안 됨

**원인:**
- Flask 프로세스 중단
- 방화벽 설정 변경
- DB 연결 실패

**해결 방법:**
```bash
# 1. 프로세스 확인
ps -ef | grep msys

# 2. 프로세스가 없으면 기동
./start_moni.sh

# 3. 로그 확인
tail -n 50 /data/external_data_monitoring/log/external_data_monitoring.log
```

### 8.3.2 DB 연결 오류

**증상:** 대시보드 데이터 미표시

**해결 방법:**
```bash
# 1. DB 서버 연결 확인
psql -h [DB_HOST] -U [DB_USER] -d [DB_NAME] -c "SELECT 1"

# 2. 설정 확인
cat /data/external_data_monitoring/msys/.env | grep DB_
```

### 8.3.3 메일 발송 실패

**증상:** API 키 만료 알림 미발송

**해결 방법:**
- SMTP 서버 연결 확인: `telnet 100.1.28.73 25`
- `.env` 메일 설정 확인
- 관리자 설정 → 메일 테스트 실행

## 8.4 긴급 연락처

| 역할 | 연락처 | 비고 |
|------|--------|------|
| 시스템 담당자 | - | - |
| DB 담당자 | - | - |
| 인프라 담당자 | - | - |

---



---pb---

# 9 백업 및 복구

> **기준 버전 / 최종 확인일**: v1.1.0 · 2026-07-22


> 백업·복구를 **Task 기반 시나리오**로 재현한다(작성 지침 `../common/operator-manual/DEVELOPMENT/05-composition-nav.md §1.5`). 각 단계에 실행 명령·확인지점을 명시한다.

---

## 9.1 백업 전략

| 대상 | 주기 | 방법 | 보관 기간 |
|------|------|------|----------|
| 소스 코드 | 배포 시 | ZIP 백업 | 최근 5개 |
| 설정 파일 | 매일 | `.env` 복사 | 30일 |
| DB 스키마 | 변경 시 | DDL 저장 | 영구 |
| DB 데이터 | 매일 | pg_dump | 7일 |

## 9.2 백업 절차

### 9.2.1 소스 코드 백업

```bash
# 배포 전 백업
cp -r /data/external_data_monitoring/msys /data/external_data_monitoring/msys_backup_$(date +%Y%m%d)
```

### 9.2.2 DB 백업

```bash
# 전체 DB 백업
pg_dump -h [DB_HOST] -U [DB_USER] -d [DB_NAME] > backup_$(date +%Y%m%d_%H%M%S).sql

# 특정 테이블 백업
pg_dump -h [DB_HOST] -U [DB_USER] -d [DB_NAME] -t tb_user > tb_user_backup.sql
```

### 9.2.3 설정 백업

```bash
cp /data/external_data_monitoring/msys/.env /data/external_data_monitoring/backup/env_backup_$(date +%Y%m%d)
```

## 9.3 복구 절차

### 9.3.1 소스 코드 복구

```bash
# 1. 서비스 중지
./kill_data_moni.sh

# 2. 백업 복원
cp -r /data/external_data_monitoring/msys_backup_YYYYMMDD/* /data/external_data_monitoring/msys/

# 3. 서비스 기동
./start_moni.sh
```

### 9.3.2 DB 복구

```bash
# 1. DB 연결
psql -h [DB_HOST] -U [DB_USER] -d [DB_NAME]

# 2. 복원
\i backup_YYYYMMDD_HHMMSS.sql
```

---

## 9.4 운영 시나리오 (Task 기반)

### 9.4.1 일일 백업 점검

- **상황/목표**: 매일 정기 백업(설정·DB)이 정상 생성됐는지 확인한다.
- **단계**:
  1. 전일 백업 파일 존재·크기 확인(`ls -lh backup/`).
  2. `pg_dump` 로그에 오류 없는지 확인(§2.2).
  3. 보관 기간(§1) 초과분 정리.
- **완료 확인**: 당일자 `.env`·`*.sql` 백업 파일이 정상 크기로 존재.

### 9.4.2 배포 실패 → 소스 롤백

- **상황/목표**: 배포 후 서비스 이상 → 직전 백업으로 신속 롤백.
- **단계**:
  1. 서비스 중지(`./kill_data_moni.sh`).
  2. 직전 백업 복원(§3.1).
  3. 서비스 기동(`./start_moni.sh`) → [대시보드](04-common-menus/01-dashboard.md)·[장애 대응 §2.1](07-troubleshooting.md) 절차로 정상 확인.
- **완료 확인**: 대시보드 정상 표시 + 수집 재개. **미복구 시** DB 복구(§3.2) 병행.

---



---pb---

# 10 구성·설정 시나리오 (신규 데이터/코드/키 추가)


> **기준 버전 / 최종 확인일**: v1.1.0 · 2026-07-22
> 이 시스템은 **관리자 모드**로, 신규 데이터·그룹·키 추가는 순서와 시점을 모르면 매우 어렵다. 아래는 **실제 프로비저닝 업무를 순서대로** 재현한 시나리오다. 각 단계는 관련 메뉴로 링크하고 요소 이미지를 붙인다(`images/`).
>
> **핵심 개념(코드 체계, `tb_con_mst`)**
> - **그룹 코드 = `cd_cl`** — **CD 뒤 숫자가 100의 배수**(예: `CD100`·`CD200`·`CD300`). 하나의 **외부데이터 분류(서버군)를 정의**한다.
> - **상세 코드 = `cd`** — 그룹 범위 **(그룹번호+1 ~ +100)** 안의 코드(예: 그룹 `CD300` → 상세 `CD301`~`CD400`). **개별 데이터(예: 데이터 A)**를 정의한다.
> - 상세코드를 처음 추가하면 **상위 그룹이 자동 활성화**(`use_yn='Y'`)된다. 그룹을 삭제하면 **하위 상세 전체가 함께 삭제**된다.

---

## 10.1 시나리오 리스트 (이럴 땐 여기)

| 상황 | 시나리오 | 특히 주의 |
|------|----------|-----------|
| 완전히 새로운 외부데이터 분류(서버군)가 생김 | [§2 신규 그룹 + 데이터 추가](#2-신규-외부데이터-그룹-추가-데이터-a) | **그룹 코드를 가장 먼저** 정의 |
| 기존 분류에 데이터만 하나 더 | [§3 기존 그룹에 상세코드 추가](#3-기존-그룹에-상세코드데이터-추가) | 그룹 코드 새로 만들지 말 것 |
| API 키 만료 임박/교체 | [§4 API 키 등록·갱신](#4-api-키-등록갱신) | 코드가 먼저 존재해야 등록 가능 |
| 데이터 정의(수집 파라미터) 변경 | [§5 상세코드 정보 수정](#5-상세코드-정보수집-파라미터-수정) | 운영 중 값이면 영향 확인 |
| 데이터/그룹 사용 중단 | [§6 비활성·삭제](#6-데이터그룹-비활성삭제) | 그룹 삭제 = 상세 전체 삭제 |

---

## 10.2 신규 외부데이터 그룹 추가 (데이터 A)

- **상황/목표**: 기존에 없던 새 외부데이터 분류가 생겨, 그 안의 데이터 A를 수집하도록 등록한다.
- **필요 권한**: 관리자(데이터 정의·API 키 관리 권한).
- **선후 순서(반드시 이 순서)**:

| 순서 | 작업 | 무엇을 | **언제/왜** |
|------|------|--------|-------------|
| 1 | **그룹 코드(`cd_cl`) 정의** | 100단위 코드(예: `CD300`)로 그룹 생성 | **가장 먼저.** 그룹 코드가 그룹(분류)을 정의하므로, 없으면 상세코드를 걸 곳이 없다. **새 분류가 생길 때 최초 1회만** |
| 2 | **그룹 상세코드(`cd`) 추가** | 그룹 범위(예: `CD301`)로 데이터 A 정의 — 이름(`cd_nm`)·설명(`cd_desc`)·수집 파라미터(`item1~10`) | 그룹 정의 직후. **상세 첫 추가 시 그룹이 자동 활성화**됨 |
| 3 | (자동) 관리자 설정 생성 | 해당 코드의 성공률 임계값·색상 등 기본값 | 상세코드 생성 시 자동(`/api/data_definition/create_mngr_sett`) — 값 조정만 확인 |
| 4 | **API 키 등록** | 데이터 A 코드로 키 등록 — 만료(`DUE`)·시작일·담당자 이메일 | **코드가 존재한 뒤.** 미등록 코드는 API 키 관리에서 "키 없는 코드"로 노출됨 |
| 5 | 수집 스케줄·스펙·매핑 | 수집 주기(cron)·데이터 스펙·컬럼 매핑 | 키 등록 후, 실수집 전 |

- **단계별 화면**:
  1. 데이터 정의 관리에서 **그룹 코드 생성**(100단위).
     > 📷 *화면 캡처 미보유 — 운영 환경에서 재캡처 필요(없는 자산 참조 금지 원칙에 따라 링크 제거).*
  2. 그 그룹에 **상세코드(데이터 A) 추가** — 이름·설명·수집 파라미터 입력.
     > 📷 *화면 캡처 미보유 — 운영 환경에서 재캡처 필요(없는 자산 참조 금지 원칙에 따라 링크 제거).*
  3. [API 키 관리](04-common-menus/08-api-key-mngr.md)에서 데이터 A 코드로 **키 등록**(만료·담당자).
     > 📷 *화면 캡처 미보유 — 운영 환경에서 재캡처 필요(없는 자산 참조 금지 원칙에 따라 링크 제거).*
- **완료 확인**: 데이터 정의 목록에 그룹(활성)·데이터 A가 보이고, API 키 관리에 만료일이 등록됨. [대시보드](04-common-menus/01-dashboard.md)/[수집 스케줄](04-common-menus/02-collection-schedule.md)에 신규 Job이 예정으로 표시.
- **실패 시**: 상세코드가 안 걸리면 그룹 코드(100단위)가 먼저 생성됐는지 확인. 그래도 안 되면 [장애 대응](07-troubleshooting.md)·담당자 에스컬레이션.

> 데이터 정의 관리 화면의 정확한 메뉴 경로/버튼은 실제 화면에서 확인해 이미지를 캡처한다(API: `POST /api/data_definition/create`). 코드 체계(그룹=100단위, 상세=그룹범위)는 `service/data_definition_service.py`로 검증됨.

---

## 10.3 기존 그룹에 상세코드(데이터) 추가

- **상황/목표**: 이미 있는 분류(그룹 코드 존재)에 데이터 한 종만 추가.
- **순서**: §2의 **2~5단계만** 수행(그룹 코드 새로 만들지 않음). 그룹 범위 안의 빈 상세코드를 사용.
- **완료 확인**: 상세코드가 해당 그룹 아래 추가되고 API 키까지 등록됨.

---

## 10.4 API 키 등록·갱신

- **상황/목표**: 신규 코드에 키 등록 또는 만료 임박 키 교체.
- **선행**: 대상 **코드가 존재**해야 함(없으면 §2·§3 먼저).
- **단계**: [API 키 관리](04-common-menus/08-api-key-mngr.md) → 대상 코드 선택 → 만료(`DUE`)·시작일·담당자 이메일 입력 → 저장 → 필요 시 메일 테스트.
- **완료 확인**: 목록에 만료일 갱신, 만료 30일 이내 목록에서 제외.

---

## 10.5 상세코드 정보(수집 파라미터) 수정

- **상황/목표**: 운영 중 데이터의 이름/설명/수집 파라미터(`item1~10`) 변경.
- **주의**: 운영 중 값이면 수집에 영향. 변경 후 [대시보드](04-common-menus/01-dashboard.md)에서 다음 수집이 정상인지 확인.

---

## 10.6 데이터/그룹 비활성·삭제

- **상황/목표**: 데이터 또는 분류 전체 사용 중단.
- **🔴 주의**: **그룹(100단위 코드)을 삭제하면 그 그룹의 상세코드가 전부 함께 삭제**된다(cascade). 데이터 한 종만 내릴 땐 **상세코드만** 삭제/비활성.
- **완료 확인**: 대상이 목록에서 사라지거나 비활성 표시. 대시보드/수집 스케줄에서 해당 Job 미표시.

---



---pb---

# 부록 A 자주 쓰는 명령어 모음

## 부록 A.1 서비스 제어

```bash
# 기동
./start_moni.sh

# 중지
./kill_data_moni.sh

# 프로세스 확인
ps -ef | grep msys
```

## 부록 A.2 로그 확인

```bash
# 실시간
tail -f /data/external_data_monitoring/log/external_data_monitoring.log

# 오늘 100줄
tail -n 100 /data/external_data_monitoring/log/external_data_monitoring.log

# 오류 검색
grep "ERROR" /data/external_data_monitoring/log/external_data_monitoring.log
```

## 부록 A.3 DB 명령어

```bash
# 접속
psql -h [DB_HOST] -U [DB_USER] -d [DB_NAME]

# 테이블 목록
\dt

# 사용자 조회
SELECT * FROM tb_user;

# 세션 종료
\q
```

---

> 다음 문서: [config-reference.md](config-reference.md)


---pb---

# 부록 B 설정값 참조표

## 부록 B.1 .env 설정 항목

| 변수명 | 설명 | 기본값 | 예시 |
|--------|------|--------|------|
| DB_HOST | DB 서버 주소 | localhost | 100.1.28.73 |
| DB_NAME | DB 이름 | - | etl_db_dev |
| DB_USER | DB 사용자 | - | etl_user |
| DB_PASSWORD | DB 비밀번호 | - | [비밀번호] |
| DB_PORT | DB 포트 | 5432 | 5432 |
| FLASK_HOST | 서버 바인드 주소 | 0.0.0.0 | 0.0.0.0 |
| FLASK_PORT | 서버 포트 | 18080 | 18080 |
| FLASK_DEBUG | 디버그 모드 | False | False |
| ADMIN_SESSION_LIFETIME_DAYS | 관리자 세션 유지 일수 | 7 | 7 |
| DEFAULT_SESSION_LIFETIME_MINUTES | 일반 사용자 세션 유지 분 | 20 | 20 |
| MAIL_SERVER | 메일 서버 주소 | - | 100.1.28.73 |
| MAIL_PORT | 메일 서버 포트 | 25 | 25 |

## 부록 B.2 사용자 상태 코드

| 상태 | 설명 |
|------|------|
| PENDING | 가입 신청 대기 |
| APPROVED | 승인 완료 |
| DORMANT | 휴면 |
| INACTIVE | 비활성 |
| PENDING_RESET | 비밀번호 초기화 대기 |

---

> 메뉴얼 끝
