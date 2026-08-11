# 라이브러리 관리 규칙

> 이 문서는 외부 라이브러리/의존성 사용 시 항상 최우선으로参照한다.

---

## 핵심 원칙

1. **로컬 vendor 저장소 사용** — CDN/외부 링크 금지
2. **새 라이브러리 추가 시 vendor에 다운로드 후 사용**
3. **이 문서에 파일 경로/용도 기록** — 다른 개발자가 확인 가능해야 함

---

## 라이브러리 추가 절차

### 1. 기존 라이브러리 확인

먼저 `static/vendor/js/`에서 **기존 라이브러리 여부 확인**:

```bash
glob static/vendor/js/*.js
```

| 원하는 라이브러리 | 로컬 경로 |
|----------------|----------|
| Chart.js | `static/vendor/js/chart.umd.js` |
| jQuery | `static/vendor/js/jquery-3.6.0.min.js` |
| Luxon | `static/vendor/js/luxon.min.js` |
| D3.js | `static/vendor/js/d3.v7.min.js` |
| Axios | `static/vendor/js/axios.min.js` |
| XLSX | `static/vendor/js/xlsx.full.min.js` |
| DataTables | `static/vendor/js/dataTables.js` |
| Flatpickr | `static/vendor/js/flatpickr.min.js` |

### 2. 로컬에 저장

없는 경우:
1. npm/yarn으로 다운로드 via 프로젝트 내부망에 전달 가능한 방식
2. 또는 외부에서 다운로드 후 `static/vendor/js/`에 복사

### 3. 문서 기록

이 문서의 **현재 사용 중인 라이브러리** 테이블에 추가:

```markdown
| 라이브러리 | 경로 | 용도 |
|-----------|------|------|
| {라이브러리명} | vendor/js/{파일명} | {용도} |
```

---

## 현재 사용 중인 라이브러리

### JavaScript

| 라이브러리 | 경로 | 용도 |
|-----------|------|------|
| Chart.js | `static/vendor/js/chart.umd.js` | 차트 시각화 (bar, line 등) |
| Chart.js Plugins | `static/vendor/js/chartjs-plugin-datalabels.min.js` | 차트 데이터 라벨 |
| Chart.js Luxon Adapter | `static/vendor/js/chartjs-adapter-luxon.min.js` | 차트 시간 어댑터 |
| jQuery | `static/vendor/js/jquery-3.6.0.min.js` | DOM 조작 |
| Luxon | `static/vendor/js/luxon.min.js` | 날짜/시간 처리 |
| D3.js | `static/vendor/js/d3.v7.min.js` | 데이터 시각화 |
| Axios | `static/vendor/js/axios.min.js` | HTTP 요청 |
| XLSX | `static/vendor/js/xlsx.full.min.js` | 엑셀 파일 처리 |
| DataTables | `static/vendor/js/dataTables.js` | 테이블 데이터 관리 |
| Flatpickr | `static/vendor/js/flatpickr.min.js` | 날짜 선택기 |

### Fonts

| 폰트 | 경로 | 용도 |
|------|------|------|
| IBM Plex Sans KR 400 | `static/vendor/fonts/ibm-plex-sans-kr-400.ttf` | 한글 본문 (regular) |
| IBM Plex Sans KR 500 | `static/vendor/fonts/ibm-plex-sans-kr-500.ttf` | 한글 본문 (medium) |
| IBM Plex Mono 400 | `static/vendor/fonts/ibm-plex-mono-400.ttf` | 코드/데이터 (regular) |
| IBM Plex Mono 500 | `static/vendor/fonts/ibm-plex-mono-500.ttf` | 코드/데이터 (medium) |

### CSS

| 라이브러리 | 경로 | 용도 |
|-----------|------|------|
| Tailwind CSS | `static/vendor/css/tailwindcss.css` | 유틸리티 CSS |
| Inter | `static/vendor/css/inter.css` | 영문 폰트 |
| IBM Plex | `static/vendor/css/ibm-plex.css` | 영문 폰트 |
| Flatpickr | `static/vendor/css/flatpickr.min.css` | 날짜 선택기 스타일 |
| DataTables | `static/vendor/css/dataTables.tailwindcss.min.css` | 테이블 스타일 |

---

## HTML에서 사용법

### 직접 로드 (base.html 공통)

```html
<script src="{{ url_for('static', filename='vendor/js/chart.umd.js') }}"></script>
```

### 모듈Import (개별 페이지)

```javascript
import { Chart } from '../vendor/js/chart.js';
```

> **참고**: ES Module 로드 방식은 페이지별Webpack/빌드 구성에 따라 다를 수 있음. 기존 패턴 참고のこと.

---

## 확인 체크리스트

새로운 라이브러리 사용 전:

- [ ] `static/vendor/js/`에 파일 존재 여부 확인
- [ ] 없다면 다운로드 후 로컬에 저장
- [ ] 이 문서의 라이브러리 테이블에 추가
- [ ] CDN/외部 링크 사용 **없음** 확인

---

*최종 수정일: 2026-04-21*