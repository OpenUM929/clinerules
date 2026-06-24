# Modern Minimal Design System — 개요

> 이 디자인 시스템은 감정 분석 시스템의 UI 기본기를 정의한다.
> 모든 페이지는 이 시스템을 기준으로 일관된 스타일을 적용한다.

## 스타일

**Modern Minimal** — 보라색(#6366f1) 주 색상, 밝은 그라디언트 배경, 깔끔한 현대적 UI

## 목업 파일

모든 목업은 `web/templates/mockup/` 폴더에 있으며, 브라우저로 열어 확인한다:

| 파일 | 내용 |
|------|------|
| `design_system.html` | 디자인 시스템 전체 컴포넌트 종합 |
| `mockup_metadata_batch.html` | 메타데이터 배치 처리 4단계 위자드 |

## 디자인 토큰 참조 (CSS Custom Properties)

모든 디자인 값은 CSS custom properties로 정의되며,
`static/css/base.css`에 중앙 관리된다.

## 파일 구조

| 파일 | 내용 | 라인 |
|------|------|------|
| `01-design-tokens.md` | 색상, 타이포그래피, 간격, 테두리, 그림자 | < 200 |
| `02-components-button.md` | 버튼 변형/크기/상태 | < 200 |
| `03-components-card.md` | 카드, 옵션카드, 정보섹션, 결과아이템 | < 200 |
| `04-components-form.md` | 입력필드, 체크박스, 태그, 색상선택 | < 200 |
| `05-components-feedback.md` | 배지, 상태메시지, 진행바, 단계표시 | < 200 |
| `06-navigation.md` | 네비게이션 스타일 | < 200 |
| `07-tables-layout.md` | 테이블, 레이아웃 유틸리티 | < 200 |

## 적용 원칙

1. 모든 페이지는 `base.html`을 상속하고 `base.css`를 로드한다
2. 페이지 고유 스타일만 각 템플릿의 `<style>`에 추가한다
3. 중복되는 컴포넌트 스타일은 `base.css`에만 정의한다
4. 인라인 스타일(`style="..."`) 사용을 지양하고 클래스를 사용한다
