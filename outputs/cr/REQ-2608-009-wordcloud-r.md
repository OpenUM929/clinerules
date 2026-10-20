## 릴리즈 노트

- CR ID  : REQ-2608-009
- 버전   : (미배포 — 내부망 배포 전)
- 배포일자: 미정 (실동작 검증 후)

---

### 변경 사항 요약
> 그룹분석·결과물 관리·Plans Kanban·욕설 리스트 4개 화면의 결함 5건을 수정하고 기능 3건을 신설했다. 단위 테스트 99건 통과, 브라우저 실동작 검증은 대기 중이다.

### 상세 변경 사항

**1. 월별 CR 현황 복구 (`/admin/plans`)**
- CR 문서 경로가 지침 저장소 4구역 재편(`docs/cr` → `outputs/cr`)을 따라가지 않아 화면이 오류 없이 비어 있었다. 경로 교정 후 60건 집계.
- 최근 계획서에 비어 있던 에픽을 기존 어휘 5종 범위에서 채웠다(새 어휘 생성 없음).

**2. 결과물 ZIP 다운로드 500 수정 (`/perspective_test`)**
- 그래프 저장 결과의 `positive`/`negative` 는 연도별 추이 **수치 배열**인데, 다운로드 라우트가 제출용 저장과 같은 이름의 **이미지 URL 문자열**로 가정해 `AttributeError` 로 500 이 났다.
- 구현 중 발견한 별건: 지표 5종이 모두 같은 ZIP 파일명(`E001_graph.png`)이 되어 압축 해제 시 4장이 사라지는 결함도 함께 수정했다.

**3. 결과물 관리 게시판 재편 (`/output-board`)**
- 엔트리 단위 → **저장 묶음 단위**(그래프 5종 = 1행). 즉석 ZIP 다운로드 추가.
- 사번 열 제거, 체크박스 선택 삭제 + 전체 삭제 추가.
- 삭제는 이미지 파일까지 지우고 `outputs/` 는 `.gitignore` 대상이라 복구 수단이 없다 → **건수 직접 입력 · 명시 플래그 · 관리자 재확인 3중** 안전장치.
- 확인창의 건수와 삭제 결과의 건수가 서로 다른 단위(묶음 vs 저장 항목)여서 생긴 혼선을 두 숫자 동시 표기로 해소.

**4. 욕설 리스트 추출 배치 표기 (`/profanity-list`)**
- 배치 관리 화면과 같은 날짜 폴백(`2026-06-11 batch_20260611_0`)을 쓰도록 표시명 정본을 `display_name_with_fallback()` 하나로 모았다.

**5. 그래프 「전체 선택」 재개 (`/perspective_test`)**
- 중단 후 재개 시 5종이 아니라 1종만 돌고 완료되던 결함을 수정. **재개는 화면 상태가 아니라 세션에 저장된 설정을 따르도록** 재설계했다.

**6. 제출용 저장의 그래프 (`/perspective_test`)**
- 그래프 PNG 는 만들어졌으나 세션 결과에 URL 이 기록되지 않아 ZIP 에서 빠졌다 → `배포/그래프/사번_지표명_긍부정그래프.png` 로 포함.
- 제출용 전용 그래프 패널 신설: 지표 5종 복수 선택 + 데이터에 존재하는 연도 체크박스(기존 「최근 N년」 드롭다운 대체).
- 「그래프 저장」이 「전체 선택」이면 제출용 그래프를 못 쓰게 하던 제약을 제거했다.

**7. 추이 그래프 중립 표시 (`/perspective_test`)**
- 중립은 그동안 문장 기준 지표에서 **집계 자체에서 버려지고** 있었고, 단어 기준 지표에서는 **긍정 안에 포함**돼 있었다(워드클라우드 이미지와 맞춘 경계).
- 「긍정/부정 문장 수」 지표에 한해 중립 계열을 그리는 옵션을 추가했다. **기본 꺼짐** — 켜지 않으면 기존 산출물과 값·그림이 같다.

**8. 영향받는 페이지**
- `/admin/plans`, `/perspective_test`, `/output-board`, `/profanity-list`

---

### 수정된 파일

| 구분 | 파일명 |
|------|--------|
| Backend | `wordcloud_project/src/routes/plans_routes.py` |
| Backend | `wordcloud_project/src/routes/perspective_routes.py` |
| Backend | `wordcloud_project/src/services/gallery_db_service.py` |
| Backend | `wordcloud_project/src/services/perspective_service.py` |
| Backend | `wordcloud_project/src/services/batch_manager.py` |
| Backend | `wordcloud_project/src/services/profanity_db_service.py` |
| Frontend | `wordcloud_project/web/templates/output_board.html` (신규) |
| Frontend | `wordcloud_project/web/templates/perspective_test.html` |
| Docs | `wordcloud_project/plans/2026/08/27_01~27_04`, `28_01~28_04` (계획서·테스트·백업) |

---

### 버그 수정

| # | 증상 | 원인 | 조치 |
|---|------|------|------|
| 1 | 월별 CR 현황 전면 공백 | `CR_DIR` 경로가 지침 재편을 미추종, 폴더 부재 시 조용히 빈 목록 | 경로 교정 |
| 2 | 결과물 ZIP 500 | 같은 키(`positive`)가 경로에 따라 배열/문자열 | 타입 가드 |
| 3 | ZIP 안 그래프 4장 소실 | 지표 5종이 동일 파일명 | 원본 파일명 사용 + 충돌 시 접미 번호 |
| 4 | 배치 열 ID 단독 표시 | `batch_summary.json` 부재(데이터 문제) | 날짜 폴백 정본 일원화 |
| 5 | 「전체 선택」 재개 1종만 | 저장값 복원이 패널 열기 안에만 존재 | 재개는 세션 설정을 정본으로 |
| 6 | 제출용 ZIP 에 그래프 누락 | 그래프 응답 URL 폐기 | 세션 결과에 `graphs` 기록 |
| 7 | 삭제 확인 495 → 결과 715 | 묶음 수와 엔트리 수 단위 불일치(계산 오류 아님) | 두 단위 동시 표기 + 입력 단위 통일 |

---

### 알려진 제약

- **모든 계획서가 `Pre-Done`** — 브라우저 실동작 검증 전. 이 릴리즈 노트는 검수 완료를 뜻하지 않는다.
- `REQ-2604-002-wordcloud.md` 가 UTF-16 LE 이라 CR 파서가 조용히 버린다(61→60). 보고만 하고 수정하지 않았다.
- 배치 저장 분할(사용자 요구 1항)은 dev 에 배치 데이터가 없어 실측이 불가능해 계획서(`28_01`)만 수립했다.
