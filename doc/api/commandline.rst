.. currentmodule:: versionah

Command line
============

.. note::

  The documentation in this section is aimed at people wishing to contribute to
  `versionah`, and can be skipped if you are simply using the tool from the
  command line.

.. autoclass:: ValidatingAction

.. autofunction:: guess_type
.. autofunction:: bump_version
.. autofunction:: set_version
.. autofunction:: display
.. autofunction:: main(argv=sys.argv)

Examples
--------

.. testsetup::

    from versionah import guess_type

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
