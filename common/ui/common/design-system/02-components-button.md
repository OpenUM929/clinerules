# Components: Button System

## 기본 구조

```css
.btn {
    display: inline-flex; align-items: center; justify-content: center;
    gap: var(--space-2);
    padding: 10px 20px; border: 1px solid transparent;
    border-radius: var(--radius-md);
    font-size: var(--font-size-body); font-weight: var(--font-weight-semibold);
    cursor: pointer; font-family: var(--font-family);
}
```

## 색상 변형 (Variants)

| 클래스 | 배경 | 텍스트 | 테두리 | 호버 |
|--------|------|--------|--------|------|
| `.btn-primary` | #6366f1 | white | 없음 | #4f46e5 + shadow-primary-hover |
| `.btn-secondary` | #f3f4f6 | #374151 | #d1d5db | #e5e7eb |
| `.btn-success` | #28a745 | white | 없음 | #218838 + 그림자 |
| `.btn-danger` | #dc3545 | white | 없음 | #c82333 |
| `.btn-ghost` | transparent | #495057 | 없음 | #f3f4f6 |
| `.btn-outline-primary` | transparent | #6366f1 | #6366f1 | #6366f1 + white text |
| `.btn-outline-danger` | transparent | #dc3545 | #dc3545 | #dc3545 + white text |

## 크기 변형 (Sizes)

| 클래스 | padding | 글자크기 |
|--------|---------|---------|
| `.btn-sm` | 6px 12px | 12px |
| `.btn` (기본) | 10px 20px | 14px |
| `.btn-lg` | 12px 24px | 16px |
| `.btn-block` | — | width: 100% |

## 상태 (States)

| 상태 | 적용 방식 |
|------|-----------|
| 기본 | 각 variant 기본 스타일 |
| Hover | `:hover` — 배경 어둡게 + translateY(-1px) + 그림자 |
| Active | `:active` — translateY(0) |
| Disabled | `:disabled` — opacity 0.5, cursor not-allowed, 변형 없음 |
| Loading | opacity 0.7 + cursor: wait (별도 처리) |

## 사용 예시 (HTML)

```html
<button class="btn btn-primary">분석 시작</button>
<button class="btn btn-secondary">취소</button>
<button class="btn btn-success">저장</button>
<button class="btn btn-danger">삭제</button>
<button class="btn btn-sm btn-primary">작은 버튼</button>
<button class="btn btn-primary btn-block">전체 폭 버튼</button>
<button class="btn btn-primary" disabled>비활성화</button>
```

## 통일 규칙

1. 모든 버튼은 `btn` 클래스를 기본으로 사용한다
2. 색상은 `btn-{variant}`로 지정한다
3. 크기는 `btn-{size}`로 지정한다 (생략 시 기본)
4. 인라인 `style`로 버튼 스타일을 직접 지정하지 않는다
5. width:100%가 필요한 경우 `btn-block`을 사용한다
