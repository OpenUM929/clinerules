---
reportTheme: technical
---

# 파인튜닝 데이터 파이프라인

↑ [목록으로](00-index.md)

> **핵심**: 감정/리더십 작업·데이터 도착 시 `hr-kote-finetune` 데이터셋을 **append-only**로 누적하고(상시 RUNBOOK 절차), 사람 검증 gold를 승격해 재학습한다. 최우선 가치는 **긍↔부 오분류 방지**다. 이 폴더(`plans/`)는 배포 제외 — 학습 데이터는 여기서만 다룬다.
> **기준 버전 / 최종 확인일**: v1.1.0 · 2026-07-22 (commit `7b106b5`)
> **상시 절차 정본**: `plans/_datasets/kote_finetune/RUNBOOK.md` (완료 개념 없는 상시 문서)

---

## 데이터셋 레이아웃 (`wordcloud_project/plans/_datasets/kote_finetune/`)

| 경로 | 내용 |
|------|------|
| `emotion/emotion.jsonl` | 감정어 스트림(append-only, 라인당 1 JSON) |
| `leadership/leadership.jsonl` | 리더십 스트림(append-only) |
| `RUNBOOK.md` | 상시 절차 + 누적 로그(단일 진입점) |
| `README.md` | 폴더 규약 · **문서 지도** |
| `AUDIT_STANDARD.md` | 실배치 감사 재현 절차·시드·스크립트 |
| `ROADMAP.md` · `MODELING_LEVERS_PLAN.md` | 상시 현황·로드맵 |
| `scripts/` | `promote_gold.py`, `finetune_sentiment.py`, `ensemble_eval_r8_260708.py` 등 |

- **누적 방식**: append-only(기존 행 수정·삭제 금지, 정정은 동일 `id` 신규 리비전). [[project_kote_dataset_runbook]]
- **문서 배치 규약**: 상시 현황·로드맵은 `plans` 금지, `_datasets/kote_finetune`에 둔다(일회성 설계만 `plans/2026/…`). 헷갈리면 `README.md §문서 지도`부터 본다. [[project_dataset_doc_placement]] · [[project_dataset_doc_map]]

### export(`weak_export_*.jsonl`) 스키마 — 필드 보존 여부

`acquired_handoff.py`가 문장 단위로 방출하는 라인 형식이다.

```python
line = {"x": sent, "y": label, "s": [pos, neg, neu], "e": top3}
if field:                       # :98 — field 신호는 파인튜닝 핵심 피처
    line["f"] = str(field)
```

- 🔴 **`f` 키는 2026-07-14에 추가됐다**(`:88` 주석, 구 튜플 호환). **그 이전 export 에는 `f` 가 없고**, 그렇다고 필드 정보가 소실된 것은 아니다 — 배치 분리 방식에 따라 `id` 접두사나 배치 ID에 남아 있다.
- ⚠️ **코드에 있다고 데이터에 있는 것이 아니다.** 2026-07-28 시점 `_datasets/kote_finetune/emotion/` 의 jsonl **12종을 전수 스캔한 결과 `f` 기록 행이 0건**이었다(2023뿐 아니라 2024·2025도). 키가 실제로 채워진 첫 산출물은 **2026-07-29 2023년 칸별 재추출본**(`data/23년 장점.csv`·`23년 단점.csv`, `batch_20260729_0/1`)이다. `f` 를 근거로 삼기 전 **그 파일에서 직접 세어 확인**하라.
- **`f` 를 남기는 조건**은 매핑 UI에서 `evaluation_document_strength`·`evaluation_document_weakness` 를 **각각 매핑**한 것이다(`batch_processor.py:236` `if mappings.get(f)`). 한쪽만/합쳐 매핑하면 `f` 는 비고, 그 배치 산출물에서는 칸을 복원할 수 없다.
- **`f` 가 0건이라는 관측만으로 "필드가 없다"고 결론내지 말 것.** 소재 4곳 전체 확인이 필수다 → [06. 배치 처리 §필드 소재 지도](06-batch.md) · [[project_field_lost_in_260714_rebatch]]
- `data/*.csv`(`x/y/s/e`)는 **배치 출력물**이지 원천 입력이 아니다. 첫 줄 헤더의 `batch` 키가 생산 배치 ID다. 인용 전 입출력 방향을 확정한다.

---

## 트리거 (RUNBOOK §1)

다음 중 하나면 RUNBOOK §2 체크리스트 수행:
- 감정어/리더십 **분석·알고리즘 강화** 작업(검토 1회 = gold 확정 1회로 겸함).
- 취득 코퍼스 **CSV 도착**(`data/*.csv` 반입).
- `acquired_sentences`에 **신규 행 적재**(핸드오프: `acquired_handoff.py`).

> ⚠️ **범위 임의 축소 금지**: 과거 범위를 "규칙 트랙 한정"으로 줄여 데이터셋 빌드를 생략한 사고(입력 36만, 기록 0)가 있었다. RUNBOOK §2-0은 1~6단계를 **한 명령**으로 묶어 재량 개입을 차단한다. [[feedback_execute_plan_no_descope]]

---
---pb---

## 라벨링 원칙 (긍↔부 안전)

- **개선요청 화행 = 부정**("~할 필요/키워야", 사용자 재정). 양가 성향 서술만 중립. [[feedback_improvement_request_is_negative_gold]]
- 무종결 단편·긍부 혼재·극성 불명확 → **중립**. 요청 표지 → 부정. 명확한 행위 서술만 → 긍정. [[feedback_incomplete_fragment_neutral]]
- 양가 업무태도(꼼꼼·철저·객관·소신)는 **기업 관점 긍정**, 명시 해악표지(고압적/편향/기복)가 붙을 때만 부정. 사생활·성격은 중립. [[feedback_ambiguous_trait_employer_lens]]
- 판정은 **블라인드 선판정 → 모델과 대조 → 불일치/저확신만 escalation**, 일치는 silver. 큐에 gold(원본 라벨)를 담지 말 것(미판정 큐가 숨는 버그). [[feedback_prefill_judgment_escalate_uncertain]] · [[project_group_review_gold_conflation]]
- 사전 라벨(코퍼스 y/s/e = KoTE 출력)은 정답이 아니다 → 문장 직접 재판정. [[feedback_distrust_prelabels_reanalyze]]

---

## gold 승격 · 재학습

| 스크립트 | 용도 | 주의 |
|----------|------|------|
| `scripts/promote_gold.py` | 검증된 사람 라벨을 정식 gold 스트림에 적립 | positive gold 826 적립 완료(2026-06-30, D5). [[project_gold_promotion_d5]] |
| `scripts/finetune_sentiment.py` | 파인튜닝(**seed42, 개발용**) | A/B 무효 기준 — 배포 비교에 쓰지 말 것 |
| `scripts/ensemble_eval_r8_260708.py` | 재학습·평가(**배포 정본 경로**) | `--save-seed 45`가 배포 기준선 |

> 🔴 **재학습 정본 = `ensemble_eval_r8 … --save-seed 45`**. `finetune_sentiment.py`(seed42)는 개발용이라 배포 A/B에 무효다. [[project_retrain_path_seed45]]

- **다음 이득 지점**: 쉬운 silver 증강은 정확도를 오히려 떨어뜨린다(천장). 하드샘플 능동학습·사람분 승격(현재 stranded 라벨 다수 미반영)이 다음 수. [[project_finetune_data_ceiling]] · [[project_training_promotion_gap]]
- **진짜 어려운 클래스는 중립**(긍↔부 아님): 모델은 중립→긍, 규칙은 중립→부로 파괴하므로 사람 라벨이 정본. [[project_neutral_is_the_hard_class]]
- 신규 그룹은 정서가 아니라 **화행**(개선요청·평가회피·역량서술), 기본 극성 neutral. [[project_finetune_groups_are_speechacts]]

> **데이터셋 작업 위임**: 이 파이프라인의 실행자는 `dataset-curator` 에이전트이며, RUNBOOK §0의 "핵심 엔지니어" 역할(가드레일 내장)로 일한다. [[feedback_dataset_core_engineer_role]]

---
↑ [목록으로](00-index.md) · [← 이전: 06. 배치 처리](06-batch.md) · [다음: 08. 개발 환경·테스트·트러블슈팅 →](08-dev-setup-troubleshooting.md)
