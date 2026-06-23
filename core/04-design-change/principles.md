# 공통 원칙

- 명시적 요청 없이 기존 디자인 변경 금지
- 다른 페이지들과의 일관성 검토 필수 (표준 절차 시)
- 계획 범위를 벗어나는 "선의의 추가 개선" 금지
- **팝업/모달 내 텍스트 오버플로우 방지 원칙**
  - 동적으로 생성되는 텍스트(그룹명, 작업명 등)는 JavaScript 단에서 `maxLength` 제한 + `substring(...)` 적용
  - CSS에서는 `max-width: 100%`, `overflow: hidden`, `text-overflow: ellipsis`, `white-space: nowrap` 필수 적용
  - 툴팁(`title` 속성)으로 전체 텍스트는 노출하여 생략된 정보는 호버로 확인 가능하도록 유지
