Usage
=====

The :program:`versionah` script is the main workhorse of :mod:`versionah`.

Let's start with some basic examples:

.. code-block:: sh

    ▶ versionah display _version.py  # Read the version data from _version.py
    2.4.3
    ▶ versionah bump minor _version.py  # Bump the minor component
    2.5.0
    ▶ versionah bump major _version.py  # Bump the major component
    3.0.0

    ▶ versionah set 0.2.0 _version.rb  # Set the version in _version.rb to 0.2.0
    0.2.0
    ▶ versionah bump minor _version.h  # Bump the minor component in _version.h
    0.4.0

Options
-------

.. program:: versionah

.. cmdoption:: --version

   Show program's version number and exit

.. cmdoption:: -h, --help

   Show this help message and exit

.. cmdoption:: -d <format>, --display=<format>

   Display output in ``format``, where ``format`` is one of the list of
   {date,dotted,hex,libtool,tuple,web}


Commands
--------

``bump`` - Bump version in given file
'''''''''''''''''''''''''''''''''''''

.. cmdoption:: -t <mode>, --type=<mode>

   Define the file type used for version file.  Default is guessed based on file
   extension.

.. cmdoption:: <type>

   Bump ``type`` by one, where ``type`` is one of {major,minor,micro,patch}

``set`` - Set version in given file
'''''''''''''''''''''''''''''''''''

.. cmdoption:: -n <name>, --name=<name>

   Project name to use in output

.. cmdoption:: -t <mode>, --type=<mode>

   Define the file type used for version file.  Default is guessed based on file
   extension.

.. cmdoption:: <version>

   Set to a specific version

``display`` - Display version in given file
'''''''''''''''''''''''''''''''''''''''''''
