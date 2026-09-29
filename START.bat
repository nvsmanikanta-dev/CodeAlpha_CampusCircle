@echo off
setlocal
cd /d "%~dp0"
title CampusCircle - Local Server

echo ========================================
echo   CampusCircle - Local Setup and Start
echo ========================================

if not exist ".venv\Scripts\python.exe" (
    echo Creating Python environment...
    where py >nul 2>&1
    if not errorlevel 1 (
        py -3 -m venv .venv
    ) else (
        python -m venv .venv
    )
    if errorlevel 1 goto :fail
)

set "PROJECT_PYTHON=%CD%\.venv\Scripts\python.exe"
if not exist "%PROJECT_PYTHON%" goto :fail

echo Installing Python packages...
"%PROJECT_PYTHON%" -m pip install -r requirements.txt
if errorlevel 1 goto :fail

echo Preparing the database...
"%PROJECT_PYTHON%" manage.py migrate --noinput
if errorlevel 1 goto :fail

echo Loading sample community posts...
"%PROJECT_PYTHON%" manage.py seed_demo
if errorlevel 1 goto :fail

echo.
echo Open http://127.0.0.1:8000/register/ in your browser.
echo Press Ctrl+C to stop the server.
echo.
"%PROJECT_PYTHON%" manage.py runserver 127.0.0.1:8000
echo.
echo Server stopped. If it did not start, check the message above.
pause
exit /b 0

:fail
echo.
echo Setup failed. Read the error above, then run START.bat again.
pause
exit /b 1
