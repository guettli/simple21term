#!/usr/bin/env python

from distutils.core import setup

setup(name='xyz',
      version='1.0',
      description='What and who tree',
      author='Thomas Güttler',
      author_email='guettli.xyz@thomas-guettler.de',
      url='https://github.com/guettli/xyz/',
      packages=['xyz'],
      install_requires=['Django>=3.0.3', 'django-mptt>=0.11.0'],
      )
