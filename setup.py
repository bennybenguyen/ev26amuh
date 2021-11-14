from distutils.core import setup
from setuptools import find_packages

setup(name='idm-id',
      version='0.1',
      author='Benny Nguyen',
      author_email='benny.nguyen',
      packages=find_packages(),
      install_requires=['numpy', 'Pillow', 'ipywidgets','matplotlib'])
