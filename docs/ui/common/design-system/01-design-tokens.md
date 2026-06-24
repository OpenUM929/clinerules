# Design Tokens — 색상 / 타이포그래피 / 간격

## 1. 색상 (Color Palette)

### 주 색상
| Token | 값 | 용도 |
|-------|-----|------|
| `--color-primary` | `#6366f1` | 버튼, 링크, 액센트, 활성화 |
| `--color-primary-hover` | `#4f46e5` | primary 호버 |
| `--color-primary-light` | `#ede9fe` | 연한 강조 배경 |
| `--color-primary-subtle` | `rgba(99,102,241,0.08)` | 업로드 영역 등 미세한 배경 |

### 기능 색상
| Token | 값 | 용도 |
|-------|-----|------|
| `--color-success` | `#28a745` | 완료, 긍정 |
| `--color-success-hover` | `#218838` | success 호버 |
| `--color-danger` | `#dc3545` | 삭제, 부정 |
| `--color-danger-hover` | `#c82333` | danger 호버 |
| `--color-warning` | `#f59e0b` | 진행 중, 경고 |
| `--color-info` | `#17a2b8` | 정보, 대기 |
| `--color-secondary` | `#f3f4f6` | 보조 버튼 배경 |
| `--color-secondary-hover` | `#e5e7eb` | secondary 호버 |

### 표면 색상
| Token | 값 | 용도 |
|-------|-----|------|
| `--bg-body` | `#f0f0f0` | 전체 페이지 배경 |
| `--bg-surface` | `#ffffff` | 카드, 패널, 입력 필드 배경 |
| `--bg-muted` | `#f8f9fa` | 정보 섹션, 테이블 헤더 |
| `--bg-nav` | `linear-gradient(180deg, #ffffff 0%, #f8fbff 100%)` | 네비게이션 배경 |
| `--bg-content` | `linear-gradient(135deg, #ffffff 0%, #f8fbff 100%)` | 콘텐츠 영역 배경 |

### 텍스트 색상
| Token | 값 | 용도 |
|-------|-----|------|
| `--text-primary` | `#1f2937` | h1, h2 제목 |
| `--text-secondary` | `#333333` | h3~h6 제목 |
| `--text-body` | `#495057` | 본문, 버튼 텍스트 |
| `--text-muted` | `#666666` | 설명, 레이블 |
| `--text-subtle` | `#999999` | 메타 정보, 결과 레이블 |
| `--text-inverse` | `#ffffff` | primary/success 버튼 텍스트 |

### 테두리 색상
| Token | 값 | 용도 |
|-------|-----|------|
| `--border-color` | `#dee2e6` | 기본 테두리 (info-section) |
| `--border-color-light` | `#e5e7eb` | 가벼운 테두리 (입력 필드, 태그) |
| `--border-color-muted` | `#e0e0e0` | 카드 테두리 |

---

## 2. 타이포그래피 (Typography)

### 폰트
```
--font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
```

### 제목 계층
| Token | 크기 | 두께 | 색상 | 밑줄 | 용도 |
|-------|------|------|------|------|------|
| `--font-size-hero` | 32px | 700 | #1f2937 | 없음 | 페이지 최상단 타이틀 |
| `--font-size-h1` | 26px | 700 | #1f2937 | 2px primary | 페이지 메인 제목 |
| `--font-size-h2` | 20px | 700 | #1f2937 | 없음 | 섹션 제목 |
| `--font-size-h3` | 17px | 600 | #333 | 없음 | 서브섹션 제목 |
| `--font-size-h4` | 15px | 600 | #333 | 2px primary | 카드/옵션 타이틀 |

### 본문/라벨 계층
| Token | 크기 | 두께 | 색상 | 용도 |
|-------|------|------|------|------|
| `--font-size-body` | 14px | 400 | #495057 | 본문, 버튼, 테이블 |
| `--font-size-sm` | 13px | 400 | #666 | 레이블, 설명, 입력값 |
| `--font-size-xs` | 12px | 600 | #999 | 결과 레이블(uppercase) |
| `--font-size-2xs` | 11px | 400 | #999 | 메타, 단계 텍스트 |

---

## 3. 간격 (Spacing Scale)

| Token | 값 | 사용처 |
|-------|-----|--------|
| `--space-1` | 4px | 미세 여백 |
| `--space-2` | 8px | color-btn gap, 태그 간격 |
| `--space-3` | 12px | checkbox/radio gap |
| `--space-4` | 16px | 옵션 카드 padding |
| `--space-5` | 20px | 카드 padding, 페이지 마진 |
| `--space-6` | 24px | 업로드 영역 padding |
| `--space-8` | 30px | 섹션 마진 |
| `--space-10` | 40px | 큰 마진, 페이지 padding |

---

## 4. 테두리 반경 (Border Radius)

| Token | 값 | 용도 |
|-------|-----|------|
| `--radius-sm` | 4px | 배지, 작은 태그 |
| `--radius-md` | 6px | 버튼, 입력 필드 |
| `--radius-lg` | 8px | 카드, info-section |
| `--radius-xl` | 12px | 큰 카드, 모달 |
| `--radius-full` | 50% | 원형 (step-circle, color-btn) |

---

## 5. 그림자 (Shadows)

| Token | 값 | 용도 |
|-------|-----|------|
| `--shadow-sm` | 0 1px 3px rgba(0,0,0,0.08) | 카드 기본 그림자 |
| `--shadow-md` | 0 2px 8px rgba(0,0,0,0.1) | 떠 있는 카드 |
| `--shadow-lg` | 0 4px 20px rgba(0,0,0,0.1) | 모달, 드롭다운 |
| `--shadow-primary` | 0 2px 8px rgba(99,102,241,0.2) | primary 버튼 기본 |
| `--shadow-primary-hover` | 0 4px 12px rgba(99,102,241,0.3) | primary 버튼 호버 |
