# 문제: 탭 전환 시 Nav 메뉴 높이 변경

## 증상
- "데이터 수집 일정" Nav 메뉴 ↔ "관리자 설정" Nav 메뉴 전환 시
- 전체 페이지 높이가 달라짐 (UI 깨짐 현상)

## 원인
- 각 탭의 `.tab-content` 높이가 내용에 따라 다름
- `display: none` ↔ `display: block` 전환 시 브라우저 레이아웃 재계산

## 분석 필요 사항
```css
/* templates/mngr_sett.html Line 148-156 */
#mngr_sett_page .tab-content {
    display: none;
    padding-top: 20px;
}

#mngr_sett_page .tab-content.active {
    display: block;
}
```

## 해결 방안 (후속 분석 필요)

### Option A: 최소 높이 설정
```css
#mngr_sett_page .tab-content {
    display: none;
    padding-top: 20px;
    min-height: 600px; /* 최소 높이 설정 */
}
```

### Option B: 고정 높이 컨테이너
```css
.content-section {
    min-height: 700px; /* 탭 영역 고정 */
}
```

### Option C: flex/grid 레이아웃
- 컨테이너 높이를 flexbox로 고정
- 탭 콘텐츠 영역을 flex-grow로 확장

## 검증 방법
1. 브라우저 개발자 도구(F12) 열기
2. Elements 탭에서 `.tab-content` 높이 확인
3. 탭 전환 시 높이 변화 감지
4. CSS 수정 후 재검증

## 미해결 상태
- 추가 분석 및 테스트 필요
- 관련 CR: 미생성
