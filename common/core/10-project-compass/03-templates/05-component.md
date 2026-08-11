# 템플릿 5: 컴포넌트 폴더 특화 상세 문서

> 상위 나침반 [`../03-templates.md`](../03-templates.md) 에서 분리.

## 템플릿 5: 컴포넌트 폴더 특화 상세 문서

```markdown
# {폴더명}/components 상세 가이드

## 역할

{UI 컴포넌트 설명}

## 컴포넌트 목록

| 컴포넌트 | 파일 | Props 요약 | 사용 위치 |
|---------|------|-----------|---------|
| `Button` | `Button.tsx` | `variant`, `onClick` | 전역 |
| `Modal` | `Modal.tsx` | `isOpen`, `onClose` | 여러 페이지 |

## 스타일 규칙

- CSS 방법론: {Tailwind / CSS Modules / styled-components}
- 디자인 토큰 위치: `{경로}`
- 반응형 breakpoint: `{규칙}`

## 수정 가이드

### 새 컴포넌트 추가 시
- [ ] {네이밍 규칙} 준수
- [ ] Storybook 스토리 추가 (있는 경우)
- [ ] Props 타입 정의
- [ ] 이 목록 업데이트
```
