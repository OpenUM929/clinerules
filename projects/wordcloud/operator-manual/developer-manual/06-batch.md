---
reportTheme: technical
---

# 배치 처리

↑ [목록으로](00-index.md)

> **핵심**: 약 **1.9만명** 규모의 대량 처리를 청크 수집 → 직원별 처리 → 요약으로 수행하고, 진행 상황을 **작업서(Work Order)** 로 DB에 영구화해 중단 시 Resume한다. 추적 로직은 **O(n) 이하**(O(n²) 금지)를 지킨다.
> **기준 버전 / 최종 확인일**: v1.1.0 · 2026-07-22 (commit `7b106b5`)

---

## 구성 요소

| 파일 | 책임 |
|------|------|
| `src/services/batch_processor.py` | 대규모 배치 실행 오케스트레이션(청크 수집→직원 처리→요약)·체크포인트 |
| `src/services/batch_work_order_service.py` | 작업서(설정 스냅샷 + 진행) 영구화·Resume 지원 |
| `batch_service.py` · `batch_manager.py` · `batch_events.py` · `batch_staging.py` | 오케스트레이션·진행 이벤트·staging DB |
| `src/routes/batch_routes.py` | `/api/batch` 실행·진행·Resume API |

- 규모 제약: 배치 대상 약 1.9만명. 추적 자료구조는 선형 이하로 유지한다. [[project_batch_scale_19k]]
- **dev 환경은 배치 실행 불가**(원데이터 내부 전용), dev에는 CSV만 반입한다. [[project_dev_no_batch_csv_only]]

---

## 작업서(Work Order) 생명주기

`batch_work_order_service.py`가 관리하는 상태 전이:

```
create_work_order        → status='running'   (설정 스냅샷 저장, items 초기화)   :30
update_work_order_progress→ 헤더 카운트 갱신(진행/성공/실패/행수)                :70
add_completed_employees  → 완료 직원 items append (INSERT OR IGNORE, O(델타))    :92
complete_work_order      → status='completed'                                    :123
fail_work_order          → status='failed' (전체 중단 시만; 직원 단위 오류 아님) :139
```

- **완료 직원 목록은 별도 items 테이블**(`batch_work_order_items`, PK=(batch_id, employee_id))에 1직원 1행으로 append한다. JSON 배열 통째 재기록을 피해 수만 명에서도 **O(델타)**를 보장한다(`:92-107`).
- Resume 대상 조회: `get_latest_incomplete_work_order()`(`:180`)는 `status IN ('interrupted','failed')`만 반환한다. `running`은 서버가 살아 처리 중이므로 제외한다.
- Resume skip 대상: `get_completed_employee_ids(batch_id)`(`:110`)로 이미 완료한 직원을 건너뛴다.

---
---pb---

## 배치 이력 표시 규약

- 배치 이력은 **배치 작업서(batch_id) 기준**으로 출력한다. 평가 중복제거로 실제 반영 건수가 0이어도 작업서 자체는 이력에 표시한다(작업이 있었음을 숨기지 않음). [[project_batch_history_by_workorder]]
- 게시판 목록: `get_all_work_orders(limit)`(`:166`) — `created_at DESC, id DESC` 최신순.

---

## 필드 무관 처리 주의

실데이터 감사에서 **필드(장점/단점) 무관 배치** 산출이 발견됐다([[project_prod25_audit]]). 감정 판정은 필드 프리픽스에 강하게 의존하므로([03 문서](03-emotion-engine.md) §1), 배치가 필드를 올바로 전달하는지가 정확도의 핵심이다. 재추론·대조 시 필드 프리픽스를 반드시 포함한다. [[project_batch_260709_model_gap]]

---
---pb---

## 🔴 필드(장점/단점) 소재 지도 — 산출물에서 필드를 찾는 법

> 2026-07-27~28, 산출물 1개에 필드 키가 없다는 이유로 **"자료에 필드가 없다"고 3회 오판**했다. 필드는 아래 4곳 중 어딘가에 있고, 어디에 있는지는 **배치 실행 시점과 반입 방식**이 결정한다. 부재를 단정하기 전에 4곳을 모두 본다. → [`17-hallucination-prevention/09-data-absence.md`](../../../../common/core/17-hallucination-prevention/09-data-absence.md)

### 발생 지점 (원천)

`batch_processor.py:216` 이 극성 문서 컬럼을 정의하고, `_extract_rows_from_chunk`(`:229`)이 **컬럼별로 별도 evaluation 레코드를 방출**하면서 필드를 부착한다.

```python
POLARITY_DOCUMENT_FIELDS = {                       # :216
    'evaluation_document_strength': '장점',
    'evaluation_document_weakness': '단점',
}
...
ev['evaluation_document_field'] = polarity          # :291  (0707_01 Phase2)
```

- 즉 **1직원 → 장점 레코드 1건 + 단점 레코드 1건**. 매핑된 컬럼이 비면 그 레코드는 방출되지 않는다.

### 보존 경로 4곳

| # | 경로 | 형태 | 유효 조건 |
|---|------|------|-----------|
| ① | 원본 DB `evaluations.evaluation_document_field` | `장점`/`단점` 문자열 | **0707_01 이후** 실행 배치. 정본 |
| ② | export 의 `f` 키 | `{"x":…, "f":"장점"}` | `acquired_handoff.py:98` — **0714 추가**. 그 이전 export 에는 없음 |
| ③ | 레코드 `id` 접두사 | `batch_…_1-` = 장점 / `batch_…_0-` = 단점 | 장점·단점을 **별도 배치로 실행**했을 때 |
| ④ | 배치 ID ↔ 반입 파일명 대응 | RUNBOOK 반입 로그의 파일명 | 파일을 나눠 반입해 배치가 여러 개로 쪼개졌을 때 |

### 실측 대응표 (로컬 보유 export)

| export | 연도 | 필드 소재 | 문장 수 |
|---|---|---|---|
| `weak_export_260623.jsonl` | 2025 | ④ 배치 5개 ↔ `default/장점_2·3차`, `단점_1·2·3차` | 739,918 |
| `weak_export_260624.jsonl` | 2024 | ③ `_1-`=장점 443,637 / `_0-`=단점 426,730 | 870,367 |
| `weak_export_260708.jsonl` | 2024 재실행 | 단일 배치(`batch_20260708_0`) — **필드 없음** | 886,985 |
| `weak_export_260714.jsonl` | 2023+2024+2025 통합 | 연도별 단일 배치 — **필드 없음** | 2,705,461 |
| `data/23·24·25.csv` | 각 연도 | 배치 **출력물**(헤더 `batch` 키가 생산 배치 ID). 키는 `x/y/s/e` 뿐 — **필드 없음** | 1,025,634 / 868,889 / 758,880 |
| `data/23년 장점.csv` · `23년 단점.csv` | 2023 | ② `f` 키 **실기록 최초 사례**(`batch_20260729_0`=장점 / `_1`=단점) | 521,817 / 503,817 (합 1,025,634) |

### 2023년 — 칸별 재추출로 복원 완료 (2026-07-29)

2023년(`batch_20260713_0`)은 장점·단점을 **한 배치로 합쳐** 실행해 그 산출물에는 ①~④ 어디에도 필드가 없었다. **해소 방법은 원본 DB에서 칸을 나눠 재추출하는 것 하나뿐**이며, 2026-07-29 실제로 그렇게 재추출해 `f` 키가 실린 확정본을 얻었다(위 표 마지막 행). 합본 `23.csv`와 **행수·문장집합 100% 일치**를 검증했다(장점 521,817 + 단점 503,817 = 1,025,634).

> 🔴 **함께 확정된 사실 — 2023년 본배치는 필드 프리픽스를 적용해 판정했다.** `data/23.csv` 의 `y` 가 재추출본에 `f"{field} 평가: {text}"` 를 적용해 재추론한 결과와 **769,406문장 100.0000% 일치**(칸별 불일치 0). 즉 **판정에는 필드가 쓰였고 export 에만 안 실렸다.** 24·25 산출물의 분포(칭찬 56.38%/56.58%)도 프리픽스 적용 조건과 맞고 미적용 재추론(51.94%/52.50%)과는 4%p 이상 어긋난다.
> → **"export 에 `f` 가 없다" 를 "그 배치가 필드 없이 돌았다" 로 읽지 말 것.** 산출물 분포로 조건을 역검정할 수 있다. 검정 스크립트: `…/27_03_completion-report/result/verify_2023_prefix_regime_260729.py`

> ⚠️ 아래 가설들은 **합본 산출물만 가지고 필드를 복원하려는 시도**로, 전수 검정으로 모두 기각됐다. 같은 상황을 다시 만나면 이 가설들을 재시도하지 말고 **곧바로 칸별 재추출**을 요청하라.

| 가설 | 검정 결과 |
|------|-----------|
| export `f` 키 | 2023년분 **0건** (당시 보유 export 12종 전부 0건 — 코드에는 있으나 실사용 이력 없음) |
| 레코드 순번 홀짝 | `applied_rule` 별 홀수 비중 **49.3~52.2%** — 교대 아님 (앞 8행이 교대로 보인 것은 우연) |
| 원본 `db_id` 홀짝 | 짝수 단점 75,367 / 홀수 74,969 — **50:50** |
| 판정 패킷으로 대체 | 패킷은 **저마진 하드 16.5%** 편향 표본(171,872건). 전수 대표성 없음 |

**(이력) 재추출 전에 쓴 대체 수단**: 2024·2025년 161만 문장(필드 확정본)을 사전으로 삼아 **동일 문장의 필드를 이관**했다(순도 95% 이상 쏠릴 때만 확정). 커버리지 27.95%(286,062건)에 **반복 상용구 편향**이 있어, 같은 절차를 2024·2025년에 재현해 실측한 편향계수(1.96·1.90배)로 보정해 추정치를 냈다.
→ 스크립트 `…/27_03_completion-report/result/measure_field_census_2023_260728.py` · `measure_transfer_bias_260728.py`

**정본(전수 확정)**: 위 재추출본 기준 → `…/27_03_completion-report/result/measure_field_census_2023_full_260729.py`. 재배치·재학습은 불필요했고, **DB 재추출만으로 해소**됐다.

---

## 장시간 작업 중 UI 처리

배치처럼 오래 걸리는 작업 중에는 **전면 블러 오버레이 금지**. Nav·버튼만 비활성화하고 진행 상황(진행률·경과시간, `progress_time.py`)은 계속 보이게 한다. [[feedback_busy_disable_not_block]]

---
↑ [목록으로](00-index.md) · [← 이전: 05. 빌드·배포](05-build-deploy.md) · [다음: 07. 파인튜닝 데이터 파이프라인 →](07-finetune-pipeline.md)
