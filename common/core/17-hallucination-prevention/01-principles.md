# 핵심 원칙

> 상위 나침반 [`../17-hallucination-prevention.md`](../17-hallucination-prevention.md) 에서 분리.

## 핵심 원칙

**Claude가 스스로 만든 정보를 마치 존재하는 것처럼 처리하는 환각(Hallucination) 행위를 철저히 방지한다.**

사용자가 비교분석, 영향도 분석, 현황 정리 등을 요청할 때, Claude는 반드시 **원본 문서/코드를 직접 읽고 검증한 후에만** 결과를 작성해야 한다.

---
