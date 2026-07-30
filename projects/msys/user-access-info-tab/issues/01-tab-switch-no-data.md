# 문제: 다른 탭 갔다 왔을 때 데이터 안 보임

## 증상
- 처음 접속(F5): ✅ 데이터 정상 출력  
- 다른 탭 → 사용자접속정보 탭 클릭: ❌ 빈 화면 (데이터 없음)

## 원인
1. `init()`에서만 데이터 로드 (`await this.refresh()` 호출)
2. 탭 클릭 시 `ui.js`의 핸들러가 주석 처리되어 있어 `refresh()` 미호출

## 해결 방안 (단계별)

### Step 1: ui.js에서 주석 해제
**파일**: `static/js/modules/mngr_sett/ui.js` Line 51-56

```javascript
// 기존 (주석 처리됨)
// if (tab.dataset.tab === 'userAccessInfo' && window.userAccessInfo) {
//     window.userAccessInfo.refresh();
// }

// 수정 후 (주석 해제)
if (tab.dataset.tab === 'userAccessInfo' && window.userAccessInfo) {
    window.userAccessInfo.updateMonthHeaders();
    window.userAccessInfo.updateThresholdInputs();
    window.userAccessInfo.refresh(1, null, null, true); // forceReload=true
}
```

### Step 2: init()에서 refresh() 제거
**파일**: `static/js/tabs/userAccessInfo/index.js` Line 95

```javascript
// 기존
async init() {
    ...
    await this.refresh();  // ← 이 줄 제거
    this.setupEventListeners();
    ...
}

// 수정 후
async init() {
    ...
    // await this.refresh();  // 제거됨 - ui.js에서만 호출
    this.setupEventListeners();
    ...
}
```

### Step 3: forceReload 파라미터 추가
**파일**: `static/js/tabs/userAccessInfo/index.js` Line 203-207

```javascript
// 기존
async refresh(page = 1, pageSize = null, searchTerm = null) {
    ...
    await userListRenderer.render(page, ps, term);
}

// 수정 후
async refresh(page = 1, pageSize = null, searchTerm = null, forceReload = false) {
    ...
    await userListRenderer.render(page, ps, term, 'none', 0, forceReload);
}
```

## 검증 방법
1. F5로 페이지 새로고침
2. 다른 탭(예: 기본 설정) 클릭
3. 다시 "사용자접속정보" 탭 클릭
4. 데이터가 정상적으로 표시되는지 확인

## 관련 커밋
- REQ-2604-024: 363e13e
