# Url Analyzer Service (url_analyzer_service.py)

## 파일 위치

`service/url_analyzer_service.py` (117줄)

## 역할

URL/HTML 분석 - HTML/텍스트에서 데이터 추출 (BeautifulSoup)

## 주요 함수

| 함수 | 기능 |
|------|------|
| `analyze(content)` | HTML/텍스트에서 데이터 추출 |
| `_is_html(content)` | HTML 여부 판단 |
| `extract_headings(soup)` | 제목 추출 |
| `extract_paragraphs(soup)` | 단락 추출 |
| `extract_tables(soup)` | 테이블 추출 |

## 의존성

- `bs4` (BeautifulSoup) - HTML 파싱

## 관련 문서

- [services/README.md](README.md) - services 개요
- [services/data-spec-service.md](data-spec-service.md) - 데이터 사양 서비스