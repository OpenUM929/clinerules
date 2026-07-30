# Sarcasm Analysis (반어법 감지)

## 파일 위치
`wordcloud_project/src/modules/sarcasm_analysis.py` (221줄)

## 역할
텍스트 반어법(Sarcasm) 감지 - Transformer 기반 모델 사용

## 함수

| 이름 | 기능 |
|------|------|
| `analyze_sarcasm(text)` | 텍스트 반어법 감지 |

## 모델

| 구분 | 모델 경로 | 설명 |
|------|----------|------|
| Fine-tuned | 커스텀 파인튜닝 모델 | 반어법 감지 전용 |
| Base | `beomi/kcbert-base` | KcBERT 기반 |

## 감지 결과

- **Sarcasm**: 반어로 판단
- **Normal**: 정상 문장
- Confidence 점수 포함

## 의존성

- `transformers` - Hugging Face 모델 로드
- `torch` - PyTorch 백엔드

## 관련 문서

- [project_wordcloud/modules/emotion-analysis.md](emotion-analysis.md)
- [project_wordcloud/routes/api-routes.md](../routes/api-routes.md)