# API 엔드포인트

> 프로젝트의 API 엔드포인트 정리

---

## 인증 (routes/auth_routes.py)

```
POST   /login              - 사용자 로그인
POST   /register          - 사용자 등록
GET    /logout           - 로그아웃
POST   /change_password  - 비밀번호 변경
GET    /guest_login      - 게스트 로그인
POST   /request-reset-password - 비밀번호 초기화 요청
```

---

## 대시보드

```
GET /api/dashboard/summary         - 대시보드 요약
GET /api/dashboard/min-max-dates   - 데이터 날짜 범위
GET /api/dashboard/event-log       - 이벤트 로그
```

---

## Jandi

```
GET /api/job-list            - Job ID 목록
GET /api/jandi-data          - 히트맵 데이터
GET /api/job_mst_info       - Job 상세정보
```

---

## 수집일정

```
GET /api/collection_schedule   - 일정 데이터
GET /api/group-memo          - 그룹 메모
POST/PUT/DELETE /api/group-memo - 그룹 메모 CRUD
GET /api/memos-batch        - 배치 메모
```

---

## 관리자/설정

```
GET /api/statistics              - 메뉴 접근 통계
GET /api/statistics/config      - 통계 설정
GET /api/statistics/recent_date - 최근 데이터 날짜
POST /api/excel_template/upload - 엑셀 템플릿 업로드
GET /api/excel_template/download - 엑셀 템플릿 다운로드
```

---

## 매핑

```
GET  /mapping/api/all       - 전체 매핑
GET  /mapping/api/unmapped - 미매핑 컬럼
POST /mapping/api/add      - 매핑 추가
POST /mapping/api/update  - 매핑 업데이트
DELETE /mapping/api/delete - 매핑 삭제
```

---

## 관리자 설정 (routes/mngr_sett_routes.py)

```
GET  /api/mngr_sett/settings/all    - 전체 설정 조회
GET  /api/mngr_sett/settings/{id}   - 개별 설정 조회
POST /api/mngr_sett/settings        - 설정 생성
PUT  /api/mngr_sett/settings/{id}   - 설정 수정
DELETE /api/mngr_sett/settings/{id} - 설정 삭제
GET  /api/mngr_sett/icon/list      - 아이콘 목록
POST /api/mngr_sett/icon/upload    - 아이콘 업로드
```

---

## 데이터 리포트 (routes/data_report_routes.py)

```
GET /api/data-report/summary    - 리포트 요약
GET /api/data-report/details    - 리포트 상세
GET /api/data-report/export     - 리포트 내보내기
```

---

## 카드 요약 (routes/card_summary_routes.py)

```
GET /api/card-summary/data      - 카드 요약 데이터
```

---

## 데이터 스펙 (routes/data_spec_routes.py)

```
GET    /api/data-spec          - 명세서 목록
POST   /api/data-spec          - 명세서 생성
GET    /api/data-spec/{id}    - 명세서 상세
PUT    /api/data-spec/{id}    - 명세서 수정
DELETE /api/data-spec/{id}    - 명세서 삭제
GET    /api/data-spec/{id}/params - 명세서 파라미터
```

---

## 분석 (routes/analysis_routes.py)

```
GET /chart_analysis    - 차트 분석 페이지
GET /data_analysis     - 데이터 분석 페이지
```

---

## 오늘의 날짜

```
GET /api/today_date    - 현재 KST 날짜
```

---

## 관련 문서

- [screens.md](screens.md) - 화면/페이지
- [file-structure.md](file-structure.md) - 파일 구조