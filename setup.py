#!/usr/bin/env python

import sys

from setuptools import setup, find_packages


readme = open('README').read()

long_description = """Simple snake game using Qt."""

setup(
    name='BattleSnake',
    version='0.01',
    description=long_description,
    long_description=long_description,
    author='Hung Dinh',
    packages=find_packages(),
    test_suite='nose.collector',
    tests_require=['nose'],
    install_requires=['PySide'],
    classifiers=[
    ],
)
