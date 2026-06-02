# 프로젝트 시나리오 테스트 (Project Scenarios - msys)

**문서 위치**: `.clinerules/docs/project_wordcloud/scenario-test_project.md`

> ⚠️ 이 문서는 project_wordcloud 기준입니다. msys 시나리오는 `.clinerules/docs/msys/` 문서를 참조하세요.

---

## 시나리오 P-1: 분석 페이지 워드클라우드 옵션 누락

### 상황
사용자: "분석 페이지에서 워드클라우드 설정 옵션이 없어"

### 참조 문서

| 순서 | 문서 | 확인 내용 |
|------|------|----------|
| 1 | routes/api-routes.md | 엔드포인트 확인 |
| 2 | services/wordcloud-service.md | 옵션 처리 로직 |
| 3 | modules/wordcloud-generator.md | 생성 옵션 |

### 분석 결과
- batch-processor 옵션 누락: `background_color`, `apply_emotion_colors`, `remove_profanity`, `max_words`

### 해결 경로
1. batch-processor.md 옵션 확인 → api_routes.md에 추가 → index.html에 UI 추가

---

## 시나리오 P-2: 배치 처리 워드클라우드 생성 안됨

### 상황
사용자: "배치 처리하면 워드클라우드가 안 만들어져"

### 참조 문서

| 순서 | 문서 | 확인 내용 |
|------|------|----------|
| 1 | services/batch-processor.md | 생성 로직 |
| 2 | modules/wordcloud-generator.md | 메서드 확인 |
| 3 | routes/batch-routes.md | 엔드포인트 |

### 해결 경로
batch-processor → wordcloud_generator 호출 체인 추적

---

## 시나리오 P-3: 메타데이터 저장 경로 문제

### 상황
사용자: "메타데이터가 저장안되는데 어디에 저장되는거야?"

### 참조 문서

| 순서 | 문서 | 확인 내용 |
|------|------|----------|
| 1 | services/metadata-service.md | 저장 로직 |
| 2 | models/metadata-manager.md | save 메서드 |
| 3 | config/settings.py | 경로 상수 |

### 저장 경로
- 배치: `batch/batch_YYYYMMDD_X/tmeta/employee_{id}.json`
- 단일: `processed_data/YYYYMM/single/employee_{id}.json`

---

## 시나리오 P-4: 감정 분석 결과不正确

### 상황
사용자: "감정 분석 결과가 이상한데 어떤 모델 사용하는거야?"

### 참조 문서

| 순서 | 문서 | 확인 내용 |
|------|------|----------|
| 1 | modules/emotion-analysis.md | 모델 정보 |
| 2 | config/settings.py | 모델 경로 |
| 3 | services/analysis-service.md | 파이프라인 |

### 분석 결과
- 모델: KcBERT (j5ng/aibert-base-v1)
- 40+ 감정 범주 분류

---

## 시나리오 P-5: 반어법 감지 정확도 낮음

### 상황
사용자: "반어법 감지가 잘 안되는데 개선할 수 있어?"

### 참조 문서

| 순서 | 문서 | 확인 내용 |
|------|------|----------|
| 1 | modules/sarcasm-analysis.md | 감지 모델 |
| 2 | modules/emotion-analysis.md | 감정 분석 |
| 3 | services/analysis-service.md | 파이프라인 |

### 해결 방향
1. 규칙 기반 보완 (특정 단어/패턴)
2. 모델 재학습
3. 감정 + 반어법 앙상블