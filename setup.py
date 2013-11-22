#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from distutils.core import setup

if sys.version_info < (2,5):
    raise NotImplementedError("Sorry, you need at least Python 2.5 or Python 3.x to use bottle.")

import bottle

setup(name='kholloscope',
      version=bottle.__version__,
      description="Petit framework pour grand kholloscope.",
      long_description=bottle.__doc__,
      author=bottle.__author__,
      author_email='network@colombaro.fr',
      url='https://github.com/LeoColomb/kholloscope',
      py_modules=['bottle'],
      scripts=['kholloscope.py'],
      license='MIT',
     )


