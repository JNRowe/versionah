Version templates
=================

Version files are created from templates using Jinja_.  Before writing your own
templates you should read the splendid `Jinja template designer`_ documentation.

.. note::

   If you create some cool templates of your own please consider posting them in
   an issue_ or pushing them to a fork on GitHub_, so that others can benefit.

.. _template_locations-label:

Template locations
------------------

Templates are loaded from directories in the following order:

* If it exists, ``${XDG_DATA_HOME:~/.local}/versionah/templates``
* Any :file:`versionah/templates` directory in the directories specified by
  :envvar:`XDG_DATA_DIRS`
* The `versionah` package's ``templates`` directory

.. note::
   For OS X users there is a fallback to ``~/Library/Application Support``,
   if ``XDG_DATA_HOME`` is unset.

Precedence
----------

The first name match in the order :ref:`specified above
<template_locations-label>` selects the template, so a :file:`py.jinja` file in
:file:`${XDG_DATA_HOME}/versionah/templates` overrides the :file:`py.jinja`
template provided with `versionah`.

Naming
------

Templates should be named after the common type suffix if possible, doing so
allows `versionah` to guess an appropriate template from a supplied file.  For
example, ``py.jinja`` will apply by default to all files ending in ``.py``.

However, templates *can* be given any name you wish.  This makes it simple to
have project specific templates, should the need arise.  This functionality is
especially useful if you have shared data as you can use Jinja's
:ref:`template-inheritance` support to reduce the duplication needed in each
template.

Data
----

Each template is provided with the following variables for use in the output:

* ``magic`` for the magic string to support reading `versionah` files
* ``major``, ``minor``, ``micro`` and ``patch`` for the version components
* ``tuple`` all version components as a tuple
* ``resolution`` number of components used by version
* ``name`` for the package name
* ``dateobj`` for release date as a `datetime.date` object
* ``now`` and ``utcnow`` for template creation timestamps, refer to the
  `datetime` documentation for information on :meth:`~datetime.datetime.now` and
  :meth:`~datetime.datetime.utcnow`
* The output file's name as ``filename``
* All supported display methods [#]_, for example ``dotted`` and ``libtool``

Jinja templates support object attribute and method access, so the ``utcnow``
object can be called with the :meth:`~datetime.datetime.strftime` method for
custom timestamp output.  For example, ``{{ utcnow.strftime("%a, %e %b %Y
%H:%M:%S %z") }}`` could be used to output an :rfc:`2822` date stamp [#]_.

The ``text`` display's template is simply:

.. code-block:: jinja

    {{ magic }}

which results in output such as::

    This is mypkg version 2.2.4 (2011-02-19)

If you're authoring your own templates and you find you need extra data for
use in their generation open an issue_.

.. [#] Technically the result of any ``Version`` method beginning with ``as_``
       is passed along to the template, with the ``as_`` prefixes removed.

.. [#] But don't do that, as :meth:`~datetime.datetime.strftime` is locale
       dependent ;)

Filters
-------

`versionah` defines the following filters beyond the huge range of `built-in
filters`_ in Jinja_:

.. note::

   If you write extra filters and believe they could be of use to other
   `versionah` users please consider posting them in an issue_ or pushing them
   to a fork on GitHub_, so that others can benefit from your work.

``regexp``
''''''''''

This filter applies a regular expression to a value, it is a thin wrapper around
:func:`re.sub` and takes the same arguments.

For example, it is used in the C template to make valid identifiers from
``filename`` by replacing invalid characters with underscores:

.. code-block:: jinja

    {% set escaped_name = filename|upper|regexp("[^A-Z]", "_") %}

.. _Jinja: http://jinja.pocoo.org/
.. _Jinja template designer: http://jinja.pocoo.org/docs/templates/
.. _issue: https://github.com/JNRowe/versionah/issues
.. _GitHub: https://github.com/JNRowe/versionah/
.. _mail: jnrowe@gmail.com
.. _built-in filters: http://jinja.pocoo.org/docs/templates/#list-of-builtin-filters
