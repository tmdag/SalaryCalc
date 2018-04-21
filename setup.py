
import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

options = {
    'build_exe': {
        'includes': ['atexit'],
        'excludes': ['gtk', 'Tkinter']
    }
}

executables = [
    Executable('salarycalc/SalaryCalcVFX.py', base=base)
]

setup(name='SalaryCalc',
      version='0.0.1.dev0',
      author='Albert Szostkiewicz',
      author_email='tmdag@tmdag.com',
      description='Calculates Canadian Taxes',
      install_requires=['PyQt5', 'pyqtgraph', 'json'],
      options=options,
      executables=executables
      packages=find_packages(),
      zip_safe=False)