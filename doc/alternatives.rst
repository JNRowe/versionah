Alternatives
============

Before diving in and spitting out this package I looked at the alternatives
below.  If I have missed something please drop me a mail_.

shtool
------

shtool_ provides a great version management applet, one which I used for many
years in various projects [#]_.  Unfortunately, the output formats are
hard-coded in the script making it extremely difficult to use in the projects
I work on.

A few ideas have been borrowed from ``shtool``, and |progref| should be seen as
a homage to the version applet from ``shtool``.

If you don’t need the template support of |progref| and find the other
functionality ``shtool`` provides useful, then I’d strongly recommend using
``shtool``.  There is little point depending on two external projects when one
can suffice.

Since version 0.8.0 of |progref| it has been possible to parse ``shtool``
generated files [#]_.  You can also write ``shtool``-compatible files with
|progref| v0.14.0 and later [#]_, see the :option:`versionah bump --shtool`
documentation.

.. rubric:: Footnotes

.. [#] According to the `shtool ChangeLog`_ I used it at least as far back as
   2004 when I contributed M4_ support, and I didn’t spike |progref| until
   2011.

.. [#] 0.8.0 was the release I cut to as I started to migrate existing projects
   that used ``shtool``.

.. [#] 0.14.0 was the release I cut to support a project that didn’t want to
   migrate to |progref|, where I had already become accustomed to |progref|’s
   interface in the intervening three months.

.. _mail: jnrowe@gmail.com
.. _shtool: http://www.gnu.org/software/shtool/shtool.html
.. _shtool ChangeLog: http://www.gnu.org/software/shtool/ChangeLog.txt
.. _M4: http://www.gnu.org/software/m4/m4.html
