# 사용자접속정보 탭 - 문제 해결 나침반

## 탭 개요
사용자 접속 현황을 히트맵/선차트로 시각화하는 탭

## 주요 파일
- `static/js/tabs/userAccessInfo/index.js`      # 메인 모듈
- `static/js/tabs/userAccessInfo/userList.js`   # 사용자 목록 렌더링
- `static/js/modules/mngr_sett/ui.js`           # 탭 클릭 핸들러
- `templates/mngr_sett.html`                    # 탭 HTML

---

## 문제 목록

| # | 문제 | 증상 | 파일 |
|---|------|------|------|
| 1 | [탭 이동 후 데이터 안 보임](./issues/01-tab-switch-no-data.md) | 다른 탭→재접속 시 빈 화면 | ui.js, index.js |
| 2 | [처음 접속 시 애니메이션 2번](./issues/02-animation-double-call.md) | F5 후 애니메이션 중복 실행 | index.js, userList.js |
| 3 | [Nav 메뉴 높이 변경](./issues/03-nav-height-diff.md) | 탭 전환 시 전체 높이 변동 | CSS/html 구조 |

---

## 패턴/원칙

### 데이터 로드 패턴
```
init() → 설정만 초기화 (refresh() 호출 금지)
      ↓
탭 클릭 → ui.js → refresh(forceReload=true) → 데이터 로드
```

### 중복 호출 방지
- `forceReload` 파라미터로 캐시 우회
- `isInitialized`로 init() 중복 실행 방지

---

## 관련 CR
- REQ-2604-024: 탭 전환 시 데이터 refresh 및 애니메이션 중복 수정
