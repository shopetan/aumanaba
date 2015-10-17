#!/usr/bin/env python
# coding: utf-8
from setuptools import setup, find_packages
from pip_github_test import __author__, __version__, __license__

setup(
    name             = 'aumanaba',
    version          = __version__,
    description      = 'python library from github using pip',
    license          = __license__,
    author           = __author__,
    author_email     = 'shoppe_shopetan@yahoo.co.jp',
    url              = 'https://github.com/shopetan/aumanaba.git',
    keywords         = 'pip github python manaba login',
    packages         = find_packages(),
    install_requires = [],
)
