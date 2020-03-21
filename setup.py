#!/usr/bin/env python

from distutils.core import setup

setup(name='zero21',
      version='1.0',
      description='Zero21Tree: A tree of #Hashtags to increase obviousness',
      author='Thomas Güttler',
      author_email='guettli.zero21@thomas-guettler.de',
      url='https://github.com/guettli/zero21tree/',
      packages=['zero21'],
      install_requires=[
            'Django>=3.0.3',
            'django-mptt>=0.11.0',
            'django-sitetree',
      ],
      )
