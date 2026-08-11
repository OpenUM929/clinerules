# File Parser

## 파일 위치
`wordcloud_project/src/services/file_parser.py` (189줄)

## 역할
CSV/Excel 파일 파싱 및 인코딩 감지, 컬럼 정보 추출

## 주요 함수

| 함수 | 기능 |
|------|------|
| `parse_csv_with_encoding(file_content, filename)` |多种 인코딩으로 CSV 파싱 시도 |
| `extract_column_info(df)` | 컬럼 정보 (이름, 타입, 샘플) 추출 |
| `normalize_dataframe(df)` | DataFrame 인코딩 UTF-8 정규화 |
| `parse_uploaded_file(file)` | 업로드 파일 (CSV/Excel) 파싱 |
| `parse_csv_file(file)` | CSV 파일만 파싱 |

## 지원 파일 형식

- CSV (다양한 인코딩: UTF-8, CP949, EUC-KR 등)
- Excel (.xlsx, .xls)

## 인코딩 감지 순서

1. utf-8
2. utf-8-sig
3. cp949
4. euc-kr
5. cp932
6. shift-jis
7. latin1

## 관련 문서

- [project_wordcloud/services/batch-service.md](batch-service.md)
- [project_wordcloud/services/batch-manager.md](batch-manager.md)