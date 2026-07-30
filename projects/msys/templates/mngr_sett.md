# mngr_sett

## 파일
- Template: `D:\dev\msys\templates\mngr_sett.html`
- Route: `D:\dev\msys\routes\admin_routes.py`

## 도메인
관리자 설정 - Job ID별 설정, 아이콘 관리, 사용자 관리, 권한 관리

## 확장
- `base.html`

## 탭 구조 (10개)
1. **기본 설정** - Job ID별 임계값, 아이콘, 색상
2. **수집 스케줄 설정** - 스케줄 표시 설정
3. **Icon 관리** - 아이콘 CRUD
4. **차트/시각화 설정** - 차트 색상, 잔디 색상
5. **사용자 관리** - 사용자 목록, 권한
6. **데이터 접근 권한** - Job ID별 접근 권한
7. **엑셀 양식 관리** - 양식 다운로드
8. **통계** - 통계 정보
9. **데이터정의** - 데이터 정의
10. **팝업 관리** - 팝업 CRUD

## 기본 설정 탭
### 테이블 설정
- Job ID, Job 이름, Job 설명
- 연속 실패시 표시방법 (CNT, Icon, Color)
- 성공률 기준 임계치 (일간/주간/월간/반기/연간)
- 대시보드 표시 여부

### 기능
- 검색, 페이징
- 설정 동기화
- 내보내기/가져오기 (JSON)
- 컬러 팔레트

## Icon 관리 탭
### 필드
| 필드 | ID | 설명 |
|------|-----|------|
| 아이콘 코드 | iconCode | 이모지 |
| 아이콘 이름 | iconName | 이름 |
| 설명 | iconDescription | 설명 |
| 표시 여부 | iconDisplayYn | Y/N |

### 기능
- 추가/수정/삭제
- 내보내기/가져오기 (CSV)
- 페이징

## 사용자 관리 탭
- 사용자 목록 (ID, 상태, 가입일, 메뉴 권한)
- 비밀번호 초기화
- 사용자 삭제
- 대량 사용자 추가
- 검색

## 데이터 접근 권한 탭
- 사용자별 허용 Job ID 설정
- Modal로 권한 할당/제거

## 팝업 관리 탭
- 팝업 목록 (제목, 내용, 표시 여부, 기간)
- 추가/수정/삭제

## 연관 문서
- Service: [../services/mngr-sett-service.md](../services/mngr-sett-service.md), [../services/icon-service.md](../services/icon-service.md)
- DAO: [../dao/mngr-sett-dao.md](../dao/mngr-sett-dao.md), [../dao/icon-dao.md](../dao/icon-dao.md)
- Route: [../routes/admin-routes.md](../routes/admin-routes.md)
