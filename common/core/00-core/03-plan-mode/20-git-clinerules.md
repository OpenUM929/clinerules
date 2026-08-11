# Git 커밋 시 .clinerules 취급 규칙

## Git 커밋/푸시 시 `.clinerules` 지침 파일 취급 규칙

> ⚠️ **협업 보존 규칙**: 다른 팀원이 `.clinerules`를 동시에 작업할 수 있으므로, 반드시 아래 규칙을 준수한다.

1. **교체 금지**: `.clinerules/` 하위 파일을 커밋할 때, **파일 전체를 교체(replace/overwrite)**하지 않는다.
2. **차이 확인**: 푸시 전 `git diff HEAD~1 -- .clinerules/` 또는 `git show origin/master:.clinerules/파일명`으로 원격 내용과 비교한다.
3. **추가 방식**: 기존 내용이 유지된 상태에서, **우리가 추가한 항목만 Append** 하는 방식으로 커밋한다.
4. **삭제 방지**: 기존 지침의 섹션, 규칙, 문맥이 **삭제되거나 누락되지 않도록**, `git diff --cached -- .clinerules/`로 변경 내역을 반드시 검토한다.
5. **충돌 대응**: 원격 파일과 로컬 파일이 다를 경우, `git merge` 방식으로 양쪽 내용을 병합한 후 커밋한다. 병합 불가 시 사용자에게 보고한다.
