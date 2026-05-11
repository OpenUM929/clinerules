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
├── DEVELOPMENT.md                     # 메뉴얼 작성 개발 가이드
├── 00-getting-started.md              # 빠른 시작 가이드
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
├── 05-mngr-sett.md                    # 관리자 설정 (별도 파일)
├── 06-daily-operations.md             # 일상 운영
├── 07-troubleshooting.md              # 장애 대응
├── 08-backup-recovery.md              # 백업/복구
└── appendix/
    ├── command-cheatsheet.md
    └── config-reference.md
```

## 작성 원칙

1. **조작 중심**: "이 버튼을 누륵 ~된다" 형식으로 절차 서술
2. **모니터링 포함**: 상태 확인 방법, 정상/비정상 기준, 확인 주기 명시
3. **스크린샷 활용**: 기능 영역만 확대 캡처 + 화살표/번호로 설명
4. **실무 지향**: 이론 설명 최소화, 실제 업무 흐름 중심

## 버전 이력

| 버전 | 날짜 | 작성자 | 변경 내용 |
|------|------|--------|-----------|
| 1.0 | 2026-05-11 | - | 초안 작성 |
