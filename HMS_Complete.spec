# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['logic.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
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
    name='HMS_Complete',
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
    icon=['keycard.ico'],
)


import os
import sys

# Add all files in the current directory to the executable
files = []
for root, dirpath, filenames in os.walk('.'):
    for file in filenames:
        files.append(os.path.join(root, file))

# Add all files in the subdirectories to the executable
for root, dirpath, filenames in os.walk('images'):
    for file in filenames:
        files.append(os.path.join(root, file))

a = Analysis(['login.py'], pathex=['C:\PythonProjectVSP\Tkinter\Hotel Management System\HMS_Complete'])
pyz = PYZ(a.pure, a.zipped_data,
             cipher=None)
exe = EXE(pyz,
          a.scripts,
          a.binaries + files,
          a.zipfiles,
          a.datas,
          [],
          name='HMS_System',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
