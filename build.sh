#!/bin/bash
echo "========================================"
echo "AskForHelp Chatbot - Build Script (Linux/macOS)"
echo "========================================"
echo

echo "Cleaning previous builds..."
rm -rf dist/ build/ __pycache__/ AskForHelp.spec
echo

echo "Building executable with PyInstaller..."
echo "This may take a few minutes..."
echo

pyinstaller --onefile --windowed --name AskForHelp     --add-data "model_config.py:."     --add-data "model_behavior_config.py:."     --add-data "AI_GUIDANCE.md:."     --add-data "MODEL_BEHAVIOR_GUIDE.md:."     --add-data "README.md:."     --add-data "QUICK_START.md:."     --add-data "INSTALLATION_GUIDE.md:."     --add-data "FEATURES_SUMMARY.md:."     --add-data "PROJECT_SUMMARY.md:."     --hidden-import=requests     --hidden-import=PIL     --hidden-import=tkinter     --hidden-import=subprocess     --hidden-import=smtplib     --hidden-import=email     --hidden-import=base64     --hidden-import=io     --hidden-import=datetime     --hidden-import=threading     --hidden-import=platform     --hidden-import=socket     --hidden-import=json     --hidden-import=glob     askforhelp_chatbot.py

if [ $? -eq 0 ]; then
    echo
    echo "========================================"
    echo "Build completed successfully!"
    echo "========================================"
    echo
    echo "Executable location: dist/AskForHelp"
    echo
    echo "To distribute:"
    echo "1. Copy dist/AskForHelp to target machine"
    echo "2. Ensure Ollama is installed and running"
    echo "3. Run ./AskForHelp"
    echo
else
    echo
    echo "========================================"
    echo "Build failed!"
    echo "========================================"
    echo
    echo "Check the error messages above."
    echo
fi
