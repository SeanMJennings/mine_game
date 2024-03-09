try {
     write-host "`Found Chocolatey: " -fore yellow
     choco --version
 }
 catch {
     write-host "`Installing Chocolatey: " -fore yellow
     Invoke-WebRequest https://chocolatey.org/install.ps1 -UseBasicParsing | Invoke-Expression
 }
 
 try {
     write-host "nFound Python: " -fore yellow
     python --version
 }
 catch {
     write-host "nInstalling Python: " -fore yellow
     choco install python
 }
 
 
python -m venv .venv
.\.venv\Scripts\Activate.ps1
 
try {
    write-host "nFound Poetry: " -fore yellow
    poetry --version
}
catch {
    write-host "nInstalling Poetry: " -fore yellow
    (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python
    if ($env:Path -split ';' -notcontains  $env:APPDATA + "\Roaming\Python\Scripts") {
       [Environment]::SetEnvironmentVariable("Path", $env:Path + ";%APPDATA%\Roaming\Python\Scripts", "User")
    }
}

 poetry install