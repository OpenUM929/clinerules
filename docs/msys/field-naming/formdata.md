# FormData 처리 규칙

## Backend (Flask) - 올바른 예

```python
@app.route('/api/popups', methods=['POST'])
def create_popup():
    data = {
        'TITL': request.form.get('titl'),        # ✓ DB 컬럼명 (대문자)
        'CONT': request.form.get('cont'),        # ✓ DB 컬럼명 (대문자)
        'START_DT': request.form.get('start_dt'), # ✓ DB 컬럼명 (대문자)
        # ...
    }
```

## Frontend (JS) - 올바른 예

```javascript
const formData = new FormData();
formData.append('titl', document.getElementById('popupTitle').value);        // ✓ 소문자
formData.append('cont', document.getElementById('popupContent').value);      // ✓ 소문자
formData.append('start_dt', startDate + ' 00:00:00');                        // ✓ 소문자
```

## 위반 시 조치

필드명 불일치로 인한 400/500 오류 발생 시:
1. **원인**: 계층 간 필드명 불일치
2. **해결**: DB 컬럼명 기준으로 모든 계층 통일
3. **예방**: 개발 전 해당 테이블 DDL 확인 필수
