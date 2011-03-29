Getting started
===============

Initial setup
-------------

The first time we run :command:`versionah` we must supply the initial version
number, and optionally a name for the package:

.. code-block:: sh

    ▶ versionah -t c -s0.2.0 src/version.h
    0.2.0
    ▶ versionah -t c -s0.2.0 -n my_app src/version.h
    0.2.0

:file:`Makefile` usage
----------------------

If your project currently uses make_ it is a simple task to add version bumping
rules:

.. sourcecode:: make

    $(addprefix version-, major minor micro):
        versionah -b $(subst version-,, $@) src/version.h

The above example makes it possible to call :makevar:`version-minor` to bump the
minor component in :file:`src/version.h`.

.. note::

   If you use automake_ then you can use the :makevar:`PACKAGE_NAME` variable to
   set the :option:`--name` value.

``libtool`` example
-------------------

It is quite easy to use the versioning information for libtool_ build rules in
make_ files:

.. sourcecode:: make

    $(LIBRARY_NAME): $(LIBRARY_OBJS)
        $(LIBTOOL) --mode=link $(CC) -o $(LIBRARY_NAME) $(LIBRARY_OBJS) \
            -rpath $(libdir) \
            -version-info `versionah -d libtool src/version.h`

:command:`pod2man` example
--------------------------

If you generate your documentation using perl_'s :command:`pod2man` then a
sample :file:`Makefile` rule to include your program's version information would
be:

.. sourcecode:: make

    man.1: man.pod
        pod2man --section=1 --release="`versionah -d dotted src/version.h`" \
            --date="`versionah -d date src/version.h`" $< $@

.. _make: http://www.gnu.org/software/make/make.html
.. _automake: http://sources.redhat.com/automake/
.. _libtool: http://www.gnu.org/software/libtool/
.. _perl: http://www.perl.org/
