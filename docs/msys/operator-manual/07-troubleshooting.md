# 장애 대응

↑ [목록으로](00-index.md)

> 증상 → 진단 → 조치를 **Task 기반 시나리오**로 재현한다(작성 지침 `DEVELOPMENT/05-composition-nav.md §1.5`). 각 단계는 관련 메뉴로 링크하고 화면 근거 이미지를 붙인다(`images/`).

---

## 1. 장애 등급 정의

| 등급 | 기준 | 대응 시간 |
|------|------|----------|
| P1 (심각) | 서비스 전체 중단 | 즉시 |
| P2 (경계) | 주요 기능 장애 | 2시간 이내 |
| P3 (주의) | 일부 기능 이상 | 4시간 이내 |
| P4 (정보) | 경미한 이슈 | 다음 영업일 |

## 2. 장애 대응 시나리오 (Task 기반)

### 2.1 P1 — 서비스 접속 불가 긴급 대응

- **상황/목표**: 웹 접속이 안 됨(P1). 원인을 신속 진단하고 서비스를 복구한다.
- **단계**:
  1. **증상 확인**: 대시보드 URL 접속 실패 재현.
     <img src="images/troubleshoot-scn1-nored.png" width="600" alt="접속 실패 화면">
  2. **진단**: 프로세스(`ps -ef | grep msys`) → 없으면 중단, 있으면 로그 확인(§3.1).
     <img src="images/troubleshoot-scn1-ps.png" width="600" alt="프로세스 확인 결과">
  3. **조치**: `./start_moni.sh` 기동 → 로그로 정상 부팅 확인.
  4. **복구 확인**: [대시보드](04-common-menus/01-dashboard.md)가 정상 표시되고 요약 패널이 로드되는지 확인.
     <img src="images/troubleshoot-scn1-recovered.png" width="600" alt="대시보드 복구 확인">
- **완료 확인**: 대시보드 정상 + 이벤트 로그에 신규 수집 기록. **미복구 시** DB 연결(§3.2)·인프라 담당(§4) 에스컬레이션.

### 2.2 P2 — 특정 수집 Job 연속 실패

- **상황/목표**: 대시보드에서 특정 Job이 연속 실패(빨간색). 원인 구분(스케줄 vs 시스템)해 조치.
- **단계**: [대시보드 §5.1](04-common-menus/01-dashboard.md)로 실패 Job 식별 → 이벤트 로그 상태코드(CD902/CD903) 확인 → [수집 스케줄](04-common-menus/02-collection-schedule.md) 점검 → 필요 시 재수집/담당자 통보.
- **완료 확인**: 실패 원인 확정 및 조치 티켓 생성.

---

## 3. 자주 발생하는 문제

### 3.1 서비스 접속 불가

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

### 3.2 DB 연결 오류

**증상:** 대시보드 데이터 미표시

**해결 방법:**
```bash
# 1. DB 서버 연결 확인
psql -h [DB_HOST] -U [DB_USER] -d [DB_NAME] -c "SELECT 1"

# 2. 설정 확인
cat /data/external_data_monitoring/msys/.env | grep DB_
```

### 3.3 메일 발송 실패

**증상:** API 키 만료 알림 미발송

**해결 방법:**
- SMTP 서버 연결 확인: `telnet 100.1.28.73 25`
- `.env` 메일 설정 확인
- 관리자 설정 → 메일 테스트 실행

## 4. 긴급 연락처

| 역할 | 연락처 | 비고 |
|------|--------|------|
| 시스템 담당자 | - | - |
| DB 담당자 | - | - |
| 인프라 담당자 | - | - |

---

↑ [목록으로](00-index.md) · [← 이전: 일상 운영](06-daily-operations.md) · [다음: 백업 및 복구 →](08-backup-recovery.md)
