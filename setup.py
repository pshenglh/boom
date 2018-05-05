#encoding:utf8
import sys
from cx_Freeze import setup, Executable

build_exe_option = {'packages': [], 'excludes': []}

setup(name='数据处理',
      version='0.1',
      description='...',
      options={'build_exe': build_exe_option},
      executables=[Executable('boom.py', base='Win32GUI')])