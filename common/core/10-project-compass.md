# 10. Project Compass (프로젝트 나침반 생성)

> 🧭 **나침반 문서** — 내용을 담지 않고 위치만 가리킨다.
> 줄수 상한·나침반 판정의 **정본은 [23-compass-rule.md](23-compass-rule.md)** 다. 이 문서는 "새 프로젝트를 스캔해 나침반 문서 트리를 만드는 절차"를 다룬다.

---

## 트리거

"프로젝트 분석", "프로젝트 가이드 만들어줘", "소스 문서화", "에이전트용 가이드", "나침반 문서", "compass 문서", 새 프로젝트 폴더를 공유하며 문서 생성을 요청할 때.

---

## 핵심 개념

> "문서는 직접 정보를 담지 않는다. 정보가 있는 곳을 가리킨다."

| 종류 | 역할 | 상한 |
|------|------|------|
| 나침반 문서 | 하위 문서 경로만 나열 | 60줄 ([23-compass-rule.md](23-compass-rule.md) CMP-2) |
| 상세 문서 | 실제 역할·파일 설명·체크리스트 | 160줄 (80줄 초과 시 경고) |

---

## 실행 절차

| Step | 내용 | 문서 |
|------|------|------|
| 1 | 프로젝트 구조 스캔 | [10-project-compass/01-scan.md](10-project-compass/01-scan.md) |
| 2 | 문서 트리 설계 | [10-project-compass/02-design.md](10-project-compass/02-design.md) |
| 3 | 문서 생성(템플릿) | [10-project-compass/03-templates.md](10-project-compass/03-templates.md) |
| 4 | 분리 규칙 적용 | [10-project-compass/04-split-rule.md](10-project-compass/04-split-rule.md) |
| 5 | 품질 확인 | [10-project-compass/05-quality-checklist.md](10-project-compass/05-quality-checklist.md) |
| 6 | 진입점 나침반 생성 | `{{guideline.project_dir}}/README.md` |

---

## 관련 문서

| 주제 | 문서 |
|------|------|
| 나침반 규약(판정·상한·콘텐츠·분리 완료조건) | [23-compass-rule.md](23-compass-rule.md) |
| 문서 분리 절차 | [08-guideline-modification/03-document-separation.md](08-guideline-modification/03-document-separation.md) |
| 폴더 명칭 | [08-guideline-modification/04-folder-naming.md](08-guideline-modification/04-folder-naming.md) |
| 자동 검사 | `tools/lint_guidelines.py` (`C1`~`C5`) |
