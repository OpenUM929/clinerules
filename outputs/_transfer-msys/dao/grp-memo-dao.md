# Grp Memo DAO (grp_memo_dao.py)

## 파일 위치

`dao/grp_memo_dao.py` (132줄)

## 역할

그룹 메모 (메모장) 접근 - TB_GRP_MEMO 조회/저장

## 주요 함수

| 함수 | 기능 |
|------|------|
| `get_memo(grp_id, depth, memo_date)` | 메모 조회 |
| `insert_memo(grp_id, depth, memo_date, content, writer_id)` | 메모 추가 |
| `update_memo(grp_id, depth, memo_date, content, writer_id)` | 메모 수정 |
| `delete_memo(grp_id, depth, memo_date)` | 메모 삭제 |

## 테이블 구조

| 필드 | 설명 |
|------|------|
| grp_id | 그룹 ID (CD100, CD101 등) |
| depth | 그룹 깊이 (1=상위그룹, 2=하위그룹, 3=개별job) |
| memo_date | 메모 대상 날짜 |
| content | 메모 내용 (최대 2000자) |
| writer_id | 작성자 ID |

## 관련 문서

- [dao/README.md](README.md) - DAO 개요
- [routes/collection-schedule-routes.md](../routes/collection-schedule-routes.md) - 수집 일정 라우트