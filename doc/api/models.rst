.. currentmodule:: versionah.models

``Version``
===========

.. note::

  The documentation in this section is aimed at people wishing to contribute to
  `versionah`, and can be skipped if you are simply using the tool from the
  command line.

.. autodata:: VALID_PACKAGE
.. autodata:: VALID_VERSION
.. autodata:: VALID_DATE
.. autodata:: VERSION_COMPS

.. autoclass:: Version(components=(0, 1, 0), name='unknown', date=datetime.today())

.. autofunction:: split_version

Examples
--------

.. testsetup::

    import datetime

    from versionah.models import Version, split_version

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

Version string parsing
''''''''''''''''''''''

    >>> split_version('4.3.0')
    (4, 3, 0)
    >>> split_version('4.3.0.1')
    (4, 3, 0, 1)
    >>> split_version('4.3.0.1.3')
    Traceback (most recent call last):
        ...
    ValueError: Invalid version string '4.3.0.1.3'
