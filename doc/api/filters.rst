.. currentmodule:: versionah

Jinja filters
=============

.. autodata:: FILTERS

   A `dict` mapping custom filter names to their functions.  For help with
   writing your own custom filter functions see Jinja's excellent `custom
   filter`_ documentation.

.. autofunction:: filter_regexp

.. _custom filter: http://jinja.pocoo.org/docs/api.html#custom-filters

Examples
--------

.. testsetup::

    import re

    from versionah import filter_regexp

.. doctest::

    >>> filter_regexp('valid keyword',  '[^A-Z]', '_', flags=re.IGNORECASE)
    'valid_keyword'
    >>> filter_regexp('De-voweled',  '[aeiou]', '')
    'D-vwld'
