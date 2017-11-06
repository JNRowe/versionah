Usage
=====

.. highlight:: console

The |progref| script is the main workhorse of the :mod:`versionah` module.

Let’s start with some basic examples::

    $ versionah display _version.py  # Read the version data from _version.py
    2.4.3
    $ versionah bump _version.py minor  # Bump the minor component
    2.5.0
    $ versionah bump _version.py major  # Bump the major component
    3.0.0

    $ versionah set _version.rb 0.2.0  # Set the version in _version.rb to 0.2.0
    0.2.0
    $ versionah bump _version.h minor  # Bump the minor component in _version.h
    0.4.0

Options
-------

.. program:: versionah

.. option:: --version

   Show the version and exit.

.. option:: -h, --help

   Show this message and exit.

Commands
--------

``bump`` - Bump version in given file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. program:: versionah bump

::

    versionah bump [--help] [-d <format>] [-t <mode>] [--shtool] <filename>

.. option:: -d <format>, --display=<format>

   Display output in ``format``, where ``format`` is one of the list of
   {date,dict,dotted,hex,libtool,tuple,web}.

.. option:: -t <mode>, --type=<mode>

   Define the file type used for version file.  Default is guessed based on
   file extension.  This option can be specified multiple times when processing
   multiple files.

.. option:: --shtool

   Write shtool compatible output.

.. option:: --help

   Show help message and exit.

``display`` - Display version in given file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. program:: versionah display

::

    versionah display [--help] [-d <format>] <filename>

.. option:: -d <format>, --display=<format>

   Display output in ``format``, where ``format`` is one of the list of
   {date,dict,dotted,hex,libtool,tuple,web}.

.. option:: --help

   Show help message and exit.

``set`` - Set version in given file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. program:: versionah set

::

    versionah set [--help] [-d <format>] [-t <mode>] [--shtool] [-n <name>] <filename>

.. option:: -d <format>, --display=<format>

   Display output in ``format``, where ``format`` is one of the list of
   {date,dict,dotted,hex,libtool,tuple,web}.

.. option:: -t <mode>, --type=<mode>

   Define the file type used for version file.  Default is guessed based on
   file extension.  This option can be specified multiple times when processing
   multiple files.

.. option:: --shtool

   Write shtool compatible output.

.. option:: -n <name>, --name=<name>

   Project name to use in output.

.. option:: --help

   Show help message and exit.
