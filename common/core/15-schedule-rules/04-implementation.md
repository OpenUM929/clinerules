# 구현 상세

> 상위 나침반 [`../15-schedule-rules.md`](../15-schedule-rules.md) 에서 분리.

## 4. 구현 상세

### 4.1 데이터 구조

```typescript
// 슬롯 상태 인터페이스
interface SlotState {
  activityId: string;
  executed: boolean;
}

// 주간 계획 상태
const [weekly, setWeekly] = useState<Record<string, { am: SlotState | null; pm: SlotState | null }>>(
  Object.fromEntries(DAYS.map((d) => [d, { am: null, pm: null }]))
);

// 현재 위치 추적
const [currentSlotIndex, setCurrentSlotIndex] = useState<number>(1); // 1~14
const [weekNumber, setWeekNumber] = useState<number>(1);            // 주차 카운터
```

### 4.2 변환 함수

```typescript
// 인덱스 → 요일+시간대 변환
const indexToSlot = (index: number) => {
  const dayIndex = Math.floor((index - 1) / 2);  // 0~6
  const period = index % 2 === 1 ? "am" : "pm";   // 홀수=AM, 짝수=PM
  return { day: DAYS[dayIndex], period };
};

// 요일+시간대 → 인덱스 변환
const slotToIndex = (day: string, period: string) => {
  const dayIndex = DAYS.indexOf(day);  // 0~6
  const periodOffset = period === "am" ? 0 : 1;
  return dayIndex * 2 + periodOffset + 1;
};
```

### 4.3 핵심 함수

| 함수 | 설명 |
|------|------|
| `addToWeekly(activityId)` | 활동을 주간 계획에 추가 |
| `runSingle(activityId)` | 오늘의 활동 실행 |
| `moveToNextSlot()` | 다음 슬롯으로 이동 |
| `resetWeeklyAll()` | 모든 슬롯 초기화 |
| `resetWeeklyAm()` | AM 슬롯만 초기화 |
| `resetWeeklyPm()` | PM 슬롯만 초기화 |

### 4.4 실행 흐름

1. 사용자가 스케줄에서 `[실행]` 버튼 클릭
2. `runSingle(activityId)` 호출
3. 오늘의 슬롯 실행 → `weekly[day][period].executed = true`
4. `moveToNextSlot()` 호출 → 다음 슬롯으로 이동
5. 14개 슬롯 모두 실행 완료 시 `currentSlotIndex > 14`
6. 자동으로 다음 주로 전환 (`weekNumber++`, `currentSlotIndex = 1`)

---
