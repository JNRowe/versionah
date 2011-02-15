#
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

from __future__ import print_function

from . import _version


__version__ = _version.triple
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

import errno
import optparse
import re
import sys

import jinja2

try:
    from termcolor import colored
except ImportError:  # pragma: no cover
    colored = None  # pylint: disable-msg=C0103

# Select colours if terminal is a tty
# pylint: disable-msg=C0103
if colored and sys.stdout.isatty():
    success = lambda s: colored(s, "green")
    fail = lambda s: colored(s, "red")
    warn = lambda s: colored(s, "yellow")
else:  # pragma: no cover
    success = fail = warn = str
# pylint: enable-msg=C0103


# Pull the first paragraph from the docstring
USAGE = __doc__[:__doc__.find('\n\n', 100)].splitlines()[2:]
# Replace script name with optparse's substitution var, and rebuild string
USAGE = "\n".join(USAGE).replace("versionah", "%prog")

VALID_VERSION = r"\d+\.\d+\.\d+"


class Version(object):
    def __init__(self, major=0, minor=1, micro=0):
        """Initialise a new ``Version`` object

        :type major: ``int``
        :param major: Major version component
        :type minor: ``int``
        :param minor: Minor version component
        :type micro: ``int``
        :param micro: Micro version component
        """
        self.major = major
        self.minor = minor
        self.micro = micro

    def bump(self, bump_type):
        """Bump a version string

        :type bump_type: ``str``
        :param bump_type: Component to bump
        """
        if bump_type == "major":
            self.major = self.major + 1
            self.minor = 0
            self.micro = 0
        elif bump_type == "minor":
            self.minor = self.minor + 1
            self.micro = 0
        elif bump_type == "micro":
            self.micro = self.micro + 1

    def as_triple(self):
        """Generate a version triple

        :rtype: ``str``
        :return: Version triple
        """
        return "%s.%s.%s" % (self.major, self.minor, self.micro)

    def as_hex(self):
        """Generate a hex version string

        :rtype: ``str``
        :return: Version as hex string
        """
        return "0x%02x%02x%02x" % (self.major, self.minor, self.micro)

    def as_libtool(self):
        """Generate a libtool version string

        :rtype: ``str``
        :return: Version as libtool string"""
        return "%i:%i" % (self.major * 10 + self.minor, 20 + self.micro)

    @staticmethod
    def display_types():
        """Supported representation types

        :rtype: ``list``
        :return: Method names for representation types
        """
        return [s[3:] for s in dir(Version) if s.startswith("as_")]

    def display(self, format):
        """Display a version string

        :type format: ``str``
        :param format: Format to display version string in
        :rtype: ``str``
        :return: Formatted version string
        """
        return getattr(self, "as_%s" % format)()

    @staticmethod
    def read(file):
        """Read a version file

        :type file: ``str``
        :param file: Version file to read
        :rtype: ``Version``
        :return: New ``Version```` object representing file
        :raise OSError: When ``file`` doesn't exist
        :raise ValueError: Unparsable version data
        """
        data = open(file).read().strip()
        match = re.search("Version (%s)" % VALID_VERSION, data)
        if not match:
            raise ValueError("No valid version identifier in %r" % file)
        major, minor, micro = split_version(match.groups()[0])
        return Version(major, minor, micro)

    def write(self, file, ftype):
        """Write a version file

        :type file: ``str``
        :param file: Version file to write
        :type ftype: ``str``
        :param ftype: File type to write
        :rtype: ``bool``
        :return: ``True`` on write success
        """
        data = self.__dict__
        data["file"] = file
        data.update(dict([(k[3:], getattr(self, k)())
                          for k in dir(self) if k.startswith("as_")]))

        env = jinja2.Environment(loader=jinja2.FileSystemLoader("templates"))
        template = env.get_template("%s.jinja" % ftype)
        open(file, "w").write(template.render(data))


def split_version(version):
    """Split version string to components

    :type version: ``str``
    :param version: Version string
    :rtype: ``list``` of ``int``
    :return: Components of version string
    """
    return map(int, version.split("."))


def process_command_line():
    """Main command line interface

    :rtype: ``tuple`` of ``optparse`` and ``string``
    :return: Parsed options and version file
    """

    parser = optparse.OptionParser(usage="%prog [options...]",
                                   version="%prog v" + __version__,
                                   description=USAGE)

    parser.set_defaults(ftype="text", bump=None, format="triple")

    parser.add_option("-t", "--type", action="store",
                      choices=("c", "python", "text"),
                      dest="ftype",
                      metavar="text",
                      help="define the file type used for version file")
    parser.add_option("-s", "--set", action="store",
                      metavar="0.1.0",
                      help="set to a specific version")
    parser.add_option("-b", "--bump", action="store",
                      choices=("major", "minor", "micro"),
                      metavar="micro",
                      help="bump type by one")
    parser.add_option("-d", "--display", action="store",
                      choices=Version.display_types(),
                      dest="format",
                      metavar="triple",
                      help="display output in format")

    options, args = parser.parse_args()

    if options.set and not re.match("%s$" % VALID_VERSION, options.set):
        parser.error("Invalid version string for set %r" % options.set)

    if not args:
        parser.error("One version file must be specified")
    elif not len(args) == 1:
        parser.error("Only one version file must be specified")

    return options, args[0]


def main():
    """Main script

    :rtype: ``int``
    :return: Exit code
    """

    try:
        options, file = process_command_line()  # pylint: disable-msg=W0612
    except SyntaxError:
        return errno.EPERM

    try:
        version = Version.read(file)
    except IOError:
        version = Version()
    except ValueError:
        print(fail(sys.exc_info()[1].args[0]))
        return errno.EEXIST

    if options.bump:
        version.bump(options.bump)
        version.write(file, options.ftype)
    elif options.set:
        major, minor, micro = split_version(options.set)
        version = Version(major, minor, micro)
        version.write(file, options.ftype)

    print(success(version.display(options.format)))

if __name__ == '__main__':
    sys.exit(main())
