#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from thumbor_filter_keep_ratio import __version__

setup(
    name='thumbor_filter_keep_ratio',
    version=__version__,
    description='A filter for Thumbor for resizing keeping aspect ratio',
    long_description='''
A Thumbor filter that resizes the image while allowing it to be less than the
provided request height and width, but always keeping the aspect ratio.
''',
    keywords='thumbor filter',
    author='single.dk',
    author_email='dev@single.dk',
    url='https://github.com/babelhq/thumbor-filter-keep-ratio',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
    ],
    packages=find_packages(),
    include_package_data=True,
)
