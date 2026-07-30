# MSYS 세부 문서 작성 가이드 (프로젝트 나침반)

> ⚠️ **공용 작성 규칙·양식·템플릿은 [../../common/operator-manual/DEVELOPMENT.md](../../../common/operator-manual/DEVELOPMENT.md) 가 정본이다(모든 프로젝트 공용 단일 소스, 2026-07-27 이관).**
> 이 파일은 **MSYS 전용 잔여 사항**만 안내한다. 작성 전 반드시 공용 나침반을 먼저 열어 00~08 원자 문서를 확인한 뒤, 아래 MSYS 전용 문서를 참고한다.

---

## MSYS 전용 문서

| 문서 | 다루는 내용 |
|------|------------|
| [DEVELOPMENT/msys-specifics.md](DEVELOPMENT/msys-specifics.md) | 캡처 영역 예시(메뉴별) · 관리자 설정(mngr_sett) 작성 특이사항 · 상태코드 사전 예시(CD901~904) |

## 빌드

MSYS 운영/개발 메뉴얼 통합 빌드는 공용 스크립트를 사용한다(공용 나침반 [06-integrated-build.md](../../../common/operator-manual/DEVELOPMENT/06-integrated-build.md) §2 참고):

```powershell
cd .clinerules/docs/msys/operator-manual
python ../../common/operator-manual/build/build_integrated.py .
python ../../common/operator-manual/build/build_integrated.py developer-manual
```

`docs/msys/operator-manual/build/`, `docs/msys/operator-manual/developer-manual/build/`에는 각 매뉴얼의 `MANIFEST.txt`만 둔다(`print.css`·`build_integrated.py`는 공용 위치의 단일 사본을 쓴다).
