# jandi_routes

**문서 위치**: `.clinerules/docs/msys/routes/jandi-routes.md`

## 파일
- `D:\dev\msys\routes\jandi_routes.py` (92줄)

## 역할
잔디 모니터링 - Job ID 목록, 마스터 상세정보, 히트맵 데이터

## Blueprint
```python
bp = Blueprint('jandi', __name__, url_prefix='/')
```

## 엔드포인트

| 경로 | 메서드 | 함수 | 설명 |
|------|--------|------|------|
| `/jandi` | GET | `jandi_page()` | 잔디 페이지 |
| `/api/job-list` | GET | `get_job_list()` | Job ID 목록 (DataTables) |
| `/api/job_mst_info` | GET | `get_job_mst_info()` | 마스터 상세정보 |
| `/api/jandi-data` | GET | `get_jandi_data()` | 잔디 히트맵 데이터 |
| `/api/jandi/raw_data` | GET | `get_jandi_data()` | 원시 데이터 |

## 파라미터
| 파라미터 | 타입 | 설명 |
|----------|------|------|
| start | int | DataTables 시작 위치 |
| length | int | DataTables 페이지 크기 |
| search[value] | string | 검색어 |
| start_date | string | 시작 날짜 |
| end_date | string | 종료 날짜 |
| allData | boolean | 전체 데이터 조회 |
| job_id | string | Job ID |

## 의존성
- Service: `service/mst_service.py`, `service/jandi_service.py`

## 연관 문서
- [../services/jandi-service.md](../services/jandi-service.md)
- [../templates/jandi.md](../templates/jandi.md)
