# Emotion Analysis (감정 분석)

## 파일 위치
`wordcloud_project/src/modules/emotion_analysis.py` (291줄)

## 역할
텍스트 감정 분석 - Transformer 기반 KcBERT 모델 사용

## 클래스

| 이름 | 기능 |
|------|------|
| `EmotionAnalysis` | 감정 분석기 클래스 (Singleton) |

## 주요 함수

| 함수 | 기능 |
|------|------|
| `analyze(text)` | 텍스트 감정 분석 |
| `get_scores()` | 감정 점수 반환 |

## 감정 범주

40+ 감정 범주 (불평, 환영, 감동, 화남, 슬픔 등)

## 모델

| 구분 | 모델 경로 | 설명 |
|------|----------|------|
| Fine-tuned | 설정 파일 참조 | 파인튜닝된 감정 분석 모델 |
| Base | `j5ng/aibert-base-v1` | KcBERT 기반 모델 |

## 의존성

- `transformers` - Hugging Face 모델 로드
- `torch` - PyTorch 백엔드

## 관련 문서

- [project_wordcloud/services/analysis-service.md](../services/analysis-service.md)
- [project_wordcloud/modules/sarcasm-analysis.md](sarcasm-analysis.md)