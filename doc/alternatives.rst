Alternatives
============

Before diving in and spitting out this package I looked at the alternatives
below.  If I have missed something please drop me a mail_.

shtool
------

shtool_ provides a great version management applet, one which I used for a
number of years in certain projects [#]_ .  Unfortunately, the output formats
are hard-coded in the script making it very difficult to use in most of the
projects I work on.

A few ideas have been borrowed from ``shtool``, and `versionah` should be seen
as a homage to the version applet from ``shtool``.

If you don't need the template support of `versionah` and find the other
functionality ``shtool`` provides useful then I'd strongly recommend using
``shtool``.  There is little point depending on two external projects when one
can suffice.

Since version 0.8.0 it has been possible to parse ``shtool`` generated files,
and you can write ``shtool``-compatible files with v0.14.0 and later.

.. [#] According to the `shtool ChangeLog`_ I used it at least as far back as
   2004 when I contributed M4_ support.

.. _mail: jnrowe@gmail.com
.. _shtool: http://www.gnu.org/software/shtool/shtool.html
.. _shtool ChangeLog: http://www.gnu.org/software/shtool/ChangeLog.txt
.. _M4: http://www.gnu.org/software/m4/m4.html
