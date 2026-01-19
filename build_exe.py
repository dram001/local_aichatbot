#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build Script for AskForHelp Chatbot
Creates a standalone Windows executable using PyInstaller
"""

import os
import sys
import subprocess
import shutil
import platform

def check_dependencies():
    """Check if required dependencies are installed"""
    print("Checking dependencies...")
    
    try:
        import PyInstaller
        print("✓ PyInstaller is installed")
    except ImportError:
        print("✗ PyInstaller is not installed")
        print("Installing PyInstaller...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
        print("✓ PyInstaller installed successfully")
    
    try:
        import requests
        print("✓ requests is installed")
    except ImportError:
        print("✗ requests is not installed")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
        print("✓ requests installed successfully")
    
    try:
        import PIL
        print("✓ Pillow is installed")
    except ImportError:
        print("✗ Pillow is not installed")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pillow"])
        print("✓ Pillow installed successfully")
    
    print("\nAll dependencies are ready!\n")

def create_spec_file():
    """Create a PyInstaller spec file for custom build configuration"""
    spec_content = '''# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['askforhelp_chatbot.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('model_config.py', '.'),
        ('model_behavior_config.py', '.'),
        ('AI_GUIDANCE.md', '.'),
        ('MODEL_BEHAVIOR_GUIDE.md', '.'),
        ('README.md', '.'),
        ('QUICK_START.md', '.'),
        ('INSTALLATION_GUIDE.md', '.'),
        ('FEATURES_SUMMARY.md', '.'),
        ('PROJECT_SUMMARY.md', '.'),
    ],
    hiddenimports=[
        'requests',
        'PIL',
        'tkinter',
        'subprocess',
        'smtplib',
        'email',
        'base64',
        'io',
        'datetime',
        'threading',
        'platform',
        'socket',
        'json',
        'glob',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='AskForHelp',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # Set to True for console window, False for GUI only
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['assets/icon.ico'] if os.path.exists('assets/icon.ico') else None,
)
'''
    
    with open('AskForHelp.spec', 'w', encoding='utf-8') as f:
        f.write(spec_content)
    
    print("✓ Created PyInstaller spec file: AskForHelp.spec")

def create_build_script():
    """Create a Windows batch file for building the executable"""
    batch_content = '''@echo off
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
'''
    
    with open('build.bat', 'w', encoding='utf-8') as f:
        f.write(batch_content)
    
    print("✓ Created build script: build.bat")

def create_build_script_linux():
    """Create a Linux/macOS build script"""
    script_content = '''#!/bin/bash
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

pyinstaller --onefile --windowed --name AskForHelp \
    --add-data "model_config.py:." \
    --add-data "model_behavior_config.py:." \
    --add-data "AI_GUIDANCE.md:." \
    --add-data "MODEL_BEHAVIOR_GUIDE.md:." \
    --add-data "README.md:." \
    --add-data "QUICK_START.md:." \
    --add-data "INSTALLATION_GUIDE.md:." \
    --add-data "FEATURES_SUMMARY.md:." \
    --add-data "PROJECT_SUMMARY.md:." \
    --hidden-import=requests \
    --hidden-import=PIL \
    --hidden-import=tkinter \
    --hidden-import=subprocess \
    --hidden-import=smtplib \
    --hidden-import=email \
    --hidden-import=base64 \
    --hidden-import=io \
    --hidden-import=datetime \
    --hidden-import=threading \
    --hidden-import=platform \
    --hidden-import=socket \
    --hidden-import=json \
    --hidden-import=glob \
    askforhelp_chatbot.py

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
'''
    
    with open('build.sh', 'w', encoding='utf-8') as f:
        f.write(script_content)
    
    # Make executable
    os.chmod('build.sh', 0o755)
    print("✓ Created build script: build.sh")

def create_readme_build():
    """Create a README for building the executable"""
    readme_content = '''# Building AskForHelp Executable

This guide explains how to build a standalone executable for the AskForHelp chatbot.

## Prerequisites

### Windows
1. Install Python 3.8 or higher
2. Install required packages:
   ```bash
   pip install pyinstaller pillow requests
   ```

### Linux/macOS
1. Install Python 3.8 or higher
2. Install required packages:
   ```bash
   pip3 install pyinstaller pillow requests
   ```

## Building the Executable

### Windows (Recommended Method)

#### Option 1: Using the build script (Easiest)
1. Open Command Prompt or PowerShell
2. Navigate to the project directory
3. Run the build script:
   ```bash
   build.bat
   ```
4. The executable will be created in the `dist` folder as `AskForHelp.exe`

#### Option 2: Using PyInstaller directly
```bash
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
```

### Linux/macOS

#### Option 1: Using the build script (Easiest)
1. Open Terminal
2. Navigate to the project directory
3. Run the build script:
   ```bash
   chmod +x build.sh
   ./build.sh
   ```
4. The executable will be created in the `dist` folder as `AskForHelp`

#### Option 2: Using PyInstaller directly
```bash
pyinstaller --onefile --windowed --name AskForHelp \
    --add-data "model_config.py:." \
    --add-data "model_behavior_config.py:." \
    --add-data "AI_GUIDANCE.md:." \
    --add-data "MODEL_BEHAVIOR_GUIDE.md:." \
    --add-data "README.md:." \
    --add-data "QUICK_START.md:." \
    --add-data "INSTALLATION_GUIDE.md:." \
    --add-data "FEATURES_SUMMARY.md:." \
    --add-data "PROJECT_SUMMARY.md:." \
    --hidden-import=requests \
    --hidden-import=PIL \
    --hidden-import=tkinter \
    --hidden-import=subprocess \
    --hidden-import=smtplib \
    --hidden-import=email \
    --hidden-import=base64 \
    --hidden-import=io \
    --hidden-import=datetime \
    --hidden-import=threading \
    --hidden-import=platform \
    --hidden-import=socket \
    --hidden-import=json \
    --hidden-import=glob \
    askforhelp_chatbot.py
```

## Build Options

### Console Window
- **--windowed** (Recommended): No console window, GUI only
- **--console**: Shows console window (useful for debugging)

### File Name
- **--name AskForHelp**: Sets the executable name

### Single File
- **--onefile**: Creates a single executable file (recommended)
- Without this option: Creates a folder with multiple files

### Data Files
- **--add-data**: Includes additional files in the executable
- Format: `source;destination` (Windows) or `source:destination` (Linux/macOS)

### Hidden Imports
- **--hidden-import**: Explicitly includes Python modules that might not be detected automatically

## Post-Build Steps

### Windows
1. The executable is located at `dist\AskForHelp.exe`
2. You can copy this file to any Windows machine
3. No Python installation required on target machine

### Linux/macOS
1. The executable is located at `dist/AskForHelp`
2. Make it executable: `chmod +x dist/AskForHelp`
3. You can copy this file to any compatible machine

## Distribution

### Required Components
The executable is self-contained, but the target machine must have:
1. **Ollama installed and running** (for AI model)
2. **Network access** (to connect to Ollama API)

### Installation Instructions for Users
1. Install Ollama from https://ollama.ai/
2. Pull the required model: `ollama pull llama2` (or your preferred model)
3. Start Ollama: `ollama serve`
4. Run AskForHelp.exe

### File Size
- **Windows**: Approximately 50-80 MB (depending on included libraries)
- **Linux/macOS**: Approximately 40-70 MB

## Troubleshooting

### Build Fails
1. **Missing dependencies**: Ensure all required packages are installed
2. **Permission errors**: Run as administrator (Windows) or with sudo (Linux/macOS)
3. **Antivirus interference**: Some antivirus software may block PyInstaller

### Executable Doesn't Start
1. **Check Ollama**: Ensure Ollama is running on localhost:11434
2. **Check model**: Ensure the model specified in model_config.py is available
3. **Check firewall**: Ensure no firewall is blocking the connection

### Missing Files Error
If you get errors about missing files:
1. Ensure all data files are in the same directory as the script
2. Check the --add-data paths in the build command
3. Try building with --console to see error messages

## Customization

### Changing the Icon
1. Create or obtain an .ico file (Windows) or .icns file (macOS)
2. Add to build command: `--icon=path/to/icon.ico`
3. Rebuild the executable

### Including Additional Files
Add more --add-data entries:
```bash
--add-data "additional_file.txt;."
```

### Excluding Modules
If you want to reduce file size:
```bash
--exclude-module matplotlib
--exclude-module numpy
```

## Advanced: Using a Spec File

For complex builds, create a `.spec` file:

1. Generate initial spec file:
   ```bash
   pyi-makespec askforhelp_chatbot.py --onefile --windowed
   ```

2. Edit the generated `askforhelp_chatbot.spec` file

3. Build using the spec file:
   ```bash
   pyinstaller askforhelp_chatbot.spec
   ```

## Build Configuration Examples

### Minimal Build (Smallest Size)
```bash
pyinstaller --onefile --windowed --name AskForHelp ^
    --add-data "model_config.py;." ^
    --add-data "model_behavior_config.py;." ^
    --add-data "AI_GUIDANCE.md;." ^
    --exclude-module matplotlib ^
    --exclude-module numpy ^
    askforhelp_chatbot.py
```

### Full Build (All Features)
```bash
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
```

## Notes

- The executable will be larger than the Python script because it includes all necessary libraries
- Build time can be 1-5 minutes depending on your system
- Always test the executable on a clean machine to ensure it works
- Keep the original Python files for future updates and debugging

## Support

If you encounter issues:
1. Check the troubleshooting section above
2. Review PyInstaller documentation: https://pyinstaller.org/en/stable/
3. Ensure all dependencies are correctly installed
4. Try building with --console to see detailed error messages
'''

    with open('BUILD_INSTRUCTIONS.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print("✓ Created build instructions: BUILD_INSTRUCTIONS.md")

def main():
    """Main build process"""
    print("=" * 60)
    print("AskForHelp Chatbot - Executable Build Process")
    print("=" * 60)
    print()
    
    # Check if running on Windows
    if platform.system() != "Windows":
        print("⚠️  Warning: This build script is optimized for Windows.")
        print("   For Linux/macOS, use build.sh instead.")
        print()
    
    # Check dependencies
    check_dependencies()
    
    # Create build scripts
    print("Creating build scripts...")
    create_build_script()
    create_build_script_linux()
    create_readme_build()
    print()
    
    print("=" * 60)
    print("Build scripts created successfully!")
    print("=" * 60)
    print()
    print("Next steps:")
    print("1. Run 'build.bat' (Windows) or './build.sh' (Linux/macOS)")
    print("2. The executable will be created in the 'dist' folder")
    print("3. See BUILD_INSTRUCTIONS.md for detailed usage")
    print()
    print("Note: The executable requires Ollama to be installed and running")
    print("      on the target machine.")
    print()

if __name__ == "__main__":
    main()
