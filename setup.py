from setuptools import find_packages, setup

setup(name='SalaryCalc',
      version='0.0.1.dev0',
      author='Albert Szostkiewicz',
      author_email='tmdag@tmdag.com',
      description='Calculates Canadian Taxes',
      install_requires=['PyQt5', 'pyqtgraph', 'json'],
      packages=find_packages(),
      zip_safe=False)