#! /usr/bin/python -tt
# coding=utf-8
"""setup.py - Build and installation support"""
# Copyright © 2011, 2012  James Rowe <jnrowe@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import imp

from setuptools import setup

# Hack to import _version file without importing versionah/__init__.py, its
# purpose is to allow import without requiring dependencies at this point.
ver_file = open('versionah/_version.py')
_version = imp.load_module('_version', ver_file, ver_file.name,
                           ('.py', ver_file.mode, imp.PY_SOURCE))

install_requires = map(str.strip, open('extra/requirements.txt').readlines())
colour_requires = map(str.strip,
                      open('extra/requirements-colour.txt').readlines()[1:])

setup(
    name='versionah',
    version=_version.dotted,
    url='http://jnrowe.github.com/versionah/',
    author='James Rowe',
    author_email='jnrowe@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Documentation',
        'Topic :: Software Development',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Code Generators',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Version Control',
        'Topic :: System :: Software Distribution',
        'Topic :: Utilities',

    ],
    packages=['versionah', ],
    include_package_data=True,
    package_data={'': ['templates/*.jinja', ], },
    entry_points={'console_scripts': ['versionah = versionah:main', ]},
    zip_safe=False,
    install_requires=install_requires,
    extras_require={
        'colour': colour_requires,
        'color': colour_requires,
    },
)
