#! /usr/bin/python -tt

import imp

from setuptools import setup

# Hack to import _version file without importing versionah/__init__.py, its
# purpose is to allow import without requiring dependencies at this point.
ver_file = open("versionah/_version.py")
_version = imp.load_module("_version", ver_file, ver_file.name,
                           (".py", ver_file.mode, imp.PY_SOURCE))

setup(
    name='versionah',
    version=_version.dotted,
    url="http://jnrowe.github.com/versionah/",
    author="James Rowe",
    author_email="jnrowe@gmail.com",
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
    install_requires = ['Jinja2>=2'],
)
