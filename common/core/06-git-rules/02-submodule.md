# 서브모듈 커밋/푸시 규칙

> 상위 나침반 [`../06-git-rules.md`](../06-git-rules.md) 에서 분리.

## 서브 모듈 커밋/푸시 규칙 (CRITICAL)

**서브 모듈은 root 저장소와 별도로 관리됩니다.**

### 처리 원칙
- **서브 모듈 수정 시**: 서브 모듈 저장소에서 별도 커밋 + 푸시
- **메인 저장소 수정 시**: 메인 저장소에서 별도 커밋 + 푸시
- **서브 모듈 SHA 업데이트 시**: 메인 저장소에서 커밋 + 푸시

### 커밋/푸시 순서
1. 서브 모듈 변경 → 서브 모듈 저장소에 커밋 + 푸시
2. 메인 저장소에서 서브 모듈 SHA 업데이트 → 메인 저장소에 커밋 + 푸시

### 확인 명령어
```bash
# 서브 모듈 상태 확인
git submodule status

# 서브 모듈에서 커밋/푸시
git -C .clinerules status
git -C .clinerules add .
git -C .clinerules commit -m "..."
git -C .clinerules push

# 메인 저장소에서 서브 모듈 SHA 업데이트 후 커밋/푸시
git add .clinerules
git commit -m "update submodule"
git push
```

---
