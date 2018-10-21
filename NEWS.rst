User-visible changes
====================

.. See doc/upgrading.rst for a more explantory discussion of major changes

.. contents::
   :local:

0.16.0 - 2017-11-06
-------------------

* Python 3 *only*, for Python 2 support you must use 0.15.0 or earlier
* Support for multiple output files per call
* ``.`` is now allowed in package names
* click_ and jnrbase_\ ``[colour,iso_8601,template]`` are now required
* ``aaargh`` and ``blessings`` are no longer required
* pytest_ is used for running tests; ``expecter``, ``mock`` and ``nose`` are no
  longer required

.. _click: https://pypi.python.org/pypi/click/
.. _jnrbase: https://pypi.python.org/pypi/jnrbase/
.. _pytest: https://pypi.python.org/pypi/pytest/

0.15.0 - 2014-01-31
-------------------

* Defaults to bumping micro version, as that is the common case
* New templates for golang and lua

0.14.0 - 2013-05-22
-------------------

* shtool_ compatible writing support

0.13.0 - 2013-05-09
-------------------

* Switched to a subcommand-based interface
* aaargh_ is now required
* Support for localisation, submit pull requests with your translations!

.. _aaargh : https://pypi.org/project/aaargh/

0.12.0 - 2012-07-19
-------------------

* blessings_ replaces termcolor_ for fancy output
* argparse_ is now required for Python 2.6
* Tests now use nose2_, expecter_ and nose2-cov_
* attest_ is no longer required for running tests
* cloud_sptheme_ is no longer required for building documentation
* On OS-X we fall back to ``~/Library/Application Support`` for templates
* pip_ requirements files are now included in ``extra``

.. _blessings: https://pypi.org/project/blessings/
.. _argparse: https://pypi.org/project/argparse/
.. _nose2: https://pypi.org/project/nose2/
.. _expecter: https://pypi.org/project/expecter/
.. _nose2-cov: https://pypi.org/project/nose2-cov/
.. _cloud_sptheme: https://pypi.org/project/cloud_sptheme/
.. _pip: https://pypi.org/project/pip/

0.11.0 - 2012-01-30
-------------------

* Added a basic JSON_ template, useful for handling version data for ``nodejs``
  packages
* Improved developer documentation
* attest_ and  behave_ are now required to run the testsuite

.. _JSON: www.json.org/
.. _attest: https://pypi.org/project/Attest/
.. _behave: https://pypi.org/project/behave/

0.10.0 - 2011-03-30
-------------------

* Added a ``h`` template, for writing C header files
* ``dateobj`` exported to templates for full access to `datetime.date`_ methods
* Man page available by calling ``make man`` in doc directory
* Sphinx_ examples in Getting Started document

.. _Sphinx: http://sphinx.pocoo.org/
.. _datetime.date: http://docs.python.org/library/datetime.html#date-objects

0.9.0 - 2011-03-21
------------------

* Installable with setuptools_
* Release date output with ``--display date`` option

.. _setuptools: https://pypi.org/project/distribute/

0.8.0 - 2011-02-26
------------------

* Support for reading shtool_ generated files
* ``major``, ``minor``, ``micro`` and ``patch`` are exported to templates
* Added an M4_ template, useful for working with autoconf_

..  _shtool: http://www.gnu.org/software/shtool/shtool.html
.. _M4: http://www.gnu.org/software/m4/m4.html
.. _autoconf: http://www.gnu.org/software/autoconf/autoconf.html

0.7.0 - 2011-02-21
------------------

* User templates now override system templates
* Ruby template
* Default file type is now based on version file’s extension
* Support for comparing version numbers when used as a library

0.6.0 - 2011-02-19
------------------

* Support for versions containing two or four components
* ``regexp`` filter for use in custom templates

0.5.0 - 2011-02-19
------------------

* Includes a release date in version output
* Support for package names with dashes and underscores

0.4.0 - 2011-02-18
------------------

* Support for including a package name in output

0.3.0 - 2011-02-15
------------------

* Support for output templates using Jinja_
* Coloured output using termcolor_ if available
* No longer supports Python 2.5 or lower

.. _Jinja: http://jinja.pocoo.org/
.. _termcolor: https://pypi.org/project/termcolor/

0.2.0 - 2011-02-15
------------------

* Python 3 support

0.1.0 - 2011-02-15
------------------

* Initial release
