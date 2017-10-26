#! /usr/bin/env python
"""setup.py - Setuptools tasks and config for versionah"""
# Copyright © 2011-2017  James Rowe <jnrowe@gmail.com>
#
# This file is part of versionah.
#
# versionah is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# versionah is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# versionah.  If not, see <http://www.gnu.org/licenses/>.

import imp

from sys import version_info

from setuptools import setup
from setuptools.command.test import test


class PytestTest(test):
    def finalize_options(self):
        test.finalize_options(self)
        self.test_args = ['tests/', ]
        self.test_suite = True

    def run_tests(self):
        from sys import exit
        from pytest import main
        exit(main(self.test_args))


# Hack to import _version file without importing versionah/__init__.py, its
# purpose is to allow import without requiring dependencies at this point.
with open('versionah/_version.py') as ver_file:
    _version = imp.load_module('_version', ver_file, ver_file.name,
                               ('.py', ver_file.mode, imp.PY_SOURCE))


def parse_requires(file):
    deps = []
    with open('extra/%s' % file) as req_file:
        entries = [s.split('#')[0].strip() for s in req_file.readlines()]
    for dep in entries:
        if not dep or dep.startswith('#'):
            continue
        elif dep.startswith('-r '):
            deps.extend(parse_requires(dep.split()[1]))
            continue
        elif ';' in dep:
            dep, marker = dep.split(';')
            if not eval(marker.strip(), {
                    'python_version': '%s.%s' % tuple(version_info[:2])
                }):
                continue
        deps.append(dep)
    return deps


install_requires = parse_requires('requirements.txt')

tests_require = parse_requires('requirements-test.txt')

with open("README.rst") as f:
    long_description = f.read()

setup(
    name='versionah',
    version=_version.dotted,
    description="Simple version specification management",
    long_description=long_description,
    author="James Rowe",
    author_email="jnrowe@gmail.com",
    url="https://github.com/JNRowe/versionah",
    license="GPL-3",
    keywords="versioning admin packaging",
    packages=['versionah', ],
    include_package_data=True,
    package_data={
        '': ['versionah/locale/*/LC_MESSAGES/*.mo',
             'versionah/templates/*.jinja', ],
    },
    entry_points={'console_scripts': ['versionah = versionah.cmdline:cli', ]},
    install_requires=install_requires,
    tests_require=tests_require,
    cmdclass={'test': PytestTest},
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Documentation',
        'Topic :: Software Development',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Code Generators',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Version Control',
        'Topic :: System',
        'Topic :: System :: Software Distribution',
        'Topic :: Utilities',
    ],
)
