# 공통 UI 레이아웃 및 컴포넌트 (Common Layout & Components)

> **이 파일은 나침반이다. 구체적 내용은 아래 하위 문서에 있다.**

## 디자인 시스템

Modern Minimal 스타일의 전체 UI 기본기는 아래 문서들을 참조한다.

| 문서 | 내용 |
|------|------|
| [design-system/00-overview.md](design-system/00-overview.md) | 디자인 시스템 개요 + mockup 파일 경로 |
| [design-system/01-design-tokens.md](design-system/01-design-tokens.md) | 색상, 타이포그래피, 간격, 테두리, 그림자 |
| [design-system/02-components-button.md](design-system/02-components-button.md) | 버튼 시스템 |
| [design-system/03-components-card.md](design-system/03-components-card.md) | 카드 시스템 |
| [design-system/04-components-form.md](design-system/04-components-form.md) | 폼 요소 |
| [design-system/05-components-feedback.md](design-system/05-components-feedback.md) | 배지, 상태 메시지, 진행 표시 |
| [design-system/06-navigation.md](design-system/06-navigation.md) | 네비게이션 |
| [design-system/07-tables-layout.md](design-system/07-tables-layout.md) | 테이블, 레이아웃 유틸리티 |

## 기본 레이아웃
- `templates/base.html` 상속 구조
- 공통 CSS: `static/css/base.css` (디자인 토큰 + 컴포넌트)
- 네비게이션 CSS: `static/css/nav.css`

## 목업 파일
| 파일 | 내용 |
|------|------|
| `mockup/design_system.html` | 디자인 시스템 전체 컴포넌트 종합 목업 |
| `mockup/mockup_metadata_batch.html` | 메타데이터 배치 처리 4단계 위자드 목업 |
| `mockup/design_mockups.html` | 기존 디자인 목업 |
| `mockup/nav_mockup.html` | 네비게이션 비교 목업 |
| `mockup/pages_mockup.html` | 페이지별 목업 |

## UI 작업 시 체크리스트
- [ ] 디자인 시스템 문서 참조: `design-system/00-overview.md`
- [ ] base.html의 디자인 토큰과 일관성 확인
- [ ] mockup(`mockup/design_system.html`) 참조
- [ ] 인라인 스타일 대신 시스템 클래스 사용