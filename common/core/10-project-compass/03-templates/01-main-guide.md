# 템플릿 1: MAIN_GUIDE.md (최상위 나침반)

> 상위 나침반 [`../03-templates.md`](../03-templates.md) 에서 분리.

## 템플릿 1: MAIN_GUIDE.md (최상위 나침반)

```markdown
# {프로젝트명} — AI 에이전트 가이드

> **나침반 문서**: 이 문서는 경로만 안내합니다. 상세 정보는 하위 GUIDE.md에 있습니다.

## 프로젝트 개요

| 항목 | 내용 |
|------|------|
| 목적 | {한 줄 설명} |
| 언어 | {TypeScript / Python / ...} |
| 프레임워크 | {Next.js 14 / FastAPI / ...} |
| 진입점 | `{파일 경로}` |
| 실행 | `{npm run dev / uvicorn app.main:app ...}` |
| 테스트 | `{npm test / pytest ...}` |

## 문서 경로 (나침반)

| 경로 | 담당 영역 |
|------|----------|
| [`_guide/src/GUIDE.md`](_guide/src/GUIDE.md) | 소스 코드 전체 |
| [`_guide/tests/GUIDE.md`](_guide/tests/GUIDE.md) | 테스트 |
| [`_guide/infra/GUIDE.md`](_guide/infra/GUIDE.md) | 인프라/배포 |
| [`_guide/config/GUIDE.md`](_guide/config/GUIDE.md) | 환경설정 파일들 |

## 에이전트 작업 규칙

1. **작업 전**: 관련 폴더의 GUIDE.md를 먼저 확인한다
2. **파일 추가**: 해당 폴더 GUIDE.md 파일 목록에 추가한다
3. **폴더 추가**: `_guide/`에 동일 경로로 GUIDE.md를 생성한다
4. **수정 완료 후**: GUIDE.md의 수정 이력 또는 주의사항을 업데이트한다

## 아키텍처 요약

{데이터 흐름 또는 레이어 구조를 2-5줄로 설명}
예: 요청 → Router → Service → Repository → DB
```

---
