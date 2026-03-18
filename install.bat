@echo off
echo =========================
echo Installing pson (Windows)
echo =========================

REM Check if Python exists
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed.
    pause
    exit /b
)

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip

REM Install package
echo Installing pson...
python -m pip install .

if %errorlevel% neq 0 (
    echo.
    echo ❌ Installation failed.
) else (
    echo.
    echo ✅ pson installed successfully!
    echo Try: pson -v
)

pause