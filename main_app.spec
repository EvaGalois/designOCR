# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['main_app.py'],
    pathex=[],
    binaries=[
        ('ppocr/PaddleOCR-json.exe', 'ppocr'),
        (r'D:\Scoop\apps\mambaforge\current\envs\checkOCR\Lib\site-packages\PyQt5\Qt5\bin\QtWebEngineProcess.exe', 'QtWebEngineProcess.exe'),
        (r'D:\Scoop\apps\mambaforge\current\envs\checkOCR\Library\bin\Qt5Core_conda.dll', 'Qt5Core_conda.dll')
        ],
    datas=[],
    hiddenimports=['encodings', 'encodings.*'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='main_app',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,  # 设置为True以便查看任何错误或消息
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='main_app',
)