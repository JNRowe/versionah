Usage
=====

The :program:`versionah` script is the main workhorse of `versionah`.

Let's start with some basic examples:

.. code-block:: sh

    ▶ versionah display _version.py  # Read the version data from _version.py
    2.4.3
    ▶ versionah bump _version.py minor  # Bump the minor component
    2.5.0
    ▶ versionah bump _version.py major  # Bump the major component
    3.0.0

    ▶ versionah set _version.rb 0.2.0  # Set the version in _version.rb to 0.2.0
    0.2.0
    ▶ versionah bump _version.h minor  # Bump the minor component in _version.h
    0.4.0

Options
-------

.. program:: versionah

.. cmdoption:: --version

   Show program's version number and exit

.. cmdoption:: -h, --help

   Show this help message and exit

Commands
--------

``bump`` - Bump version in given file
'''''''''''''''''''''''''''''''''''''

.. program:: versionah bump

.. cmdoption:: -d <format>, --display=<format>

   Display output in ``format``, where ``format`` is one of the list of
   {date,dict,dotted,hex,libtool,tuple,web}

.. cmdoption:: -t <mode>, --type=<mode>

   Define the file type used for version file.  Default is guessed based on file
   extension.

.. cmdoption:: --shtool

   Write shtool compatible output

.. cmdoption:: <type>

   Bump ``type`` by one, where ``type`` is one of {major,minor,micro,patch}

``set`` - Set version in given file
'''''''''''''''''''''''''''''''''''

.. program:: versionah set

.. cmdoption:: -d <format>, --display=<format>

   Display output in ``format``, where ``format`` is one of the list of
   {date,dict,dotted,hex,libtool,tuple,web}

.. cmdoption:: -n <name>, --name=<name>

   Project name to use in output

.. cmdoption:: -t <mode>, --type=<mode>

   Define the file type used for version file.  Default is guessed based on file
   extension.

.. cmdoption:: <version>

   Set to a specific version

``display`` - Display version in given file
'''''''''''''''''''''''''''''''''''''''''''

.. program:: versionah display

.. cmdoption:: -d <format>, --display=<format>

   Display output in ``format``, where ``format`` is one of the list of
   {date,dict,dotted,hex,libtool,tuple,web}
