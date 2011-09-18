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
