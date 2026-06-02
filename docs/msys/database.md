# 데이터베이스

> 프로젝트의 테이블 및 필드 명명 규칙

---

## 테이블 목록 (DDL/)

| 테이블 | 설명 |
|--------|------|
| `tb_user` | 사용자 정보 |
| `tb_user_auth_ctrl` | 권한 관리 |
| `tb_con_mst` | 수집 마스터 |
| `tb_con_hist` | 수집 이력 |
| `tb_col_mapp` | 컬럼 매핑 |
| `tb_grp_memo` | 그룹 메모 |
| `tb_menu` | 메뉴 |
| `tb_data_spec` | 데이터 명세 |
| `tb_mngr_sett` | 관리자 설정 |
| `tb_api_key_mngr` | API 키 관리 |

---

## 테이블 명명 규칙

| 규칙 | 예시 |
|------|------|
| 대문자 + 접두사 | `TB_USER`, `TB_CON_MST`, `TB_COL_MAPP` |
| 의미: `TB_{기능}` | `TB_USER` (사용자), `TB_CON_MST` (수집 마스터) |

---

## 컬럼 명명 규칙

| 규칙 | 예시 |
|------|------|
| 소문자 + snake_case | `user_id`, `user_pwd`, `acc_cre_dt` |
| 약어 사용 | `dt` (date), `cd` (code), `sts` (status) |

---

## 자주 사용하는 약어

| 약어 | 원어 |
|------|------|
| `dt` | date, datetime |
| `cd` | code |
| `sts` | status |
| `mngr` | manager |
| `mst` | master |
| `hist` | history |
| `schd` | schedule |
| `clt` | collection |
| `apr` | approve |
| `acc` | account |

---

## 관련 문서

- [overview.md](overview.md) - 프로젝트 개요
- [file-structure.md](file-structure.md) - 파일 구조
- [data-handling-rules.md](data-handling-rules.md) - 시간 처리 규칙
- [field-naming-convention.md](field-naming-convention.md) - 필드 명명 규칙