# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['askforhelp_chatbot.py'],
    pathex=[],
    binaries=[],
    datas=[('model_config.py', '.'), ('model_behavior_config.py', '.'), ('AI_GUIDANCE.md', '.'), ('MODEL_BEHAVIOR_GUIDE.md', '.'), ('README.md', '.'), ('QUICK_START.md', '.'), ('INSTALLATION_GUIDE.md', '.'), ('FEATURES_SUMMARY.md', '.'), ('PROJECT_SUMMARY.md', '.')],
    hiddenimports=['requests', 'PIL', 'tkinter', 'subprocess', 'smtplib', 'email', 'base64', 'io', 'datetime', 'threading', 'platform', 'socket', 'json', 'glob'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='AskForHelp',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
