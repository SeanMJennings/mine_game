try {
     choco --version
     write-host "`Found Chocolatey: " -fore yellow
 }
 catch {
     write-host "`Installing Chocolatey: " -fore yellow
     Invoke-WebRequest https://chocolatey.org/install.ps1 -UseBasicParsing | Invoke-Expression
     if ($env:Path -split ';' -notcontains  $env:ALLUSERSPROFILE + "\chocolatey\bin") {
        [Environment]::SetEnvironmentVariable("Path", $env:Path + ";%ALLUSERSPROFILE%\chocolatey\bin", "User")
     }
 }
 
 try {
     python --version
     write-host "nFound Python: " -fore yellow
 }
 catch {
     write-host "nInstalling Python: " -fore yellow
     choco install python
 }
 

try {
    python -m venv .venv
}
catch {}

.\.venv\Scripts\Activate.ps1
 
try {
    poetry --version
    write-host "nFound Poetry: " -fore yellow
}
catch {
    write-host "nInstalling Poetry: " -fore yellow
    (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python
    if ($env:Path -split ';' -notcontains  $env:APPDATA + "\Roaming\Python\Scripts") {
       [Environment]::SetEnvironmentVariable("Path", $env:Path + ";%APPDATA%\Roaming\Python\Scripts", "User")
    }
}

 poetry install