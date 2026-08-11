# 상세 템플릿 (복구·이력 추적용)

> 상위 나침반 [`../07-cr-template.md`](../07-cr-template.md) 에서 분리.

### 상세 템플릿 (e.txt 기반) - 복구/이력 추적용

> 복구 시에도 내용 파악이 용이하도록 상세 기록

```markdown
## Change Request

- CR ID        : REQ-yymm-nnn
- 레파지토리   : 
- 요청 타입    : feat / fix / docs / style / refactor / perf / test / chore / inquiry / analysis
- 대상 스코프  : 
- 작업 유형    : 기능 작업 / 비기능 작업
- 요청자       : 
- 요청 날짜    : YYYY.MM.DD

---

## 📊 현재 상태
> 변경 전 문제 상황, 버그 현상, 개선 필요성

## ✅ 완료된 것
> - [x] 완료된 작업 항목 1
> - [x] 완료된 작업 항목 2

## 🔄 진행 중인 것
> - [ ] 진행 중인 작업 항목

## ❓ 미결 결정사항
> 아직 결정되지 않은 사항, 추후 검토 필요 사항

## 📋 다음 작업
> - [ ] 다음에 해야 할 작업

## ⚠️ 주의사항 / 이전 실수
> 이번 작업에서 피해야 할 점, 학습한 내용

## 📁 관련 파일 경로
| 구분 | 파일 경로 | 변경 유형 | 상세 내용 |
|------|-----------|-----------|-----------|
| Backend | `path/to/file.py` | 수정 | 함수 `X()`의 파라미터 `Y`를 `Z`로 변경 |
| Frontend | `path/to/new.js` | 생성 | 신규 모듈, 기능: A, B, C |
| Database | `path/to/old.sql` | 삭제 | 미사용 테이블 제거 |

## 📝 상세 변경 내용

### Before / After

**파일: `path/to/file.py`**
```python
# Before
def old_func():
    pass

# After  
def new_func():
    return True
```

---

## FP / 작업 구분

| 항목 | 내용 |
|------|------|
| 작업 유형 | 기능 작업 / 비기능 작업 |
| 기능 점수 (FP) | N (비기능 작업 시 "-") |
| 예상 공수 | NH |

---

## 📢 공지용 요약

**[상세 내용]**
> 

**[요약]**
> 
```

---
