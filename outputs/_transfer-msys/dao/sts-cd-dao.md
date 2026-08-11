# Sts Cd DAO (sts_cd_dao.py)

## 파일 위치

`dao/sts_cd_dao.py` (161줄)

## 역할

상태 코드 마스터 접근 - CD900 계열 조회

## 주요 함수

| 함수 | 기능 |
|------|------|
| `get_all()` | 전체 상태 코드 조회 |
| `get_by_cd(cd)` | 단일 상태 코드 조회 |
| `insert(data)` | 상태 코드 추가 |
| `update(data)` | 상태 코드 수정 |
| `delete(cd)` | 상태 코드 삭제 |

## 관련 문서

- [dao/README.md](README.md) - DAO 개요
- [services/status-code-service.md](../services/status-code-service.md) - 상태 코드 서비스