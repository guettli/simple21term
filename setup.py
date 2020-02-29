#!/usr/bin/env python

from distutils.core import setup

setup(name='whatandwhotree',
      version='1.0',
      description='What and who tree',
      author='Thomas Güttler',
      author_email='guettli.whatandwhotree@thomas-guettler.de',
      url='https://github.com/guettli/whatandwhotree/',
      packages=['whatandwhotree'],
      install_requires=['Django>=3.0.3', 'django-mptt>=0.11.0'],
      )
