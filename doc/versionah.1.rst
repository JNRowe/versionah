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

    versionah [option]... <file>

DESCRIPTION
-----------

:mod:`versionah` is a simple tool to help you, or more specifically *me*, easily
maintain version information for a project.  Its entire aim is to make the act
of displaying or bumping a project's version number a thoughtless task.

OPTIONS
-------

--version
    Show program's version number and exit

-h, --help
    Show this help message and exit

-t <mode>, --type=<mode>
    Define the file type used for version file.  Default is guessed based on
    file extension.

-n <name>, --name=<name>
    Package name for version

-s <version>, --set=<version>
    Set to a specific version

-b <type>, --bump=<type>
    Bump ``type`` by one, where ``type`` is one of {major,minor,micro,patch}

-d <format>, --display=<format>
    Display output in ``format``, where ``format`` is one of the list of
    {date,dotted,hex,libtool,tuple,web}

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

Copyright © 2011-2012  James Rowe.

This program is free software: you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the
Free Software Foundation, either version 3 of the License, or (at your
option) any later version.
