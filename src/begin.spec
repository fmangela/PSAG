# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['begin.py'],
    pathex=[],
    binaries=[],
    datas=[('image', 'image')],
    hiddenimports=['Algorithm_Packet', 'IO_Stream', 'UI_initialize'],
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
    a.binaries,
    a.datas,
    [],
    name='小学算数题生成器_v0.1.1021',
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
    icon=['image\\calcu.ico'],
)
