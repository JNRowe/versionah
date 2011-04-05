Version templates
=================

Version files are created from templates using Jinja_.  Before writing your own
templates you should read the awesome `Jinja template designer`_ documentation.

Template locations
------------------

Templates are loaded from directories in the following order:

* If it exists, :file:`${XDG_DATA_HOME:~/.local}/versionah/templates`
* Any :file:`versionah/templates` directory in the directories specified by
  :envvar:`XDG_DATA_DIRS`
* The package's ``templates`` directory

For information on the usage of :envvar:`XDG_DATA_HOME` and
:envvar:`XDG_DATA_DIRS` read `XDG Base Directory Specification`_

.. note::

   If you create some cool templates of your own please consider posting them in
   an issue_ or pushing them to a fork on GitHub_, so that others can benefit.

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

However, templates *can* be given any name you wish.  This makes it simple to
have project specific templates, should the need arise.  This functionality is
especially useful if you have shared data as you can use Jinja's ``extends`` tag
to reduce the duplication needed in each template.

Data
----

Each template is provided with the following variables for use in the output:

* ``magic`` for the magic string to support reading :mod:`versionah` files
* ``major``, ``minor``, ``micro`` and ``patch`` for the version components
* ``tuple`` all version components as a tuple
* ``resolution`` number of components used by version
* ``name`` for the package name
* ``dateobj`` for release date as a :py:func:`datetime.date` object
* The output file's name as ``filename``
* All display methods [#]_, for example ``dotted`` and ``libtool``

Jinja templates support object attribute and method access, so the ``date``
object can be called with a ``strftime`` method for custom date output.  For
example, ``{{ dateobj.strftime("%a, %e %b %Y %H:%M:%S %z") }}`` can be used to
output an :rfc:`2822` date stamp.

The ``text`` display's template is simply:

.. code-block:: jinja

    {{ magic }}

which results in output such as::

    This is mypkg version 2.2.4 (2011-02-19)

If you're authoring your own templates and you find you need extra data for
their generation drop me a mail_.

.. [#] Technically the result of any ``Version`` method beginning with ``as_``
       is passed along to the template, with the ``as_`` prefixes removed.

Filters
-------

:mod:`versionah` defines the following filters beyond the huge range `built-in
filters` of Jinja_:

.. note::

   If you write extra filters that you believe could be of use to other
   :mod:`versionah` users please consider posting them in an issue_ or pushing
   them to a fork on GitHub_, so that others can benefit from your work.

``regexp``
''''''''''

This filter applies a regular expression to a value, it is a thin wrapper around
:py:func:`re.sub` and takes the same arguments.

For example, it is used in the C template to make valid identifiers from
``filename`` by replacing invalid characters with underscores:

.. code-block:: jinja

    {% set escaped_name = filename|upper|regexp("[^A-Z]", "_") %}

.. _Jinja: http://jinja.pocoo.org/
.. _Jinja template designer: http://jinja.pocoo.org/docs/templates/
.. _XDG Base Directory Specification: http://standards.freedesktop.org/basedir-spec/basedir-spec-latest.html
.. _issue: https://github.com/JNRowe/versionah/issues
.. _GitHub: https://github.com/JNRowe/versionah/
.. _mail: jnrowe@gmail.com
.. _built-in filters: http://jinja.pocoo.org/docs/templates/#list-of-builtin-filters
