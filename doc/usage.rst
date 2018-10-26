Usage
=====

.. highlight:: console

The |progref| script is the main workhorse of the :mod:`versionah` module.

Let’s start with some basic examples::

    $ versionah display _version.py  # Read the version data from _version.py
    2.4.3
    $ versionah bump _version.py minor  # Bump the minor component
    2.5.0
    $ versionah bump _version.py major  # Bump the major component
    3.0.0

    $ versionah set _version.rb 0.2.0  # Set the version in _version.rb to 0.2.0
    0.2.0

    $ versionah bump _version.h minor  # Bump the minor component in _version.h
    0.4.0


.. click:: versionah.cmdline:cli
   :prog: versionah
   :show-nested:
