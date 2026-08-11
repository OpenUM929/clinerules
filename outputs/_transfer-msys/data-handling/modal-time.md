# 모달/팝업 시간 표시 규칙

> 메모 팝업, 공지사항 팝업 등에서의 시간 표시 규칙

## 시간 표시 기준

- **생성 시간 표시**: 항상 `formatDBDateTime()` 사용
- **수정 시간 표시**: `formatDBDateTime()` 사용
- **시간 정보 요소 ID 규칙**: `{feature}-date-info`, `{feature}-created-at`

## 신규/수정 구분 표시

- **신규 생성 시**: 시간 정보 영역 숨김 (`display: none`)
- **수정/조회 시**: 시간 정보 표시 (`display: block`)
- **작성자 정보**: `writer_id` 필드와 함께 표시

## ✅ 올바른 예시

```javascript
import { formatDBDateTime } from '../modules/common/dateUtils.js';

// 메모 팝업 시간 표시
function showMemoPopup(loadedMemo) {
    const createdAt = loadedMemo.created_at;  // "2026-04-16 15:30:00"
    const writerId = loadedMemo.writer_id;
    
    // 시간 표시
    const dateInfoEl = document.getElementById('memo-date-info');
    const writerEl = document.getElementById('memo-writer');
    
    if (loadedMemo) {
        // 수정/조회 모드: 시간 표시
        dateInfoEl.textContent = formatDBDateTime(createdAt);  // "26.04.16 15:30"
        writerEl.textContent = writerId;
        dateInfoEl.style.display = 'block';
        writerEl.style.display = 'block';
    } else {
        // 신규 생성 모드: 시간 숨김
        dateInfoEl.style.display = 'none';
        writerEl.style.display = 'none';
    }
}
```

## ❌ 금지 예시

```javascript
// ❌ 금지: 직접 Date 파싱
const date = new Date(loadedMemo.created_at);  // 잘못된 파싱 가능성
const formatted = date.toLocaleString();  // 환경에 따라 형식 불일치

// ❌ 금지: 시간대 변환 없이 직접 표시
document.getElementById('memo-date-info').textContent = loadedMemo.created_at;
// 결과: "2026-04-16 15:30:00" (긴 형식, YY.MM.DD HH:mm 형식이 아님)
```
