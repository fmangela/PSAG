# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(['begin.py'],
             pathex=[r'D:\My_Own_Project\PSAG\src'],
             binaries=[],
             datas=[],  # 包含图片文件的路径和名称
             hiddenimports=['Algorithm_Packet', 'IO_Stream'],  # 替换成你的库包名称，如果有多个用逗号隔开
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
          cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='begin',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )  # 如果你的程序需要在控制台中运行，请设置为True；否则设置为False

app = BUNDLE(exe,
             name='begin',
             icon=None)