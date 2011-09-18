.. currentmodule:: versionah

``Version``
===========

.. autodata:: VALID_PACKAGE
.. autodata:: VALID_VERSION
.. autodata:: VALID_DATE

.. autoclass:: Version(components=(0, 1, 0), name='unknown', date=datetime.today())

Examples
--------

.. testsetup::

    import datetime

    from versionah import Version

Reading version data from a file
''''''''''''''''''''''''''''''''

    >>> Version.read('tests/data/test_a')
    Version((0, 1, 0), 'test', datetime.date(2011, 2, 19))
    >>> Version.read('tests/data/test_b')
    Version((1, 0, 0), 'test', datetime.date(2011, 2, 19))
    >>> Version.read('tests/data/test_c')
    Version((2, 1, 3), 'test', datetime.date(2011, 2, 19))


Writing version date to a file
''''''''''''''''''''''''''''''

    >>> v = Version((0, 1, 0), 'test', datetime.date(2011, 2, 19))
    >>> v.write('test_data.python', 'py')  # doctest: +SKIP
    >>> v.write('test_data.hh', 'h')  # doctest: +SKIP
    >>> v.write('test_data.m4', 'm4')  # doctest: +SKIP

Bumping a version component
'''''''''''''''''''''''''''

    >>> v = Version((0, 1, 0), 'test', datetime.date(2011, 2, 19))
    >>> v.bump('minor')
    >>> v.components
    (0, 2, 0)
    >>> v.bump('major')
    >>> v.components
    (1, 0, 0)
    >>> v.bump_major()
    >>> v.components
    (2, 0, 0)
