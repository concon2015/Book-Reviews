# PowerShell in a Month of Lunches Cheatsheet
## Chapter 2
[PowerShell Github Page](https://github.com/PowerShell/PowerShell)

[PowerShell Install on Windows](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-windows?view=powershell-7.4)

[PowerShell Install on Linux](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-linux?view=powershell-7.4)

[PowerShell Install on macOS](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-macos?view=powershell-7.4)

[Visual Studio Code](https://code.visualstudio.com/)

[PowerShell Extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-vscode.PowerShell)

`$PSVersionTable` - Variable that shows the current version of PowerShell

## Chapter 3

`help | get-process`  Command to get help in a page by page view. Equivalent to `Get-Help Get-Process | more`

`Get-Help`  Command to display summary help information.

`Update-Help`  Download updates to help files (NOTE: Must run in admin prompt)

**Parameter Sets** - The SYNTAX section will display common ways commands can be used. Parameters must all exist in the same set. Cannot cross parameters from different sets.

```
SYNTAX

Get-Item [-Stream <String[]>] [-Credential <PSCredential>] [-Exclude <String[]>] [-Filter <String>] [-Force] [-Include <String[]>] -LiteralPath <String[]> [<CommonParameters>]

Get-Item [-Path] <String[]> [-Stream <String[]>] [-Credential <PSCredential>] [-Exclude <String[]>] [-Filter <String>] [-Force] [-Include <String[]>] [<CommonParameters>]
```

**Mandatory Parameters vs Optional Parameters**
	
Mandatory - Only the parameter flag is inside of brackets
    
`[-Path] <String[]>`


Optional - Entire parameter and data type are inside brackets    
    
`[-Stream <String[]>]` 

**Positional Parameters**

* Don’t need to provide parameter name as long as all positional paremeters are in the right order

```
Get-Help Get-Process -full
. . . . . . . . . . . . . .
. . . . . . . . . . . . . .
-Name <System.String[]>
 Specifies one or more processes by process name. You can type multiple process names (separated by commas) and use wildcard characters. The parameter name (`Name`) is optional.
        Required?                    false
        Position?                    0
        Default value                None
        Accept pipeline input?       True (ByPropertyName)
        Accept wildcard characters?  True
```

**Parameter Types**
```
Get-Help Get-Process -full
. . . . . . . . . . .
. . . . . . . . . . .
-Name <System.String[]>
```

* [ ] Indicates that the parameter can accept an array of values or values separated by a comma


**Cmdlet Examples**
	
`Get-Help Get-Process -Examples`

**About Topics**

`help *about*`  Get general information about powershell nuances that isn't covered in cmdlet help files


**Online Help**

`Get-Help Get-Process -online`  Open help documentation in web browser

## Chapter 4

**Execution Policy**

The `Set-ExecutionPolicy` command dictates what scripts if any are allowed to run on a system

* `Set-ExecutionPolicy -Restricted` - Only Microsoft signed scripts can run
* `Set-ExecutionPolicy -AllSigned` - Only signed scripts can run
* `Set-ExecutionPolicy -RemoteSigned` - All local scripts and signed remote scripts can run
* `Set-ExecutionPolicy -Unrestricted` - All scripts can run
* `Set-ExecutionPolicy -Bypass` - This execution policy is designed for configurations in which a PowerShell script is built into a larger application or for configurations in which PowerShell is the foundation for a program that has its own security model.

**Cmdlet Naming Convention**

Cmdlets follow a verb - noun naming comvention

**PowerShell Verbs**

`get-verb |select verb | fw -Column 6`

```
Add                 Clear               Close               Copy                Enter               Exit
Find                Format              Get                 Hide                Join                Lock
Move                New                 Open                Optimize            Push                Pop
Redo                Remove              Rename              Reset               Resize              Search
Select              Set                 Show                Skip                Split               Step
Switch              Undo                Unlock              Watch               Connect             Disconnect
Read                Receive             Send                Write               Backup              Checkpoint
Compare             Compress            Convert             ConvertFrom         ConvertTo           Dismount
Edit                Expand              Export              Group               Import              Initialize
Limit               Merge               Mount               Out                 Publish             Restore
Save                Sync                Unpublish           Update              Debug               Measure
Ping                Repair              Resolve             Test                Trace               Approve
Assert              Build               Complete            Confirm             Deny                Deploy
Disable             Enable              Install             Invoke              Register            Request
Restart             Resume              Start               Stop                Submit              Suspend
Uninstall           Unregister          Wait                Use                 Block               Grant
Protect             Revoke              Unblock             Unprotect
```
[Approved PowerShell Verbs](https://learn.microsoft.com/en-us/powershell/scripting/developer/cmdlet/approved-verbs-for-windows-powershell-commands?view=powershell-7.4)

**Aliases**

`Get-Alias -Definition 'Get-Process'`

`Get-Alias |select -Property displayname | fw -c 5`

```
? -> Where-Object       % -> ForEach-Object     ac -> Add-Content       cat -> Get-Content      cd -> Set-Location
chdir -> Set-Location   clc -> Clear-Content    clear -> Clear-Host     clhy -> Clear-History   cli -> Clear-Item
clp -> Clear-ItemPrope… cls -> Clear-Host       clv -> Clear-Variable   cnsn -> Connect-PSSess… compare -> Compare-Obj…
copy -> Copy-Item       cp -> Copy-Item         cpi -> Copy-Item        cpp -> Copy-ItemProper… cvpa -> Convert-Path
dbp -> Disable-PSBreak… del -> Remove-Item      diff -> Compare-Object  dir -> Get-ChildItem    dnsn -> Disconnect-PSS…
ebp -> Enable-PSBreakp… echo -> Write-Output    epal -> Export-Alias    epcsv -> Export-Csv     erase -> Remove-Item
etsn -> Enter-PSSession exsn -> Exit-PSSession  fc -> Format-Custom     fhx -> Format-Hex       fl -> Format-List
foreach -> ForEach-Obj… ft -> Format-Table      fw -> Format-Wide       gal -> Get-Alias        gbp -> Get-PSBreakpoint
gc -> Get-Content       gcb -> Get-Clipboard    gci -> Get-ChildItem    gcm -> Get-Command      gcs -> Get-PSCallStack
gdr -> Get-PSDrive      gerr -> Get-Error       ghy -> Get-History      gi -> Get-Item          gin -> Get-ComputerInfo
gjb -> Get-Job          gl -> Get-Location      gm -> Get-Member        gmo -> Get-Module       gp -> Get-ItemProperty
gps -> Get-Process      gpv -> Get-ItemPropert… group -> Group-Object   gsn -> Get-PSSession    gsv -> Get-Service
gtz -> Get-TimeZone     gu -> Get-Unique        gv -> Get-Variable      h -> Get-History        history -> Get-History
icm -> Invoke-Command   iex -> Invoke-Expressi… ihy -> Invoke-History   ii -> Invoke-Item       ipal -> Import-Alias
ipcsv -> Import-Csv     ipmo -> Import-Module   irm -> Invoke-RestMeth… iwr -> Invoke-WebReque… kill -> Stop-Process
ls -> Get-ChildItem     man -> help             md -> mkdir             measure -> Measure-Obj… mi -> Move-Item
mount -> New-PSDrive    move -> Move-Item       mp -> Move-ItemProperty mv -> Move-Item         nal -> New-Alias
ndr -> New-PSDrive      ni -> New-Item          nmo -> New-Module       nsn -> New-PSSession    nv -> New-Variable
ogv -> Out-GridView     oh -> Out-Host          popd -> Pop-Location    ps -> Get-Process       pushd -> Push-Location
pwd -> Get-Location     r -> Invoke-History     rbp -> Remove-PSBreakp… rcjb -> Receive-Job     rcsn -> Receive-PSSess…
rd -> Remove-Item       rdr -> Remove-PSDrive   ren -> Rename-Item      ri -> Remove-Item       rjb -> Remove-Job
rm -> Remove-Item       rmdir -> Remove-Item    rmo -> Remove-Module    rni -> Rename-Item      rnp -> Rename-ItemProp…
rp -> Remove-ItemPrope… rsn -> Remove-PSSession rv -> Remove-Variable   rvpa -> Resolve-Path    sajb -> Start-Job
sal -> Set-Alias        saps -> Start-Process   sasv -> Start-Service   sbp -> Set-PSBreakpoint scb -> Set-Clipboard
select -> Select-Object set -> Set-Variable     shcm -> Show-Command    si -> Set-Item          sl -> Set-Location
sleep -> Start-Sleep    sls -> Select-String    sort -> Sort-Object     sp -> Set-ItemProperty  spjb -> Stop-Job
spps -> Stop-Process    spsv -> Stop-Service    start -> Start-Process  stz -> Set-TimeZone     sv -> Set-Variable
tee -> Tee-Object       type -> Get-Content     where -> Where-Object   wjb -> Wait-Job         write -> Write-Output
```


**Truncating Parameter Names**

You can abreviate parameter names using as long as they are unique.
`-ComputerName` can be abbreviated to `-Comp`

## Chapter 5

**PowerShell Providers**
A PowerShell provider allows commmand line access to data and components of the ssytem that wouldn't otehrtwise be accessible.

`Get-PSProvider`
```
Name                 Capabilities                                      Drives
----                 ------------                                      ------
Registry             ShouldProcess                                     {HKLM, HKCU}
Alias                ShouldProcess                                     {Alias}
Environment          ShouldProcess                                     {Env}
FileSystem           Filter, ShouldProcess, Credentials                {C, G, Temp}
Function             ShouldProcess                                     {Function}
Variable             ShouldProcess                                     {Variable}
```

**PSDrive**

A PSDrive allows you to connect a Provider to data storage.

`Get-PSDrive`
```
Name     Root
----     ----
Alias
C        C:\
Cert     \
Env
Function
G        G:\
HKCU     HKEY_CURRENT_USER
HKLM     HKEY_LOCAL_MACHINE
Temp     C:\Users\USERNAME\AppData\Local\Temp\
Variable
WSMan
```

**Navigate System**

`cd c:\temp\folder1` is an alias for `Set-Location`

You can also naviage in other drives such as `Set-Location hkcu:` or `cd env:`

**View Files, Folders, and Data**

`Get-ChildItem C:\temp`

```
    Directory: C:\temp

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a---           2/15/2024  7:57 AM              0 file1.txt
-a---           2/15/2024  7:57 AM              0 file2.txt
-a---           2/15/2024  7:57 AM              0 file3.txt
```

## Chapter 6


