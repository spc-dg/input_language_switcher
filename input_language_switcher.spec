# -*- mode: python ; coding: utf-8 -*-


block_cipher = None

from PyInstaller.utils.hooks import collect_submodules

hidden_imports_pynput = collect_submodules('pynput')
hidden_imports_subprocess = collect_submodules('subprocess')
all_hidden_imports = hidden_imports_pynput + hidden_imports_subprocess


a = Analysis(['input_language_switcher.py'],
             pathex=['ath=C:\\Users\\Alexander\\Desktop\\inputswitch_v1', 'C:\\Users\\Alexander\\Desktop\\inputswitch_v1'],
             binaries=[],
             datas=[],
             hiddenimports=all_hidden_imports,
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
          name='input_language_switcher',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
