# 재사용 체크리스트 (신규 프로젝트 적용 절차)

> 상위 나침반 [`../kanban-board-guide.md`](../kanban-board-guide.md) 에서 분리.

## 6. 재사용 체크리스트 (신규 프로젝트 적용 절차)

신규 Flask 웹시스템에 칸반보드를 도입할 때 다음 순서로 적용한다:

> 파일 경로는 대상 프로젝트의 계층 구조를 따른다. 아래 `<라우트 계층>`·`<템플릿 계층>` 은 `project.json` 의 `paths.app_root` 아래 **실제 폴더를 확인해 대입**한다 — 이 문서의 예시 경로를 그대로 만들지 않는다.

- [ ] 1. 설정 모듈에 `PLANS_DIR` 설정 추가 (칸반 대상 베이스 폴더)
- [ ] 2. `<라우트 계층>/<보드 라우트 모듈>.py` 생성 — **라우트 10종** (§3.3) + 핵심 함수 전사
- [ ] 3. `<템플릿 계층>/<보드 템플릿>.html` 생성 — CSS/HTML/JS 전사 (도메인명 replace)
- [ ] 4. 진입점(`{{entrypoint}}`)에 `plans_bp` 블루프린트 등록
- [ ] 5. 공통 레이아웃 템플릿에 네비 링크 추가 (관리자 전용)
- [ ] 6. `BASE_DIR/MM/_index.md` 초기 데이터 작성 (1개월부터 시작, 5·6·7컬럼 선택 사용)
- [ ] 7. 관리자 로그인 체계 확인 (`admin_required` 연동)
- [ ] 8. 브라우저 `/admin/plans` 접속 → 6컬럼 정상 표시 확인
- [ ] 9. CR 현황 탭 사용 시: `cr_dir` 을 `project.json` 의 `{{paths.cr_root}}` 로 설정 + `REQ-*.md` 문서 포맷 준수
- [ ] 10. `_index.md` 상태값 변경 → 10초 내 칸반보드 자동 갱신 확인
- [ ] 11. **4탭** 확인: 칸반(`kanban`) / CR(`git`) / 간트(`gantt`) / 추세(`trend`) 전환 정상
- [ ] 12. 간트: `epic`/`end_date`/`depends`/`related_cr` 컬럼 채워 스윔레인·간선·마일스톤 표시
- [ ] 13. 추세: `trend` / `trend-type`(monthly·yearly) 차트 정상 렌더
- [ ] 14. 링크 린터(`/api/plans/lint`) UI wiring 시 `violations`·`pass` 표시 (선택)
- [ ] 15. **`kanban-board-api-contract.md` 를 API 단일 소스로 준수** (스키마 변경 시 계약서 동기화)
