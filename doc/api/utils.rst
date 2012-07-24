.. currentmodule:: versionah

Utilities
=========

.. note::

  The documentation in this section is aimed at people wishing to contribute to
  `versionah`, and can be skipped if you are simply using the tool from the
  command line.

.. autodata:: STR_TYPE

The following three functions are defined for purely cosmetic reasons, as they
make the calling points easier to read.

.. autofunction:: success

.. autofunction:: fail

.. autofunction:: warn

.. autofunction:: split_version

Examples
--------

.. testsetup::

    from versionah import (fail, success, split_version)

Output formatting
'''''''''''''''''

    >>> success('well done!')
    u'\x1b[38;5;10mwell done!\x1b[m\x1b(B'
    >>> fail('unlucky!')
    u'\x1b[38;5;9munlucky!\x1b[m\x1b(B'

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
