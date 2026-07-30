# 08. 수정 이력 및 테스트 결과

> 나침반: [../DEVELOPMENT.md](../DEVELOPMENT.md) · `08-guideline-modification/05-post-modification.md` 준수(지침 수정 후 테스트 기록).

---

## 1. 수정 이력

| 날짜 | 대상 | 변경 내용 |
|------|------|-----------|
| 2026-07-15 | DEVELOPMENT.md | A4 인쇄·파일 구성·탐색·통합 생성 규칙 신설, 명명 예외·체크리스트 보강 |
| 2026-07-15 | build/ 툴링 | `build/print.css`·`MANIFEST.txt`·`build_integrated.py` 추가, `00-index.md` 진입점 추가 |
| 2026-07-15 | DEVELOPMENT.md | 이미지+설명·시나리오 강화: 요소 단위 캡처 의무화, Playwright 절차, 운영 시나리오 섹션/문서 규칙 신설 |
| 2026-07-15 | **DEVELOPMENT/ 분리** | 라인 초과(≈395줄, 절차+예시 혼재) → **나침반 + 원자 문서 8종**(`01-structure`~`08-change-log`)으로 분리(`03-document-separation.md` 준수). **예시급 보강**: 템플릿에 `데이터 흐름 및 처리 로직`·`관련 DB 테이블 및 쿼리` 조건부 표준 절 + 요소 표 규격(`#id`·계산/색상·상태코드) 추가 |
| 2026-07-16 | **운영자 관점 재조정** | 지침 담당자↔운영자 관점 검토 결과 반영: (1) **운영자 우선 순서** — 데이터 흐름·DB/쿼리를 `(참고·심화)`로 강등·맨 뒤 배치(운영자 건너뛰기 가능), (2) 문서 상단 **기준 버전/최종 확인일** 메타 필수, (3) **용어·상태코드 사전**(03 §3) 필수, (4) 시나리오에 **필요 권한·에스컬레이션** 명시, (5) **빠른 작업 색인**(00-index) 필수, (6) **이미지 실제 캡처 게이트**(자리표시=초안/캡처=완료) |
| 2026-07-16 | **공용 지침 위치·명칭 규약 명문화** | 지침이 공용(범용)임을 명시하고, 매뉴얼 위치를 `.clinerules/<프로젝트 지침 폴더>/operator-manual/`로 고정. 예시는 중립 표기로 정리|
| 2026-07-16 | **구성/프로비저닝 시나리오 필수화** | 관리자 모드 신규 추가 절차 대응: 시나리오는 모니터링뿐 아니라 **설정 작업(신규 데이터·코드·키 추가)**을 다루고 **순서·시점·선후 의존**을 표로 명시(01 §4, 05 §1.5). 표준 시나리오 문서에 `NN-provisioning-scenarios.md` 카테고리 추가. 실제 산출: `09-provisioning-scenarios.md`(그룹코드=`tb_con_mst.cd_cl` 100단위, 상세=그룹범위, API키는 코드 선행 — `service/data_definition_service.py`로 검증). MANIFEST·00-index 등재 |
| 2026-07-21 | **🔴 md_editor(A4 정본) 파이프라인 전환 — 최우선 정본 신설** | `A/a4-authoring-guide.md`(md_editor 정본, 최우선)를 **[00-a4-authoring-guide.md](00-a4-authoring-guide.md)** 로 편입하고 나침반 §0에 최우선 정본 선언(충돌 시 무조건 우선). **마크업 규칙 전환**: `<img width>`·`<div style>`·`<!-- pagebreak -->`·width≤640·`print.css` 임베드 → **프론트매터 `reportTheme`·`![]()`·`img.<문서명>/`·`---pb---`·한 블록≤257mm** 로 통일. 반영 문서: 나침반 DEVELOPMENT.md(§0·문서지도·한눈요약), 01-structure(프론트매터·`![]()`·`img.<문서명>/` 템플릿), 02-image-capture(삽입 문법·폴더), 04-a4-print(→00 요약으로 전면 재작성), 03-content-rules(표 분할·개조식 목록), 07-checklist(reportTheme·`---pb---`·마크업 잔재 0 항목). **06-integrated-build/`print.css`/`build_integrated.py` 는 삭제하지 않고 "오프라인 PDF 레거시 대체 경로"로 강등**(가역·도구 손실 방지). 근거: md_editor 도구(`report-theme.css`·`tiptap-editor.tsx`)는 외부 저장소, 본 리포 정본 매뉴얼은 아직 구 HTML 파이프라인(`<img width>` 14곳)이라 전환 지침 명문화 필요 |

| 2026-07-23 | **🟢 시각 양식 정본 = print.css 통합빌드로 환원(사용자 결정)** | 이 리포의 운영자·개발 메뉴얼 **시각 양식(form)의 정본을 `print.css` 통합빌드로 확정**. 계기: `integrated-manual.html`(print.css)의 대제목 밑줄 경계선 디자인을 채택했으나 `reportTheme=report`(회색 박스)와 다르고 md_editor 테마 CSS는 외부 저장소라 이 리포에서 못 고침. 조치: (1) **06-integrated-build.md** 를 "레거시"→**정본 렌더·양식**으로 승격 + print.css 양식 사양표(§3) 명문화, (2) **00-a4-authoring-guide.md** 상단에 "마크업 위생 규칙은 렌더러 무관 유효 / 시각 양식은 이 리포=print.css·외부도구=reportTheme" 범위 배너 추가, (3) 나침반 **DEVELOPMENT.md** 문서지도·한눈요약 갱신. 툴링: `build_integrated.py` 보정 — 선두 **프론트매터(`reportTheme:`) 제거**, 정본 페이지나눔 토큰 **`---pb---`** 인식(구 `<!-- pagebreak -->` 별칭 유지), **임의 매뉴얼 폴더 인자** 지원(하위 폴더는 상위 공용 print.css 자동 사용). 산출: `developer-manual/build/MANIFEST.txt` 신설, 운영·개발 메뉴얼 `integrated-manual.{md,html}` 재빌드(프론트매터·`---pb---` 누수 0 검증). **마크업 위생 규칙(표준 md·`![]()`·`---pb---`)은 변경 없음** — 바뀐 것은 시각 양식 정본 경로뿐 |
| 2026-07-27 | **🔴 공용 부분을 `common/operator-manual/`로 물리적 이관(사용자 요청)** | 여러 원자 문서가 이미 "모든 프로젝트 공용"이라고 선언만 해두고 실제로는 한 프로젝트 폴더 안에만 존재해 다른 프로젝트는 그 존재조차 알 수 없던 문제를 해결. 조치: `common/ui/common/design-system/` 선례를 따라 **`common/operator-manual/`** 신설. 완전 공용(00-a4-authoring-guide, 01-structure, 04-a4-print, 05-composition-nav, 07-checklist) 이동, 부분 공용(02-image-capture·03-content-rules·06-integrated-build)은 공통 규칙만 남기고 프로젝트 전용 예시는 제외. 08-change-log 도 공용으로 이관. 프로젝트 전용 잔여(캡처 영역 예시 표·메뉴 특이사항·상태코드 예시 표)는 각 프로젝트 `operator-manual/DEVELOPMENT/` 하위 전용 문서로 존치. 빌드 툴링(`build_integrated.py`·`print.css`)도 `common/operator-manual/build/`로 이관하고 CSS fallback 을 3단(대상 폴더 자신 → 그 프로젝트 공용 → 전체 프로젝트 공용)으로 확장, HTML 타이틀 하드코딩도 프로젝트 중립 문구로 수정. |

## 2. 테스트 결과

| 날짜 | 테스트 내용 | 결과 |
|------|------------|------|
| 2026-07-15 | 통합 빌드 최종 상태 재집계 | ✓ `build/MANIFEST.txt` 34개, `integrated-manual.html` `class="pagebreak"` 34개 |
| 2026-07-15 | 예시급 표준 검증 — 예시 메뉴얼(`01-dashboard`) 재현 가능성 | ✓ 템플릿에 데이터 흐름·DB/쿼리·요소 표 규격 추가로 예시 골격 8절 재현 가능 |
| 2026-07-15 | 표준 적용 시범 — `01-dashboard`(운영 시나리오·탐색 링크 추가), `06-daily-operations`(E2E 시나리오화) | ✓ 섹션 번호 정합·탐색 링크 정상 |
| 2026-07-15 | 분리 후 나침반 경로 검증 | ✓ `00-core.md:39`가 `operator-manual/DEVELOPMENT.md`(나침반) 가리킴 — 경로 유지, 갱신 불필요 |

## 3. 검증 시나리오 (05.post-modification 준수)

- 신규 작성자가 나침반(`DEVELOPMENT.md`) → `01-structure.md` 템플릿을 따르면, 데이터성 메뉴는 접속·화면구성(요소 표)·데이터 흐름·조작·운영 시나리오·모니터링·문제·DB/쿼리의 8절을 갖춰 **예시 메뉴얼급** 산출이 나온다. 요소 이미지·시나리오 누락은 체크리스트([07-checklist.md](07-checklist.md))에서 걸러진다.
