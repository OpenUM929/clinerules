# 공통 모듈 수정 시 영향도 분석

**적용 대상**: `static/js/modules/common/*.js` 수정 시

## 1단계: 사용처 전수 조사

```bash
# 모든 import 경로 검색
grep -r "from.*{모듈명}" --include="*.js" static/js/
# 또는
rg "from.*{모듈명}" static/js/
```

## 2단계: 상대 경로 검증

1. glob으로 실제 파일 위치 확인
2. 각 import하는 파일의 filePath 기준 상위 디렉토리 구조 파악
3. 상대 경로 계산:
   - 예: `tabs/dataDefinition/dataDefinition.js` → `modules/common/dateUtils.js`
   - 차이: `../../modules/common/dateUtils.js`

## 3단계: 검증 체크리스트

| 검증 항목 | 확인 방법 |
|-----------|----------|
| 실제 파일 존재 | glob 패턴 매칭 |
| import 경로 정확성 | filePath 기준 상대 경로 계산 |
| 모든 사용처 수정 | grep 결과 기반 전수 조사 |
| 테스트 실행 | 각 페이지 로드 확인 |

## 4단계: 결과 기록

수정 완료 후 결과를 본 문서 하단에 기록:

```
[YYYY-MM-DD] {모듈명} 수정 결과:
- 수정 파일: x
- 영향 받은 파일: x
- 테스트 결과: 성공/실패
- 문제점: (있을 경우)
```
