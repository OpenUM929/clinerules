# API 변경 시 체크리스트 (재발 방지 지침)

## 문제 발생 이력

### 1. 기능 라이브러리 로드 실패 (2026-04-02)
**증상**: `기능 라이브러리를 불러오는데 실패했습니다.` 에러 반복 발생

**원인**:
1. **모델 정의 확인 없이 필드 참조**: `FeatureCategory` 모델에 없는 `description` 필드 참조
   - `AttributeError: 'FeatureCategory' object has no attribute 'description'`
2. **API 엔드포인트 불일치**: 프론트엔드 `/api/templates/custom_template/full` vs 백엔드 `/api/feature-library`
3. **SyntaxError**: replace_in_file 사용 시 중괄호 불일치

**해결**:
1. `models.py`를 먼저 읽고 실제 필드만 사용
2. 프론트엔드 API 호출 URL을 백엔드 라우트에 맞춤
3. 전체 파일 다시 작성하여 문법 오류 수정

## 필수 체크리스트 (MANDATORY)

### 백엔드 API 추가/수정 시
- [ ] **1. models.py 먼저 읽기**: 참조하는 모델의 실제 필드 확인
- [ ] **2. 기존 API 라우트 확인**: 중복 또는 충돌하는 라우트가 없는지 확인
- [ ] **3. Blueprint 등록 확인**: `app.py`에 새 blueprint가 등록되었는지 확인
- [ ] **4. 서버 재시작/F5 판단**: 코드 유형별 재시작·F5 여부는 [../../common/development/server-reload-guide.md](server-reload-guide.md) 참조 (`.py`/설정/블루프린트는 재시작, 템플릿/정적은 F5)
- [ ] **5. API 테스트**: curl 또는 브라우저로 직접 호출하여 응답 확인

### 프론트엔드 API 호출 수정 시
- [ ] **1. 백엔드 라우트와 URL 일치 확인**: `/api/xxx` 경로가 백엔드와 일치하는지 확인
- [ ] **2. HTTP 메서드 확인**: GET/POST/PUT/DELETE가 백엔드와 일치하는지 확인
- [ ] **3. 요청/응답 데이터 형식 확인**: JSON 키 이름이 일치하는지 확인
- [ ] **4. 에러 처리 개선**: HTTP 상태 코드와 에러 메시지를 구체적으로 표시

### 코드 수정 시 일반 규칙
- [ ] **1. 관련 파일 전체 읽기**: 수정 전 관련 파일을 먼저 읽어서 전체 구조 파악
- [ ] **2. 작은 단위로 수정**: 한 번에 하나의 변경만 수행
- [ ] **3. 즉시 테스트**: 수정 후 즉시 테스트하여 오류 발견
- [ ] **4. SyntaxError 방지**: replace_in_file 사용 시 SEARCH/REPLACE 블록 정확히 작성

## 디버깅 가이드

### API 호출 실패 시
```bash
# 1. Flask 서버 로그 확인
cd backend; python app.py

# 2. API 직접 호출 테스트
curl http://127.0.0.1:5000/api/feature-library

# 3. 브라우저 개발자 도구 Network 탭 확인
# - 요청 URL 확인
# - 응답 상태 코드 확인
# - 응답 본문 확인
```

### 모델 필드 오류 시
```python
# models.py에서 실제 필드 확인
class FeatureCategory(db.Model):
    __tablename__ = 'feature_categories'
    
    category_cd = db.Column(db.String(100), primary_key=True)
    category_nm = db.Column(db.String(200), nullable=False)
    display_order = db.Column(db.Integer, default=0)
    # description 필드가 없음!
```

### SyntaxError 발생 시
- replace_in_file이 실패하면 write_to_file로 전체 파일 다시 작성
- Python 문법 검사: `python -m py_compile backend/routes/features.py`