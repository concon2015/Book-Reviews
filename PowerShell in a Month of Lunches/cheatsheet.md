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
A PowerShell provider allows commmand line access to data and components of the system that wouldn't otehrtwise be accessible.

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

**Pipeline**

 * The pipe character | is used to chain commands together and pass input from one command to the next. Performs similar to Unix/Linux pipe.

    Example : `Get-ChildItem | Select-Object -Property Name`

**Commands to Export Output**

* `Export-CSV` Note: Can be imported with `Import-CSV`
* `ConvertTo-Json | Out-File file.json`
* `Export-Clixml` Note: This format keeps all objectes in tact and can be imported with `Import-Clixml`
* `Out-File`
* `ConvertTo-Html | Out-File index.html`

**Comparing Objects**

`Compare-Object -Reference .\object1.txt -Difference .\object2.txt`

**Printing File Contents**
`Get=Contents file.txt`


## Chapter 7

**Installing Modules**
`Install-Module Az`

**Check Installed Modules**
`Get-Module Az -ListAvailable`

**List Module Commands**
`Get-Command -Module Microsoft.PowerShell.Archive`

## Chapter 8

* Object = Single thing
* Property = Piece of information about an object
* Method = Action you can take on an object
* Collection = Group of objects

**Get Member**
`Get-ChildItem | Get-Member`
* Alias `gm`
* Used to list properties and methods for an object

**Sorting Objects**

`Get-Process | Sort-Object -Property Name`

**Selecting Properties**

`Get-Process | Select-Object -Property Name,ID,CPU`

## Chapter 10

**Pipeline Input**
* Some commands can accept input from pipeline input. It if found in the help pages
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

**Hash Table**

`Get-Process | Select-Object -Property @{name="New Name";expression="Name"}`

**Parenthetical Commands**

`Get-Command -Module (Get-Content .\modules.txt)`

## Chapter 11

**Formatting**

* Format Table `Get-Process | Format-Table -Property Name,ID,Responding -GroupBy Responding` Alias `ft`
* Format List `Get-Process | Format-List -Property Name,ID,Responding` Alias `fl`
* Format Wide `Get-Process | Format-Wide -Property Name -Column 5` Alias `fw`

* Alawys format commands the furtherst to the right as posssible. 

## Chapter 12

**Filtering**

* Some commands offer native filtering. `Get-Process -Name *pwsh*,svc*`

* Other commands can be filtered using `Where-Object`
    
    * `Get-Process | Where-Object -FilterScript {$_.WorkingSet -gt 100MB}`
    * `Get-Process | Where-Object {$_.Name -match 'pws'}`

* Filter to the left as much as you can


**Comparison Operators**

* Prefix "i" means "is not"
* Prefix "c" means "case sensitive"

Equality

    -eq, -ieq, -ceq - equals

    -ne, -ine, -cne - not equals

    -gt, -igt, -cgt - greater than

    -ge, -ige, -cge - greater than or equal

    -lt, -ilt, -clt - less than

    -le, -ile, -cle - less than or equal


Matching

    -like, -ilike, -clike - string matches wildcard pattern

    -notlike, -inotlike, -cnotlike - string doesn't match wildcard pattern

    -match, -imatch, -cmatch - string matches regex pattern

    -notmatch, -inotmatch, -cnotmatch - string doesn't match regex pattern

Replacement

    -replace, -ireplace, -creplace - replaces strings matching a regex pattern

Containment

    -contains, -icontains, -ccontains - collection contains a value

    -notcontains, -inotcontains, -cnotcontains - collection doesn't contain a value

    -in - value is in a collection

    -notin - value isn't in a collection

Type

    -is - both objects are the same type

    -isnot - the objects aren't the same type

**$_. Keyword**

`$_.` refers to the current object in the pipeline. 

Properties can be appended such as `$_.WorkingSet`

`Get-Process | Where-Object -FilterScript {$_.WorkingSet -gt 100MB}`

## Chapter 13

WSMan stands for Web Services for Management. This is the communication protocol for remote powershell. This opererates over HTTP and HTTPS. (Note: traffic is still encrypted over http). WSMan runs via the WinRM process. This is installed by default on Windows but not enabled. Can be enabled via GPO.

PowerShell remoting can be done with (Windows), macOS, and Linux over SSH

**Enable PS Remoting**

From an admin PowerShell window, run `Enable-PSRemoting`

**Opening an Interactive PS Session**

`Enter-PSSession -ComputerName computer1 -Username user1` use `-ComputerName` to create a session over WinRM

`Enter-PSSession -Hostname Computer1 -Username user1` use `-Hostname` to create a session over SSH

**Closing an Interactive PS Session**

`Exit-PSSession`

**Running Remote Commands**

`Invoke-Command -ComputerName windows1,windows2 -ScriptBlock {Get-Process svchost}`

**Remoting Tips and Tricks**

Use hostname instead of IP address

`help about_Remote_Troubleshooting -Online` for detailed troubleshooting steps

Do as much processing as you can on the remote machine within the `-ScriptBlock` to reduce transmitted data and increase processing speed. Really makes a difference when running commands on multiple machines

## Chapter 14

**Start Jobs**

`Start-Job -ScriptBlock {gci}` Spins up a new process

`Start-ThreadJob -ScriptBlock {gci}` Runs in the same process

`Invoke-Command -ComputerName windows1 -ScriptBlock {gci} -AsJob -JobName RemoteJob` Run a remote command as a job

**Getting Job Results**

`Get-Job` Lists all jobs and current statuses

`Receive-Job -id 1` Gets job output and clears output queue

`Receive-Job -id 1 -Keep` Gets job output and leaves output queue intact

**Managing Jobs**

`Remove-Job -id 1` Removes job and all cached output

`Stop-Job` Stop job and keep all cached output

`Wait-Job` Used to pause execution until job has finished

## Chapter 15