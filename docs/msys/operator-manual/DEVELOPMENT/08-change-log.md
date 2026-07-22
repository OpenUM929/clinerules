# 08. 수정 이력 및 테스트 결과

> 나침반: [../DEVELOPMENT.md](../DEVELOPMENT.md) · `08-guideline-modification/05.post-modification.md` 준수(지침 수정 후 테스트 기록).

---

## 1. 수정 이력

| 날짜 | 대상 | 변경 내용 |
|------|------|-----------|
| 2026-07-15 | DEVELOPMENT.md | A4 인쇄·파일 구성·탐색·통합 생성 규칙 신설, 명명 예외·체크리스트 보강 |
| 2026-07-15 | build/ 툴링 | `build/print.css`·`MANIFEST.txt`·`build_integrated.py` 추가, `00-index.md` 진입점 추가 |
| 2026-07-15 | DEVELOPMENT.md | 이미지+설명·시나리오 강화: 요소 단위 캡처 의무화, Playwright 절차, 운영 시나리오 섹션/문서 규칙 신설 |
| 2026-07-15 | **DEVELOPMENT/ 분리** | 라인 초과(≈395줄, 절차+예시 혼재) → **나침반 + 원자 문서 8종**(`01-structure`~`08-change-log`)으로 분리(`03.document-separation.md` 준수). **예시급 보강**: 템플릿에 `데이터 흐름 및 처리 로직`·`관련 DB 테이블 및 쿼리` 조건부 표준 절 + 요소 표 규격(`#id`·계산/색상·상태코드) 추가 |
| 2026-07-16 | **운영자 관점 재조정** | 지침 담당자↔운영자 관점 검토 결과 반영: (1) **운영자 우선 순서** — 데이터 흐름·DB/쿼리를 `(참고·심화)`로 강등·맨 뒤 배치(운영자 건너뛰기 가능), (2) 문서 상단 **기준 버전/최종 확인일** 메타 필수, (3) **용어·상태코드 사전**(03 §3) 필수, (4) 시나리오에 **필요 권한·에스컬레이션** 명시, (5) **빠른 작업 색인**(00-index) 필수, (6) **이미지 실제 캡처 게이트**(자리표시=초안/캡처=완료) |
| 2026-07-16 | **공용 지침 위치·명칭 규약 명문화** | 지침이 공용(범용)임을 명시하고, 매뉴얼 위치를 `.clinerules/docs/<프로젝트키>/operator-manual/`(MSYS=`msys`, 워드클라우드=`project_wordcloud`)로 고정. 예시(mngr_sett·cd_cl 등)는 MSYS 예시이며 각 프로젝트는 실제 코드 검증 내용으로 채움(이식 금지) — `05-composition-nav §1.0`, 나침반 상단 명시 |
| 2026-07-16 | **구성/프로비저닝 시나리오 필수화** | 관리자 모드 신규 추가 절차 대응: 시나리오는 모니터링뿐 아니라 **설정 작업(신규 데이터·코드·키 추가)**을 다루고 **순서·시점·선후 의존**을 표로 명시(01 §4, 05 §1.5). 표준 시나리오 문서에 `NN-provisioning-scenarios.md` 카테고리 추가. 실제 산출: `09-provisioning-scenarios.md`(그룹코드=`tb_con_mst.cd_cl` 100단위, 상세=그룹범위, API키는 코드 선행 — `service/data_definition_service.py`로 검증). MANIFEST·00-index 등재 |
| 2026-07-21 | **🔴 md_editor(A4 정본) 파이프라인 전환 — 최우선 정본 신설** | `A/a4-authoring-guide.md`(md_editor 정본, 최우선)를 **[00-a4-authoring-guide.md](00-a4-authoring-guide.md)** 로 편입하고 나침반 §0에 최우선 정본 선언(충돌 시 무조건 우선). **마크업 규칙 전환**: `<img width>`·`<div style>`·`<!-- pagebreak -->`·width≤640·`print.css` 임베드 → **프론트매터 `reportTheme`·`![]()`·`img.<문서명>/`·`---pb---`·한 블록≤257mm** 로 통일. 반영 문서: 나침반 DEVELOPMENT.md(§0·문서지도·한눈요약), 01-structure(프론트매터·`![]()`·`img.<문서명>/` 템플릿), 02-image-capture(삽입 문법·폴더), 04-a4-print(→00 요약으로 전면 재작성), 03-content-rules(표 분할·개조식 목록), 07-checklist(reportTheme·`---pb---`·마크업 잔재 0 항목). **06-integrated-build/`print.css`/`build_integrated.py` 는 삭제하지 않고 "오프라인 PDF 레거시 대체 경로"로 강등**(가역·도구 손실 방지). 근거: md_editor 도구(`report-theme.css`·`tiptap-editor.tsx`)는 외부 저장소, 본 리포 정본 매뉴얼은 아직 구 HTML 파이프라인(`<img width>` 14곳)이라 전환 지침 명문화 필요 |

## 2. 테스트 결과

| 날짜 | 테스트 내용 | 결과 |
|------|------------|------|
| 2026-07-15 | 통합 빌드 최종 상태 재집계 | ✓ `build/MANIFEST.txt` 34개, `integrated-manual.html` `class="pagebreak"` 34개 |
| 2026-07-15 | 예시급 표준 검증 — 예시 메뉴얼(`01-dashboard`) 재현 가능성 | ✓ 템플릿에 데이터 흐름·DB/쿼리·요소 표 규격 추가로 예시 골격 8절 재현 가능 |
| 2026-07-15 | 표준 적용 시범 — `01-dashboard`(운영 시나리오·탐색 링크 추가), `06-daily-operations`(E2E 시나리오화) | ✓ 섹션 번호 정합·탐색 링크 정상 |
| 2026-07-15 | 분리 후 나침반 경로 검증 | ✓ `00-core.md:39`가 `operator-manual/DEVELOPMENT.md`(나침반) 가리킴 — 경로 유지, 갱신 불필요 |

## 3. 검증 시나리오 (05.post-modification 준수)

- 신규 작성자가 나침반(`DEVELOPMENT.md`) → `01-structure.md` 템플릿을 따르면, 데이터성 메뉴는 접속·화면구성(요소 표)·데이터 흐름·조작·운영 시나리오·모니터링·문제·DB/쿼리의 8절을 갖춰 **예시 메뉴얼급** 산출이 나온다. 요소 이미지·시나리오 누락은 체크리스트([07-checklist.md](07-checklist.md))에서 걸러진다.
