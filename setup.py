#! /usr/bin/python -tt

from setuptools import setup

from versionah import __version__

setup(
    name='versionah',
    version=__version__,
    url="https://github.com/JNRowe/versionah",
    author="James Rowe",
    author_email="jnrowe@gmail.com",
    classifiers=[
        'Programming Language :: Python',
    ],
    packages=['versionah', ],
    include_package_data=True,
    package_data={'': ['templates/*.jinja', ], },
    entry_points={'console_scripts': ['versionah = versionah:main', ]},
    zip_safe=False,
    install_requires = ['Jinja2>=2'],
)
