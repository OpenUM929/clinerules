# 실제 사례 기반 교훈

> 상위 나침반 [`../06-git-rules.md`](../06-git-rules.md) 에서 분리.

## 실제 사례 기반 교훈

- **".clinerules 내려받고 싶다"** → `.clinerules` 폴더의 Git 저장소에서 pull해야 함. root 저장소를 건드리면 안 됨. Git 명령어 실행 전 반드시 대상 저장소 확인
- **`git reset --hard`로 로컬 최신 커밋이 덮어씌워짐** → `git reflog`로 이전 커밋 해시 찾아 복구 가능. 하지만 예방이 최선
