Getting started
===============

:file:`Makefile` usage
----------------------

If your project currently uses make_ it is a simple task to add version bumping
rules:

.. sourcecode:: make

  $(addprefix version-, major minor micro):
  	versionah -b $(subst version-,, $@) src/version.h

The above example makes it possible to call :makevar:`version-minor` to bump the
minor version in :file:`src/version.h`.

.. note::

   If you use automake_ then you can use the :token:`PACKAGE_NAME` variable to
   set the :option:`--name` value too.

.. _make: http://www.gnu.org/software/make/make.html
.. _automake: http://sources.redhat.com/automake/
