# CR ID 생성 규칙

> 상위 나침반 [`../06-git-rules.md`](../06-git-rules.md) 에서 분리.

## CR ID 생성 규칙

- 형식: `REQ-yymm-nnn`
- 예시: `REQ-2604-001` (2026년 4월 첫 번째 요청)

### CR ID 중복 방지

1. **Claude가 직접 확인**: `bash` 도구로 `.clinerules/outputs/cr/` 폴더 조회
   - 명령어: `ls .clinerules/outputs/cr/` 또는 `Get-ChildItem .clinerules/outputs/cr/`
   - 기존 ID 확인 → 다음 번호 자동 부여 (예: 001~009 존재 → 010 부여)
   - **결과 즉시 사용자에게 보고**: "확인 결과: REQ-2604-010 사용 가능"
   - ❌ **금지**: "확인 필요"라고만 하고 실제 확인 미루기

2. 기존 기능의 버그 수정이 아니면 반드시 새 CR ID 사용
   - 예: 시간대 수정 중 메모 기능 추가 → 다른 CR ID

---
