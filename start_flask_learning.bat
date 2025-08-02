@echo off
echo Flask Learning Starter
echo ======================
echo.
echo Welcome to your Flask learning journey!
echo.
echo This script will help you get started with learning Flask.
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.7 or newer from https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

echo Opening the Flask learning starter...
echo.
python start_flask_learning.py

pause
