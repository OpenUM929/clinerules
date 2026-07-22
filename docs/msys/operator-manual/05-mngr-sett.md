# 관리자 설정 (mngr_sett)

> ⚠️ **별도 파일 + 탭 하위파일**: 본 메뉴는 탭이 6개로 방대하므로, **구성/탭 설명은 이 파일**에 두고 **각 탭 상세는 `05-mngr-sett.tabN.md` 하위파일**로 분리합니다 (작성 지침 §7.3).

---

## 1. 메뉴 접속 방법

- **경로**: 상단 메뉴 → 관리자 설정
- **URL**: `/mngr_sett`
- **필요 권한**: `mngr_sett`
- **상세 권한**: 관리자 설정 페이지 접근 및 설정 변경 권한

---

## 2. 화면 구성 (탭 목록)

<img src="images/mngr-sett-overview.png" width="600" alt="관리자 설정 전체 화면">

| 탭 | 파일 | 설명 |
|----|------|------|
| ① 설정 | [05-mngr-sett.tab1.md](05-mngr-sett.tab1.md) | Job ID별 설정, 임계값, 색상, 스케줄 표시, 백업/복원 |
| ② 사용자 | [05-mngr-sett.tab2.md](05-mngr-sett.tab2.md) | 사용자 승인/거절/삭제, 권한 설정, 대량 추가 |
| ③ 데이터 권한 | [05-mngr-sett.tab3.md](05-mngr-sett.tab3.md) | 사용자별 Job ID 접근 권한 설정 |
| ④ 상태 코드 | [05-mngr-sett.tab4.md](05-mngr-sett.tab4.md) | 상태 코드 동기화 및 커스터마이징 |
| ⑤ 아이콘 | [05-mngr-sett.tab5.md](05-mngr-sett.tab5.md) | 아이콘 등록/수정/삭제, 가져오기/내보내기 |
| ⑥ API 관리 | [05-mngr-sett.tab6.md](05-mngr-sett.tab6.md) | API 키 등록/수정/조회, 만료 알림, 메일 테스트 |

---

## 3. 모니터링 체크리스트

- [ ] 사용자 승인 대기 목록 매일 확인
- [ ] API 키 만료 30일 이내 항목 주간 확인
- [ ] 상태 코드 동기화 월간 실행
- [ ] 설정 백업 월간 실행

---

## 4. 자주 발생하는 문제

| 증상 | 원인 | 해결 방법 |
|------|------|-----------|
| 사용자 승인 후 로그인 불가 | 비밀번호 초기화 미반영 | 관리자가 비밀번호 재초기화 |
| API 키 알림 미발송 | SMTP 설정 오류 | `.env` 메일 서버 설정 확인 |
| 상태 코드 미동기화 | CD900 그룹 변경 | 수동 동기화 버튼 실행 |

---

> ↑ [목록으로](00-index.md) · 이전: [04-common-menus/13-external-links.md](04-common-menus/13-external-links.md) · 다음: [06-daily-operations.md](06-daily-operations.md) →
