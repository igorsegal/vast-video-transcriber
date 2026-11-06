Set-Location -LiteralPath 'D:\mcp-drummond'
$ErrorActionPreference = 'Stop'

if ([string]::IsNullOrWhiteSpace($env:DEEPSEEK_API_KEY)) {
    $secureKey = Read-Host 'Введите DeepSeek API key' -AsSecureString
    $env:DEEPSEEK_API_KEY = [System.Net.NetworkCredential]::new('', $secureKey).Password
    Remove-Variable secureKey
}

& 'D:\mcp-drummond\start_mcp.bat' run 'b340b394977da5a48f9ead70' --max-requests 3

if ($LASTEXITCODE -ne 0) {
    throw 'Аудит остановлен — пришли вывод. Повторно пока не запускай.'
}

Write-Host 'Готово: D:\mcp-drummond\reports\b340b394977da5a48f9ead70\AUDIT_REPORT.md'
