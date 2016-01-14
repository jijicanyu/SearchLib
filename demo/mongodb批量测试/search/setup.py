#!/usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup, find_packages
 
__version__ = '0.0.1'
__author__ = 'tdifg'
__email__ = 'ymmxza@gmail.com'

setup(
     name='SearchLib',
     version=__version__,
     url='https://github.com/tdifg/search',
     keywords= ('searchlib','zoomeye'),
     license='BSD',
     author=__author__,
     author_email=__email__,
     description='Easy to use search lib for all the search engines',
     packages=find_packages(exclude=['.', '.*']),
     include_package_data=True,
     zip_safe=False,
     platforms='any',
     install_requires=['lxml == 3.4.4','pymongo == 3.0.3','requests == 2.7.0','selenium == 2.47.3'],
    )
