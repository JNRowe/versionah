``versionah``` - Simple version specification management
========================================================

Introduction
------------

``versionah`` is a `GPL v3`_ licensed module for maintaining version information
files for use in project management.

Requirements
------------

``versionah`` should run on Python_ v2.5 or newer.  The only external library
``versionah`` currently depends on is jinja_.  If ``versionah`` doesn't work
with the version of Python you have installed, file an issue_ and I'll endeavour
to fix it.

Example
-------

The simplest way to show how ``versionah`` works is by example::

    ▶ versionah.py _version.py
    2.4.3
    ▶ versionah.py -b minor _version.py
    2.5.0
    ▶ versionah.py -b major _version.py
    3.0.0

API Stability
-------------

API stability isn't guaranteed across versions, although frivolous changes won't
be made.

When ``versionah`` 1.0.0 is released the API will be frozen, and any changes
which aren't backwards compatible will force a major version bump.

Bugs
----

If you find any problems, bugs or just have a question about this package either
file an issue_ or drop me a mail_.

If you've found a bug please attempt to include a minimal testcase so I can
reproduce the problem, or even better a patch!

.. _GPL v3: http://www.gnu.org/licenses/
.. _Python: http://www.python.org/
.. _jinja: http://jinja.pocoo.org/
.. _mail: jnrowe@gmail.com
.. _issue: http://github.com/JNRowe/versionah/issues
