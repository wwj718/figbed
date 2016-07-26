#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    "qiniu"
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='figbed',
    version='0.1.5',
    description="figbed is an easy to use fig bed when you writing with markdown",
    long_description=readme + '\n\n' + history,
    author="wenjie wu",
    author_email='wuwenjie718@gmail.com',
    url='https://github.com/wwj718/figbed',
    packages=[
        'figbed',
    ],
    package_dir={'figbed':
                 'figbed'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD license",
    zip_safe=False,
    keywords='figbed',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    entry_points={
         'console_scripts': [
                         'figbed = figbed.figbed:main'
            ]
        },
    tests_require=test_requirements
)
