# api_key_mngr

## 파일
- Template: `D:\dev\msys\templates\api_key_mngr.html`
- Route: `D:\dev\msys\routes\ui\api_key_mngr_routes.py`

## 도메인
API 키 만료 관리 - 키 목록, Gantt 차트, 위험군 관리, 메일 알림 설정

## 확장
- `base.html`

## 탭 구조
1. **API 키 관리** - 정상/비정상 테이블
2. **기간 차트** - Gantt 차트
3. **위험군** - 1개월 이내 만료 키
4. **설정** - 메일 알림/스케줄 설정

## API 키 관리 탭
### 필터
- 전체/정상/만료임박(30일)/만료임박(7일)/오버
- 검색: 키 이름 또는 CD
- 페이지당 수량: 10/20/50/100

### 테이블 컬럼
| 컬럼 | 설명 |
|------|------|
| 코드명 | cd |
| 명칭 | cd_nm |
| API값 | API 값 |
| API책임자이메일 | api_ownr_email_addr |
| 기간 | due (년) |
| 등록일 | start_dt |
| 남은 기간 | 계산값 |
| 알림 메일 전송 | 전송 상태 |
| 수정 | 버튼 |

## 기간 차트 탭
- Gantt 차트로 API 키 유효기간 시각화
- 필터, 검색 기능

## 위험군 탭
- 1개월 이내 만료 키 목록
- 메일 전송 상태 (전송완료/실패/대기중)

## 설정 탭
### 메일 알림 설정
- 30일 전 / 7일 전 / 당일 메일 설정
- 제목, 받는사람, 내용 (템플릿 변수 지원)
- 미리보기, 히스토리 버전

### 스케줄 설정
- 일별 스케줄 주기 설정

## 템플릿 변수
| 변수 | 설명 |
|------|------|
| {{cd}} | 코드 값 |
| {{cd_nm}} | 코드 명칭 |
| {{expiry_dt}} | 만료일 |
| {{days_remaining}} | 남은 일수 |
| {{start_dt}} | 등록일 |
| {{due}} | 기간 (년) |
| {{api_ownr_email_addr}} | 책임자 이메일 |

## JS 파일
- `/static/js/pages/api_key_mngr.js`

## 연관 문서
- Service: [../services/api-key-mngr-service.md](../services/api-key-mngr-service.md)
- DAO: [../dao/api-key-mngr-dao.md](../dao/api-key-mngr-dao.md)
- Route: [../routes/api-key-mngr-routes.md](../routes/api-key-mngr-routes.md)
