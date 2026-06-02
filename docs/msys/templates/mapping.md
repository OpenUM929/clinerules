# mapping

## 파일
- Template: `D:\dev\msys\templates\mapping_management.html`
- Route: `D:\dev\msys\routes\mapping_routes.py`

## 도메인
데이터베이스 테이블 컬럼 매핑 관리 - 레거시 ↔ 신규 컬럼명 변환

## 확장
- `base.html`

## 엔드포인트
| 용도 | URL | 메서드 |
|------|-----|--------|
| 매핑 관리 | GET /mapping/ | 페이지 렌더링 |
| 매핑되지 않은 컬럼 | GET /mapping/api/unmapped | JSON |
| 매핑 목록 | GET /mapping/api/all | JSON |
| 매핑 저장 | POST /mapping/api/add | JSON |
| 매핑 삭제 | DELETE /mapping/api/delete/{id} | JSON |

## UI 구성
### 매핑되지 않은 신규 컬럼
- 테이블명, 컬럼명
- 새로고침 버튼

### 매핑 관리 테이블
| 컬럼 | 설명 |
|------|------|
| ID | 매핑 ID |
| 이전 테이블명 | bf_tbl_nm |
| 이전 컬럼명 | bf_col_nm |
| 새 테이블명 | new_tbl_nm |
| 새 컬럼명 | new_col_nm |
| 설명 | 설명 |
| 수정일 | update_dt |

## Modal
- 매핑 추가/수정 Modal
- 필드: 이전 테이블명, 이전 컬럼명, 새 테이블명, 새 컬럼명, 설명

## JS 파일
- `/static/js/pages/mapping.js`

## 연관 문서
- Service: [../services/mapping-service.md](../services/mapping-service.md)
- DAO: [../dao/mapping-dao.md](../dao/mapping-dao.md)
- Route: [../routes/mapping-routes.md](../routes/mapping-routes.md)
