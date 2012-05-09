.. currentmodule:: versionah

Command line
============

.. note::

  The documentation in this section is aimed at people wishing to contribute to
  `versionah`, and can be skipped if you are simply using the tool from the
  command line.

.. autodata:: USAGE

.. autofunction:: process_command_line(argv=sys.argv[1:])
.. autofunction:: main(argv=sys.argv)

Examples
--------

.. testsetup::

    from versionah import process_command_line

Parsing command line options
''''''''''''''''''''''''''''

    >>> process_command_line(['test.py', ])
    (<Values at ...: {'file_type': 'py', 'bump': None, 'display_format': 'dotted', 'set': None, 'name': None}>, 'test.py')
    >>> process_command_line(['-t', 'h', 'test', ])
    (<Values at ...: {'file_type': 'h', 'bump': None, 'display_format': 'dotted', 'set': None, 'name': None}>, 'test')