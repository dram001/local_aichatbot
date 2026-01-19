@echo off
echo ========================================
echo AskForHelp Chatbot - Build Script
echo ========================================
echo.

echo Cleaning previous builds...
if exist "dist" rmdir /s /q "dist"
if exist "build" rmdir /s /q "build"
if exist "__pycache__" rmdir /s /q "__pycache__"
if exist "AskForHelp.spec" del "AskForHelp.spec"
echo.

echo Building executable with PyInstaller...
echo This may take a few minutes...
echo.

pyinstaller --onefile --windowed --name AskForHelp ^
    --add-data "model_config.py;." ^
    --add-data "model_behavior_config.py;." ^
    --add-data "AI_GUIDANCE.md;." ^
    --add-data "MODEL_BEHAVIOR_GUIDE.md;." ^
    --add-data "README.md;." ^
    --add-data "QUICK_START.md;." ^
    --add-data "INSTALLATION_GUIDE.md;." ^
    --add-data "FEATURES_SUMMARY.md;." ^
    --add-data "PROJECT_SUMMARY.md;." ^
    --hidden-import=requests ^
    --hidden-import=PIL ^
    --hidden-import=tkinter ^
    --hidden-import=subprocess ^
    --hidden-import=smtplib ^
    --hidden-import=email ^
    --hidden-import=base64 ^
    --hidden-import=io ^
    --hidden-import=datetime ^
    --hidden-import=threading ^
    --hidden-import=platform ^
    --hidden-import=socket ^
    --hidden-import=json ^
    --hidden-import=glob ^
    askforhelp_chatbot.py

if %ERRORLEVEL% equ 0 (
    echo.
    echo ========================================
    echo Build completed successfully!
    echo ========================================
    echo.
    echo Executable location: dist\AskForHelp.exe
    echo.
    echo To distribute:
    echo 1. Copy dist\AskForHelp.exe to target machine
    echo 2. Ensure Ollama is installed and running
    echo 3. Run AskForHelp.exe
    echo.
) else (
    echo.
    echo ========================================
    echo Build failed!
    echo ========================================
    echo.
    echo Check the error messages above.
    echo.
)

pause
