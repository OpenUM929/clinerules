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

## 장시간 작업 중 UI 처리

배치처럼 오래 걸리는 작업 중에는 **전면 블러 오버레이 금지**. Nav·버튼만 비활성화하고 진행 상황(진행률·경과시간, `progress_time.py`)은 계속 보이게 한다. [[feedback_busy_disable_not_block]]

---
↑ [목록으로](00-index.md) · [← 이전: 05. 빌드·배포](05-build-deploy.md) · [다음: 07. 파인튜닝 데이터 파이프라인 →](07-finetune-pipeline.md)
