# API 키 관리

> **핵심 기능**: 데이터 수집에 사용되는 API 키의 등록, 조회, 수정, 삭제 및 만료 알림 메일 스케줄 관리를 수행합니다.
> **탭 하위파일**: 각 탭 상세는 `08-api-key-mngr.tabN.md`로 분리합니다 (작성 지침 §7.3).

---

## 1. 메뉴 접속 방법

- **경로**: 상단 메뉴 → API 키 관리
- **URL**: `/api_key_mngr`
- **필요 권한**: `api_key_mngr`
- **로그**: 메뉴 접근 시 `tb_user_acs_log` 테이블에 접근 이력이 기록됩니다.

---

## 2. 화면 구성 (탭 목록)

| 탭 | 파일 | 설명 |
|----|------|------|
| API 키 관리 | [08-api-key-mngr.tab1.md](08-api-key-mngr.tab1.md) | API 키 목록 조회/등록/수정/삭제, 메일 테스트 |
| 기간 차트 | [08-api-key-mngr.tab2.md](08-api-key-mngr.tab2.md) | API 키 유효기간 간트 차트 시각화 |
| 위험군 | [08-api-key-mngr.tab3.md](08-api-key-mngr.tab3.md) | 1개월 이내 만료 API 키 관리 |
| 설정 | [08-api-key-mngr.tab4.md](08-api-key-mngr.tab4.md) | 메일 알림 및 스케줄 설정 |

---

## 3. 데이터 흐름 및 처리 로직

### 3.1 전체 데이터 흐름도

```
[사용자] → [api_key_mngr.html] → [api_key_mngr.js]
                                             ↓
                         [fetch('/api/api_key_mngr')]
                                             ↓
                         [api_key_mngr_routes.py]
                                             ↓
                         [ApiKeyMngrService]
                                             ↓
                         [ApiKeyMngrMapper]
                                             ↓
                         [TB_API_KEY_MNGR]
                                             ↓
                         [메일 스케줄러 연동]
```

### 3.2 API 키 상태 분류 기준

| 상태 | 조건 |
|------|------|
| 정상 | 만료일 - 오늘 > 30일 |
| 만료 임박(30일) | 7일 < 만료일 - 오늘 ≤ 30일 |
| 만료 임박(7일) | 0일 < 만료일 - 오늘 ≤ 7일 |
| 오버 | 만료일 - 오늘 ≤ 0일 |

### 3.3 메일 알림 스케줄

```
1. 스케줄러가 설정된 주기/시간에 실행
2. TB_API_KEY_MNGR에서 대상 키 조회 (30일/7일/당일 기준)
3. 메일 템플릿 변수 치환
4. SMTP 서버 통해 메일 발송
5. 발송 결과를 TB_API_KEY_MNGR_MAIL_LOG에 기록
```

---

## 4. 모니터링 체크리스트

- [ ] **오버 상태 키**가 있는지 확인 (즉시 갱신 필요)
- [ ] **만료 임박(7일)** 키가 있는지 확인
- [ ] **메일 전송 상태**에서 실패 항목이 있는지 확인
- [ ] **위험군** 키에 대해 담당자가 조치했는지 확인
- [ ] **스케줄 설정**이 활성화되어 있는지 확인
- [ ] **메일 알림 템플릿**이 최신 상태인지 확인

---

## 5. 자주 발생하는 문제

| 증상 | 원인 | 해결 방법 |
|------|------|-----------|
| API 키가 오버로 표시됨 | 만료일이 지남 | 즉시 API 키 갱신 후 등록일/기간 수정 |
| 메일 전송 실패 | SMTP 설정 오류 또는 잘못된 이메일 주소 | 설정 탭의 SMTP 설정 확인, 책임자 이메일 주소 확인 |
| 알림 메일이 가지 않음 | 스케줄 비활성화 또는 주기 설정 부적절 | 설정 탭에서 스케줄 활성화 및 주기 확인 |
| CD 업데이트 후 키가 사라짐 | TB_MNGR_SETT에서 CD가 삭제됨 | TB_CON_MST의 ITEM10 값 확인 |
| 간트 차트가 비어있음 | 등록된 API 키 없음 | API 키 등록 필요 |
| 일괄 수정이 안 됨 | 선택된 항목 없음 | 체크박스로 항목 선택 확인 |

---

## 6. 관련 DB 테이블 및 쿼리

### 6.1 주요 테이블

| 테이블 | 설명 |
|--------|------|
| `tb_api_key_mngr` | API 키 기본 정보 (코드, 값, 책임자, 등록일, 기간) |
| `tb_api_key_mngr_mail_log` | 메일 발송 이력 (발송일, 상태, 결과) |
| `tb_api_key_mngr_mail_sett` | 메일 알림 설정 (템플릿, 스케줄) |
| `tb_api_key_mngr_mail_schd` | 메일 스케줄 정보 (주기, 시간, 활성화 여부) |
| `tb_con_mst` | 수집 작업 마스터 (CD, ITEM10, UDATE_DT) |
| `tb_mngr_sett` | 관리자 설정 (CD 목록) |

### 6.2 API 키 관리 API

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

> ↑ [목록으로](../00-index.md) · 이전: [07-mapping.md](07-mapping.md) · 다음: [09-jandi.md](09-jandi.md) →
