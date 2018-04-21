# salaryCalc
Small tool to calculate Canada, BC tax based on hourly/annual rate.

## Requirements:
This is Python3 code style. It will not work in older Python versions.
Code is using few 3rd party modules like:
- PyPDF2
- pyqtgraph
- PyQT5
- cx_Freeze (for build/compile)

## Usage:
Double click on build version or manually run
```
python3 salarycalc/salaryCalcVFX.py
```
## Installation:
Setup is using cx_Freeze which can build executable on your machine. [cx_Freeze Homepage](http://cx-freeze.readthedocs.io/en/latest/index.html)
```
pip3 install cx_Freeze
python3 setup.py build 
```
## OSX Installation:
```
pip3 install cx_Freeze
python3 setup.py bdist_mac
```
or install packages to run code manually
```
pip3 install PyPDF2, pyqtgraph, numpy, PyQT5
```
![screenshot](https://github.com/tmdag/salaryCalc/blob/master/images/screen.jpg)