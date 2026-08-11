---
reportTheme: technical
---

# 감정분석 엔진

↑ [목록으로](00-index.md)

> **핵심**: 문장/절 단위 KoTE 원시점수 → HR 파인튜닝 모델(선택) → **도메인 규칙 계층 override** → 사람 보정(corrections)의 4단 파이프라인. 규칙은 모두 `perspective_service.py`에 있고, 최우선 불변식은 **긍↔부 오분류 0**이다.
> **기준 버전 / 최종 확인일**: v1.1.0 · 2026-07-22 (commit `7b106b5`)
> **규칙 상세 정본**: [`project_wordcloud/modules/emotion-analysis.md`](../../modules/emotion-analysis.md)

---

## 두 개의 모델 (역할 분리)

| 모델 | 파일 | 역할 | 로드/폴백 |
|------|------|------|-----------|
| 베이스 KoTE(44감정) | `src/modules/kote_shared.py:10` `KoTEModel` | 문장별 44감정 확률 → 긍/부/중 원시 점수 | 스레드 안전 싱글톤. emotion·leadership이 **동일 GPU 인스턴스 공유**(VRAM 중복로드 방지) |
| HR 도메인 3분류 극성 | `src/modules/hr_sentiment.py:49` `_HRSentimentModel` | positive/negative/neutral **극성만** 결정(인사평가 파인튜닝) | 별도 지연로드 싱글톤. 디렉터리 부재·로드/추론 실패 시 **`None` 반환 → 규칙 폴백**(무중단) |

- HR 모델 라벨 순서: `0=positive, 1=negative, 2=neutral`(`hr_sentiment.py:19` `_ID2LABEL`).
- **필드 프리픽스 규약**(train/serve 정합): 장점/단점 필드가 있으면 입력을 `f'{field} 평가: {text}'`로 변환해 추론한다(`hr_sentiment.py:68-76` `_prefixed`). 재추론 대조 시 이 프리픽스를 빠뜨리면 오진한다.
- 캘리브레이션: 모델 디렉터리의 `calibration.json` temperature로 확률 눈금만 보정(`hr_sentiment.py:22-34`). **argmax 라벨은 T와 무관** — `predict_proba`의 confidence는 escalation 라우팅에만 쓴다.
- on/off 스위치: `USE_HR_SENTIMENT_MODEL`(기본 on, `src/config/settings.py:27`). 모델 실측 지문(sha256·loaded_at)은 `model_status()`(`hr_sentiment.py:136`)로 조회한다.

> **모델 파일 위치**: `settings.py:20,26` 기준 `D:\dev\wordcloud\model\`(= `wordcloud_project`의 형제 폴더). 배포 시 `-Package` 모드가 이 `model/`을 동봉한다([05 문서](05-build-deploy.md)).

---

## 문장·절 분리 (전처리)

`src/modules/text_preprocessing.py` — 무거운 의존이 없는 경량 모듈.

- `split_sentences(text)`(`:27`): `.!?\n`로 분할 + 인사말·5자 미만·깨진 HTML 엔티티(`&#NNNN;`)·자모 난타 노이즈 제외. **production 집계·갤러리가 쓰는 정본**.
- `split_clauses(sentence)`(`:75`): 역접·양보 연결어미(`으나/지만/는데/…`)·대조 접속부사(`그러나/반면/…`) 경계에서 절 분리. **혼합극성 문장**("좋으나 낮음")을 단일극성 절로 쪼갠다.
  - ⚠️ **데이터셋 빌드 전용**이다(주석 `:55-58`). production `split_sentences`는 건드리지 않는다(집계 영향 격리).
  - 부정 범위 보존: 연결어미는 완결 용언 뒤에 오므로 `않/없/안`을 절 중간에서 끊지 않는다("강압적이지 않으나"는 한 절 유지).
  - 표지 없으면 `[sentence]` 그대로 반환(안전한 기본값), 과분할은 4자 미만 조각 흡수(`_CLAUSE_MIN_LEN`).

---
---pb---

## 규칙 계층 (`perspective_service.py` — 엔진 위에 얹는 도메인 판정)

문장 override의 **단일 정의**는 `_sentence_sentiment_override_explain(pos, neg, sentence, …)`(`:1221`)이며, `sentence_sentiment_override`(`:1408`)는 이를 호출해 점수만 반환한다. **분기 조건·반환 점수는 두 함수가 완전히 동일해야 한다**(동작 보존 계약, `:1226`).

분기 **순서**가 곧 우선순위다(0702_03 reorder 반영). 대표 분기:

| 순서 | 분기(rule_id) | 방향 | 핵심 검출기 |
|------|--------------|------|-------------|
| 1 | 개인안녕/건강 조언 → 중립 | →중립 | `is_personal_wellbeing_neutral`(`:984`), `is_health_advice`(`:943`) |
| 2 | 광의 혼합 긍부 → 중립 | →중립 | `is_mixed_pos_neg`(`:1030`) (0715 사용자 카테고리3) |
| 3 | 무결점/무응답/약점-못찾음 선언 → 중립 | →중립 | `is_no_weakness_declaration`(`:857`), `is_no_response`(`:432`) |
| 4 | 긍정 구제(positive_rescue) | →긍정 | `has_positive_implying_phrase`(`:451`) + `has_improvement_request`(`:721`) 등 게이트 |
| 5 | 개선요청/결핍 프레이밍 → 부정 | →부정 | `_has_improvement_request_core`(`:667`), `has_constructive_need`(`:607`), `_is_speculative_need`(`:1071`), `_has_request_marker`(`:1129`) |

- **개선요청 화행 = 부정**(사용자 재정, [[feedback_improvement_request_is_negative_gold]]): "~할 필요/키워야"는 중립이 아니라 부정으로 확정. 단 명확한 긍정 절이 선행하는 혼합("뛰어나나 개선 필요")은 →중립(`improvement_request_neutral`, `:1362`).
- **긍↔부 안전 방향**: 규칙이 바꾸는 방향은 항상 →중립 또는 한 방향뿐이며, 긍정↔부정을 직접 뒤집는 분기는 두지 않는다. 다의·조사 트랩(`이나` 나열=or vs 양보) 때문에 대조어 게이트가 세분돼 있다(`_has_improve_blocking_contrast`, `:165`).

### 모델 라벨 override (파인튜닝 켜졌을 때)

`apply_model_label_override(model_label, sentence, field=None)`(`:1436`, 13_03 Track2)는 모델 출력 위에 얹는 **좁은 고정밀** 교정이다.

- 허용: 모델이 명백 긍정을 부정으로 본 것 등을 **부→긍은 하지 않는다** — 그건 override로 안전 교정 불가라 **재학습(Track1) 몫**(`:1452`).
- 필드신호 override(무서술어 단편→필드극성)는 **폐기**됨: 모델이 필드 프리픽스로 이미 내장(`:1448`). [[project_override_bypass_is_correct]] 참조.

> ⚠️ **규칙 수정 절대 원칙**: 어떤 분기를 추가·변경하든 **장점/단점 코퍼스 양쪽 적대셋**으로 긍↔부 0을 검증하고(한쪽만 보면 거짓 자신감), 그룹 단위 일치율로 감사한다. 문장 두더지잡기 금지.

---

## 사람 보정 (corrections) — 최종 권위

- 저장 위치: `evaluations.sentiment_corrections` 컬럼(TEXT JSON, 스키마 v4에서 추가 — [04 문서](04-data-layer.md)).
- 로드: `load_...corrections`가 `SELECT id, sentiment_corrections FROM evaluations WHERE employee_id=?`로 읽는다(`:2165-2172`).
- **키잉 = `_db_id`**: `evaluation_id`는 **중복될 수 있으므로** 보정값 키로 쓰지 않는다. 고유한 DB row `id`를 `ev_obj['_db_id']`에 실어(`:1766, 1879, 1947`) `corrections_map.get(ev.get('_db_id'))`로 조회한다(`:2293, 2471`). [[project_eval_id_not_unique]]
- 우선순위: corrections가 있으면 규칙·모델 출력을 덮어쓴다(사람 라벨이 정본).

---
↑ [목록으로](00-index.md) · [← 이전: 02. 모듈 지도](02-module-map.md) · [다음: 04. 데이터 계층 →](04-data-layer.md)
