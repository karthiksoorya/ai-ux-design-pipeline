$ErrorActionPreference = "Stop"
$projectRoot = $PSScriptRoot
$env:PYTHONPATH = Join-Path $projectRoot "src"

$userProfile = [Environment]::GetFolderPath("UserProfile")
$workspaceProfile = if ($projectRoot -match "^([A-Za-z]:\\Users\\[^\\]+)") { $Matches[1] } else { $null }
$profiles = @($userProfile, $workspaceProfile) | Where-Object { $_ } | Select-Object -Unique
$bundledPython = $profiles |
    ForEach-Object { Join-Path $_ ".cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe" } |
    Where-Object { Test-Path -LiteralPath $_ } |
    Select-Object -First 1

if ($bundledPython) {
    & $bundledPython -m ai_ux_workflow demo @args
} elseif (Get-Command python -ErrorAction SilentlyContinue) {
    & python -m ai_ux_workflow demo @args
} elseif (Get-Command py -ErrorAction SilentlyContinue) {
    & py -3 -m ai_ux_workflow demo @args
} else {
    throw "Python 3.10 or newer is required."
}
