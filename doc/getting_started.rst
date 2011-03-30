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

.. code-block:: make

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

.. code-block:: make

    $(LIBRARY_NAME): $(LIBRARY_OBJS)
        $(LIBTOOL) --mode=link $(CC) -o $(LIBRARY_NAME) $(LIBRARY_OBJS) \
            -rpath $(libdir) \
            -version-info `versionah -d libtool src/version.h`

Using the version information as the ``libtool`` interface age requires strict
practise in maintaining the semantics of your version data, but doing so
provides significant value to your users even if they aren't using the library
interface.

``Sphinx`` example
------------------

If you generate your project's documentation using Georg Brandl's excellent
Sphinx_ tool, then you have a few options for including the version information.

Import the data
'''''''''''''''

If you're storing your version data in Python_ format then you can simply import
the file, and access the data directly in your :file:`conf.py`::

    from versionah import _version
    # The short X.Y version.
    version = ".".join(_version.tuple[:2])
    # The full version
    release = _version.dotted

You may need to mangle :py:data:`sys.path` if you can't import the version file
from your :file:`conf.py`.  For example, in :mod:`versionah`'s :file:`conf.py`
we add the project root directory to :py:data:`sys.path` with the following
snippet::

    root_dir = os.path.sep.join(os.path.realpath(__file__).split(os.path.sep)[:-2])
    sys.path.insert(0, root_dir)

Use the :command:`versionah` output
'''''''''''''''''''''''''''''''''''

Another option is to call :command:`versionah` inside your :file:`conf.py`::

    import subprocess
    # The full version
    release = subprocess.check_output(["versionah", "../versionah/_version.py"])
    # The short X.Y version.
    version = ".".join(release.split(".")[:2])

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
.. _Sphinx: http://sphinx.pocoo.org/
.. _Python: http://www.python.org/
.. _perl: http://www.perl.org/
