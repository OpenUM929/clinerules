# tools — 지침 집행 도구

## dlp_guard.ps1

사내 보안 프로그램이 확장자 단위로 추적 파일을 일괄 삭제하는 사고(2026-08-20, wordcloud 프로젝트에서 최초 확인)에 대한 점검·복원 도구. `.clinerules` 를 서브모듈로 쓰는 모든 프로젝트가 공용으로 쓴다 — 프로젝트 이름을 하드코딩하지 않으며, 항상 실행 시점의 저장소 루트(`.clinerules` 의 부모 폴더) 를 기준으로 동작한다.

```bash
powershell -NoProfile -File .clinerules/tools/dlp_guard.ps1              # 점검
powershell -NoProfile -File .clinerules/tools/dlp_guard.ps1 -Restore     # 삭제분만 HEAD 에서 복원
powershell -NoProfile -File .clinerules/tools/dlp_guard.ps1 -Snapshot    # git 이 못 지키는 자산 백업(.dlpbak)
```

**자동 점검 적용(권장)**: `.clinerules/.claude/settings.json` 을 프로젝트 루트 `.claude/settings.json` 에 그대로 복사하면 SessionStart 훅으로 매 세션 시작 시 자동 점검된다(평시 무출력, 삭제 발견시에만 경고).

**프로젝트별 커스터마이즈**: 이 스크립트 자체는 수정하지 않는다. 저장소 루트에 `.dlp_guard.json` 을 두면 감시 확장자(`targetExt`)·제외 경로(`excludePrefix`)를 프로젝트별로 덮어쓸 수 있다(스크립트 상단 주석 참조).

## lint_guidelines.py

지침 저장소가 규칙을 실제로 지키는지 검사한다. 규칙 문서(`common/core/19`~`26`)의 조항과 검사 ID 가 1:1 대응한다. 검사 대상은 지침 저장소(`.clinerules/`)와 저장소 루트의 에이전트 정의(`.claude/agents/*.md`)다.

```bash
python .clinerules/tools/lint_guidelines.py                  # 전체
python .clinerules/tools/lint_guidelines.py --severity error # error 만
python .clinerules/tools/lint_guidelines.py --json           # 기계 판독용
python .clinerules/tools/lint_guidelines.py --baseline .clinerules/tools/lint_baseline.txt
python .clinerules/tools/lint_guidelines.py --write-baseline .clinerules/tools/lint_baseline.txt
```

종료 코드: error 1건 이상 → `1`, 없으면 `0`.

### 검사 항목

| ID | 검사 | 규칙 문서 |
|----|------|-----------|
| `P1` | `project.json` 존재·파싱·`project_id` 형식 | 19-project-identity |
| `P2` | `guideline.project_dir` == `projects/<project_id>` | 19 / 20 |
| `P3` | `paths.*`·`entrypoint` 실존 | 19 |
| `P4` | 플레이스홀더가 스키마 정의 키만 사용 | 19 §3 |
| `L1` | `common/` 이 구체 프로젝트 경로 참조 | 21 ISO-1 |
| `L2` | `common/` 에 등록 프로젝트 고유어 · **금칙어 사전 자가진단**(파일 부재·분류 미로드) | 21 ISO-2 / ISO-9 |
| `L3` | 프로젝트 간 상호 참조 | 21 ISO-3 |
| `L4` | `projects/` 직하가 자기 프로젝트 1개 | 21 ISO-4 |
| `L5` | 구역 폴더 존재·미정의 최상위 폴더 없음 | 20 §1 |
| `L6` | `common/` 에 프로젝트 구조 토큰(폴더 계층·파일 경로·테이블명) (타 프로젝트 error / 자기 warn) | 21 ISO-7 |
| `N1` | 폴더별 번호 중복 | 22 NUM-7 |
| `N2` | 번호 필수 구역의 무번호 파일 | 22 NUM-3 |
| `N3` | 파일 시스템 ↔ `NUMBERS.md` 대사 | 22 NUM-5 |
| `N4` | 파일명 형식·slug 길이 | 22 NUM-1 |
| `N5` | 나침반 파일명 == 하위 폴더명 | 22 NUM-2 |
| `C1` | 나침반 60줄 초과 | 23 CMP-2 |
| `C2` | 상세 문서 160줄 초과(80줄 경고) | 23 CMP-2 |
| `C3` | 나침반 금지 콘텐츠 | 23 CMP-3 |
| `C4` | 나침반 배지 누락 | 23 CMP-1 |
| `C5` | 하위 폴더 보유 나침반의 라우팅 표 | 23 CMP-4 |
| `K1` | 링크 실존 | 23 CMP-5 |
| `K2` | 이미지 실존 | 00-core/04-reference-verification |
| `A1` | 에이전트 정의 프론트매터·필수 키 | 26 AGT-3 |
| `A2` | `name` == 파일명, 저장소 내 유일 | 26 AGT-4 |
| `A3` | 정의 본문의 타 프로젝트 고유어 | 26 AGT-2 |
| `A4` | 정의 본문의 자기 프로젝트 고유값 하드코딩 | 26 AGT-1 |
| `A5` | 정의가 참조한 지침 경로 실존 | 26 AGT-5 |
| `A6` | 정의 본문의 구조 토큰 (타 프로젝트 error / 자기 warn) | 26 AGT-8 |
| `A7` | 정의 본문의 프로젝트 귀속 식별자(요구사항 ID·버전·커밋 해시) | 26 AGT-9 |

`A*` 는 `.claude/agents/*.md` 만 검사하며, 폴더가 없으면 건너뛴다. 카탈로그 `README.md` 는 정의가 아니므로 `A1`·`A2` 대상에서 제외한다.

`L2`·`A3`·`A4` 는 [`common/PROJECTS-REGISTRY.md`](../common/PROJECTS-REGISTRY.md) 의 `이름` 분류를, `L6`·`A6` 은 `경로·구조` 분류를 사전으로 쓴다. `경로·구조` 는 앞 단어 경계로 매칭하고(`statistics_dao/` 는 `dao/` 로 치지 않는다), 슬래시 뒤에 대문자가 오는 개념 나열(`DDL/SQL`)은 경로로 보지 않는다. `A7` 은 사전이 아니라 형식(정규식)으로 판정한다. **사전이 없거나 두 분류 중 하나라도 비면 `L2` error 로 실패한다** — 격리 검사가 무성으로 꺼진 채 "0건"이 나오는 것을 막는 자가진단이다(21 ISO-9).

`outputs/` 는 산출물 구역이라 검사 대상에서 제외한다. 코드 블록(``` ``` ```) 안은 예시이므로 링크·형식 검사에서 제외한다.

### baseline

기존 위반을 한 번에 없앨 수 없을 때 `--baseline` 으로 현재 위반을 등록해 두고 **새로 생긴 위반만** 실패로 처리한다. baseline 은 줄여 나가되 늘리지 않는다.

### 언제 실행하는가

- 지침 문서를 수정한 직후 (`common/core/03-workflow/05-post-guideline-change.md` 필수 단계)
- 문서 이동·rename 전후 (before/after 비교로 신규 파손만 판정)
- 새 프로젝트 온보딩 완료 시 (`common/core/25-project-onboarding.md` Step 6)
