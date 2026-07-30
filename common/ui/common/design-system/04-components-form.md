# Components: Form Elements

## 1. 텍스트 입력 (`.input` / `.textarea`)

```css
.input { width: 100%; padding: 10px 12px;
         border: 1px solid var(--border-color-light); border-radius: var(--radius-md);
         font-size: var(--font-size-sm); font-family: var(--font-family);
         background: var(--bg-surface); color: var(--text-body); }
.input:focus { outline: none; border-color: var(--color-primary);
               box-shadow: 0 0 0 2px rgba(99,102,241,0.15); }
.input-sm { padding: 6px 8px; width: 80px; }

.textarea { width: 100%; min-height: 120px; padding: 10px 12px;
            border: 1px solid var(--border-color-light); border-radius: var(--radius-md);
            font-size: var(--font-size-sm); font-family: var(--font-family);
            resize: vertical; background: var(--bg-surface); color: var(--text-body); }
.textarea:focus { outline: none; border-color: var(--color-primary);
                  box-shadow: 0 0 0 2px rgba(99,102,241,0.15); }
```

```html
<input class="input" type="text" placeholder="입력...">
<textarea class="textarea" placeholder="분석할 문장..."></textarea>
```

## 2. Select 드롭다운 (`.select`)

```css
.select { padding: 8px 12px; border: 1px solid var(--border-color-light);
          border-radius: var(--radius-md); font-size: var(--font-size-sm);
          font-family: var(--font-family); background: var(--bg-surface); }
.select:focus { outline: none; border-color: var(--color-primary); }
```

## 3. 체크박스 / 라디오 그룹

```css
.checkbox-group { display: flex; flex-wrap: wrap; gap: var(--space-3); margin: 10px 0; }
.checkbox-label { display: inline-flex; align-items: center; gap: 6px;
                  cursor: pointer; font-size: var(--font-size-sm); }
.radio-group { display: flex; flex-wrap: wrap; gap: var(--space-3); margin: 10px 0; }
.radio-label { display: inline-flex; align-items: center; gap: 6px;
               cursor: pointer; font-size: var(--font-size-sm); }
```

```html
<div class="checkbox-group">
    <label class="checkbox-label"><input type="checkbox" checked> 옵션 A</label>
    <label class="checkbox-label"><input type="checkbox"> 옵션 B</label>
</div>
<div class="radio-group">
    <label class="radio-label"><input type="radio" name="size" checked> 표준</label>
    <label class="radio-label"><input type="radio" name="size"> 소형</label>
</div>
```

## 4. 형태소 선택 태그 (`.tag-group` + `.tag-label`)

형태소나 옵션을 버튼 형태로 선택할 때 사용.

```css
.tag-group { display: flex; flex-wrap: wrap; gap: 10px; margin: 10px 0; }
.tag-label { display: inline-flex; align-items: center; gap: 6px;
             background: var(--bg-muted); padding: 8px 12px;
             border-radius: var(--radius-md); cursor: pointer;
             border: 1px solid var(--border-color-light); font-size: var(--font-size-sm); }
.tag-label:hover { background: var(--color-secondary-hover); border-color: #adb5bd; }
.tag-label input[type="checkbox"] { cursor: pointer; }
```

## 5. 크기 선택 (`.size-options`)

```css
.size-options { display: flex; flex-wrap: wrap; gap: var(--space-2); margin: 10px 0; }
.size-options label { display: inline-flex; align-items: center; gap: 6px;
                      background: var(--bg-muted); padding: 8px 12px;
                      border-radius: var(--radius-md); cursor: pointer;
                      border: 1px solid var(--border-color-light); white-space: nowrap; }
.size-options label:hover { background: var(--color-secondary-hover); }
```

## 6. 색상 선택 (`.color-options` + `.color-btn`)

```css
.color-options { display: flex; flex-wrap: wrap; gap: var(--space-2); margin: 10px 0; }
.color-btn { width: 40px; height: 40px; border-radius: var(--radius-md);
             border: 2px solid var(--border-color-light); cursor: pointer; }
.color-btn:hover { border-color: var(--color-primary); transform: scale(1.1); }
.color-btn.selected { border-color: var(--color-primary);
                      box-shadow: 0 0 0 3px rgba(99,102,241,0.2); transform: scale(1.1); }
```

```html
<div class="color-options">
    <button class="color-btn selected" style="background:white;"></button>
    <button class="color-btn" style="background:black;"></button>
    <button class="color-btn" style="background:lightblue;"></button>
</div>
```

## 7. 복합 옵션 그룹

```css
.max-words-group { display: flex; align-items: center; gap: 10px; margin: 10px 0; }
.emotion-colors-group { display: flex; align-items: center; gap: 10px; margin: 8px 0; }
.emotion-colors-group label { display: flex; align-items: center; gap: 6px; cursor: pointer; }
```

```html
<div class="max-words-group">
    <label>최대 단어 수:</label>
    <input class="input-sm" type="number" value="100">
    <span>개</span>
</div>
<div class="emotion-colors-group">
    <label><input type="checkbox"> 감정 기반 색상 적용</label>
</div>
<small>(긍정: 파랑, 부정: 빨강, 중립: 회색)</small>
```
