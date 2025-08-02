@echo off
echo Flask Example Runner
echo ===================
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

REM Check if Flask is installed
python -c "import flask" >nul 2>&1
if %errorlevel% neq 0 (
    echo Flask is not installed. Installing Flask...
    pip install flask
    if %errorlevel% neq 0 (
        echo ERROR: Failed to install Flask
        echo Please install Flask manually with: pip install flask
        echo.
        pause
        exit /b 1
    )
    echo Flask installed successfully!
    echo.
)

echo Starting Flask example application...
echo.
echo Open your browser to http://127.0.0.1:5001
echo.
echo Press Ctrl+C to stop the server
echo.

python flask_example.py

pause
