.. currentmodule:: versionah.vcs

Version control support
=======================

.. note::

  The documentation in this section is aimed at people wishing to contribute to
  `versionah`, and can be skipped if you are simply using the tool from the
  command line.

.. autoclass:: VCS
.. autoclass:: Git
.. autoclass:: Mercurial
.. autoclass:: Fossil

.. autodata:: SUPPORTED_VCS
   :annotation: = {name: sh.Command instance, ...}

Examples
--------

.. testsetup::

    from versionah.vcs import Git

Creating a commit
'''''''''''''''''

    >>> g = Git()
    >>> g.add(['file1', 'file2'])  # doctest: +SKIP
    >>> g.commit(['file1', 'file2'], 'commit message')  # doctest: +SKIP
