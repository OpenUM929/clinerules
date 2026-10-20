# 05. 지침 수정 후 의무 절차

## 모든 지침 수정 완료 후

1. **시나리오 작성**: 수정된 규칙이 올바르게 동작하는지 검증
2. **00-core.md 경로 검증**: 나침반이 올바른 문서를 가리키는지 확인
3. **테스트 결과 기록**: 해당 문서 하단에 기록

---

## 테스트 결과

| 날짜 | 테스트내용 | 결과 |
|-----|----------|------|
| 2026-04-21 | 08 문서 분리 (160줄 → 5개 파일) | ✓ 통과 |
| 2026-04-21 | 00-core.md 경로 업데이트 | ✓ 통과 |
| 2026-04-21 | 참조 검증 절차 추가 | ✓ 통과 |
| 2026-04-21 | project-compass.md 생성 (10번호) | ✓ 통과 |
| 2026-04-21 | files → references 폴로 이동 | ✓ 통과 |
| 2026-04-21 | 00-core.md project-compass 추가 | ✓ 통과 |
| 2026-04-21 | 10-project-compass 폴로 생성 및 파일 이동 | ✓ 통과 |
| 2026-04-21 | references 폴로 삭제 | ✓ 통과 |
| 2026-04-21 | project_wordcloud 분석 (routes/modules/services GUIDE) | ✓ 통과 |
| 2026-04-21 | project_wordcloud README.md 업데이트 | ✓ 통과 |
| 2026-04-22 | 성능 분석 SKILL 파일 생성 (11-performance-optimization-plan.md) | ✓ 통과 |
| 2026-04-22 | 영향도 분석 SKILL 파일 생성 (12-impact-analysis-report.md) | ✓ 통과 |
| 2026-04-22 | 요구사항 명확화 SKILL 파일 생성 (13-requirements-clarification.md) | ✓ 통과 |
| 2026-04-22 | 00-core.md 분류표/문서 위치표 업데이트 | ✓ 통과 |
| 2026-04-22 | files/ 폴로 삭제 | ✓ 통과 |
| 2026-04-22 | 00-core.md에 폴로 명칭/누락된 규칙 문서 링크 추가 | ✓ 통과 |
| 2026-05-11 | 04.design-change.md: 팝업/모달 텍스트 오버플로우 방지 원칙 추가 | ✓ 통과 |
| 2026-05-11 | 06.git-rules.md: fix를 비기능 작업으로 재분류 (FP → 시간H) | ✓ 통과 |
| 2026-05-14 | 06.git-rules.md: 빌드 자동화 규칙 섹션 추가 (pre-commit hook, msys.zip) | ✓ 통과 |
| 2026-06-04 | CLAUDE.md: 작업 시작 전 필수 체크 3단계 블록 추가 (지침 미확인 방지) | ✓ 통과 |
| 2026-06-19 | Modern Minimal Design System 생성 (8개 파일, ~200라인 이하) | ✓ 통과 |
| 2026-06-19 | 04.design-change.md: 표준 절차 1단계에 design-system/ 참조 추가 | ✓ 통과 |
| 2026-06-19 | layout-and-components.md: 나침반으로 변경 + design-system/ 참조 | ✓ 통과 |
| 2026-06-19 | 00-core.md: 핵심 규칙 문서 위치표에 Design System 항목 추가 | ✓ 통과 |
| 2026-07-02 | 03-plan-mode.md: 항목 14 요구사항 원자화 및 답변 대장 추가(원자 질문 표·재확인·작업 후 실측 답 기입) | ✓ 통과 |
| 2026-08-11 | 30-report-insight-structure.md 신설(INS-1~9) + 16-report-writing §2-12·§4 배선, 00-core 분류표·NUMBERS 등재 | ✓ 통과 (린터 error 0) |
| 2026-08-11 | 최초 배치를 `16-report-writing/01-insight-first.md` 로 했다가 **폴더 생성이 상위 .md 를 나침반으로 만들어 C1(60줄 상한) error** 발생 → 독립 번호 30 으로 이설 | ✓ 통과 (재실행 error 0) |
| 2026-08-11 | `.claude/agents` report-writer(인사이트 게이트·수량 표기·작업 절차) · report-auditor(F-2 구조 감사 10항) 반영 | ✓ 통과 (A1~A7 신규 위반 0) |
| 2026-08-12 | 30-report-insight-structure **INS-11 신설**(결론 문장 형식 `**라벨**: 설명`) + §2-1 예시 교체·형식 대조표 · §7-8 자가검사 추가 | 린터 error 0 / warn 49 (신규 warn 0) |
| 2026-08-12 | 27-document-output-standard **OUT-7 신설**(장 경계 쪽 나눔, 토큰 표기는 양식 정본 §2-2 링크) | 린터 error 0 |
| 2026-08-12 | 16-report-writing §1: 대외 제출 결과보고서·주제별 세트 발행 위치를 `{{paths.report_root}}` 로 변경 + 발행 위치 경계 1줄 (`project.json` 에 `paths.report_root` 추가) | 린터 error 0 (P3·P4 통과) |
| 2026-08-12 | `.claude/agents` report-writer(INS-11 게이트 행·OUT-7·발행 위치) · report-auditor(F-2 1번 형식 검사 강화·12번 쪽 나눔 대사) 반영 | ✓ 통과 (A1~A7 신규 위반 0) |
| 2026-08-20 | 09-data-absence **ABS-9·ABS-10 신설**(재현 불가 확정 수치 = 근거에서 제외 · 표본 재현 ≠ 값 재현) + ABS-1 확인 경로 ⑥ 형상관리 이력 추가 · 체크리스트 2항 추가 · 16 §2-4 배선 | 린터 error 0 / warn 51 (신규 warn 0) |
| 2026-08-20 | **33-report-set-split.md 신설**(INS-9 상세 이설 + **INS-12 고지 도달 검사** 신설) + 30 §1 INS-12 행·§6 스텁화·§7 항목 9 · 16 §1·§2-12 · 00-core 분류표 배선 | 린터 error 0 / warn 51 (신규 warn 0) |
| 2026-08-20 | reviewer 반려 반영 — 30 INS-8·§5 표에 **INS-12 예외 단서**(결격 사유는 수치와 같은 자리) 명기 · 30·09 머리말 `rev-260820-01`(NUM-9 RV-2) · 33 §4 자가검사에 grep 명령 부여 | 린터 error 0 / warn 51 (신규 warn 0) |
| 2026-08-20 | `.claude/agents` 반영(NUM-9 RV-5) — report-writer(INS-1~12·33 §1 임계·§3 도달 검사) · report-auditor(F-2 INS-1~12·10번 33 §1·**10-1 고지 도달** 신설) · metrics-measurer(부재 판정 정본 ABS-1~8 → **ABS-1~10**) | ✓ 통과 (A1~A7 신규 위반 0) |
| 2026-08-21 | AGENTS.md: 작업 시작 전 필수 체크 블록 복구 (00-core 나침반 참조, 2026-06-04 유실 복원) | ✓ 통과 |
| 2026-08-21 | 05.testing.md: UI 시각 검증 의무 섹션 추가 (스크린샷/overflow assertion, 드롭 테이블 사례) | ✓ 통과 |
| 2026-08-21 | 03-workflow/debugging-lessons.md: 원인 가설 검증·CSS Grid overflow 함정 항목 추가 | ✓ 통과 |
| 2026-08-21 | 03-workflow/request-analysis.md: 요청 범위 외 변경 금지·모호한 UI 지칭 확인 규칙 추가 | ✓ 통과 |
| 2026-08-21 | 04-design-change/checklist.md: 시각 검증·들여쓰기 정합성·grid overflow 체크 항목 추가 | ✓ 통과 |
| 2026-08-21 | adventure-editor.tsx: 사이드바 sticky 복원·drop/bestiary `min-w-0` 보강·들여쓰기 정리 + Playwright 레이아웃 회귀 테스트 | ✓ 통과 |
| 2026-08-21 | **34-submission-form-canon.md 신설**(FORM-1~7 — 사용자 확정 제출본 2종에서 서식 요소·절 골격·표 컬럼 추출) + 31 §1 문말·라벨 예외·§3 골격 종속(rev-260821-01) · 16 §1 종류표 2행·규격표 1행(rev-260821-01) · NUMBERS 34 등재 · 00-core 분류표 배선 | 린터 error 1(**개정 전부터 있던** L5 `.clinerules/.claude/` — 본 개정과 무관) / warn 52 (신규 warn 2 = C2 권장 80줄 초과: 34 신설 95줄 · 31 이 78→92줄. 둘 다 160줄 상한 이내) |
| 2026-08-21 | `.claude/agents` 반영(NUM-9 RV-5) — one-paper-writer(§1 기본형 → 34 §2 확정 5절·이미지 0장 기본·문말 명사형) · fp-estimator(0단계 5항 34 §3·7절 골격·표 컬럼에서 중분류 제거·인라인 요약 세 자리 대사) · report-writer(인사이트 게이트 前 31·34 판정·문서별 규약 2행) · report-auditor(**F-3 제출 서식 8항 신설**, F-2 1·2·11 대체 규칙) | ✓ 통과 (A1~A7 신규 위반 0) |
| 2026-08-24 | **35-report-claim-integrity.md 신설**(INS-13~17 + why-first 를 INS-18 로 승격) + 30 §1 6행·§7 항목 10·§8 개정 이력(rev-260824-01) · **31 §1 개조식 적용 대상을 대외 제출 결과보고서로 확장·§1-1 위계 3단 신설·§4 측정 명령 갱신**(rev-260824-01) · 16 §1 종류표·규격표 2행·§2-12·§2-13·§6(rev-260824-01) · `projects/{{project_id}}/patent-disclosure-form.md` §6 을 포인터로 축약(rev-260824-01) · 00-core 분류표·NUMBERS 35 등재 | 린터 error 1(**개정 전부터 있던** L5 `.clinerules/.claude/` — 본 개정과 무관) / warn 53 (신규 warn 1 = 35 신설 127줄 C2 권장 80줄 초과, 160줄 상한 이내) |
| 2026-08-25 | reviewer 반려(FAIL 7건 중 5건) 반영 — 31 §4 주석·개정 이력의 **과장 서술 정정**(`[□○-]` 는 「전건 위반」이 아니라 `□`·`○` 줄만 오집계) · **30 INS-11 을 31 §1 에 위임**해 정본↔위성 모순 제거(§4 검사 2줄 병합으로 자리 확보, 160줄 유지) · 35 §1~§6 리드의 **조항 사본화 제거** · 35 §2 「참값」 행 **COM-1 일반화** · 30·31·35 머리말 `rev-260825-01` | 린터 error 1(개정 전부터 있던 L5 `.clinerules/.claude/`) / warn 53 (신규 warn 0) |
