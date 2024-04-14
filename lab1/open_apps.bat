@echo off

REM Prompt user to enter a URL
set /p url="Enter the URL to open in Google Chrome: "

REM Open Google Chrome with the specified URL
start "C:\Program Files\Google\Chrome\Application\chrome.exe" "%url%"

REM Wait for 2 seconds before opening the next application
timeout /t 2 >nul

REM Open Visual Studio Code
start "C:\Users\Students\AppData\Local\Programs\Microsoft VS Code\Code.exe"

REM Wait for 2 seconds before opening the next application
timeout /t 2 >nul

REM Open SQL Server Management Studio (SSMS)
start "C:\Program Files (x86)\Microsoft SQL Server Management Studio 19\Common7\IDE\Ssms.exe"
