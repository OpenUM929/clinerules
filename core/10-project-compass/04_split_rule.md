# 04 — 80줄 분리 규칙

## 원칙

> 80줄은 "읽기 부담 없이 한 눈에 파악 가능한 최대치"다.
> 초과 시 문서의 일부가 아니라 **구조 자체**를 재분류한다.

## 분리 트리거

문서 작성 중 아래 중 하나에 해당하면 즉시 분리:
1. 현재 줄 수가 80을 넘을 때
2. 작성 전 예상 줄 수가 80을 넘을 때 (사전 분리)
3. 새 섹션 추가로 80줄을 넘을 것이 확실할 때

## 분리 절차

### Before: 하나의 파일이 80줄 초과

```
_guide/src/components/GUIDE.md   ← 90줄 (초과!)
  # components 상세 가이드
  ## 파일 목록
  | Button.tsx | ...
  | Input.tsx  | ...
  | Modal.tsx  | ...
  ## Layout 컴포넌트
  | Header.tsx | ...
  | Sidebar.tsx| ...
  ## Form 컴포넌트
  | LoginForm.tsx | ...
  | SignupForm.tsx| ...
```

### After: 나침반으로 변환 + 내용 분리

```
_guide/src/components/GUIDE.md   ← 나침반으로 변환 (30줄)
  # components/ — 나침반
  ## 하위 문서 경로
  | ui/GUIDE.md     | 기본 UI 컴포넌트 |
  | layout/GUIDE.md | 레이아웃 컴포넌트 |
  | forms/GUIDE.md  | 폼 컴포넌트 |

_guide/src/components/ui/GUIDE.md      ← Button, Input, Modal
_guide/src/components/layout/GUIDE.md  ← Header, Sidebar
_guide/src/components/forms/GUIDE.md   ← LoginForm, SignupForm
```

## 분리 기준 — 내용 재분류 방법

| 원래 섹션 내용 | 분리 기준 |
|--------------|---------|
| 파일 목록이 많을 때 | 파일의 성격/역할로 그룹핑 |
| 여러 엔드포인트 | 도메인별로 분리 (user, post, auth) |
| 여러 모델 | 연관된 모델끼리 묶어서 분리 |
| 긴 수정 가이드 | 작업 유형별로 분리 |

## 분리 후 나침반 문서 형식

기존 상세 문서를 나침반으로 변환할 때 지켜야 할 것:

```markdown
# {폴더명}/ — 나침반

> **나침반 문서**: 내용이 분리되었습니다. 하위 문서를 확인하세요.

## 이 영역의 책임
{기존 "역할" 섹션 내용 유지 — 삭제 금지}

## 하위 문서 경로
| 경로 | 설명 |
|------|------|
| [새로 만든 경로] | 어떤 내용이 있는지 |

## 공통 규칙
{기존 문서에서 모든 하위에 공통 적용되는 규칙 — 유지}
```

유지해야 할 것: 역할 설명, 공통 규칙
제거하는 것: 구체적 파일 목록, 구체적 수정 가이드 (하위 문서로 이동)

## 분리하지 않아도 되는 경우

- 파일이 3개 이하이고 각 설명이 짧은 경우
- 80줄을 간신히 넘었지만 논리적으로 하나의 단위인 경우
  → 이 경우 약간의 초과(85줄 이내)는 허용

## 중첩 분리

분리 후 생성된 문서가 다시 80줄을 초과하면 재귀적으로 동일 절차 반복.

```
components/GUIDE.md (나침반)
  └── ui/GUIDE.md (80줄 초과 → 재분리)
        └── basic/GUIDE.md  (Button, Input 등)
        └── feedback/GUIDE.md (Modal, Toast 등)
```

## 파일 이름이 문서 이름인 경우

단일 파일의 내용이 80줄을 넘을 경우:

```
Before:
_guide/src/auth.service/GUIDE.md  ← 90줄

After:
_guide/src/auth.service/GUIDE.md  ← 나침반
_guide/src/auth.service/login/GUIDE.md
_guide/src/auth.service/token/GUIDE.md
_guide/src/auth.service/oauth/GUIDE.md
```
