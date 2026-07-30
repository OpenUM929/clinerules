# 보안 / 리스크

> 상위 나침반 [`../kanban-board-guide.md`](../kanban-board-guide.md) 에서 분리.

## 5. 보안 / 리스크

| 항목 | 대책 |
|------|------|
| 인증 | `admin_required` 데코레이터 — 모든 라우트에 적용 |
| 경로 탐색 | `dir` 파라미터는 `os.path.abspath` → `os.path.isdir` 2중 검증 |
| 인코딩 | `utf-8-sig`로 읽어 CP949/UTF-8 BOM 혼재 대응, 파싱 실패 시 graceful 생략 |
| 데이터 일관성 | 파일시스템 기반 stateless — WAS 다중 인스턴스 문제 없음 |
| 성능 | 항목 수가 200+ 건이면 `parse_all_months` 매 요청 부하 가능 → mtime 체크 후 필요한 경우만 전체 파싱 (check/list 분리) |

---
