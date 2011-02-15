#! /usr/bin/python -tt
"""versionah - Simple version specification management"""
# Copyright (C) 2011  James Rowe <jnrowe@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

__version__ = "0.1.0"
__date__ = "2011-02-15"
__author__ = "James Rowe <jnrowe@gmail.com>"
__copyright__ = "Copyright (C) 2011  James Rowe <jnrowe@gmail.com>"
__license__ = "GNU General Public License Version 3"
__credits__ = ""
__history__ = "See git repository"

from email.utils import parseaddr

__doc__ += """.

versionah is a GPL v3 licensed module for maintaining version information files
for use in project management.

.. moduleauthor:: `%s <mailto:%s>`__
""" % parseaddr(__author__)

# Pull the first paragraph from the docstring
USAGE = __doc__[:__doc__.find('\n\n', 100)].splitlines()[2:]
# Replace script name with optparse's substitution var, and rebuild string
USAGE = "\n".join(USAGE).replace("versionah", "%prog")


def bump(version, bump_type):
    """Bump a version string

    :type version: ``str``
    :param version: Version string to bump
    :type bump_type: ``str``
    :param bump_type: Component to bump
    :rtype: ``str``
    :return: Bumped version string
    """
    major, minor, micro = map(int, version.split("."))
    if bump_type == "major":
        major = major + 1
        minor = 0
        micro = 0
    elif bump_type == "minor":
        minor = minor + 1
        micro = 0
    elif bump_type == "micro":
        micro = micro + 1
    return ".".join(map(str, (major, minor, micro)))


def display(version, format):
    """Display a version string

    :type version: ``str``
    :param version: Version string to display
    :type format: ``str``
    :param format: Format to display version string in
    :rtype: ``str``
    :return: Formatted version string
    """
    major, minor, micro = map(int, version.split("."))
    if format == "triple":
        return ".".join(map(str, (major, minor, micro)))
    elif format == "hex":
        return "0x%02x%02x%02x" % (major, minor, micro)
    elif format == "libtool":
        return "%i:%i" % (major * 10 + minor, 20 + micro)


def read(file):
    """Read a version file

    :type file: ``str``
    :param file: Version file to read
    :rtype: ``file``
    :return: Version string
    :raise OSError: When ``file`` doesn't exist
    """
    return open(file).read().strip()


def write(file, version):
    """Write a version file

    :type file: ``str``
    :param file: Version file to write
    :type version: ``str``
    :param version: Version string to write
    :rtype: ``bool``
    :return: ``True`` on write success
    """
    open(file, "w").write(version)
