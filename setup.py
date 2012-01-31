# -*- coding: utf-8 -*-
from distutils.core import setup

setup(name='debmaker',
      version='0.1',
      description='Tool for generating debian files',
      packages=['debmaker'],
      package_data = {'debmaker': ['templates/git/*','templates/pypi/*']},
      scripts=['debmaker/debmake'],
)
