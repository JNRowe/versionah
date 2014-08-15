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

    versionah [OPTIONS] COMMAND [ARGS]...

DESCRIPTION
-----------

`versionah` is a simple tool to help you, or more specifically *me*, easily
maintain version information for a project.  Its entire aim is to make the act
of displaying or bumping a project's version number a thoughtless task.

Options
-------

--version
    Show the version and exit.

-h, --help
    Show this message and exit.

Commands
--------

``bump``
''''''''

Bump version in given file.

-d <format>, --display=<format>
    Display output in ``format``, where ``format`` is one of the list of
    {date,dict,dotted,hex,libtool,tuple,web}.

-t <mode>, --type=<mode>
    Define the file type used for version file.  Default is guessed based on
    file extension.  This option can be specified multiple times when
    processing multiple files.

--shtool
    Write shtool compatible output.

--vcs

    Commit version and create tag.

<filename>
    Name of the file to bump.

<type>
    Bump ``type`` by one, where ``type`` is one of {major,minor,micro,patch}.

``set``
'''''''

Set version in given file.

-d <format>, --display=<format>
    Display output in ``format``, where ``format`` is one of the list of
    {date,dict,dotted,hex,libtool,tuple,web}.

-n <name>, --name=<name>
    Project name to use in output.

-t <mode>, --type=<mode>
    Define the file type used for version file.  Default is guessed based on
    file extension.  This option can be specified multiple times when
    processing multiple files.

--vcs

    Commit version and create tag.

<filename>
    Name of the file to set the version for.

<version>
    Set to a specific version.

``display``
'''''''''''

Display version in given file

-d <format>, --display=<format>

   Display output in ``format``, where ``format`` is one of the list of
   {date,dict,dotted,hex,libtool,tuple,web}

<filename>
    Name of the file to display the version from.

BUGS
----

None known.

AUTHOR
------

Written by `James Rowe <mailto:jnrowe@gmail.com>`__

RESOURCES
---------

:Git repository:  https://github.com/JNRowe/versionah/
:Issue tracker:  https://github.com/JNRowe/versionah/issues/
:Contributors:  https://github.com/JNRowe/versionah/contributors/

COPYING
-------

Copyright © 2011-2014  James Rowe <jnrowe@gmail.com>

This program is free software: you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the
Free Software Foundation, either version 3 of the License, or (at your
option) any later version.
