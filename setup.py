#!/usr/bin/env python

from distutils.core import setup

setup(name='simple21',
      version='1.0',
      description='Simple21Tree: A tree of #Hashtags to increase obviousness',
      author='Thomas Güttler',
      author_email='guettli.simple21@thomas-guettler.de',
      url='https://github.com/guettli/simple21tree/',
      packages=['simple21'],
      install_requires=[
            'Django>=3.0.3',
            'django-mptt>=0.11.0',
      ],
      )
