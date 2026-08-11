# Components: Feedback — 배지 / 상태 메시지 / 진행 표시

## 1. 배지 (`.badge`)

상태를 짧게 표시하는 태그.

```css
.badge { display: inline-block; padding: 2px 8px; border-radius: var(--radius-sm);
         font-size: var(--font-size-2xs); font-weight: var(--font-weight-semibold); }
```

| 클래스 | 배경색 | 텍스트색 |
|--------|--------|---------|
| `.badge-primary` | #ede9fe | #3730a3 |
| `.badge-success` | #d4edda | #155724 |
| `.badge-danger` | #f8d7da | #721c24 |
| `.badge-warning` | #fff3cd | #856404 |
| `.badge-info` | #d1ecf1 | #0c5460 |

```html
<span class="badge badge-success">완료</span>
<span class="badge badge-warning">진행 중</span>
<span class="badge badge-danger">오류</span>
```

## 2. 상태 메시지 (`.status-message`)

사용자에게 시스템 상태를 알리는 블록 메시지.

```css
.status-message { padding: var(--space-3); border-radius: var(--radius-md);
                  font-size: var(--font-size-sm); margin: 10px 0; }
```

| 클래스 | 배경 | 텍스트 | 테두리 |
|--------|------|--------|--------|
| `.status-success` | #d4edda | #155724 | #c3e6cb |
| `.status-error` | #f8d7da | #721c24 | #f5c6cb |
| `.status-warning` | #fff3cd | #856404 | #ffeaa7 |
| `.status-info` | #d1ecf1 | #0c5460 | #bee5eb |

```html
<div class="status-message status-success">✅ 분석이 완료되었습니다.</div>
<div class="status-message status-error">❌ 오류가 발생했습니다.</div>
<div class="status-message status-warning">⚠️ 일부 데이터가 누락되었습니다.</div>
<div class="status-message status-info">ℹ️ 총 15개 문장이 분석되었습니다.</div>
```

## 3. 진행 바 (`.progress-bar` + `.progress-fill`)

```css
.progress-bar { width: 100%; height: 24px; background: var(--border-color-light);
                border-radius: var(--radius-xl); overflow: hidden; margin: 10px 0; }
.progress-fill { height: 100%;
                 background: linear-gradient(90deg, var(--color-primary), #8b5cf6);
                 transition: width 0.3s ease; }
```

```html
<div class="progress-bar">
    <div class="progress-fill" style="width: 65%;"></div>
</div>
<div class="progress-text">65% — 2/3 문장 분석 완료</div>
```

## 4. 단계 표시기 (`.step-indicator`)

### 대형 (기본)
```css
.step-indicator { display: flex; justify-content: center; align-items: center;
                  margin-bottom: var(--space-8); }
.step-circle { width: 40px; height: 40px; border-radius: var(--radius-full);
               background: #e5e7eb; display: flex; align-items: center;
               justify-content: center; font-size: var(--font-size-body);
               font-weight: var(--font-weight-semibold); color: var(--text-muted); }
.step.active .step-circle { background: var(--color-primary); color: var(--text-inverse); }
.step.completed .step-circle { background: var(--color-success); color: var(--text-inverse); }
```

### 소형 (compact 레이아웃용)
```css
.step-sm-circle { width: 36px; height: 36px; border-radius: var(--radius-full);
                  background: #e5e7eb; display: flex; align-items: center;
                  justify-content: center; font-size: var(--font-size-sm);
                  font-weight: var(--font-weight-semibold); color: var(--text-muted); }
```

```html
<div class="step-indicator">
    <div class="step completed">
        <div class="step-circle">✓</div>
        <div class="step-text">입력</div>
    </div>
    <span class="step-arrow">›</span>
    <div class="step active">
        <div class="step-circle">2</div>
        <div class="step-text">분석</div>
    </div>
    <span class="step-arrow">›</span>
    <div class="step">
        <div class="step-circle">3</div>
        <div class="step-text">결과</div>
    </div>
</div>
```

## 5. 업로드 영역 (`.upload-area`)

```css
.upload-area { border: 2px dashed var(--color-primary); padding: 40px;
               text-align: center; border-radius: var(--radius-lg);
               margin-bottom: var(--space-5);
               background: var(--color-primary-subtle); }
.upload-area.dragover { background: var(--color-primary-light); }
```
