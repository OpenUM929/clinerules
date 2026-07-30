# 화면 도메인 (Screen Domain)

## 파일 위치
`wordcloud_project/web/templates/`

## 화면 목록

| 화면 | 템플릿 파일 | 설명 |
|------|-----------|------|
| 메인 (감정 분석) | `index.html` | 텍스트 입력, 감정 분석, 워드클라우드 |
| 결과 보기 | `results.html` | 분석 결과 표시 |
| 워드클라우드 | `wordcloud.html` | 워드클라우드 전용 페이지 |
| 메타데이터 | `metadata.html` | 메타데이터 관리 |
| 배치 처리 | `metadata_batch.html` | 배치 처리 페이지 |
| 데이터 전처리 | `preprocess.html` | 데이터 전처리 |
| 반어법 분석 | `sarcasm.html` | 반어법 감지 |
| 불용어 관리 | `stopwords.html` | 불용어 CRUD |
| 설정 | `settings.html` | 시스템 설정 |
| 베이스 | `base.html` | 공통 레이아웃 템플릿 |

## 관련 문서

- [project_wordcloud/routes/ui-routes.md](../routes/ui-routes.md) - 페이지 라우트
- [project_wordcloud/routes/batch-routes.md](../routes/batch-routes.md) - 배치 라우트
---

## URL 매핑

| 화면 이름 | URL | 실제 파일 경로 |
|-----------|-----|----------------|
| 감정 분석 (메인) | `/` | `web/templates/index.html` |
| 워드클라우드 | `/wordcloud` | `web/templates/wordcloud.html` |
| 메타데이터 | `/metadata` | `web/templates/metadata.html` |
| 배치 처리 | `/metadata/batch` | `web/templates/metadata_batch.html` |
| 데이터 전처리 | `/preprocess` | `web/templates/preprocess.html` |
| 결과 보기 | `/results` | `web/templates/results.html` |
| 반어법 분석 | `/sarcasm` | `web/templates/sarcasm.html` |
| 불용어 관리 | `/stopwords` | `web/templates/stopwords.html` |
| 설정 | `/settings` | `web/templates/settings.html` |
| 베이스 템플릿 | - | `web/templates/base.html` |

> 화면 정의 양식·분석 경로는 공용 규약 `common/ui/common/screen-domain.md` 참조.

## 시나리오 테스트

### 시나리오: 분석 페이지 워드클라우드 옵션 문제

**상황**: 사용자가 분석 시작을 누르면 워드클라우드가 생성되지 않음

**분석 경로**:
1. `common/core/00-core.md` → "기능 문제 분석/디버깅" → `common/core/03-workflow.md`
2. 위 URL 매핑표에서 분석 페이지 파일 확인: `web/templates/index.html`
3. 관련 API: `src/routes/api_routes.py`
4. 관련 서비스: `src/services/wordcloud_service.py`, `src/modules/wordcloud_generator.py`
5. `batch_processor.py`와 비교해 옵션 누락 확인

### 시나리오: 배치 처리 페이지 디자인 변경

**상황**: 배치 처리 페이지 디자인 개선 요청

**분석 경로**:
1. `common/core/00-core.md` → "공통 UI/디자인" → `common/core/04-design-change.md`
2. 위 매핑표에서 배치 페이지 파일 확인: `web/templates/metadata_batch.html`
3. 현재 디자인 분석 후 변경 계획 수립
