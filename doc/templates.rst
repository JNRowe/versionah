Version templates
=================

Version files are created from templates using Jinja_.  Templates are loaded
from the package's ``templates`` directory, and if it exists also from
``${XDG_DATA_HOME:~/.local}/versionah/templates``.

If you create some cool templates of your own please consider posting them in an
issue_ or pushing them to a fork on GitHub_, so that others can benefit.

Data
----

Each template is provided with the following data for use in templates:

* ``magic`` for the magic string to support reading :mod:`versionah` files
* ``major``, ``minor`` and ``micro`` for the version components
* ``name`` for the package name
* The output file's name as ``filename``
* All display methods [#]_, for example ``triple`` and ``libtool``

The ``text`` display's template is simply:

.. code-block:: jinja

    {{ magic }}

which would result in output such as::

    This is mypkg version 2.2.4 (2011-02-19)

If you're authoring your own templates and you find you need extra data for
their generation drop me a mail_.

.. [#] Technically the result of any ``Version`` method beginning with ``as_``
       is included.

.. _Jinja: http://jinja.pocoo.org/
.. _issue: http://github.com/JNRowe/versionah/issues
.. _GitHub: http://github.com/JNRowe/versionah/
.. _mail: jnrowe@gmail.com
