# Navigation — Modern Minimal 스타일

> 좌측 네비게이션(`nav.css`)의 스타일 정의.
> 모든 페이지는 `base.html`을 통해 동일한 네비게이션을 공유한다.

## 기본 구조

```css
nav {
    width: 170px; min-height: 100vh; height: 100vh;
    position: sticky; top: 0;
    background: var(--bg-nav);           /* linear-gradient(180deg, #fff→#f8fbff) */
    border-right: 2px solid var(--border-color-light);
    padding: 12px 8px;
    display: flex; flex-direction: column; gap: 4px;
    flex-shrink: 0; overflow-y: auto;
}
```

## 메뉴 링크

| 상태 | 배경 | 텍스트 | 테두리 | 그림자 |
|------|------|--------|--------|--------|
| 기본 | #ffffff | #4b5563 (weight: 500) | #e5e7eb | 없음 |
| 호버 | #6366f1 | #ffffff | #6366f1 | 0 4px 12px rgba(99,102,241,0.25) |

```css
nav a { display: block; padding: 8px 10px; text-decoration: none;
        color: #4b5563; background: var(--bg-surface);
        border: 1px solid var(--border-color-light); border-radius: var(--radius-md);
        font-weight: var(--font-weight-medium); font-size: var(--font-size-sm); }
nav a:hover { background: var(--color-primary); color: var(--text-inverse);
              box-shadow: var(--shadow-primary-hover); border-color: var(--color-primary); }
```

## 섹션 구분자

```css
nav .sep { color: #bbb; font-weight: var(--font-weight-semibold);
           font-size: 10px; text-transform: uppercase; letter-spacing: 0.5px;
           padding: 8px 4px 4px; user-select: none; display: block; }
```

## 드롭다운

```css
nav .dropbtn { display: block; width: 100%; padding: 8px 10px;
               background: var(--bg-surface);
               border: 1px solid var(--border-color-light); border-radius: var(--radius-md);
               cursor: pointer; text-align: left;
               font-weight: var(--font-weight-medium); font-size: var(--font-size-sm); }
nav .dropbtn::after { content: ' ▼'; font-size: 10px; color: #999; float: right; }
nav .dropdown:hover .dropbtn { background: var(--color-primary); color: var(--text-inverse);
                                border-color: var(--color-primary);
                                box-shadow: var(--shadow-primary-hover); }
nav .dropdown-content a { border: none; background: transparent; padding: 6px 10px;
                          font-size: var(--font-size-xs); font-weight: var(--font-weight-medium); }
nav .dropdown-content a:hover { background: #f3f4f6; color: var(--color-primary); }
```

## 변경 전후 비교

| 요소 | 현재 (기존 nav.css) | Modern Minimal |
|------|-------------------|----------------|
| 배경 | #f8f9fa | linear-gradient(180deg, #ffffff → #f8fbff) |
| 링크 텍스트 | #495057 | #4b5563 |
| 폰트 웨이트 | normal | 500 (medium) |
| 호버 배경 | #6366f1 | #6366f1 (유지, 그림자 개선) |
| 호버 그림자 | 2px 0 8px rgba(0,0,0,0.15) | 0 4px 12px rgba(99,102,241,0.25) |
| 호버 테두리 | 유지 | #6366f1로 변경 |
| 섹션 구분자 | #999, bold | #bbb, 600, uppercase, letter-spacing |
| 드롭다운 호버 배경 | #e9ecef | #f3f4f6 |
