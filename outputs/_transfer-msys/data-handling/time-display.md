# 시간 표시 체계

> 모든 시간 데이터는 3단계를 거쳐 처리됨

## 3단계 처리 체계

| 단계 | 처리 위치 | 규칙 | 결과 형식 예시 |
|------|----------|------|----------------|
| 1. 저장 | Python Backend | KST 기준 문자열로 저장 | `2026-04-16 15:30:00` |
| 2. 조회 | DAO SQL | TO_CHAR로 문자열 변환 | `2026-04-16 15:30:00` |
| 3. 표시 | JavaScript Frontend | formatDBDateTime() 사용 | `26.04.16 15:30` |

## 필수 체크리스트

- [ ] DB 저장 시: KST 문자열 (`YYYY-MM-DD HH:mm:ss`)
- [ ] API 응답 시: TO_CHAR 변환된 문자열
- [ ] 화면 표시 시: `formatDBDateTime()` 결과 (`YY.MM.DD HH:mm`)

## 데이터 흐름

```
[사용자 입력] → [Python Backend: get_kst_now()] 
    → [DB 저장: TIMESTAMP WITHOUT TIME ZONE]
    → [DAO 조회: TO_CHAR 변환] 
    → [API 응답: 문자열] 
    → [Frontend: formatDBDateTime() 표시]
```

## 관련 문서

- [overview.md](overview.md) (개요)
- [basic-rules.md](basic-rules.md) (기본 규칙)
- [real-time-update.md](real-time-update.md) (실시간 업데이트)
- [timezone.md](timezone.md) (시간대 변환)
- [modal-time.md](modal-time.md) (모달/팝업)
- [checklist.md](checklist.md) (검증 체크리스트)
