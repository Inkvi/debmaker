# -*- coding: utf-8 -*-
from distutils.core import setup

setup(name='debmaker',
      version='0.2',
      description='Tool for generating debian files',
      packages=['debmaker'],
      package_data={'debmaker': ['templates/git/*', 'templates/pypi/*',
                                 'templates/control', 'templates/changelog']},
      scripts=['debmaker/debmaker'],
      )
