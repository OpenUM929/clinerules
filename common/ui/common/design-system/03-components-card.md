# Components: Card System

## 1. 기본 카드 (`.card`)

기본 컨테이너. 페이지 내 콘텐츠 블록을 감싼다.

```css
.card { background: var(--bg-surface); border: 1px solid var(--border-color-muted);
        border-radius: var(--radius-lg); padding: var(--space-5);
        box-shadow: var(--shadow-sm); }
.card-elevated { box-shadow: var(--shadow-md); }
```

```html
<div class="card">
    <p>콘텐츠 내용</p>
</div>
```

## 2. 헤더형 카드 (`.card` + `.card-header`)

```css
.card-header { margin: -20px -20px 16px -20px; padding: 16px 20px;
               background: var(--bg-muted);
               border-bottom: 1px solid var(--border-color-muted);
               border-radius: var(--radius-lg) var(--radius-lg) 0 0; }
```

```html
<div class="card">
    <div class="card-header"><h4>제목</h4></div>
    <div class="card-body">내용</div>
</div>
```

## 3. 옵션 카드 (`.option-card`)

설정 옵션 그룹을 담는 카드. h4에 보라색 하단 보더가 특징.

```css
.option-card { background: var(--bg-surface); border: 1px solid var(--border-color-muted);
               border-radius: var(--radius-lg); padding: 15px;
               box-shadow: var(--shadow-sm); margin-bottom: 15px; }
.option-card h4 { margin: 0 0 12px 0; padding-bottom: 8px;
                  border-bottom: 2px solid var(--color-primary);
                  font-size: var(--font-size-h4); font-weight: var(--font-weight-semibold); }
```

```html
<div class="option-card">
    <h4>설정 제목</h4>
    <!-- 옵션 내용 -->
</div>
```

## 4. 정보 섹션 (`.info-section`)

정보 표시용. muted 배경에 얇은 테두리.

```css
.info-section { background: var(--bg-muted); border: 1px solid var(--border-color);
                border-radius: var(--radius-lg); padding: 15px; margin: 10px 0; }
.info-section h4 { margin: 0 0 10px 0; padding-bottom: 8px;
                   border-bottom: 2px solid var(--color-primary);
                   font-size: var(--font-size-h4); font-weight: var(--font-weight-semibold); }
.info-item { padding: 8px 0; border-bottom: 1px solid #e9ecef; }
.info-item:last-child { border-bottom: none; }
.info-item strong { display: inline-block; width: 120px; color: #495057; }
```

## 5. 결과 아이템 (`.result-item`)

통계/수치 표시용. 좌측 컬러 보더로 의미 전달.

```css
.result-item { background: var(--bg-surface); border: 1px solid var(--border-color-muted);
               border-radius: var(--radius-lg); padding: 12px;
               border-left: 4px solid var(--color-primary); }
```

**보더 색상 규칙:**
| 의미 | border-left-color |
|------|-------------------|
| 일반 | `var(--color-primary)` |
| 긍정/완료 | `var(--color-success)` (#28a745) |
| 부정 | `var(--color-danger)` (#dc3545) |
| 진행 중 | `var(--color-warning)` (#f59e0b) |
| 중립 | `#6c757d` |

```html
<div class="result-item" style="border-left-color: var(--color-success);">
    <div class="result-label">긍정</div>
    <div class="result-value">66.7%</div>
</div>
```

## 6. 평가 아이템 (`.evaluation-item`)

문장별 분석 결과 표시. 좌측 2px 보더.

```css
.evaluation-item { margin-bottom: 15px; padding: 10px;
                   border-left: 2px solid var(--color-primary);
                   background-color: var(--bg-muted);
                   border-radius: 0 var(--radius-sm) var(--radius-sm) 0; }
```

## 7. 카드 그리드 (`.cards-container` / `.cards-grid`)

카드를 나열할 때 사용하는 레이아웃.

```css
.cards-container { display: flex; flex-wrap: wrap; gap: 15px; margin-top: 15px; }
.cards-container > * { flex: 1; min-width: 250px; }

.cards-grid { display: grid;
              grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
              gap: 15px; margin-bottom: var(--space-5); }
```
