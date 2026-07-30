# MSYS 운영자 메뉴얼

## 개요

본 메뉴얼은 MSYS(수집 현황 대시보드) 시스템을 운영하는 운영자 및 인수인계자를 위한 실무 중심 가이드입니다.

## 대상 독자

- 시스템 운영자
- 인수인계자
- 관리자(admin 권한 보유자)

## 메뉴얼 구조

```
operator-manual/
├── README.md                          # 본 파일
├── DEVELOPMENT.md                     # 메뉴얼 작성 개발 가이드 (§1~§10, A4/탭/탐색/통합 규칙 포함)
├── 00-index.md                        # ★ 진입점: 제목 + 서론 + 목록(TOC). 각 메뉴 상대경로 링크
├── 00-getting-started.md              # 빠른 시작 가이드 (첫 내용 페이지)
├── 01-system-overview.md              # 시스템 개요
├── 02-environment-setup.md            # 환경 설정
├── 03-deployment.md                   # 배포 절차
├── 04-common-menus/                   # 일반 메뉴
│   ├── 01-dashboard.md
│   ├── 02-collection-schedule.md
│   ├── 03-chart-analysis.md
│   ├── 04-data-analysis.md
│   ├── 05-data-spec.md
│   ├── 06-card-summary.md
│   ├── 07-mapping.md
│   ├── 08-api-key-mngr.md
│   ├── 09-jandi.md
│   ├── 10-raw-data.md
│   ├── 11-admin.md
│   ├── 12-api-test.md
│   ├── 13-external-links.md
│   └── images/
├── 05-mngr-sett.md                    # 관리자 설정 (구성+탭설명)
│   ├── 05-mngr-sett.tab1.md           #   탭① 설정
│   ├── 05-mngr-sett.tab2.md           #   탭② 사용자
│   ├── 05-mngr-sett.tab3.md           #   탭③ 데이터 권한
│   ├── 05-mngr-sett.tab4.md           #   탭④ 상태 코드
│   ├── 05-mngr-sett.tab5.md           #   탭⑤ 아이콘
│   └── 05-mngr-sett.tab6.md           #   탭⑥ API 관리
├── 06-daily-operations.md             # 일상 운영
├── 07-troubleshooting.md              # 장애 대응
├── 08-backup-recovery.md              # 백업/복구
├── appendix/
│   ├── command-cheatsheet.md
│   └── config-reference.md
├── build/                             # 빌드 툴링 (메뉴 문서 아님)
│   └── MANIFEST.txt                   # 통합 순서(파일 목록, 탭 파일 포함)
├── integrated-manual.md               # ★ 통합본(단일 md, 화면용)
└── integrated-manual.html             # ★ 통합본(A4 HTML, 브라우저→인쇄→PDF)
```

> `print.css`·`build_integrated.py`는 **모든 프로젝트 공용 단일 사본**으로 `docs/common/operator-manual/build/`에 있다(2026-07-27 이관, 작성 지침: [../common/operator-manual/DEVELOPMENT/06-integrated-build.md](../common/operator-manual/DEVELOPMENT/06-integrated-build.md)).

> **탭 보유 메뉴 하위파일**: 탭이 있는 메뉴는 `NN-menu.md`(구성+탭설명) + `NN-menu.tabN.md`(탭별)로 분리. 예: `04-common-menus/08-api-key-mngr.md` + `08-api-key-mngr.tab1~4.md`.

> **진입점**: 메뉴얼 최상단은 `00-index.md`(제목+서론+목록). `00-getting-started.md`는 그 아래 첫 내용 페이지.
> **통합본**: 일일이 인쇄하지 않으려면 `integrated-manual.html`을 브라우저에서 열고 "인쇄 → PDF 저장"(용지 A4). 재생성은 `cd .clinerules/docs/msys/operator-manual && python ../../common/operator-manual/build/build_integrated.py .`.

## 작성 원칙

1. **조작 중심**: "이 버튼을 누륵 ~된다" 형식으로 절차 서술
2. **모니터링 포함**: 상태 확인 방법, 정상/비정상 기준, 확인 주기 명시
3. **스크린샷 활용**: 기능 영역만 확대 캡처 + 화살표/번호로 설명
4. **실무 지향**: 이론 설명 최소화, 실제 업무 흐름 중심

## 버전 이력

| 버전 | 날짜 | 작성자 | 변경 내용 |
|------|------|--------|-----------|
| 1.0 | 2026-05-11 | - | 초안 작성 |
| 1.1 | 2026-07-15 | - | `00-index.md` 진입점 추가, `build/` 툴링·`integrated-manual.*` 통합본 추가, 구조 트리 갱신 |
