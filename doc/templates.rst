Version templates
=================

Version files are created from templates using Jinja_.  Templates are loaded in
the following order:

* If it exists, :file:`${XDG_DATA_HOME:~/.local}/versionah/templates`
* Any :file:`versionah/templates` directory in the directories specified by
  :envvar:`XDG_DATA_DIRS`
* The package's ``templates`` directory

For information on the usage of :envvar:`XDG_DATA_HOME` and
:envvar:`XDG_DATA_DIRS` read `XDG Base Directory Specification`_

If you create some cool templates of your own please consider posting them in an
issue_ or pushing them to a fork on GitHub_, so that others can benefit.

Precedence
----------

The first name match in the order specified above selects the template, so a
:file:`py.jinja` in :file:`${XDG_DATA_HOME:~/.local}/versionah/templates`
overrides :file:`py.jinja` provided by :mod:`versionah`.

Naming
------

Templates should be named after the common type suffix if possible, doing so
allows :mod:`versionah` to guess an appropriate template from a supplied file.
For example, ``py.jinja`` will apply by default to all files ending in ``.py``.

Data
----

Each template is provided with the following data for use in templates:

* ``magic`` for the magic string to support reading :mod:`versionah` files
* ``major``, ``minor``, ``micro`` and ``patch`` for the version components
* ``name`` for the package name
* ``dateobj`` for release date as a :py:func:`datetime.date` object
* The output file's name as ``filename``
* All display methods [#]_, for example ``dotted`` and ``libtool``

Jinja templates support object attribute and method access, so the ``date``
object can be called with a ``strftime`` method for custom date output.  For
example, ``{{ date.strftime("%a, %e %b %Y %H:%M:%S %z") }}`` can be used to
output an :rfc:`2822` date stamp.

The ``text`` display's template is simply:

.. code-block:: jinja

    {{ magic }}

which would result in output such as::

    This is mypkg version 2.2.4 (2011-02-19)

If you're authoring your own templates and you find you need extra data for
their generation drop me a mail_.

.. [#] Technically the result of any ``Version`` method beginning with ``as_``
       is included.

Filters
-------

:mod:`versionah` defines the following filters beyond the `built-in filters` of
Jinja_:

``regexp``
----------

This filter applies a regular expression to a value, it is a thin wrapper around
:py:func:`re.sub` and takes the same arguments.

.. _Jinja: http://jinja.pocoo.org/
.. _XDG Base Directory Specification: http://standards.freedesktop.org/basedir-spec/basedir-spec-latest.html
.. _issue: https://github.com/JNRowe/versionah/issues
.. _GitHub: https://github.com/JNRowe/versionah/
.. _mail: jnrowe@gmail.com
.. _built-in filters: http://jinja.pocoo.org/docs/templates/#list-of-builtin-filters
