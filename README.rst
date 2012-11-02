``versionah`` - Simple version specification management
=======================================================

.. image:: https://secure.travis-ci.org/JNRowe/versionah.png?branch=master
   :target: http://travis-ci.org/JNRowe/versionah

Introduction
------------

``versionah`` is a simple tool to help you, or more specifically *me*, easily
maintain version information for a project.  Its entire aim is to make the act
of displaying or bumping a project's version number a thoughtless task.

It is written in Python, and released under the `GPL v3`_.

Requirements
------------

``versionah`` should run on Python_ v2.6 or newer [#]_, including Python v3.
The only external library ``versionah`` currently depends on is jinja_.  If
``versionah`` doesn't work with the version of Python you have installed, file
an issue_ and I'll endeavour to fix it.

If you would like coloured terminal output, then you will need blessings_.

.. [#] If you still run older Python versions only small changes should be
       required, for example the unrolling of conditional expressions and
       redefining of ``except..as`` structures.

Example
-------

The simplest way to show how ``versionah`` works is by example::

    $ versionah set example.txt 2.4.3
    2.4.3
    $ versionah display example.txt
    2.4.3
    $ versionah bump example.txt minor
    2.5.0
    $ versionah bump example.txt major
    3.0.0
    $ rm example.txt
    <BLANKLINE>

API Stability
-------------

API stability isn't guaranteed across versions, although frivolous changes won't
be made.

When ``versionah`` 1.0.0 is released the API will be frozen, and any changes
which aren't backwards compatible will force a major version bump.

Contributors
------------

I'd like to thank the following people who have contributed to ``versionah``.

Patches
'''''''

* Marc Abramowitz

Bug reports
'''''''''''

* Leal Hétu
* Matt Leighy

Ideas
'''''

* Ryan Lewis

If I've forgotten to include your name I wholeheartedly apologise.  Just drop me
a mail_ and I'll update the list!

Bugs
----

If you find any problems, bugs or just have a question about this package either
file an issue_ or drop me a mail_.

If you've found a bug please attempt to include a minimal testcase so I can
reproduce the problem, or even better a patch!

.. _GPL v3: http://www.gnu.org/licenses/
.. _Python: http://www.python.org/
.. _jinja: http://jinja.pocoo.org/
.. _blessings: http://pypi.python.org/pypi/blessings/
.. _mail: jnrowe@gmail.com
.. _issue: https://github.com/JNRowe/versionah/issues/
