# 일상 운영

↑ [목록으로](00-index.md)

> 본 문서는 **여러 메뉴를 넘나드는 하루 운영 업무를 시나리오(Task)로** 재현한다(작성 지침 `DEVELOPMENT.md §7.5`). 각 단계는 해당 메뉴 문서로 링크하고, 조작하는 **요소만 캡처한 이미지**(§2 규칙)를 붙인다. 이미지는 이 문서와 같은 위치의 `images/`에 저장한다.

---

## 1. 하루 운영 시나리오 (End-to-End)

### 1.1 오전 점검 루틴 — 야간 수집 결과 확인 → 실패 대응

- **상황/목표**: 매일 오전, 전일 야간 수집 정상 여부를 확인하고 실패 Job을 조치한다.
- **사전 조건**: 서비스 기동 상태(§2 일일 점검), `dashboard` 권한.
- **단계**:
  1. 서비스 기동 확인(§2) 후 **대시보드** 진입 → 일간 성공률 확인.
     <img src="images/daily-scn1-dashboard.png" width="600" alt="대시보드 일간 성공률">
     - 상세는 [04-common-menus/01-dashboard.md](04-common-menus/01-dashboard.md) §5.1 참조.
  2. **연속 실패(빨간색) Job** 발견 시 Job ID로 검색 → 이벤트 로그에서 상태 코드(CD902/CD903) 확인.
     <img src="images/daily-scn1-eventlog.png" width="600" alt="실패 Job 이벤트 로그">
  3. 원인이 **스케줄/주기** 문제로 의심되면 [02-collection-schedule.md](04-common-menus/02-collection-schedule.md)에서 해당 Job 스케줄 점검.
  4. 시스템 오류로 의심되면 §3 로그 확인 → 필요 시 [07-troubleshooting.md](07-troubleshooting.md) 절차 수행.
- **완료 확인**: 실패 Job의 원인 파악 및 조치/에스컬레이션 완료. 이벤트 로그 저장으로 근거 확보.

### 1.2 신규 수집 등록 → 정상 수집 확인

- **상황/목표**: 신규 수집 대상을 등록하고, 첫 수집이 정상 동작하는지 확인한다.
- **단계**:
  1. [02-collection-schedule.md](04-common-menus/02-collection-schedule.md)에서 수집 스케줄 등록/활성화.
     <img src="images/daily-scn2-schedule.png" width="600" alt="수집 스케줄 등록">
  2. 예정 시각 경과 후 **대시보드**에서 해당 Job의 당일 성공 건수 확인.
     <img src="images/daily-scn2-dashboard-check.png" width="600" alt="신규 Job 수집 결과">
- **완료 확인**: 대시보드 상세 테이블에 신규 Job이 나타나고 일간 성공률이 집계됨.

### 1.3 API 키 만료 대응

- **상황/목표**: 주간 점검에서 만료 임박 API 키를 발견해 갱신·알림 처리한다.
- **단계**:
  1. [08-api-key-mngr.md](04-common-menus/08-api-key-mngr.md)에서 만료 30일 이내 키 목록 확인.
     <img src="images/daily-scn3-apikey-expiry.png" width="600" alt="API 키 만료 목록">
  2. 갱신/메일 테스트 수행(해당 탭 문서 참조).
- **완료 확인**: 만료 임박 키가 갱신되거나 담당자 알림이 발송됨.

---

## 2. 정기 점검 항목

### 일일 점검
| 시간 | 항목 | 방법 |
|------|------|------|
| 09:00 | 서비스 기동 상태 | `ps -ef \| grep msys` |
| 09:00 | 대시보드 정상 표시 | 웹 접속 확인 (§1.1) |
| 17:00 | 에러 로그 확인 | `tail -n 100 external_data_monitoring.log` |

### 주간 점검
| 요일 | 항목 |
|------|------|
| 월요일 | 사용자 승인 대기 목록 확인 |
| 월요일 | API 키 만료 30일 이내 목록 확인 (§1.3) |
| 금요일 | 디스크 사용량 확인 |

## 3. 로그 확인 방법

```bash
# 실시간 로그 확인
tail -f /data/external_data_monitoring/log/external_data_monitoring.log

# 오늘 로그 확인
tail -n 500 /data/external_data_monitoring/log/external_data_monitoring.log

# 특정 날짜 로그 확인
cat /data/external_data_monitoring/log/external_data_monitoring.log.2026-05-11
```

## 4. 세션 타임아웃

| 사용자 유형 | 세션 유지 시간 |
|------------|--------------|
| 관리자 | 7일 |
| 일반 사용자 | 20분 |

---

↑ [목록으로](00-index.md) · [← 이전: 관리자 설정](05-mngr-sett.md) · [다음: 장애 대응 →](07-troubleshooting.md)
