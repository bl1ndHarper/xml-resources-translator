@echo off
title XML Translator

echo Starting Translator...
echo ----------------------------------------

REM
where python >nul 2>nul
if errorlevel 1 (
    echo ❌ Python3 was not found. Download and configure Python.
    pause
    exit /b
)

REM
python __main__.py

pause
