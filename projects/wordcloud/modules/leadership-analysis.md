# Leadership Analysis (리더십 분석)

## 파일 위치
`wordcloud_project/src/modules/leadership_analysis.py` (389줄)

## 역할
텍스트에서 리더십 역량 분석 - KOTE 모델 사용

## 클래스

| 이름 | 기능 |
|------|------|
| `LeadershipAnalysis` | 리더십 분석기 (Singleton) |

## 분석 대상 역량

6가지 리더십 역량 점수 계산

## 모델

- KOTE 모델 (`model/kote_for_easygoing_people`)

## 의존성

- `transformers` - Hugging Face 모델
- `torch` - PyTorch 백엔드

## 관련 문서

- `project_wordcloud/modules/metadata-analysis.md` (문서 미작성)