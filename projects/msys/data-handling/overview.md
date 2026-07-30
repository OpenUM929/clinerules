# 데이터 처리 규칙 개요

> ⚠️ **위반 시 경고 후 사용자 확인 필수**

## 시간/날짜 처리 규칙 요약

| 계층 | 규칙 | 비고 |
|------|------|------|
| DB 저장 | KST (UTC+9), TIMESTAMP WITHOUT TIME ZONE | |
| DAO SQL | TO_CHAR 변환 필수 | 문자열 반환 |
| Python | `get_kst_now()` 사용 | datetime.now() 금지 |
| JavaScript | `getKSTNow()`, `formatDBDateTime()` | new Date() 금지 |

## 금지 사항

- datetime 객체를 jsonify로 반환
- TO_CHAR 없이 datetime 조회
- new Date()로 시간 생성
- ISO 8601 형식 저장

## 하위 문서

| 문서 | 설명 |
|------|------|
| [basic-rules.md](basic-rules.md) | 기본 시간 처리 규칙 |
| [time-display.md](time-display.md) | 시간 표시 체계 (3단계) |
| [real-time-update.md](real-time-update.md) | 실시간 업데이트 |
| [timezone.md](timezone.md) | 시간대 변환 주의사항 |
| [modal-time.md](modal-time.md) | 모달/팝업 시간 표시 |
| [checklist.md](checklist.md) | 검증 체크리스트 |
