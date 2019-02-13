#!/usr/bin/env python

#from distutils.core import setup
from setuptools import setup, find_packages


setup(name='debugsql',
      version='0.20160102',
      description='Tool to pretty-print sql via sqlalchemy/django in pdb or clipse/pycharm console',
      author=u'Lukasz Mach',
      author_email='lukasz.mach@pagema.net',
      url='http://pagema.net',
      scripts=[],
      license="BSD3",
      keywords="debug sql eclipse console sqlalchemy django",
      packages=find_packages(),
      install_requires=['docutils>=0.3', "prettytable"],
      package_data={},
    )
