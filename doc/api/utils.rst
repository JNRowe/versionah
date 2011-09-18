.. currentmodule:: versionah

Utilties
========

.. autodata:: STR_TYPE
.. data:: colored(bool)

   :const:`True` if :pypi:`termcolor` is available and `sys.stdout` is a TTY.

The following three functions are defined for purely cosmetic reasons, as they
make the calling points easier to read.

.. autofunction:: success

   Produce green text, if possible(see :data:`colored`).

.. autofunction:: fail

   Produce red text, if possible(see :data:`colored`).

.. autofunction:: warn

   Produce yellow text, if possible(see :data:`colored`).

.. autofunction:: split_version

Examples
--------

Output formatting
'''''''''''''''''

    >>> success('well done!')
    '\x1b[32mwell done!\x1b[0m'
    >>> fail('unlucky!')
    '\x1b[31munlucky!\x1b[0m'

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
