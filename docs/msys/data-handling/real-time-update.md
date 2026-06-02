# 실시간 데이터 업데이트 규칙

> 실시간 현황 등 주기적 업데이트가 필요한 데이터 처리

## 시간 동기화

- **서버 시간 기준**: 모든 시간 비교는 서버가 제공한 시간 기준으로 수행
- **클라이언트 시간 사용 금지**: `new Date()`로 시간 생성하지 말 것

## 주기적 갱신

- **setInterval 사용 시**: 시간 비교는 서버 응답 시간 기준
- **마지막 업데이트 시간**: 서버 응답의 `server_time` 또는 데이터의 `updated_at` 사용

## 캐시 시간

- **타임스탬프**: 클라이언트 캐시의 타임스탬프는 서버 응답의 시간 사용
- **동기화**: 주기적 갱신 시 서버 시간을 함께 받아 클라이언트 시간과 동기화

## ✅ 올바른 예시

```javascript
// 실시간 데이터 업데이트
async function updateRealtimeData() {
    const response = await fetch('/api/realtime-data');
    const data = await response.json();
    
    // ✅ 서버가 준 시간 사용
    const serverTime = data.server_time;  // "2026-04-16 15:30:00"
    updateDashboard(data, serverTime);
    
    // 마지막 업데이트 시간 기록 (서버 시간 기준)
    lastUpdateTime = serverTime;
}

// 주기적 갱신
setInterval(updateRealtimeData, 30000);  // 30초마다
```

## ❌ 금지 예시

```javascript
// ❌ 금지: 클라이언트 시간 사용
function updateRealtimeData() {
    const currentTime = new Date();  // 클라이언트 시간 - 금지!
    updateDashboard(data, currentTime);
}

// ❌ 금지: 클라이언트 시간으로 마지막 업데이트 기록
setInterval(() => {
    lastUpdateTime = new Date().toISOString();  // UTC로 저장됨 - 문제 발생!
}, 30000);
```
