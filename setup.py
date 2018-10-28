#!/usr/bin/env python

from distutils.core import setup

with open('README.md') as readme_file:
    long_description = readme_file.read()

setup(name='Xlinja',
      version='0.1.0',
      description='Jinja2 with MS-Excel',
      long_description=long_description,
      author='Kazufumi Ohkawa',
      author_email='kerolinq@gmail.com',
      url='https://github.com/kzfm/Xlinja',
      packages=['.'],
      install_requires=['click'],
      entry_points={
          'console_scripts':['xlinja=xlinja:cmd'],
        },
      license='MIT',
     )
