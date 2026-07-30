# navbar

## 파일
- Template: `templates/navbar.html`

## 도메인
네비게이션 바 - 상단 메뉴, 사용자 정보

## 포함 위치
- `base.html`에서 `{% include "navbar.html" %}`로 포함

## 구조
```
nav (bg-blue-800)
├── 로고: "수집 현황 대시보드"
├── 메뉴 링크 (g.user.permissions 기반)
└── 사용자 메뉴
    ├── 로그인 상태: 사용자 ID, 세션 타이머, 드롭다운
    └── 비로그인: 로그인 버튼
```

## 사용자 메뉴
- 비밀번호 변경 (`/change-password`)
- 로그아웃 (`/logout`)

## 메뉴 동적 생성
- `menu_items`에서 `g.user.permissions` 권한 확인
- `menu_id`가 권한에 있으면 메뉴 표시
- 외부 링크 (`is_external`)인 경우 새 탭

## 세션 타이머
- `session-timer` 요소에 남은 시간 표시
- `session_timer.js`에서 관리

## 스타일
- Tailwind CSS 사용
- Sticky positioning (z-50)
