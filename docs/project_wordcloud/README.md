# Wordcloud Project Rules

> 이 프로젝트의 핵심 나침반. 공통 규칙은 `.clinerules/core/`를 따른다.

---

## 🔴 PseudonymManager (가명 관리) — 절대 실수 금지 규칙

### 1. 생성 시 인자 필수 (필수)

`PseudonymManager`는 **무조건 2개의 인자**와 함께 생성한다.

```python
# ✅ 올바른 생성
from src.config.settings import PSEUDONYM_MAPPINGS_PATH, ADMIN_PASSWORD
from src.modules.pseudonym_manager import PseudonymManager

mgr = PseudonymManager(PSEUDONYM_MAPPINGS_PATH, ADMIN_PASSWORD)

# ❌ 절대 금지 — 인자 누락
mgr = PseudonymManager()  # TypeError → Internal Server Error
```

**위반 시 즉시 `TypeError` 발생 → 서버 500 에러 → 욕설 리스트/가명화 기능 전체 마비.**

### 2. 조회 시 원본 복원 (필수)

DB에서 `employees` 테이블을 조회할 때, `name`, `department` 컬럼은 **가명(pseudonym)으로 저장**되어 있을 수 있다.  
**UI 출력, CSV 다운로드, API 응답 전에 반드시 원본 복원.**

```python
# ✅ 올바른 복원
raw_name = row['name'] or ''
real_name = pseudo_mgr.get_real_id(raw_name) if raw_name else ''
display_name = real_name if real_name and real_name != raw_name else raw_name

raw_dept = row['department'] or ''
real_dept = pseudo_mgr.get_real_id(raw_dept) if raw_dept else ''
display_dept = real_dept if real_dept and real_dept != raw_dept else raw_dept
```

**위반 시 사용자가 "가명으로 출력된다"고 분노함.**

### 3. 복원 누락 방지 체크리스트

`profanity_db_service.py`, `perspective_service.py`, `batch_processor.py` 등에서 `PseudonymManager`를 사용할 때마다 아래를 확인:

- [ ] `PseudonymManager(PSEUDONYM_MAPPINGS_PATH, ADMIN_PASSWORD)` 형태로 생성했는가?
- [ ] `employees.name`, `employees.department`를 조회한 후 `get_real_id()`를 호출했는가?
- [ ] 복원된 `display_name`, `display_dept`를 UI/CSV/API 응답에 사용했는가?
- [ ] `get_pseudonym()`으로 생성된 데이터는 복원이 불필요하나, **조회 시는 반드시 복원**해야 하는가?

---

## 프로젝트 구조

- 백엔드: Python + Flask
- 핵심 모델: KoTE (Korean Text Emotion)
- 위치: `wordcloud_project/`

---

## 관련 문서

- [modules/profanity-filter.md](modules/profanity-filter.md) - 비속어 필터
- [services/batch-processor.md](services/batch-processor.md) - 배치 처리
- [services/analysis-service.md](services/analysis-service.md) - 분석 서비스
