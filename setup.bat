@echo off
REM AskForHelp Chatbot Setup Script
REM This script helps configure the email settings

echo ========================================
echo AskForHelp Chatbot Setup
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.12 or higher
    pause
    exit /b 1
)

echo [✓] Python is installed

REM Check if Ollama is installed
ollama --version >nul 2>&1
if errorlevel 1 (
    echo Error: Ollama is not installed
    echo Please install Ollama from https://ollama.ai
    pause
    exit /b 1
)

echo [✓] Ollama is installed

REM Check if qwen3:4b model is available
ollama list | findstr "qwen3:4b" >nul 2>&1
if errorlevel 1 (
    echo [!] qwen3:4b model not found
    echo Downloading qwen3:4b model...
    ollama pull qwen3:4b
    if errorlevel 1 (
        echo Error: Failed to download qwen3:4b model
        pause
        exit /b 1
    )
)

echo [✓] qwen3:4b model is available

REM Check if requests library is installed
python -c "import requests" >nul 2>&1
if errorlevel 1 (
    echo [!] requests library not found
    echo Installing requests library...
    pip install requests
    if errorlevel 1 (
        echo Error: Failed to install requests library
        pause
        exit /b 1
    )
)

echo [✓] requests library is installed

REM Check if Pillow library is installed
python -c "import PIL" >nul 2>&1
if errorlevel 1 (
    echo [!] Pillow library not found
    echo Installing Pillow library...
    pip install Pillow
    if errorlevel 1 (
        echo Error: Failed to install Pillow library
        pause
        exit /b 1
    )
)

echo [✓] Pillow library is installed

echo.
echo ========================================
echo Setup Complete!
echo ========================================
echo.

REM Ask if user wants to configure email
set /p configure_email="Do you want to configure email settings now? (y/n): "
if /i "%configure_email%"=="y" (
    echo.
    echo Email Configuration
    echo -------------------
    echo.
    echo Please edit the email_config_template.py file and rename it to email_config.py
    echo.
    echo Instructions:
    echo 1. Open email_config_template.py in a text editor
    echo 2. Fill in your email credentials
    echo 3. Save the file as email_config.py
    echo.
    echo For Gmail users:
    echo - Enable 2-Factor Authentication
    echo - Generate an App Password (16 characters)
    echo - Use the App Password in the configuration
    echo.
)

echo.
echo To start the chatbot, run:
echo python askforhelp_chatbot.py
echo.
pause
