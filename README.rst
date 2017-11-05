``versionah`` - Simple version specification management
=======================================================

|travis| |coveralls| |pypi|

.. image:: https://secure.travis-ci.org/JNRowe/versionah.png?branch=master
   :target: http://travis-ci.org/JNRowe/versionah
   :alt: Test state on master

.. image:: https://img.shields.io/coveralls/JNRowe/versionah/master.png
   :target: https://coveralls.io/repos/JNRowe/versionah
   :alt: Coverage state on master

.. image:: https://img.shields.io/pypi/v/jnrbase.png
   :target: https://pypi.python.org/pypi/jnrbase
   :alt: Current PyPI release

Introduction
------------

``versionah`` is a simple tool to help you — or more specifically *me* — easily
maintain version information for a project.  Its entire aim is to make the act
of displaying or bumping a project’s version number a thoughtless task.

It is written in Python, and released under the `GPL v3`_.

Requirements
------------

``versionah`` should run on Python_ v3.5 or newer.  The only external libraries
``versionah`` depends on are click_ and jinja_.  If ``versionah`` doesn’t work
with the version of Python you have installed, file an issue_ and I’ll
endeavour to fix it.

Example
-------

The simplest way to show how ``versionah`` works is by example:

.. code:: console

    $ versionah set example.txt 2.4.3
    2.4.3
    $ versionah display example.txt
    2.4.3
    $ versionah bump example.txt minor
    2.5.0
    $ versionah bump example.txt major
    3.0.0

API Stability
-------------

API stability isn’t guaranteed across versions, although frivolous changes won’t
be made.

When ``versionah`` 1.0.0 is released the API will be frozen, and any changes
which aren’t backwards compatible will force a major version bump.

Contributors
------------

I’d like to thank the following people who have contributed to ``versionah``.

Patches
'''''''

* Marc Abramowitz
* Ansel Cloutier
* TakesxiSximada

Bug reports
'''''''''''

* Leal Hétu
* Matt Leighy

Ideas
'''''

* Ryan Lewis
* Ryan Sutton

If I’ve forgotten to include your name I wholeheartedly apologise.  Just drop me
a mail_ and I’ll update the list!

Bugs
----

If you find any problems, bugs or just have a question about this package either
file an issue_ or drop me a mail_.

If you’ve found a bug please try to include a minimal testcase so I can
reproduce the problem, or even better a patch!

.. _GPL v3: http://www.gnu.org/licenses/
.. _Python: http://www.python.org/
.. _click: http://click.pocoo.org/
.. _jinja: http://jinja.pocoo.org/
.. _mail: jnrowe@gmail.com
.. _issue: https://github.com/JNRowe/versionah/issues/

.. |travis| image:: https://secure.travis-ci.org/JNRowe/versionah.png?branch=master
   :target: http://travis-ci.org/JNRowe/versionah
   :alt: Test state on master

.. |coveralls| image:: https://img.shields.io/coveralls/JNRowe/versionah/master.png
   :target: https://coveralls.io/repos/JNRowe/versionah
   :alt: Coverage state on master

.. |pypi| image:: https://img.shields.io/pypi/v/jnrbase.png
   :target: https://pypi.python.org/pypi/jnrbase
   :alt: Current PyPI release
