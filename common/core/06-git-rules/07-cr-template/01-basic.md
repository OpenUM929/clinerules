# 기본 CR 템플릿

> 상위 나침반 [`../07-cr-template.md`](../07-cr-template.md) 에서 분리.

### 기본 템플릿

```markdown
## Change Request

- CR ID        : REQ-yymm-nnn
- 레파지토리   : (00-core.md의 "현재 프로젝트" 섹션에서 확인 후 작성)
- 요청 타입    : feat / fix / docs / style / refactor / perf / test / chore / inquiry / analysis
- 대상 스코프  : (예: routes, services, dao, templates)
- 작업 유형    : 기능 작업 / 비기능 작업
- 요청자       : (사용자 이름)
- 요청 날짜    : YYYY.MM.DD

---

### 지침 진행 과정

1. 00-core.md 확인 → "[작업 유형]"
2. 참조 문서: [문서 경로]
3. 분석 내용: 확인한 파일 및 함수, 데이터 흐름

---

### 변경 요약 (1줄, 50자 이내)
> 

### 변경 배경 / 이유
> 

### 변경 전 → 변경 후
- Before: 
- After : 

### 영향 범위
> 

---

### 작업 상세 내역 (파일별)

> **Claude가 반드시 작성**: 수정된 각 파일의 상세 변경 내용을 테이블로 정리
> - 순번, 파일 경로, 변경 유형(생성/수정/삭제), 상세 내용
> - Before/After 코드 예시 포함

| 순번 | 파일 경로 | 변경 유형 | 상세 내용 |
|------|-----------|-----------|-----------|
| 1 | `path/to/file.py` | 수정 | 함수 `X()`의 파라미터 `Y`를 `Z`로 변경 |
| 2 | `path/to/new.js` | 생성 | 신규 모듈, 기능: A, B, C |
| 3 | `path/to/old.css` | 삭제 | 미사용 스타일 제거 |

**변경 코드 요약:**
```python
# Before
def old_func():
    pass

# After  
def new_func():
    return True
```

---
