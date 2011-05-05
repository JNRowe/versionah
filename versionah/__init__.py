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


__version__ = _version.dotted
__date__ = _version.date
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
""" % parseaddr(__author__)  # pylint: disable-msg=W0622

import datetime
import errno
import optparse
import os
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

if sys.version_info[0] == 3:
    STR_TYPE = str
else:
    STR_TYPE = basestring

# Pull the first paragraph from the docstring
USAGE = __doc__[:__doc__.find('\n\n', 100)].splitlines()[2:]
# Replace script name with optparse's substitution var, and rebuild string
USAGE = "\n".join(USAGE).replace("versionah", "%prog")

VALID_PACKAGE = "[A-Za-z]+(?:[_-][A-Za-z]+)*"
VALID_VERSION = r"\d+\.\d+(?:\.\d+){,2}"
# ISO-8601, and %d-%b-%Y formatting for shtool compatibility
VALID_DATE = r"(?:\d{4}-\d{2}-\d{2}|\d{2}-(?:[A-Z][a-z]{2})-\d{4})"

# Custom filters for Jinja
FILTERS = {}


def filter_regexp(string, pattern, repl, count=0, flags=0):
    """Jinja filter for regexp replacements

    See ``re.sub`` for documentation
    """
    if sys.version_info[:2] > (2, 6):
        return re.sub(pattern, repl, string, count, flags)
    else:
        return re.sub(pattern, repl, string, count)
FILTERS["regexp"] = filter_regexp


class Version(object):
    """Main version identifier representation"""

    user_dir = os.environ.get("XDG_DATA_HOME",
                              os.path.join(os.environ.get("HOME", "/"),
                                           ".local"))
    system_dirs = os.environ.get("XDG_DATA_DIRS",
                                 "/usr/local/share/:/usr/share/").split(":")
    mk_data_dir = lambda s: os.path.join(s, "versionah", "templates")
    pkg_data_dirs = [mk_data_dir(user_dir), ]
    for directory in system_dirs:
        pkg_data_dirs.append(mk_data_dir(directory))

    env = jinja2.Environment(loader=jinja2.ChoiceLoader(
        list(jinja2.FileSystemLoader(s) for s in pkg_data_dirs)))
    env.loader.loaders.append(jinja2.PackageLoader("versionah", "templates"))
    env.filters.update(FILTERS)
    filetypes = [s.split(".")[0] for s in env.list_templates()]

    def __init__(self, components=(0, 1, 0), name="unknown",
                 date=datetime.date.today()):
        """Initialise a new ``Version`` object

        :type components: ``str`` or ``tuple`` of ``int``
        :param components: Version components
        :param str name: Package's name
        :param datetime.date date: Date associated with version
        """
        if isinstance(components, STR_TYPE):
            components = split_version(components)
        if not 2 <= len(components) <= 4:
            raise ValueError("Invalid number of components %r"
                             % (components, ))
        if not all((isinstance(n, int) and n >= 0) for n in components):
            raise ValueError("Invalid component values %r" % (components, ))
        self.set(components)
        self.name = name
        self.date = date

    def __repr__(self):
        """Self-documenting string representation

        :rtype: ``str``
        :return: String representation of object"""
        return "%s(%r, %r, %r)" % (self.__class__.__name__, self.components,
                                   self.name, self.date)

    def __str__(self):
        """Return default string representation

        We return a dotted version string, as that is the most common format.

        :rtype: ``str``
        :return: Default strings representation of object"""
        return "%s v%s" % (self.name, self.as_dotted())

    @staticmethod
    def __prepare_cmp_object(other):
        """Prepare object for comparison with Version

        This presents a tuple for comparison with Version.components_full.

        :type other: ``Version``, ``list``, ``tuple`` or ``str``
        :param other: Object to munge
        :rtype: ``tuple``
        :return: Full version component tuple for object
        :raise NotImplementedError: Incomparable other
        """
        if isinstance(other, Version):
            return other.components_full
        elif isinstance(other, (tuple, list)):
            return (tuple(other) + (0, 0, 0))[:4]
        elif isinstance(other, str):
            return (split_version(other) + (0, 0, 0))[:4]
        else:
            raise NotImplementedError("Unable to compare Version and %r"
                                      % type(other))

    def __eq__(self, other):
        """Test ``Version`` objects for equality

        Importantly, padded version components are checked so that 0.1 is
        considered equal to 0.1.0.0.
        """
        return self.components_full == self.__prepare_cmp_object(other)
    __ne__ = lambda self, other: not self == (other)

    def __lt__(self, other):
        return self.components < self.__prepare_cmp_object(other)

    def __gt__(self, other):
        return self.components_full > self.__prepare_cmp_object(other)

    def __le__(self, other):
        return self < other or self == other

    def __ge__(self, other):
        return self > other or self == other

    def set(self, components):
        """Set version components

        :type components: ``tuple`` of ``int``
        :param components: Version components
        """
        if isinstance(components, STR_TYPE):
            components = split_version(components)
        padded = (components + (0, 0, 0))[:4]
        self.major, self.minor, self.micro, self.patch = padded
        self._resolution = len(components)

    @property
    def components_full(self):
        """Generate full length component tuple for version"""
        return self.major, self.minor, self.micro, self.patch

    @property
    def components(self):
        """Generate component tuple to initial resolution"""

        return self.components_full[:self._resolution]

    def bump(self, bump_type):
        """Bump a version string

        :param str bump_type: Component to bump
        """
        if bump_type == "micro" and self._resolution < 3 \
            or bump_type == "patch" and self._resolution < 4:
            raise ValueError("Invalid bump_type %r for version %r"
                             % (bump_type, self))
        if bump_type == "major":
            self.major += 1
            self.micro = self.minor = self.patch = 0
        elif bump_type == "minor":
            self.minor += 1
            self.micro = self.patch = 0
        elif bump_type == "micro":
            self.micro += 1
            self.patch = 0
        elif bump_type == "patch":
            self.patch += 1
        self.date = datetime.date.today()

    def bump_major(self):
        """Bump major version component"""
        self.bump("major")

    def bump_minor(self):
        """Bump minor version component"""
        self.bump("minor")

    def bump_micro(self):
        """Bump micro version component"""
        self.bump("micro")

    def bump_patch(self):
        """Bump patch version component"""
        self.bump("patch")

    def as_dotted(self):
        """Generate a dotted version

        :rtype: ``str``
        :return: Standard dotted version string
        """
        return ".".join(str(s) for s in self.components)

    def as_hex(self):
        """Generate a hex version string

        :rtype: ``str``
        :return: Version as hex string
        """
        return "0x" + "".join("%02x" % n for n in self.components)

    def as_libtool(self):
        """Generate a libtool version string

        :rtype: ``str``
        :return: Version as libtool string"""
        return "%i:%i" % (self.major * 10 + self.minor, 20 + self.micro)

    def as_date(self):
        """Generate a ISO-8601 date string for release

        :rtype: ``str``
        :return: Version's release date as ISO-8601 date stamp
        """
        return self.date.isoformat()

    def as_tuple(self):
        """Generate a tuple of version components

        :rtype: ``str``
        :return: Version components as tuple
        """
        return self.components

    def as_web(self):
        """Generate a web UA-style string for release

        :rtype: ``str``
        :return: Version's string in web UA-style
        """
        return "%s/%s" % (self.name, self.as_dotted())

    @staticmethod
    def display_types():
        """Supported representation types

        :rtype: ``list``
        :return: Method names for representation types
        """
        return [s[3:] for s in dir(Version) if s.startswith("as_")]

    def display(self, display_format):
        """Display a version string

        :param str display_format: Format to display version string in
        :rtype: ``str``
        :return: Formatted version string
        """
        return getattr(self, "as_%s" % display_format)()

    @staticmethod
    def read(filename):
        """Read a version file

        :param str filename: Version file to read
        :rtype: ``Version``
        :return: New ``Version```` object representing file
        :raise OSError: When ``filename`` doesn't exist
        :raise ValueError: Unparsable version data
        """
        data = open(filename).read().strip()
        match = re.search(r"This is (%s),? [vV]ersion (%s) \((%s)\)"
                          % (VALID_PACKAGE, VALID_VERSION, VALID_DATE),
                          data)
        if not match:
            raise ValueError("No valid version identifier in %r" % filename)
        name, version_str, date_str = match.groups()
        components = split_version(version_str)
        try:
            parsed = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            parsed = datetime.datetime.strptime(date_str, "%d-%b-%Y")
        return Version(components, name, parsed.date())

    def write(self, filename, file_type):
        """Write a version file

        :param str filename: Version file to write
        :param str file_type: File type to write
        :rtype: ``bool``
        :return: ``True`` on write success
        """
        data = self.__dict__
        data["filename"] = filename
        data["dateobj"] = self.date
        data["resolution"] = self._resolution
        data["magic"] = "This is %s version %s (%s)" % (self.name,
                                                        self.as_dotted(),
                                                        self.as_date())
        data.update(dict(zip(["major", "minor", "micro", "patch"],
                             self.components)))
        data.update(dict([(k[3:], getattr(self, k)())
                          for k in dir(self) if k.startswith("as_")]))

        template = self.env.get_template("%s.jinja" % file_type)
        open(filename, "w").write(template.render(data))


def split_version(version):
    """Split version string to components

    :param str version: Version string
    :rtype: ``tuple`` of ``int``
    :return: Components of version string
    :raise ValueError: Invalid version string
    """
    if not re.match("%s$" % VALID_VERSION, version):
        raise ValueError("Invalid version string %r" % version)

    return tuple(int(s) for s in version.split("."))


def process_command_line(argv=sys.argv[1:]):
    """Main command line interface

    :param list argv: Command line arguments to process
    :rtype: ``tuple`` of ``optparse`` and ``string``
    :return: Parsed options and version file
    """

    parser = optparse.OptionParser(usage="%prog [options...]",
                                   version="%prog v" + __version__,
                                   description=USAGE)

    parser.set_defaults(file_type=None, bump=None, display_format="dotted")

    parser.add_option("-t", "--type", action="store",
                      choices=Version.filetypes,
                      dest="file_type",
                      metavar="text",
                      help="define the file type used for version file")
    parser.add_option("-n", "--name", action="store",
                      metavar="name",
                      help="package name for version")
    parser.add_option("-s", "--set", action="store",
                      metavar="0.1.0",
                      help="set to a specific version")
    parser.add_option("-b", "--bump", action="store",
                      choices=("major", "minor", "micro", "patch"),
                      metavar="micro",
                      help="bump type by one")
    parser.add_option("-d", "--display", action="store",
                      choices=Version.display_types(),
                      dest="display_format",
                      metavar="dotted",
                      help="display output in format")

    options, args = parser.parse_args(argv)

    if options.name and not re.match("%s$" % VALID_PACKAGE, options.name):
        parser.error("Invalid package name string %r" % options.set)

    if options.set and not re.match("%s$" % VALID_VERSION, options.set):
        parser.error("Invalid version string for set %r" % options.set)

    if not args:
        parser.error("One version file must be specified")
    elif not len(args) == 1:
        parser.error("Only one version file must be specified")
    file_name = args[0]

    if not options.file_type:
        suffix = os.path.splitext(file_name)[1][1:]
        options.file_type = suffix if suffix in Version.filetypes else "text"

    return options, file_name


def main():
    """Main script

    :rtype: ``int``
    :return: Exit code
    """

    try:
        options, filename = process_command_line()
    except SyntaxError:
        return errno.EPERM

    try:
        version = Version.read(filename)
    except IOError:
        version = Version()
    except ValueError:
        print(fail(sys.exc_info()[1].args[0]))
        return errno.EEXIST

    if not options.set and not os.path.exists(filename):
        print(fail("File not found"))
        return errno.ENOENT

    if options.name:
        version.name = options.name
    if options.bump:
        version.bump(options.bump)
        version.write(filename, options.file_type)
    elif options.set:
        version.set(options.set)
        version.write(filename, options.file_type)

    print(success(version.display(options.display_format)))

if __name__ == '__main__':
    sys.exit(main())
