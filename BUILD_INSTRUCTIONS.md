# Building AskForHelp Executable

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
pyinstaller --onefile --windowed --name AskForHelp     --add-data "model_config.py:."     --add-data "model_behavior_config.py:."     --add-data "AI_GUIDANCE.md:."     --add-data "MODEL_BEHAVIOR_GUIDE.md:."     --add-data "README.md:."     --add-data "QUICK_START.md:."     --add-data "INSTALLATION_GUIDE.md:."     --add-data "FEATURES_SUMMARY.md:."     --add-data "PROJECT_SUMMARY.md:."     --hidden-import=requests     --hidden-import=PIL     --hidden-import=tkinter     --hidden-import=subprocess     --hidden-import=smtplib     --hidden-import=email     --hidden-import=base64     --hidden-import=io     --hidden-import=datetime     --hidden-import=threading     --hidden-import=platform     --hidden-import=socket     --hidden-import=json     --hidden-import=glob     askforhelp_chatbot.py
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
