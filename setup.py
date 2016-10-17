# Copyright (C) 2016 Glamping Hub (https://glampinghub.com)
# License: BSD 3-Clause

import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

setup(
    name='django-keyrock',
    version='0.0.2',
    author='Glamping Hub',
    author_email='it@glampinghub.com',
    packages=find_packages('.'),
    include_package_data=True,
    package_data={'': ['LICENSE']},
    url='https://github.com/Glamping-Hub/django-keyrock',
    license='BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2 :: Only',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet'
    ],
    description='KeyRock Identity Manager client for Django',
    keywords='keyrock idm identity django',
    long_description=open('README.md').read(),
    requires=[
        'Django (>=1.5.0)',
        'requests (>=2.0.0)',
        'requests_oauthlib (>=0.6.0)',
    ],
)
