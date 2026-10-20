## Change Request

- CR ID        : REQ-2608-009
- 레파지토리   : wordcloud (`D:\dev\wordcloud`)
- 요청 타입    : feat (fix 4건 포함)
- 대상 스코프  : routes, services, templates, plans
- 작업 유형    : 기능 작업
- 요청자       : 사용자
- 요청 날짜    : 2026.08.27 ~ 2026.08.28

---

### 지침 진행 과정

1. `project.json` → `project_id=wordcloud`, `guideline.project_dir=projects/wordcloud`
2. `00-core.md` 확인 → "계획서 작성" + "백엔드 API·기능 문제 분석/디버깅" + "소스 수정 전 백업"
3. 참조 문서: `03-plan-mode/10-storage-naming.md`, `14-bugfix-gate.md`, `15-atomization.md`, `18-backup-before-modify.md`, `11-performance-optimization.md`
4. 분석 내용: 계획서 8건(27_01~27_04, 28_01~28_04)에 원인 확정 근거·원자화 표·테스트 계획을 기록. 각 계획 폴더 `backup/` 에 수정 전 원본 보관

---

### 변경 요약 (1줄, 50자 이내)
> 그룹분석·결과물 관리 화면 8건 — 결함 5건 수정 + 기능 3건 신설

### 변경 배경 / 이유
> 사용자가 두 차례에 걸쳐 화면 결함·요구를 보고했다. 다섯 건은 기존 기능이 의도대로 동작하지 않는 결함(A형)이었고, 세 건은 신규 요구(B형)였다. 결함 5건은 모두 **원인 확정 게이트**(재현 → 관측 → 반증)를 통과한 뒤 수정했다.

### 변경 전 → 변경 후

- Before:
  - Plans Kanban 의 월별 CR 현황이 오류 표시도 없이 통째로 비어 있었다
  - 그래프 ZIP 다운로드가 500 (Internal Server Error)
  - 결과물 관리 게시판이 엔트리 단위 목록이라 ZIP 관리·다운로드·삭제가 불가
  - 욕설 리스트의 추출 배치 열이 배치 ID 만 표시
  - 그래프 「전체 선택(5종)」을 중단 후 재개하면 1종만 돌고 완료
  - 제출용 저장에 그래프를 포함해도 결과물 ZIP 에 그래프가 없음
  - 제출용 그래프의 종류·연도를 고를 수단이 없음
  - 추이 그래프에 중립이 표시되지 않음
- After:
  - CR 60건 집계 표시, ZIP 200 정상, 게시판이 저장 묶음 단위 + 다운로드 + 선택/전체 삭제
  - 배치 열이 배치 관리 화면과 동일한 날짜 폴백 표기
  - 재개가 5종을 이어서 완료, 제출용 ZIP 에 `배포/그래프/` 포함
  - 제출용 전용 그래프 패널(지표 5종 × 존재 연도 체크박스)
  - 중립 계열 표시 옵션(기본 꺼짐 — 기존 산출물과 정합 유지)

### 영향 범위
> `/admin/plans`, `/perspective_test`, `/output-board`, `/profanity-list`. 백엔드는 라우트 3개 신설·1개 수정, 서비스 함수 4개 신설·5개 수정. DB 스키마 변경 없음.

---

### 작업 상세 내역 (파일별)

| 순번 | 파일 경로 | 변경 유형 | 상세 내용 |
|------|-----------|-----------|-----------|
| 1 | `src/routes/plans_routes.py` | 수정 | 27_01 — `CR_DIR` 이 `.clinerules/docs/cr` 를 가리켜 4구역 재편 후 폴더 부재. `outputs/cr` 로 교정 |
| 2 | `src/routes/perspective_routes.py` | 수정 | 27_02 ZIP 500 수정(비문자열 가드) · `GET /deploy-gallery/bundles` 신설 · `POST /deploy-gallery/bundles/delete` 신설 · 28_03 `graphs` 배열 수집 · 28_04 `include_neutral` 전달 |
| 3 | `src/services/gallery_db_service.py` | 수정 | 27_02 `list_bundles()` 신설(`GROUP BY COALESCE(group_key, id)`) · 27_04 `_bundle_conditions()` 추출 + `delete_by_filter()` 신설(`DELETE_CHUNK=500`) |
| 4 | `src/services/batch_manager.py` | 수정 | 27_03 `display_name_with_fallback()` 신설 — 배치 표시명 폴백 정본 일원화 |
| 5 | `src/services/profanity_db_service.py` | 수정 | 27_03 `_batch_label()` 이 폴백 이름의 ID 중복 표기를 피하도록 수정 |
| 6 | `src/services/perspective_service.py` | 수정 | 27_02 그래프 ZIP 파일명 충돌 방지 · 28_04 중립 집계(`_trend_sentence_counts` 6-튜플, `aggregate_sentiment_trend.neutral`, `_trend_series(include_neutral)`, 차트 3계열) |
| 7 | `web/templates/output_board.html` | 생성 | 26_03/27_02/27_04 — 저장 묶음 게시판. ZIP 다운로드, 체크박스 선택 삭제, 전체 삭제(건수 직접 입력), 묶음/저장 항목 2단위 표기 |
| 8 | `web/templates/perspective_test.html` | 수정 | 28_02 재개가 세션 설정을 따르도록 재설계 · 28_03 제출용 그래프 패널 신설 + 그래프 URL 을 세션 결과에 기록 · 28_04 중립 체크박스 |
| 9 | `plans/2026/08/27_01~27_04`, `28_01~28_04` | 생성 | 계획서 8건 + 테스트 8세트 + 수정 전 백업 |
| 10 | `plans/2026/08/_index.md` | 수정 | 계획 8건 등재 및 상태 동기화 |
| 11 | `plans/2026/08/12_01/test/test_sentiment_trend.py` | 수정 | 28_04 로 `_trend_series` 계약이 2-튜플→3-튜플로 바뀌어 갱신(원본은 28_04 `backup/` 보관) |

**핵심 변경 코드:**

```python
# 27_04 — 목록과 삭제가 같은 조건 빌더를 공유해 "보이는 것 ≠ 지워지는 것"을 구조적으로 차단
def _bundle_conditions(source, batch_title, employee_id, date_from, date_to, is_admin):
    ...
    return where, params
```

```javascript
// 28_02 — 재개는 화면 상태가 아니라 세션에 저장된 설정을 따른다
const saved = await _fetchGraphSessionOptions(resumeSessionId);
const resumeMetrics = (saved && Array.isArray(saved.metric_batch) && saved.metric_batch.length)
    ? saved.metric_batch : [(saved && saved.metric) || ...];
```

---

### 원인 확정 근거 (결함 5건)

| 계획 | 증상 | 확정된 원인 | 반증 |
|------|------|-------------|------|
| 27_01 | 월별 CR 현황 공백 | `CR_DIR` 경로가 지침 4구역 재편을 따라가지 않음. `_scan_all_crs()` 가 폴더 부재 시 오류 없이 `[]` 반환 | 경로 교정 후 60건 집계 |
| 27_02 | ZIP 다운로드 500 | 그래프 task 의 `positive`/`negative` 는 추이 **수치 배열**인데 다운로드 라우트가 이미지 URL 문자열로 가정 → `AttributeError` | 사용자 세션 5개로 재현, 가드 후 200/3.4MB·105장 |
| 27_03 | 배치 열이 ID 만 | 코드가 아니라 데이터 — 확인한 배치 8개 전수에 `batch_summary.json` 부재로 이름이 빈 문자열 | 배치 관리 화면은 날짜 폴백을 써서 달라 보였음 |
| 28_02 | 재개 시 1종만 | 저장값 복원이 `toggleGraphOptions()` 안에만 있어 재개 경로에서 `<select>` 가 HTML 첫 옵션인 채로 읽힘 → 단일 지표 분기로 새어 거부 가드에 **도달 못 함** | select 를 `all` 로 두면 0종+안내(가드 정상), 신규 실행은 5종 정상 |
| 28_03 | 제출용 ZIP 에 그래프 없음 | 처리 루프가 그래프 응답의 카운터만 올리고 URL 을 버려 세션 결과에 `graph` 키가 없음. 수집기는 그 키로만 찾음 | 그래프 저장 단독 경로는 응답에 키가 있어 정상 수집(27_02 실측) |

---

### 검증 결과

| 계획 | 단위 테스트 | 실동작 |
|------|------------|--------|
| 27_01 | 12/12 | **미검증** |
| 27_02 | 16/16 | 부분(ZIP 200·105장 실측) |
| 27_03 | 11/11 | **미검증** |
| 27_04 | 22/22 | **미검증** |
| 28_01 | — (계획만) | — |
| 28_02 | 11/11 | **미검증** |
| 28_03 | 13/13 | **미검증** |
| 28_04 | 14/14 | **미검증** |

회귀: 26_02(14) · 26_04(9) · 20_03 · 20_09(18) · 12_01(스크립트 전 항목) 통과.

> ⚠️ **모든 계획서가 `Pre-Done` 이다.** 브라우저 실동작 검증은 사용자가 서버를 기동한 뒤 수행한다(서버 무단 기동 금지). 이 커밋은 **롤백 지점 확보**를 위한 것이며 검수 완료를 뜻하지 않는다.

---

### 미해결 / 범위 밖 (정직 고지)

| 항목 | 상태 |
|------|------|
| `REQ-2604-002-wordcloud.md` 가 UTF-16 LE 이라 CR 파서가 조용히 버림(61→60) | **보고만**. `.clinerules` 파일이라 수정하지 않음 |
| `12_01/test/test_trend_save_path.py` 2건 실패 | **이번 변경과 무관한 기존 실패**. 파일명 기대가 26_02(지표 라벨 추가) 이후 stale |
| 28_01(배치 저장 분할) | dev 에 배치 데이터가 없어 실측 불가 → 원인 미확정, 계획만 수립 |

---

### FP 산정

FP: 7 (EI:2, EO:4, EQ:1, ILF:0, EIF:0)

| 유형 | 항목 | 복잡도 | FP | 설명 |
|------|------|--------|-----|------|
| EI | 저장 묶음 삭제(선택/전체) | 보통 | 1 | `POST /deploy-gallery/bundles/delete` + 필터 기반 청크 삭제 |
| EI | 제출용 그래프 옵션 입력 | 보통 | 1 | 지표 5종 × 존재 연도 체크박스 → 세션 options |
| EO | 결과물 ZIP 에 그래프 포함 | 보통 | 1 | 세션 결과에 `graphs` 기록 + 수집기 확장 |
| EO | 추이 그래프 중립 계열 | 보통 | 1 | 집계·계열·차트 3계층 확장(기본 꺼짐) |
| EO | 월별 CR 현황 출력 | 낮음 | 1 | 경로 교정으로 60건 집계 복구 |
| EO | 배치 표시명 폴백 표기 | 낮음 | 1 | `display_name_with_fallback()` 일원화 |
| EQ | 저장 묶음 목록 조회 | 보통 | 1 | `GET /deploy-gallery/bundles`(묶음 수·엔트리 수 동시 반환) |

공수: 61.6H (7 FP × 8.8H, 20 FP/월 기준 환산값)

---

### 공지용 요약

**[상세 내용]**
> 그룹분석(`/perspective_test`)·결과물 관리(`/output-board`)·Plans Kanban(`/admin/plans`)·욕설 리스트(`/profanity-list`) 4개 화면에서 보고된 8건을 처리했다. 결함 5건(CR 현황 공백, ZIP 500, 배치 라벨, 그래프 재개 1종, 제출용 ZIP 그래프 누락)은 원인 확정 게이트를 통과해 수정했고, 기능 3건(묶음 게시판 + 삭제, 제출용 그래프 종류·연도 선택, 중립 표시)은 신설했다. 배치 저장 분할(1항)은 dev 에 데이터가 없어 계획만 수립했다.

**[요약]**
> 그룹분석·결과물 관리 화면 결함 5건 수정 + 기능 3건 신설. 단위 테스트 99건 통과, 실동작 검증은 사용자 확인 대기.
