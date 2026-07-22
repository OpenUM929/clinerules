# 🔴 00-Core Rules (항상 최우선 적용)

> ⚠️ **이 파일은 나침반이다. 구체적 내용은 다른 문서에 있다.**
> **작업 유형을 파악 → 아래 분류표에서 해당 유형 찾기 → 명시된 문서로 이동 → 그 문서 읽기**
> **추측 금지. 모르면 사용자에게 "어느 문서를 봐야 합니까?" 질문**

---

## 현재 프로젝트

**[.clinerules/docs/project_wordcloud/README.md](../docs/project_wordcloud/README.md)** - 프로젝트 상세 구조 및 작업 유형 분류 참조

---

## 작업 유형 분류표

| 작업 유형 | 이동할 문서 |
|-----------|-------------|
| **🔴 계획서/기획서/설계서 작성 요청** | **[00-core/03.plan-mode.md](00-core/03.plan-mode.md) — 저장 위치·파일명 형식 반드시 확인** |
| wordcloud 관련 작업 | [.clinerules/docs/msys/README.md](../docs/msys/README.md) |
| **시간 문제** | **[.clinerules/docs/development/time-handling-rules.md](../docs/development/time-handling-rules.md)** |
| **필드명/네이밍** | **[.clinerules/docs/development/field-naming-convention.md](../docs/development/field-naming-convention.md)** |
| **비교/분석/현황 정리** | **[02.hallucination-prevention.md](02.hallucination-prevention.md) — 원본 검증 필수(추측 금지)** |
| 공통 UI/디자인 | [04.design-change.md](04.design-change.md) |
| 백엔드 API | [03.workflow.md](03.workflow.md) |
| 서버 리로드/재시작 판단 | [docs/development/server-reload-guide.md](../docs/development/server-reload-guide.md) |
| 데이터베이스 / 테이블 / DDL | [docs/development/database-naming-standard.md](docs/development/database-naming-standard.md) |
| 리팩토링 | [01.legacy-protection.md](01.legacy-protection.md) FIRST |
| **소스 수정 전 백업** | **[15-backup-before-modify.md](15-backup-before-modify.md) — 빌드/수정 전 원본 백업 필수** |
| 기능 문제 분석/디버깅 | [03.workflow.md](03.workflow.md) |
| Git 작업 | [06.git-rules.md](06.git-rules.md) |
| 공통 모듈 수정/추가 | Glob으로 실제 파일 경로 확인 후 상대 경로 계산 |
| 복구/롤백 | [07.recovery-rules.md](07.recovery-rules.md) |
| **지침 수정/추가/삭제** | **[08.guideline-modification.md](core/08-guideline-modification/01.plan-mode.md)** - 반드시 사용자 요청 시에만 |
| **프로젝트 분석/나침반 생성** | **[10.project-compass.md](10.project-compass.md)** |
| **성능 분석/최적화 계획** | **[11-performance-optimization-plan.md](11-performance-optimization-plan.md)** |
| **보고서/결과보고/완료보고 작성** | **[16-report-writing.md](16-report-writing.md) — 종류표·공통규칙·양식(개별 보고서는 여기서 정본으로 분기)** |
| **영향도 분석 보고서** | **[12-impact-analysis-report.md](12-impact-analysis-report.md)** |
| **요구사항 명확화** | **[13-requirements-clarification.md](13-requirements-clarification.md)** |
| **주석/로그 제거** | **[14.comment-log-removal.md](14.comment-log-removal.md)** |
| **스케줄 규칙** | **[15.schedule-rules.md](15.schedule-rules.md)** |
| **운영자 메뉴얼 작성/수정** | **[.clinerules/docs/msys/operator-manual/DEVELOPMENT.md](../docs/msys/operator-manual/DEVELOPMENT.md)** (나침반) — 양식·페이지·마크업 **최우선 정본은 [DEVELOPMENT/00-a4-authoring-guide.md](../docs/msys/operator-manual/DEVELOPMENT/00-a4-authoring-guide.md)**) |
| **내부망 배포 패키지 생성** | **[.clinerules/docs/project_wordcloud/deployment.md](../docs/project_wordcloud/deployment.md)** |
| - 일반 배포 (소스 전용) | `.\deploy\build_deploy.ps1` → `wordcloud-project.zip` |
| - 패키지 배포 (전체) | `.\deploy\build_deploy.ps1 -Package` → `wordcloud-internal/` |

---

## 핵심 규칙 문서 위치

| 규칙 | 문서 위치 |
|------|-----------|
| **Modern Minimal Design System** | **[.clinerules/docs/ui/common/design-system/00-overview.md](../docs/ui/common/design-system/00-overview.md)** — UI 디자인 토큰 및 컴포넌트 명세 |
| **wordcloud 프로젝트** | **[.clinerules/docs/project_wordcloud/README.md](../docs/project_wordcloud/README.md)** — 프로젝트 나침반 |
| 전역 잠금 규칙 | [00-core/01.global-rules.md](00-core/01.global-rules.md) |
| Legacy Protection | [01.legacy-protection.md](01.legacy-protection.md) |
| **환각 방지 규칙** | **[02.hallucination-prevention.md](02.hallucination-prevention.md)** — 비교/분석 작성 시 원본 검증 필수 |
| **수정 전 백업** | **[15-backup-before-modify.md](15-backup-before-modify.md)** |
| 문서 가이드 | [02.documentation.md](02.documentation.md) |
| 워크플로우 | [03.workflow.md](03.workflow.md) |
| UI/디자인 변경 | [04.design-change.md](04.design-change.md) |
| 테스트 | [05.testing.md](05.testing.md) |
| Git 작업 | [06.git-rules.md](06.git-rules.md) |
| 복구/롤백 | [07.recovery-rules.md](07.recovery-rules.md) |
| **지침 추가/삭제/수정** | **[08.guideline-modification.md](core/08-guideline-modification/01.plan-mode.md)** |
| 질문 규칙 | [09.question-rules.md](09.question-rules.md) |
| Project Compass | [10.project-compass.md](10.project-compass.md) - 프로젝트 분석/나침반 |
| 성능 분석/최적화 계획 | [11-performance-optimization-plan.md](11-performance-optimization-plan.md) |
| 영향도 분석 보고서 | [12-impact-analysis-report.md](12-impact-analysis-report.md) |
| **보고서 작성 공통 지침** | **[16-report-writing.md](16-report-writing.md)** — 종류표·공통규칙·양식 |
| 요구사항 명확화 | [13-requirements-clarification.md](13-requirements-clarification.md) |
| 스케줄 규칙 | [15.schedule-rules.md](15.schedule-rules.md) |
| 시나리오 모음 | [docs/verification/scenarios/](docs/verification/scenarios/) |
| 실행 트리거 | [00-core/02.triggers.md](00-core/02.triggers.md) |
| Plan Mode | [00-core/03.plan-mode.md](00-core/03.plan-mode.md) |
| 폴더 명칭 규칙 | [08-guideline-modification/04.folder-naming.md](core/08-guideline-modification/04.folder-naming.md) |
| 누락된 규칙 분석 및 새 지침 추가 절차 | [08-guideline-modification/06.missing-rules-analysis.md](core/08-guideline-modification/06.missing-rules-analysis.md) |

---

## 참조 검증 (반드시 적용)

- **다른 문서를 참조할 때마다 Glob으로 실제 존재 여부 확인**
- 존재하지 않는 문서 링크는 추가 금지
- 새 프로젝트 문서 생성 시 README.md 파일 필수
- 참조하는 문서가 없으면 사용자에게 "어떤 문서를 만들어야 하나?" 질문

### 자산·경로 참조도 동일하게 검증한다

문서 링크뿐 아니라 **이미지 등 자산 참조**와 **코드·스크립트에 하드코딩된 경로**도 실존을 확인한다.

| 대상 | 검증 |
|------|------|
| 이미지 참조 (`<img src>`, `![]()`) | 참조 파일이 실제로 존재하는가 |
| 스크립트의 입출력 경로 | 해당 폴더가 실제로 존재하며, 문서가 참조하는 경로와 **동일한가** |
| 설정 파일의 경로 값 | 실존 여부 |

**깨진 참조 0건 대사** — 문서 수정 후 반드시 실행한다.

```bash
# 참조 목록 vs 실제 보유 목록 대사
grep -rhno 'src="images/[^"]*"' . --include=*.md | sed 's/.*images\///;s/"//' | sort -u > /tmp/ref.txt
ls images/ | sort -u > /tmp/have.txt
comm -23 /tmp/ref.txt /tmp/have.txt   # 참조되었으나 없음 → 반드시 0건
comm -13 /tmp/ref.txt /tmp/have.txt   # 보유하나 미사용 → 검토 대상
```

> ⚠️ **실제 발생**: 캡처 스크립트의 저장 경로가 존재하지 않는 폴더를 가리켜, 실행해도 문서에 반영되지 않는 상태가 방치되어 있었다. 스크립트가 "정상 종료"해도 결과물이 목적지에 도달했는지는 별도로 확인해야 한다.
>
> 파일명이 비슷하다는 이유로 대체 자산을 지정하지 않는다. **자산을 직접 열어 내용이 일치하는지 확인**한 후 참조를 수정한다.

---

항상 "현재 작업 유형이 무엇인가"를 스스로 판단하고, 해당 규칙 파일의 내용을 가장 강하게 반영해서 행동하라!
