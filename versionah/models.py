#
# coding=utf-8
"""models - Version models for versionah"""
# Copyright © 2011-2014  James Rowe <jnrowe@gmail.com>
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

import datetime
import re
import sys

try:
    # For Python 3
    from http.cookiejar import MONTHS
except ImportError:
    from cookielib import MONTHS  # NOQA


#: Base string type, used for compatibility with Python 2 and 3
STR_TYPE = basestring if sys.version_info[0] == 2 else str


#: Regular expression to match a valid package name
VALID_PACKAGE = '[A-Za-z][A-Za-z0-9]+(?:[_\.-][A-Za-z0-9]+)*'
#: Regular expression to match a valid package version
VALID_VERSION = r'\d+\.\d+(?:\.\d+){,2}'
#: Regular expression to match a package date.  ISO-8601, and %d-%b-%Y
#: formatting for shtool compatibility
VALID_DATE = r'(?:\d{4}-\d{2}-\d{2}|\d{2}-(?:%s)-\d{4})' % '|'.join(MONTHS)

#: Supported version components
VERSION_COMPS = ('major', 'minor', 'micro', 'patch')


class Version(object):

    """Main version identifier representation."""

    def __init__(self, components=(0, 1, 0), name='unknown',
                 date=datetime.date.today()):
        """Initialise a new `Version` object.

        :type components: `str` or `tuple` of `int`
        :param components: Version components
        :param str name: Package name
        :param datetime.date date: Date associated with version
        """
        if isinstance(components, STR_TYPE):
            components = split_version(components)
        if not 2 <= len(components) <= 4:
            raise ValueError('Invalid number of components in %r'
                             % (components, ))
        if not all((isinstance(n, int) and n >= 0) for n in components):
            raise ValueError('Invalid component values in %r' % (components, ))

        # Stub attributes set via Version.set method
        self.major = self.minor = self.micro = self.patch = 0
        self._resolution = 0
        self.set(components)

        self.name = name
        self.date = date

    def __repr__(self):
        """Self-documenting string representation.

        :rtype: `str`
        :return: String representation of object
        """
        return '%s(%r, %r, %r)' % (self.__class__.__name__, self.components,
                                   self.name, self.date)

    def __str__(self):
        """Return default string representation.

        We return a dotted version string, as that is the most common format.

        :rtype: `str`
        :return: Default strings representation of object
        """
        return '%s v%s' % (self.name, self.as_dotted())

    @staticmethod
    def __prepare_cmp_object(other):
        """Prepare object for comparison with Version.

        This presents a tuple for comparison with Version.components_full.

        :type other: `Version`, `list`, `tuple` or `int`
        :param other: Object to munge
        :rtype: `tuple`
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
            raise NotImplementedError('Unable to compare Version and %r'
                                      % type(other))

    def __eq__(self, other):
        """Test `Version` objects for equality.

        Importantly, padded version components are checked so that 0.1 is
        considered equal to 0.1.0.0.

        See `~Version.__prepare_cmp_object`.

        :type other: `Version`, `list`, `tuple` or `int`
        :param other: Object to munge
        :rtype: `bool`
        """
        return self.components_full == self.__prepare_cmp_object(other)
    __ne__ = lambda self, other: not self == (other)

    def __lt__(self, other):
        """Strict less-than test against comparable object.

        See `~Version.__prepare_cmp_object`.

        :type other: `Version`, `list`, `tuple` or `int`
        :param other: Object to munge
        :rtype: `bool`
        :return: True if ``self`` is strictly less-than ``other``
        """
        return self.components < self.__prepare_cmp_object(other)

    def __gt__(self, other):
        """Strict greater-than test against comparable object.

        See `~Version.__prepare_cmp_object`.

        :type other: `Version`, `list`, `tuple` or `int`
        :param other: Object to munge
        :rtype: `bool`
        :return: True if ``self`` is strictly greater-than ``other``
        """
        return self.components_full > self.__prepare_cmp_object(other)

    def __le__(self, other):
        """Less-than or equal to test against comparable object.

        See `~Version.__prepare_cmp_object`.

        :type other: `Version`, `list`, `tuple` or `int`
        :param other: Object to munge
        :rtype: `bool`
        :return: True if ``self`` is less-than or equal to ``other``
        """
        return self < other or self == other

    def __ge__(self, other):
        """Greater-than or equal to test against comparable object.

        See `~Version.__prepare_cmp_object`.

        :type other: `Version`, `list`, `tuple` or `int`
        :param other: Object to munge
        :rtype: `bool`
        :return: True if ``self`` is greater-than or equal to ``other``
        """
        return self > other or self == other

    def __hash__(self):
        """Create object-unique hash value.

        :rtype: `str`
        :return: Object-unique hash value
        """
        return hash(repr(self))

    def set(self, components):
        """Set version components.

        :type components: `tuple` of `int`
        :param components: Version components
        """
        if isinstance(components, STR_TYPE):
            components = split_version(components)
        elif isinstance(components, list):
            components = tuple(components)
        padded = (components + (0, 0, 0))[:4]
        self.major, self.minor, self.micro, self.patch = padded
        self._resolution = len(components)

    @property
    def components_full(self):
        """Generate full length component tuple for version.

        :rtype: `tuple` of `int`
        """
        return self.major, self.minor, self.micro, self.patch

    @property
    def components(self):
        """Generate component tuple to initial resolution.

        :rtype: `tuple` of `int`
        """
        return self.components_full[:self._resolution]

    def bump(self, bump_type):
        """Bump a version string.

        :param str bump_type: Component to bump
        :raise ValueError: Invalid `bump_type` argument
        """
        if bump_type == 'micro' and self._resolution < 3 \
                or bump_type == 'patch' and self._resolution < 4:
            raise ValueError('Invalid bump_type %r for version %r'
                             % (bump_type, self.components))
        if bump_type == 'major':
            self.major += 1
            self.micro = self.minor = self.patch = 0
        elif bump_type == 'minor':
            self.minor += 1
            self.micro = self.patch = 0
        elif bump_type == 'micro':
            self.micro += 1
            self.patch = 0
        elif bump_type == 'patch':
            self.patch += 1
        else:
            raise ValueError('Unknown bump_type %r' % bump_type)
        self.date = datetime.date.today()

    def bump_major(self):
        """Bump major version component."""
        self.bump('major')

    def bump_minor(self):
        """Bump minor version component."""
        self.bump('minor')

    def bump_micro(self):
        """Bump micro version component."""
        self.bump('micro')

    def bump_patch(self):
        """Bump patch version component."""
        self.bump('patch')

    def as_dict(self):
        """Generate a dictionary of version components.

        :rtype: `dict`
        :return: Version as dictionary
        """
        return dict(zip(VERSION_COMPS, self.components))

    def as_dotted(self):
        """Generate a dotted version string.

        :rtype: `str`
        :return: Standard dotted version string
        """
        return '.'.join(str(s) for s in self.components)

    def as_hex(self):
        """Generate a hex version string.

        :rtype: `str`
        :return: Version as hex string
        """
        return '0x' + ''.join('%02x' % n for n in self.components)

    def as_libtool(self):
        """Generate a libtool version string.

        :rtype: `str`
        :return: Version as libtool string
        """
        return '%i:%i' % (self.major * 10 + self.minor, 20 + self.micro)

    def as_date(self):
        """Generate a ISO-8601 date string for release.

        :rtype: `str`
        :return: Version's release date as ISO-8601 date stamp
        """
        return self.date.isoformat()

    def as_tuple(self):
        """Generate a tuple of version components.

        :rtype: `int`
        :return: Version components as tuple
        """
        return self.components

    def as_web(self):
        """Generate a web UA-style string for release.

        :rtype: `str`
        :return: Version's string in web UA-style
        """
        return '%s/%s' % (self.name, self.as_dotted())


def split_version(version):
    """Split version string to components.

    :param str version: Version string
    :rtype: `tuple` of `int`
    :return: Components of version string
    :raise exceptions.ValueError: Invalid version string
    """
    if not re.match('%s$' % VALID_VERSION, version):
        raise ValueError('Invalid version string %r' % version)

    return tuple(int(s) for s in version.split('.'))
