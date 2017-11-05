versionah
=========

Version management made easy
----------------------------

:Author: James Rowe <jnrowe@gmail.com>
:Date: 2011-02-15
:Copyright: GPL v3
:Manual section: 1
:Manual group: Developer

SYNOPSIS
--------

    versionah [OPTIONS] COMMAND [ARGS]…

DESCRIPTION
-----------

|progref| is a simple tool to help you — or more specifically *me* — easily
maintain version information for a project.  Its entire aim is to make the act
of displaying or bumping a project’s version number a thoughtless task.

Options
-------

.. program:: versionah

.. option:: --version

    Show the version and exit.

.. option:: -h, --help

    Show this message and exit.

Commands
--------

``bump``
''''''''

.. program:: versionah bump

Bump version in given file.

.. option:: -d <format>, --display=<format>

    Display output in ``format``, where ``format`` is one of the list of
    {date,dict,dotted,hex,libtool,tuple,web}.

.. option:: -t <mode>, --type=<mode>

    Define the file type used for version file.  Default is guessed based on
    file extension.  This option can be specified multiple times when
    processing multiple files.

.. option:: --shtool

    Write shtool compatible output.

.. option:: -h, --help

    Show this message and exit.

.. option:: <filename>

    Name of the file to bump.

.. option:: <type>

    Bump ``type`` by one, where ``type`` is one of {major,minor,micro,patch}.

``display``
'''''''''''

.. program:: versionah display

Display version in given file

.. option:: -d <format>, --display=<format>

   Display output in ``format``, where ``format`` is one of the list of
   {date,dict,dotted,hex,libtool,tuple,web}

.. option:: -h, --help

    Show this message and exit.

.. option:: <filename>

    Name of the file to display the version from.

``set``
'''''''

.. program:: versionah set

Set version in given file.

.. option:: -d <format>, --display=<format>

    Display output in ``format``, where ``format`` is one of the list of
    {date,dict,dotted,hex,libtool,tuple,web}.

.. option:: -n <name>, --name=<name>

    Project name to use in output.

.. option:: -t <mode>, --type=<mode>

    Define the file type used for version file.  Default is guessed based on
    file extension.  This option can be specified multiple times when
    processing multiple files.

.. option:: --shtool

    Write shtool compatible output.

.. option:: -h, --help

    Show this message and exit.

.. option:: <filename>

    Name of the file to set the version for.

.. option:: <version>

    Set to a specific version.

BUGS
----

None known.

AUTHOR
------

Written by `James Rowe <mailto:jnrowe@gmail.com>`__

RESOURCES
---------

:Documentation: http://versionah.readthedocs.io/
:Git repository:  https://github.com/JNRowe/versionah/
:Issue tracker:  https://github.com/JNRowe/versionah/issues/
:Contributors:  https://github.com/JNRowe/versionah/contributors/

COPYING
-------

Copyright © 2011-2015  James Rowe <jnrowe@gmail.com>

versionah is free software: you can redistribute it and/or modify it under the
terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

versionah is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
versionah.  If not, see <http://www.gnu.org/licenses/>.
