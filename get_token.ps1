# Extract GitHub credential token from Windows Credential Manager
Add-Type -AssemblyName System.Runtime.WindowsRuntime
$cred = Get-StoredCredential -Target "GitHub - https://api.github.com/zhipenglu988-collab" -ErrorAction SilentlyContinue
if ($cred) {
    $token = $cred.GetNetworkCredential().Password
    Write-Host "Token found! Length: $($token.Length)"
    Write-Host "Token: $token"
} else {
    Write-Host "Credential not found via Get-StoredCredential"
    # Try alternative method
    $cred = cmdkey /list | Select-String "GitHub" | ForEach-Object { $_.ToString() }
    Write-Host "Found: $cred"
}
