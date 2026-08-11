# 문제: 처음 접속 시 애니메이션 2번 실행

## 증상
- F5로 페이지 새로고침 후 사용자접속정보 탭 클릭
- 애니메이션이 2번 연속으로 실행됨 (히트맵 막대가 2번 그려짐)

## 원인
1. `mngr_sett.js`에서 `userAccessInfo.init()` 호출
2. `init()` 낶부에서 `await this.refresh()` 호출 (1차)
3. 탭 클릭 시 `ui.js`의 핸들러에서 `refresh()` 호출 (2차)
4. `userList.js`의 `_doRenderTable()`에서 `updateMonthHeaders()` 중복 호출

## 해결 방안 (단계별)

### Step 1: init()에서 refresh() 제거
**파일**: `static/js/tabs/userAccessInfo/index.js` Line 95

```javascript
// 기존
async init() {
    ...
    await this.refresh();  // ← 제거
    this.setupEventListeners();
    ...
}

// 수정 후
async init() {
    ...
    // await this.refresh();  // 제거됨
    this.setupEventListeners();
    ...
}
```

### Step 2: _doRenderTable()에서 updateMonthHeaders() 제거
**파일**: `static/js/tabs/userAccessInfo/userList.js` Line 279-284

```javascript
// 기존
_doRenderTable(users) {
    const tbody = document.getElementById('userAccessTableBody');
    if (!tbody) return;

    // 테이블 렌더링 전에 헤더 동기화
    if (window.userAccessInfo) {
        window.userAccessInfo.updateMonthHeaders();  // ← 제거
    }
    ...
}

// 수정 후
_doRenderTable(users) {
    const tbody = document.getElementById('userAccessTableBody');
    if (!tbody) return;

    // updateMonthHeaders() 제거 - ui.js에서만 호출
    ...
}
```

### Step 3: ui.js에서만 refresh() 호출
**파일**: `static/js/modules/mngr_sett/ui.js` Line 51-56

```javascript
// 수정 후
if (tab.dataset.tab === 'userAccessInfo' && window.userAccessInfo) {
    window.userAccessInfo.updateMonthHeaders();
    window.userAccessInfo.updateThresholdInputs();
    window.userAccessInfo.refresh(1, null, null, true);
}
```

## 검증 방법
1. F5로 페이지 새로고침
2. 사용자접속정보 탭 클릭
3. 애니메이션이 1번만 실행되는지 확인

## 관련 커밋
- REQ-2604-024: 363e13e
