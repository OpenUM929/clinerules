# 시간대 변환 주의사항

> 시간대 변환 시 발생하는 대표적인 문제와 해결책

## ⚠️ 문제 발생 패턴

### 1. UTC → KST 이중 변환

- **원인**: 이미 KST인 시간에 +9시간을 더함
- **결과**: 18시간 차이 발생
- **방지**: 시간 저장 시 KST임을 명확히 표시, 변환 전 시간대 확인

### 2. ISO 8601 형식 혼용

- **원인**: `toISOString()`은 UTC 기준 (`2026-04-16T06:30:00.000Z`)
- **결과**: 9시간 차이 발생
- **방지**: ISO 8601 형식을 DB에 저장하지 말 것, KST 문자열 사용

### 3. DB 직접 조회 (TO_CHAR 미사용)

- **원인**: TO_CHAR 없이 datetime 조회
- **결과**: JavaScript에서 잘못 파싱 (UTC로 인식)
- **방지**: 항상 TO_CHAR로 문자열 변환 후 전달

## ✅ 검증 방법

### 저장된 시간이 KST인지 확인

```javascript
// DB에서 조회한 시간
const savedTime = "2026-04-16 15:30:00";  // ✅ KST (형식: YYYY-MM-DD HH:mm:ss)
const wrongTime = "2026-04-16T06:30:00.000Z";  // ❌ UTC (ISO 8601 형식)

// 파싱 테스트
console.log(formatDBDateTime(savedTime));  // "26.04.16 15:30" (✅ 정상)
console.log(formatDBDateTime(wrongTime));  // "" 또는 잘못된 값 (❌ 오류)
```

### Python에서 KST 생성 검증

```python
from utils.datetime_utils import get_kst_now

kst_now = get_kst_now()
print(kst_now.strftime('%Y-%m-%d %H:%M:%S'))  # "2026-04-16 15:30:00" 형식
print(kst_now.isoformat())  # ❌ ISO 8601 형식 - 사용 금지
```
