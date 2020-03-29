#!/usr/bin/env python

from distutils.core import setup

setup(name='simpe21',
      version='1.0',
      description='Simple21Tree: A tree of #Hashtags to increase obviousness',
      author='Thomas Güttler',
      author_email='guettli.simpe21@thomas-guettler.de',
      url='https://github.com/guettli/simpe21tree/',
      packages=['simpe21'],
      install_requires=[
            'Django>=3.0.3',
            'django-mptt>=0.11.0',
            'django-sitetree',
      ],
      )
