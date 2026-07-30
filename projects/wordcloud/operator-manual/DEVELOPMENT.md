# 워드클라우드 메뉴얼 작성 가이드 (프로젝트 나침반)

> 🧭 **나침반 문서** — 내용을 담지 않고 위치만 가리킨다.

> ⚠️ **공용 작성 규칙·양식·템플릿은 [../../common/operator-manual/DEVELOPMENT.md](../../../common/operator-manual/DEVELOPMENT.md) 가 정본이다(모든 프로젝트 공용 단일 소스, 2026-07-27 이관).**
> 이 파일은 **wordcloud 프로젝트 고유 정보**만 안내한다. 작성 전 반드시 공용 나침반을 먼저 열어 00~08 원자 문서를 확인한다.

---

## wordcloud 프로젝트 전용 작성 규칙

> 현재 wordcloud 프로젝트 전용 작성 규칙·예시는 없다. 공용 규칙만으로 충분한 동안은 이 섹션을 비워 둔다. 이 프로젝트만의 메뉴·용어·상태코드 특이사항이 생기면 `DEVELOPMENT/` 폴더를 만들어 전용 문서를 추가하고 여기서 링크한다.

## wordcloud 프로젝트 구조

- 백엔드: Python 3.10 + Flask
- 핵심 모델: KoTE (44감정) + HR 도메인 파인튜닝 3분류 극성 모델
- 앱 소스 루트: `wordcloud_project/`
- 메인 앱: `wordcloud_project/web/app.py`

## 빌드

개발 메뉴얼(`developer-manual/`) 통합 빌드는 공용 스크립트를 사용한다(공용 나침반 [06-integrated-build.md](../../../common/operator-manual/DEVELOPMENT/06-integrated-build.md) §2 참고):

```powershell
cd .clinerules/projects/wordcloud/operator-manual
python ../../common/operator-manual/build/build_integrated.py developer-manual
```

`developer-manual/build/`에는 `MANIFEST.txt`만 둔다(`print.css`·`build_integrated.py`는 공용 위치의 단일 사본을 쓴다).


---

## 메뉴얼 문서 위치

| 문서 | 위치 |
|------|------|
| 개발자 메뉴얼(목차) | [developer-manual/00-index.md](developer-manual/00-index.md) |
| 아키텍처 | [developer-manual/01-architecture.md](developer-manual/01-architecture.md) |
| 모듈 지도 | [developer-manual/02-module-map.md](developer-manual/02-module-map.md) |
| 감정 엔진 | [developer-manual/03-emotion-engine.md](developer-manual/03-emotion-engine.md) |
| 데이터 계층 | [developer-manual/04-data-layer.md](developer-manual/04-data-layer.md) |
| 빌드·배포 | [developer-manual/05-build-deploy.md](developer-manual/05-build-deploy.md) |
| 배치 | [developer-manual/06-batch.md](developer-manual/06-batch.md) |
| 파인튜닝 파이프라인 | [developer-manual/07-finetune-pipeline.md](developer-manual/07-finetune-pipeline.md) |
| 개발 환경·트러블슈팅 | [developer-manual/08-dev-setup-troubleshooting.md](developer-manual/08-dev-setup-troubleshooting.md) |
| 확장 지점 | [developer-manual/09-extension-points.md](developer-manual/09-extension-points.md) |
