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
 
 (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python
 [Environment]::SetEnvironmentVariable("Path", $env:Path + ";%APPDATA%\Roaming\Python\Scripts", "User")
 poetry install