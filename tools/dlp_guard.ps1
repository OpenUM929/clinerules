<#
    dlp_guard.ps1 — 사내 보안 프로그램의 "확장자 일괄 삭제" 대비 도구
    .clinerules 를 서브모듈로 쓰는 모든 프로젝트가 공용으로 쓰는 도구.
    프로젝트 이름 하드코딩 금지 — 항상 이 스크립트 위치(.clinerules/tools/) 기준
    2단계 상위 폴더를 저장소 루트로 삼는다.

    배경(2026-08-20 실측, wordcloud 프로젝트)
      - 사내 프로그램이 .html/.txt/.csv/.png 을 확장자 단위로 전량 하드 삭제(휴지통 우회).
      - 본체 61개 + .clinerules 56개 삭제. .py/.md/.json/.jsonl/.js/.css/.svg/.log 는 무사.
      - .git 내부는 100% 생존 → "커밋된 것은 산다"가 확인된 유일한 방어선.

    모드
      -Check     (기본) 삭제된 추적 파일 + git 이 못 지키는 무방비 자산을 보고. 삭제 발견 시 종료코드 1
      -Restore   삭제된 추적 파일만 HEAD 에서 복원(수정된 파일은 절대 건드리지 않음)
      -Snapshot  git 이 못 지키는 대상 확장자 파일을 스윕 대상 밖 확장자(.dlpbak)로 아카이브
      -Hook      SessionStart 훅용. 평시 무출력, 삭제 발견시에만 JSON 한 줄 출력

    프로젝트별 커스터마이즈 (이 스크립트는 수정하지 말 것)
      저장소 루트에 `.dlp_guard.json` 을 두면 자동으로 읽어 기본값에 병합한다.
      {
        "targetExt":     ["html", "txt", "csv", "png"],
        "excludePrefix": ["build/", "vendor-internal/"]
      }
      두 키 모두 선택. 미제공 시 아래 기본값만 사용.

    사용 예 (저장소 루트에서)
      powershell -NoProfile -File .clinerules\tools\dlp_guard.ps1
      powershell -NoProfile -File .clinerules\tools\dlp_guard.ps1 -Restore
      powershell -NoProfile -File .clinerules\tools\dlp_guard.ps1 -Snapshot
#>
[CmdletBinding()]
param(
    [switch]$Restore,
    [switch]$Snapshot,
    [switch]$Hook
)

$ErrorActionPreference = 'Stop'
try { [Console]::OutputEncoding = [System.Text.Encoding]::UTF8 } catch {}

# 기본 감시 확장자 — 프로젝트별로 다르면 .dlp_guard.json 의 targetExt 로 덮어쓴다
$TargetExt = @('html', 'txt', 'csv', 'png')

# 재생성 가능해 보호 대상에서 제외하는 경로 세그먼트(어느 깊이든 일치)
$ExcludeSegments = @('venv', '.venv', 'node_modules', 'build', 'dist', '__pycache__', 'vendor', '.playwright-mcp')
# 접두사 일치가 필요한 프로젝트별 예외 — .dlp_guard.json 의 excludePrefix 로 추가
$ExcludePrefix = @()

$RepoRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)

# ── 프로젝트별 오버라이드 로드 ────────────────────────────────────────────
$overridePath = Join-Path $RepoRoot '.dlp_guard.json'
if (Test-Path -LiteralPath $overridePath) {
    try {
        $cfg = Get-Content -LiteralPath $overridePath -Raw -Encoding UTF8 | ConvertFrom-Json
        if ($cfg.targetExt) { $TargetExt = @($cfg.targetExt) }
        if ($cfg.excludePrefix) { $ExcludePrefix = @($cfg.excludePrefix) }
    } catch {
        Write-Warning "$overridePath 파싱 실패, 기본값 사용: $_"
    }
}

$Repos = @(
    [pscustomobject]@{ Name = '본체'; Key = 'main'; Path = $RepoRoot },
    [pscustomobject]@{ Name = '.clinerules'; Key = 'clinerules'; Path = (Join-Path $RepoRoot '.clinerules') }
)

function Invoke-GitZ {
    # NUL 구분 출력을 문자열 배열로. 한글 경로 보존을 위해 quotepath 해제
    param([string]$RepoPath, [string[]]$GitArgs)
    # git 은 CRLF 경고 등을 stderr 로 내보내며, ErrorActionPreference=Stop 이면 중단된다
    $prev = $ErrorActionPreference
    $ErrorActionPreference = 'Continue'
    $out = & git -C $RepoPath -c core.quotepath=false @GitArgs 2>$null
    $ErrorActionPreference = $prev
    if ($null -eq $out) { return @() }
    $joined = ($out -join "`n")
    return @($joined -split "`0" | Where-Object { $_ -ne '' })
}

function Test-Excluded {
    param([string]$RelPath)
    $segments = $RelPath -split '/'
    foreach ($s in $segments) { if ($ExcludeSegments -contains $s) { return $true } }
    foreach ($p in $ExcludePrefix) { if ($RelPath.StartsWith($p)) { return $true } }
    return $false
}

function Get-TargetMatches {
    param([string[]]$Paths)
    $pattern = '\.(' + ($TargetExt -join '|') + ')$'
    return @($Paths | Where-Object { $_ -match $pattern -and -not (Test-Excluded $_) })
}

function Write-ExtBreakdown {
    param([string[]]$Paths, [string]$Indent = '    ')
    $Paths |
        Group-Object { ($_ -split '\.')[-1].ToLower() } |
        Sort-Object Count -Descending |
        ForEach-Object { Write-Host "$Indent$($_.Name): $($_.Count)" }
}

# ── 수집 ────────────────────────────────────────────────────────────────
$report = @()
foreach ($r in $Repos) {
    if (-not (Test-Path (Join-Path $r.Path '.git'))) { continue }

    $deleted     = Invoke-GitZ $r.Path @('ls-files', '-d', '-z')
    $untracked   = Invoke-GitZ $r.Path @('ls-files', '--others', '--exclude-standard', '-z')
    $ignored     = Invoke-GitZ $r.Path @('ls-files', '--others', '--ignored', '--exclude-standard', '-z')
    $modified    = Invoke-GitZ $r.Path @('diff', '--name-only', '-z')

    $report += [pscustomobject]@{
        Name        = $r.Name
        Key         = $r.Key
        Path        = $r.Path
        # @() 필수 — 1건일 때 문자열로 언랩되면 인덱싱이 문자 단위가 된다
        Deleted     = @($deleted)
        Unprotected = @(Get-TargetMatches ($untracked + $ignored))
        # diff 에는 삭제분도 섞이므로 제외한다(삭제는 Deleted 로 따로 보고)
        Uncommitted = @(Get-TargetMatches ($modified | Where-Object { $deleted -notcontains $_ }))
    }
}

# ── Restore ─────────────────────────────────────────────────────────────
if ($Restore) {
    $totalBefore = ($report | ForEach-Object { $_.Deleted.Count } | Measure-Object -Sum).Sum
    if ($totalBefore -eq 0) {
        Write-Host "복원할 삭제 파일이 없습니다."
        exit 0
    }
    foreach ($r in $report) {
        if ($r.Deleted.Count -eq 0) { continue }
        Write-Host "[$($r.Name)] 삭제 $($r.Deleted.Count)개 복원 중..."
        $prev = $ErrorActionPreference
        $ErrorActionPreference = 'Continue'
        for ($i = 0; $i -lt $r.Deleted.Count; $i += 50) {
            $batch = $r.Deleted[$i..([Math]::Min($i + 49, $r.Deleted.Count - 1))]
            & git -C $r.Path checkout -- @batch 2>$null
        }
        $ErrorActionPreference = $prev
        $left = (Invoke-GitZ $r.Path @('ls-files', '-d', '-z')).Count
        Write-Host "[$($r.Name)] 복원 후 남은 삭제: $left"
    }
    Write-Host "`n복원 완료. 수정(M) 상태 파일은 건드리지 않았습니다."
    exit 0
}

# ── Snapshot ────────────────────────────────────────────────────────────
if ($Snapshot) {
    $stamp   = Get-Date -Format 'yyyyMMdd-HHmmss'
    $stage   = Join-Path $RepoRoot "backups\dlp-$stamp"
    $count   = 0
    foreach ($r in $report) {
        $files = @($r.Unprotected + $r.Uncommitted) | Sort-Object -Unique
        foreach ($f in $files) {
            $src = Join-Path $r.Path $f
            if (-not (Test-Path -LiteralPath $src)) { continue }
            # 아카이브 내부 폴더명은 zip 인코딩 문제를 피해 ASCII 로 고정
            $dst = Join-Path $stage (Join-Path $r.Key $f)
            New-Item -ItemType Directory -Force -Path (Split-Path -Parent $dst) | Out-Null
            Copy-Item -LiteralPath $src -Destination $dst -Force
            $count++
        }
    }
    if ($count -eq 0) {
        Write-Host "스냅샷 대상이 없습니다(대상 확장자 파일이 모두 커밋된 상태)."
        exit 0
    }
    $zip = Join-Path $RepoRoot "backups\dlp-$stamp.zip"
    Compress-Archive -Path (Join-Path $stage '*') -DestinationPath $zip -Force
    # .zip 도 향후 차단될 수 있으므로 스윕 목록에 없는 확장자로 보관
    $final = [IO.Path]::ChangeExtension($zip, 'dlpbak')
    Move-Item -LiteralPath $zip -Destination $final -Force
    Remove-Item -LiteralPath $stage -Recurse -Force
    Write-Host "스냅샷 $count 개 → $final"
    Write-Host "복원 시: 확장자를 .zip 으로 바꿔 압축 해제"
    exit 0
}

# ── Hook (SessionStart) ─────────────────────────────────────────────────
# 삭제가 있을 때만 JSON 한 줄을 내보낸다. 평시에는 아무것도 출력하지 않는다.
if ($Hook) {
    $lines = @()
    $total = 0
    foreach ($r in $report) {
        if ($r.Deleted.Count -eq 0) { continue }
        $total += $r.Deleted.Count
        $byExt = ($r.Deleted | Group-Object { ($_ -split '\.')[-1].ToLower() } |
                  Sort-Object Count -Descending |
                  ForEach-Object { "$($_.Name) $($_.Count)" }) -join ', '
        $lines += "$($r.Name): $($r.Deleted.Count)개($byExt)"
    }
    if ($total -eq 0) { exit 0 }
    $msg = "⚠ 파일 일괄 삭제 감지 — " + ($lines -join ' / ') +
           ". 복원: powershell -NoProfile -File .clinerules\tools\dlp_guard.ps1 -Restore"
    $payload = [ordered]@{
        systemMessage      = $msg
        hookSpecificOutput = [ordered]@{
            hookEventName     = 'SessionStart'
            additionalContext = "사내 보안 프로그램의 확장자 일괄 삭제로 추적 파일 $total 개가 사라진 상태다. " +
                                "dlp_guard.ps1 -Restore 로 HEAD 에서 복원할 수 있음을 사용자에게 알릴 것. " +
                                "수정(M) 상태 파일은 손대지 말 것."
        }
    }
    $payload | ConvertTo-Json -Compress -Depth 5
    exit 0
}

# ── Check (기본) ────────────────────────────────────────────────────────
Write-Host "=== DLP 스윕 점검 ($(Get-Date -Format 'yyyy-MM-dd HH:mm')) ==="
Write-Host "감시 확장자: $($TargetExt -join ', ')`n"

$totalDeleted = 0
foreach ($r in $report) {
    Write-Host "[$($r.Name)]"
    if ($r.Deleted.Count -gt 0) {
        $totalDeleted += $r.Deleted.Count
        Write-Host "  삭제된 추적 파일: $($r.Deleted.Count)개  ← -Restore 로 복원 가능"
        Write-ExtBreakdown $r.Deleted '      '
    }
    else {
        Write-Host "  삭제된 추적 파일: 없음"
    }

    if ($r.Unprotected.Count -gt 0) {
        Write-Host "  무방비 자산(미추적/무시): $($r.Unprotected.Count)개  ← 삭제되면 복구 불가"
        $r.Unprotected | Select-Object -First 15 | ForEach-Object { Write-Host "      $_" }
        if ($r.Unprotected.Count -gt 15) { Write-Host "      ... 외 $($r.Unprotected.Count - 15)개" }
    }
    if ($r.Uncommitted.Count -gt 0) {
        Write-Host "  미커밋 수정(대상 확장자): $($r.Uncommitted.Count)개  ← 커밋 전까지 변경분 소실 위험"
        $r.Uncommitted | Select-Object -First 10 | ForEach-Object { Write-Host "      $_" }
    }
    Write-Host ""
}

if ($totalDeleted -gt 0) {
    Write-Host "⚠ 스윕 흔적 $totalDeleted 개. 즉시 실행: dlp_guard.ps1 -Restore"
    exit 1
}
Write-Host "✅ 삭제 흔적 없음"
exit 0
