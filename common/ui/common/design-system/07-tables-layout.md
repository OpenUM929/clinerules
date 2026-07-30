# Components: Table & Layout Utilities

## 1. 데이터 테이블 (`.table`)

```css
.table { width: 100%; border-collapse: collapse; font-size: var(--font-size-sm); }
.table th, .table td { padding: 12px; text-align: left;
                       border-bottom: 1px solid var(--border-color-light); }
.table th { background: var(--bg-muted); font-weight: var(--font-weight-semibold); }
.table tbody tr:hover { background: #f9fafb; }
```

```html
<table class="table">
    <thead>
        <tr><th>작업명</th><th>상태</th><th>진행률</th></tr>
    </thead>
    <tbody>
        <tr><td>2026년 상반기 평가</td>
            <td><span class="badge badge-warning">진행 중</span></td>
            <td>65%</td></tr>
    </tbody>
</table>
```

---

## 2. 레이아웃 유틸리티

### Flex

| 클래스 | 속성 |
|--------|------|
| `.flex-row` | display: flex |
| `.flex-col` | flex-direction: column |
| `.flex-center` | align-items + justify-content: center |
| `.flex-between` | align-items: center; justify-content: space-between |
| `.flex-wrap` | flex-wrap: wrap |

### Gap

| 클래스 | 값 |
|--------|-----|
| `.gap-1` | 4px |
| `.gap-2` | 8px |
| `.gap-3` | 12px |
| `.gap-4` | 16px |
| `.gap-5` | 20px |

---

## 3. 매핑 영역 (`.mapping-area`)

**배치/메타데이터 선택화면의 2단 레이아웃.**

```css
.mapping-area { display: flex; gap: var(--space-5); margin-top: var(--space-5); }
.tree-panel { flex: 1; border: 1px solid var(--border-color);
              border-radius: var(--radius-lg); padding: 15px;
              background: var(--bg-surface); }
.data-panel { flex: 2; border: 1px solid var(--border-color);
              border-radius: var(--radius-lg); padding: 15px;
              background: var(--bg-surface); }
```

### 트리 노드 (`.tree-node`)

```css
.tree-node { padding: 8px; cursor: pointer; border-radius: var(--radius-sm); }
.tree-node:hover { background: var(--color-secondary); }
.tree-node.selected { background: var(--color-primary); color: var(--text-inverse); }
.tree-node.mapped { background: var(--color-success); color: var(--text-inverse); }
```

---

## 4. 스크롤바 (공통)

```css
::-webkit-scrollbar { width: 8px; }
::-webkit-scrollbar-track { background: #f1f1f1; border-radius: 4px; }
::-webkit-scrollbar-thumb { background: #888; border-radius: 4px; }
::-webkit-scrollbar-thumb:hover { background: #555; }
```

---

## 5. 보조 컨테이너

```css
/* 텍스트 컨테이너 (스크롤 가능) */
.text-container { max-height: 200px; overflow-y: auto;
                  border: 1px solid var(--border-color); padding: 10px;
                  margin: 10px 0; background: #f9f9f9; border-radius: var(--radius-sm); }

/* 평가 결과 컨테이너 */
.evaluation-container { max-height: 300px; overflow-y: auto;
                        border: 1px solid var(--border-color); padding: 10px;
                        margin: 10px 0; border-radius: var(--radius-sm); }

/* 워드리스트 */
.word-list { margin: 5px 0 0 20px; }
.word-list li { margin: 3px 0; font-size: var(--font-size-body); color: #6c757d; }
```
