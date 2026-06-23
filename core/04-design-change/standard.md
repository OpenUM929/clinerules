# 표준 절차 (복수 요소 / 레이아웃 / 페이지 단위)

## 1단계: 필수 문서 확인

- `read_file .clinerules/docs/ui/common/design-system/00-overview.md` — 디자인 시스템 개요 확인
- `read_file docs/ui/common/screen-domain.md` — 화면 목록 및 파일 경로 확인
- `read_file docs/core/design-change-workflow.md` — 상세 작업 흐름 확인
- 대상 페이지 분석 (HTML, CSS, JavaScript)

## 2단계: 계획 수립 및 승인 요청

다음 형식으로 사용자에게 제시 후 승인받기:

```
[디자인 변경 계획]
- 대상 파일: (경로)
- 변경 내용:
  - Before: (현재 상태)
  - After:  (변경 후 상태)
- 영향 범위: (다른 페이지/컴포넌트에 미치는 영향)
진행해도 될까요?
```

## 3단계: 구현

- 승인된 계획 범위 내에서만 수정
- 계획에 없던 변경이 필요해지면 → 즉시 중단 후 추가 승인 요청

## 4단계: 완료 보고

- 수정된 파일 목록
- 변경 내용 요약
- 확인이 필요한 URL/화면
