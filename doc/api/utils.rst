.. module:: versionah.utils

Utilities
=========

.. note::

  The documentation in this section is aimed at people wishing to contribute to
  `versionah`, and can be skipped if you are simply using the tool from the
  command line.

The following three functions are defined for purely cosmetic reasons, as they
make the calling points easier to read.

.. autofunction:: success

.. autofunction:: fail

.. autofunction:: warn

Examples
--------

.. testsetup::

    from versionah.utils import fail, success

Output formatting
'''''''''''''''''

    >>> success('well done!')  # doctest: +SKIP
    '\x1b[38;5;10mwell done!\x1b[m\x1b(B'
    >>> fail('unlucky!')  # doctest: +SKIP
    '\x1b[38;5;9munlucky!\x1b[m\x1b(B'
