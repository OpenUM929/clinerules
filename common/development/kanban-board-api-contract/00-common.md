# 공통 규칙

> 상위 나침반 [`../kanban-board-api-contract.md`](../kanban-board-api-contract.md) 에서 분리.

# 계획 현황 보드 — API 계약서 (프레임워크 중립)

> 본 문서는 관리자용 **계획 현황 보드**(칸반 / CR / 간트 / 추세) 백엔드 API의
> 요청·응답 JSON 스키마를 프레임워크 중립적으로 정의한다.
> 기준 구현: `{{paths.app_root}}` 의 계획 보드 라우트 모듈 (Blueprint `plans_bp`, `url_prefix='/admin'`). 파일 위치는 프로젝트 계층에 따른다.
> 도메인(업무명·데이터명)은 일절 포함하지 않으며, 신규 프로젝트는 경로·함수명만 adapt하여 동일 제품을 재구성할 수 있다.
> 표준 지침: `kanban-board-guide.md` §3 이 문서를 참조하도록 개편됨.

---

## 0. 공통 규칙

- **모든 API는 `admin_required` 데코레이터로 보호** — 미인증 시
  `{ "success": false, "error": "관리자 로그인이 필요합니다." }` + HTTP 401.
- **공통 에러 포맷**:
  ```json
  { "success": false, "error": "<한글 메시지>", "status": 401 | 404 | 500 }
  ```
- **시간**: `_index.md` `os.path.getmtime` (epoch float, 폴링용 `modified_at`).
- **연도 기준**: `PLANS_DIR` 마지막 세그먼트(예: `2026`) — `_plans_year()`.
- **월 파라미터**: `MM` 2자리 또는 빈값(`ALL`=전체 병합). `?month=07` / 생략.

---
