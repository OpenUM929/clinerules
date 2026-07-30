# 프로젝트 레지스트리

> 이 지침 저장소를 사용하는 프로젝트 목록. **격리 검사(린터 `L2`·`L6`·`A3`·`A4`·`A6`)의 금칙어 사전**이다.
> 새 프로젝트를 온보딩하면 반드시 여기에 먼저 등록한다. 등록하지 않으면 그 프로젝트의 고유값이 `common/` 에 새어 들어가도 검출되지 않는다.

## 등록 목록

| project_id | project_name | 저장소 경로 | 지침 폴더 | 등록일 |
|------------|--------------|-------------|-----------|--------|
| `wordcloud` | 워드클라우드 인사평가 분석 시스템 | `D:\dev\wordcloud` | `projects/wordcloud/` | 2026-07-28 |
| `msys` | MSYS | `D:\dev\msys` | (미이관 — `outputs/_transfer-msys/` 이관 대기) | 2026-07-28 |

## 금칙어 (common/ · 에이전트 정의에서 검출 대상)

위 표의 `project_id` 와 아래 고유값이 `common/**` 또는 `.claude/agents/*.md` 에 있으면 격리 위반이다.
**고유값은 이름만이 아니다.** 폴더 계층·파일 경로 같은 구조 가정도 그 프로젝트에만 참이다
([`core/21-project-isolation.md`](core/21-project-isolation.md) ISO-2·ISO-7, [`core/26-agent-definitions.md`](core/26-agent-definitions.md) AGT-8).

| 분류 | 매칭 방식 | 검사 |
|------|-----------|------|
| 이름 | 대소문자 무시 부분 문자열 | `L2`·`A3` error / `A4` warn |
| 경로·구조 | 앞 단어 경계 기준 부분 문자열 | `L6`·`A6` 모두 (타 프로젝트 error, 자기 warn) |

| project_id | 분류 | 금칙어 |
|------------|------|--------|
| `wordcloud` | 이름 | `wordcloud`, `워드클라우드`, `KoTE`, `wordcloud_project`, `wordcloud-project.zip` |
| `wordcloud` | 경로·구조 | `src/routes`, `src/services`, `src/modules`, `src/config`, `src/configs`, `web/templates`, `web/static`, `vendor_python_pkgs`, `_datasets`, `plans_routes`, `plans_kanban` |
| `msys` | 이름 | `msys`, `msys_app`, `msys_venv`, `msys.zip`, `jandi` |
| `msys` | 경로·구조 | `dao/`, `mapper/`, `DDL/`, `my_setting`, `tb_sts_cd_mst`, `tb_col_mapp` |

### 등록 기준

- **실재 확인한 것만** 등록한다. 해당 저장소를 직접 나열·Read 해서 존재하는 폴더·파일·테이블만 넣는다(추측 금지).
- `경로·구조` 에는 그 프로젝트의 계층을 특정하는 토큰만 넣는다. `utils/`·`static/`·`sql/` 같은 단독 일반명은 어느 프로젝트에나 있어 오검출만 만든다.
- 이 표(3열)와 [`../tools/lint_guidelines.py`](../tools/lint_guidelines.py) 는 **한 쌍**이다. 표만 다른 저장소로 복사하면 구 버전 린터가 사전을 못 읽어 격리 검사가 조용히 꺼진다 — 함께 옮긴다.
- **이 파일이 없거나 두 분류(`이름`·`경로·구조`) 중 하나라도 못 읽으면 린터가 `L2` error 로 실패한다**([`core/21-project-isolation.md`](core/21-project-isolation.md) ISO-9). 격리 검사가 무성으로 꺼진 채 "0건"이 나오는 것을 막는 자가진단이다.
- 사고 참조 ID(요구사항 ID·릴리스 버전·커밋 해시)는 값이 매번 달라 사전으로 못 잡는다 → 정규식 검사 `A7`([`core/26-agent-definitions.md`](core/26-agent-definitions.md) AGT-9).

## 등록 절차

[`core/25-project-onboarding.md`](core/25-project-onboarding.md) Step 4 참조.
