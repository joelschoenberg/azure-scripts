### Install AppDynamics Azure Site Extension with PowerShell
### Joel Schoenberg
### 9/1/2017
###

### Build variables for getting site and extension details
###
$WebSite = "insert the Site name"
$ResourceGroupName = "insert the Resource Group name"
$ExtensionID = "AppDynamics.WindowsAzure.SiteExtension.4.3.Release"
$InstallURI = "https://" + $WebSite + ".scm.azurewebsites.net/api/siteextensions"

### Forming credential (use Azure deployment credentials)
###
$username = "insert the user name"
$password = "insert the password"
$base64AuthInfo = [Convert]::ToBase64String([Text.Encoding]::ASCII.GetBytes(("{0}:{1}" -f $username,$password)))

### Install Site Extension
###
write-output "Installing AppDynamics Azure Site Extension"

try {
    $InstallAppD = Invoke-RestMethod -Uri "$InstallURI/$ExtensionID" -Headers @{Authorization=("Basic {0}" -f $base64AuthInfo)} -Method Put
    $Status = ($InstallAppD.provisioningState).ToString() + "|" + ($InstallAppD.installed_date_time).ToString()
    Write-Output "AppD Installation Status : $Status"
    Restart-AzureRmWebApp -ResourceGroupName $ResourceGroupName -Name $WebSite -Verbose
}
catch{$_}
