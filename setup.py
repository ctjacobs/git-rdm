#!/usr/bin/env python

from distutils.core import setup

setup(name='git-rdm',
      version='1.0',
      description='Git-RDM is a research data management plugin for the Git version control system.',
      author='Christian T. Jacobs',
      author_email='christian@christianjacobs.uk',
      url='https://github.com/ctjacobs/git-rdm',
      scripts=["git-rdm"],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Intended Audience :: Science/Research',
          'Natural Language :: English',
          'Programming Language :: Python',
      ]
      )
