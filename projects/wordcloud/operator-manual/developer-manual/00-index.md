---
reportTheme: technical
---

# 유지보수 개발자용 개발 메뉴얼 (v1.1.0)

> **대상 독자**: 이 시스템을 넘겨받아 유지보수·기능개선하는 개발자.
> **합격 기준**: 코드를 처음 보는 개발자가 이 문서로 아키텍처를 이해하고 안전하게 수정·빌드·배포할 수 있어야 한다.
> **기준 버전 / 최종 확인일**: system v1.1.0 · model `hr-sentiment-v1.0` · source_commit `7b106b5` · build 2026-07-16 · 문서 확인일 2026-07-22

---

## 이 문서는 무엇인가

한국어 인사평가 문서를 분석하여 **감정(긍정/부정/중립)·단어 빈도·워드클라우드**를 생성하고, 대량 배치·수집 대시보드를 제공하는 내부망 데스크톱 시스템의 **개발자 관점 설명서**다. 운영자용 사용법이 아니라, **소스 구조·엔진 동작·데이터 계층·빌드/배포·확장 시 주의점**을 코드 실증으로 다룬다.

- 앱 소스 루트: `wordcloud_project/`
- 백엔드: Python 3.10 + Flask (블루프린트 12개)
- 핵심 모델: 베이스 KoTE(44감정) + HR 도메인 파인튜닝 3분류 극성 모델
- 기준 버전 근거: `wordcloud_project/VERSION.json`

> ⚠️ 이 문서의 모든 경로·라인 번호는 확인일(2026-07-22, commit `7b106b5`) 기준 실측이다. 코드가 바뀌면 라인 번호는 어긋날 수 있으니 함수명·상징 이름으로 재탐색하라.

---

## 문서 구성 (읽는 순서)

| # | 문서 | 다루는 내용 |
|---|------|------------|
| 01 | [아키텍처 개요](01-architecture.md) | 실행 진입점 · Flask 앱 구성 · 요청 흐름 · 디렉터리 지도 |
| 02 | [모듈 지도](02-module-map.md) | 주요 패키지/서비스의 책임과 상호관계 |
| 03 | [감정분석 엔진](03-emotion-engine.md) | KoTE 로딩/추론 · 3-class 매핑 · 규칙 계층 · 절 단위 판정 · corrections 키잉 |
| 04 | [데이터 계층](04-data-layer.md) | `.sessions` DB · `src/configs` 매핑 · 스키마 · evaluation_id 함정 |
| 05 | [빌드·배포](05-build-deploy.md) | `build_deploy.ps1` · VERSION.json 재생성 · 배포 제외 폴더 |
| 06 | [배치 처리](06-batch.md) | 대규모(약 1.9만명) 배치 · 추적 복잡도 · 작업서(Work Order) |
| 07 | [파인튜닝 데이터 파이프라인](07-finetune-pipeline.md) | `hr-kote-finetune` 데이터셋 · RUNBOOK · gold 승격 · 재학습 경로 |
| 08 | [개발 환경·테스트·트러블슈팅](08-dev-setup-troubleshooting.md) | 로컬 세팅 · 실행 안내 · 자주 겪는 함정 |
| 09 | [확장 포인트/주의](09-extension-points.md) | 공통 모듈 보호 · 시간처리·필드네이밍 표준 |

---

## 상위 참조 지침 (정본)

- 프로젝트 나침반: `wordcloud_project/CLAUDE.md`, [`.clinerules/common/core/00-core.md`](../../../../common/core/00-core.md)
- 감정 규칙 상세(모듈 개요): [`project_wordcloud/modules/emotion-analysis.md`](../../modules/emotion-analysis.md)
- 배포 절차: [`project_wordcloud/deployment.md`](../../deployment.md)
- 시간 처리: [`development/time-handling-rules.md`](../../../../common/development/time-handling-rules.md) · 필드 네이밍: [`development/field-naming-convention.md`](../../../../common/development/field-naming-convention.md)
- 데이터셋 상시 절차: `wordcloud_project/plans/_datasets/kote_finetune/RUNBOOK.md`

> **정직 고지**: 본 문서는 코드 정적 조사(Read/Grep) 기반이다. 저자는 서버를 기동하거나 배치를 실행하지 않았다(무단 실행 금지 원칙). "동작한다"는 서술은 코드 경로 확인 수준이며, 런타임 검증이 필요한 항목은 각 문서에서 "확인 필요"로 명시했다.

---
↑ 상위: [운영자 메뉴얼](../../../../outputs/_transfer-msys/operator-manual/00-index.md) · 다음: [01. 아키텍처 개요 →](01-architecture.md)
