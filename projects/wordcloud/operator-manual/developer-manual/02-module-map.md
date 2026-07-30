---
reportTheme: technical
---

# 모듈 지도

↑ [목록으로](00-index.md)

> **핵심**: 엔진(`src/modules`)은 상태를 가진 싱글톤, 서비스(`src/services`)는 도메인 로직·DAO. 감정 판정은 여러 파일에 걸쳐 계층화되어 있다.
> **기준 버전 / 최종 확인일**: v1.1.0 · 2026-07-22

---

## 엔진 계층 (`src/modules/`)

| 파일 | 책임 | 주요 심볼 |
|------|------|----------|
| `kote_shared.py` | 베이스 KoTE(44감정) 모델 싱글톤(스레드 안전). emotion·leadership이 GPU 인스턴스 공유(VRAM 중복로드 방지) | `KoTEModel`(`kote_shared.py:10`) |
| `emotion_analysis.py` | KoTE 추론 래퍼·44감정→3극성 후처리·top3 | `EmotionAnalysis`, `analyze_emotion`(`:297`), `analyze_emotion_batch`(`:323`) |
| `hr_sentiment.py` | HR 도메인 파인튜닝 3분류 극성 모델(별도 싱글톤·안전 폴백) | `predict_sentiments`(`:155`), `predict_proba`(`:173`), `model_status`(`:136`) |
| `sentence_emotion.py` | 문서→문장 분할 후 문장별 KoTE 원시 점수(배치 캐시·그룹 fallback 공유) | `compute_sentence_raw_scores`(`:13`) |
| `text_preprocessing.py` | 문장 분리·**절 분리**(혼합극성 분해) | `split_sentences`(`:27`), `split_clauses`(`:75`) |
| `wordcloud_generator.py` | 워드클라우드 이미지 렌더 | — |
| `nlp_analysis.py` | 형태소·명사 추출(빈도) | `NLPAnalysis` |
| `profanity_filter.py` | 욕설 탐지/필터(한/영) | `advanced_filter_profanity` |
| `leadership_analysis.py` | 리더십 특질 분석(KoTE 공유) | — |
| `sarcasm_analysis.py` | 비꼬임 분석 | — |
| `pseudonym_manager.py` | 가명화/역가명(암호화 매핑) | — |
| `stopword_manager.py` · `word_boost_manager.py` · `hr_context_lexicon.py` | 불용어·가중·도메인 렉시콘 | — |
| `integrated_analysis.py` | 통합(문장 override 질량 기반) 감정·단어 버킷 집계 | — |

> ⚠️ `.bak`/`.py.bak` 파일(`batch_manager.py.bak`, `wordcloud_data_service.py.bak` 등)은 **런타임에 로드되지 않는 잔재**다. 수정 대상으로 착각하지 말 것 — 임포트 경로에 없는 사본이다.

---

## 서비스 계층 (`src/services/`)

| 파일 | 책임 |
|------|------|
| `perspective_service.py` | **감정 판정 규칙 계층의 핵심**(문장/절 override·긍정구제·개선요청 부정화·모델 라벨 override)·단어 점수·감정 집계·corrections 로드([03 문서](03-emotion-engine.md)) |
| `batch_processor.py` | 대규모 배치 실행(청크 수집→병렬 직원 처리→요약)·체크포인트 |
| `batch_service.py` · `batch_manager.py` · `batch_events.py` · `batch_staging.py` | 배치 오케스트레이션·진행 이벤트·staging DB |
| `batch_work_order_service.py` | 배치 **작업서**(설정 스냅샷+진행) 영구화·Resume 지원 |
| `deploy_session_service.py` | SQLite 스키마 정의·마이그레이션·연결 헬퍼(**DAO 허브**)·부팅 마이그레이션 |
| `judgment_packet_service.py` | 감정 판정 작업 패킷(추출→AI판정→삽입, 가명 in-place) |
| `gallery_db_service.py` | 배포 갤러리(`gallery_entries`) |
| `wordcloud_data_service.py` · `wordcloud_service.py` | 워드클라우드용 데이터 조회·생성 |
| `integrated_data_service.py` | 수집 대시보드 데이터 |
| `profanity_db_service.py` | 욕설 집계 저장/조회 |
| `acquired_handoff.py` | 취득 문장(`acquired_sentences`) 핸드오프(데이터셋 연결) |
| `version_service.py` | `VERSION.json` 읽기·무결성 대조 |
| `perspective_service.py`(재게시) · `user_data_manager.py` | 직원/평가 데이터 접근 |
| `progress_time.py` | 진행률·경과시간 표시 |

---
---pb---

## 상호관계 (호출 그래프 요약)

```
routes/perspective_routes.py
   └─> services/perspective_service.py
          ├─> modules/sentence_emotion.compute_sentence_raw_scores
          │        └─> modules/emotion_analysis.analyze_emotion_batch
          │                 └─> modules/kote_shared.KoTEModel (싱글톤)
          ├─> modules/hr_sentiment.predict_sentiments (플래그 on 시)
          ├─> modules/text_preprocessing.split_sentences / split_clauses
          └─> services/deploy_session_service._get_conn  (corrections 로드)

routes/batch_routes.py
   └─> services/batch_processor.process_batch
          ├─> services/batch_staging (원문 적재 staging.db)
          ├─> services/batch_work_order_service (작업서·완료직원 items)
          ├─> models/integrated_data_manager
          └─> modules/nlp_analysis, profanity_filter, wordcloud_generator

web/app.py (부팅)
   └─> services/deploy_session_service._auto_migrate_evaluations
```

- **KoTE 단일 로드 원칙**: `emotion_analysis`와 `leadership_analysis`는 `KoTEModel` 싱글톤을 공유한다(`emotion_analysis.py:53-59`, `kote_shared.py:10-28`). 새 분석 모듈을 추가할 때 KoTE를 재로드하면 VRAM 한도를 초과할 수 있으니 반드시 이 싱글톤을 재사용하라.
- **HR 감정모델은 별도 싱글톤**(`hr_sentiment.py:36-37, 117-133`)이며 KoTE와 독립이다. 로드/추론 실패 시 `None`을 반환해 호출부가 규칙으로 폴백한다(무중단 설계).
- **DAO 단일 진입**: 모든 SQLite 접근은 `deploy_session_service._get_conn()`을 거친다. 새 테이블은 `_init_db()`의 DDL과 `_apply_schema_migrations()`의 버전 분기에 추가한다([04 문서](04-data-layer.md)).

---

## 서비스 vs 엔진 구분 원칙 (수정 시 판단 기준)

- **엔진(`src/modules`)에 두는 것**: 모델 추론, 형태소/문장/절 분리, 이미지 렌더 등 **도메인 무관 재사용 연산**.
- **서비스(`src/services`)에 두는 것**: "인사평가 감정은 이렇게 판정한다" 같은 **도메인 규칙**, DB 접근, 배치 오케스트레이션.
- 감정 **규칙**(긍정구제·개선요청 부정화 등)이 `perspective_service.py`에 있는 이유가 이것이다 — 모델 자체가 아니라 그 위에 얹는 도메인 판정이기 때문. 규칙 변경은 [03 문서](03-emotion-engine.md)의 안전 원칙을 반드시 따를 것.

---
↑ [목록으로](00-index.md) · [← 이전: 01. 아키텍처](01-architecture.md) · [다음: 03. 감정분석 엔진 →](03-emotion-engine.md)
