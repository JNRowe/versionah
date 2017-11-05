.. currentmodule:: versionah.cmdline

Command line
============

.. note::

  The documentation in this section is aimed at people wishing to contribute to
  `versionah`, and can be skipped if you are simply using the tool from the
  command line.

.. autoclass:: NameParamType
.. autoclass:: VersionParamType

.. autoclass:: CliVersion

.. autofunction:: guess_type
.. autofunction:: bump
.. autofunction:: set_version
.. autofunction:: display
.. autofunction:: cli

Examples
--------

.. testsetup::

    import datetime

    from versionah.cmdline import CliVersion, guess_type

Reading version data from a file
''''''''''''''''''''''''''''''''

    >>> CliVersion.read('tests/data/test_a')
    CliVersion((0, 1, 0), 'test', datetime.date(2011, 2, 19))
    >>> CliVersion.read('tests/data/test_b')
    CliVersion((1, 0, 0), 'test', datetime.date(2011, 2, 19))
    >>> CliVersion.read('tests/data/test_c')
    CliVersion((2, 1, 3), 'test', datetime.date(2011, 2, 19))

Writing version date to a file
''''''''''''''''''''''''''''''

    >>> v = CliVersion((0, 1, 0), 'test', datetime.date(2011, 2, 19))
    >>> v.write('test_data.python', 'py')  # doctest: +SKIP
    >>> v.write('test_data.hh', 'h')  # doctest: +SKIP
    >>> v.write('test_data.m4', 'm4')  # doctest: +SKIP

Guess file type from name
'''''''''''''''''''''''''

    >>> guess_type('main.c')
    'c'
    >>> guess_type('version.py')
    'py'
    >>> guess_type('no_suffix')
    'text'
    >>> guess_type('suffix.unknown')
    'text'
