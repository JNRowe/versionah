Usage
=====

The :program:`versionah` script is the main workhorse of :mod:`versionah`.

Let's start with some basic examples:

    ▶ versionah _version.py
    2.4.3
    ▶ versionah -b minor _version.py
    2.5.0
    ▶ versionah -b major _version.py
    3.0.0

    ▶ versionah -s0.2.0 _version.rb
    0.2.0
    ▶ versionah -b minor _version.h
    0.4.0

Options
'''''''

.. program:: versionah

.. cmdoption:: --version

   Show program's version number and exit

.. cmdoption:: -h, --help

   Show this help message and exit

.. cmdoption:: -t <mode>, --type=<mode>

   Define the file type used for version file.  Default is guessed based on file
   extension.

.. cmdoption:: -s <version>, --set=<version>

   Set to a specific version

.. cmdoption:: -b <type>, --bump=<type>

   Bump ``type`` by one, where ``type`` is one {major,minor,micro,patch}

.. cmdoption:: -d <format>, --display=<format>

   Display output in ``format``, where ``format`` is one of {date,dotted,hex,libtool}
