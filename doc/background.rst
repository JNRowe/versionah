Background
==========

I maintain a large number of projects, both my toy stuff on GitHub_ and more
serious things at the office.  While skipping around in my editor to increase a
micro version number I came to the realisation that I shouldn't be doing this
manually.

Bumping or querying version numbers should be a zero thought process, I
shouldn't need to remember the abbr:`RegExp (Regular Expression)` needed to make
my editor jump to version identifier in a particular file type.  I shouldn't
need to resort to various :kbd:`C-a` and :kbd:`C-x` in vim_ or formulating
complicated lisp functions with ``number-to-string`` and ``string-to-number``
in emacs_.

And now :mod:`versionah` is born, I should be able to realise those dreams!

Version numbers
===============

This, for some, is a very complicated topic but not for me.  Versions numbers
are made of three components; major, minor and micro.  All three components are
natural numbers, there are no exceptions.

If you find version numbers like 0.6c11 acceptable then :mod:`versionah` is not
for you.

.. note::

   If you like version numbers with two or four integer components then
   :mod:`versionah` can be for you too.  If I start maintaining a project that
   uses such a scheme support will be added, or if you supply a patch it will
   likely be accepted.

.. _GitHub: https://github.com/JNRowe/
.. _vim: http://www.vim.org/
.. _emacs: http://www.gnu.org/software/emacs/
