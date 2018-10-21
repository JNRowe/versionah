#
"""models - Version models for versionah."""
# Copyright © 2014-2017  James Rowe <jnrowe@gmail.com>
#
# SPDX-License-Identifier: GPL-3.0+
#
# This file is part of versionah.
#
# versionah is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# versionah is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# versionah.  If not, see <http://www.gnu.org/licenses/>.

import datetime
import re

from functools import total_ordering
from http.cookiejar import MONTHS
from typing import Any, Dict, Tuple


#: Regular expression to match a valid package name
VALID_PACKAGE = r'[A-Za-z][A-Za-z0-9]+(?:[_\.-][A-Za-z0-9]+)*'
#: Regular expression to match a valid package version
VALID_VERSION = r'\d+\.\d+(?:\.\d+){,2}'
#: Regular expression to match a package date.  ISO-8601, and %d-%b-%Y
#: formatting for shtool compatibility
VALID_DATE = r'(?:\d{4}-\d{2}-\d{2}|\d{2}-(?:%s)-\d{4})' % '|'.join(MONTHS)

#: Supported version components
VERSION_COMPS = ('major', 'minor', 'micro', 'patch')


@total_ordering
class Version:

    """Main version identifier representation."""

    def __init__(self, components: Tuple[int] = (0, 1, 0),
                 name: str = 'unknown',
                 date: datetime.date = datetime.date.today()) -> None:
        """Initialise a new `Version` object.

        Args:
            components: Version components
            name: Package name
            date: Date associated with version
        """
        if isinstance(components, str):
            components = split_version(components)
        if not 2 <= len(components) <= 4:
            raise ValueError(
                'Invalid number of components in {!r}'.format(components))
        if not all((isinstance(n, int) and n >= 0) for n in components):
            raise ValueError(
                'Invalid component values in {!r}'.format(components))

        # Stub attributes set via Version.set method
        self.major = self.minor = self.micro = self.patch = 0
        self._resolution = 0
        self.set(components)

        self.name = name
        self.date = date

    def __repr__(self) -> str:
        """Self-documenting string representation.

        Returns:
            String representation of object
        """
        return '{}({!r}, {!r}, {!r})'.format(self.__class__.__qualname__,
                                             self.components, self.name,
                                             self.date)

    def __str__(self) -> str:
        """Return default string representation.

        We return a dotted version string, as that is the most common format.

        Returns:
            Default strings representation of object
        """
        return '{} v{}'.format(self.name, self.as_dotted())

    @staticmethod
    def __prepare_cmp_object(other: Any) -> Tuple[int]:
        """Prepare object for comparison with Version.

        This presents a tuple for comparison with Version.components_full.

        Args
            other: Object to munge
        Returns
            Full version component tuple for object
        Raises
            NotImplementedError: Incomparable other
        """
        if isinstance(other, Version):
            return other.components_full
        elif isinstance(other, (tuple, list)):
            return (tuple(other) + (0, 0, 0))[:4]
        elif isinstance(other, str):
            return (split_version(other) + (0, 0, 0))[:4]
        else:
            raise NotImplementedError(
                'Unable to compare Version and {!r}'.format(type(other)))

    def __eq__(self, other: Any) -> bool:
        """Test `Version` objects for equality.

        Importantly, padded version components are checked so that 0.1 is
        considered equal to 0.1.0.0.

        See also:
            ``~Version.__prepare_cmp_object``

        Args:
            other: Object to munge
        Returns:
            True if ``self`` is equal to ``other``
        """
        return self.components_full == self.__prepare_cmp_object(other)

    def __lt__(self, other: Any) -> bool:
        """Strict less-than test against comparable object.

        See also:
            ``~Version.__prepare_cmp_object``

        Args:
            other: Object to munge
        Returns:
            True if ``self`` is strictly less-than ``other``
        """
        return self.components_full < self.__prepare_cmp_object(other)

    def __hash__(self) -> str:
        """Create object-unique hash value.

        Returns:
            Object-unique hash value
        """
        return hash(repr(self))

    def set(self, components: Tuple[int]) -> None:
        """Set version components.

        Args:
            components: Version components
        """
        if isinstance(components, str):
            components = split_version(components)
        elif isinstance(components, list):
            components = tuple(components)
        padded = (components + (0, 0, 0))[:4]
        self.major, self.minor, self.micro, self.patch = padded
        self._resolution = len(components)

    @property
    def components_full(self) -> Tuple[int]:
        """Generate full length component tuple for version."""
        return self.major, self.minor, self.micro, self.patch

    @property
    def components(self) -> Tuple[int]:
        """Generate component tuple to initial resolution."""
        return self.components_full[:self._resolution]

    def bump(self, bump_type: str) -> None:
        """Bump a version string.

        Args:
            bump_type: Component to bump
        Raises:
            ValueError: Invalid ``bump_type`` argument
        """
        if bump_type == 'micro' and self._resolution < 3 \
                or bump_type == 'patch' and self._resolution < 4:
            raise ValueError('Invalid bump_type {!r} for version {!r}'.format(
                bump_type, self.components)
            )
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
            raise ValueError('Unknown bump_type {!r}'.format(bump_type))
        self.date = datetime.date.today()

    def bump_major(self) -> None:
        """Bump major version component."""
        self.bump('major')

    def bump_minor(self) -> None:
        """Bump minor version component."""
        self.bump('minor')

    def bump_micro(self) -> None:
        """Bump micro version component."""
        self.bump('micro')

    def bump_patch(self) -> None:
        """Bump patch version component."""
        self.bump('patch')

    def as_dict(self) -> Dict[str, int]:
        """Generate a dictionary of version components.

        Returns:
            Version as dictionary
        """
        return {k: v for k, v in zip(VERSION_COMPS, self.components)}

    def as_dotted(self) -> str:
        """Generate a dotted version string.

        Returns:
            Standard dotted version string
        """
        return '.'.join(str(s) for s in self.components)

    def as_hex(self) -> str:
        """Generate a hex version string.

        Returns:
            Version as hex string
        """
        return '0x' + ''.join('%02x' % n for n in self.components)

    def as_libtool(self) -> str:
        """Generate a libtool version string.

        Returns:
            Version as libtool string
        """
        return '%i:%i' % (self.major * 10 + self.minor, 20 + self.micro)

    def as_date(self) -> str:
        """Generate a ISO-8601 date string for release.

        Returns:
            Version’s release date as ISO-8601 date stamp
        """
        return self.date.isoformat()

    def as_tuple(self) -> Tuple[int]:
        """Generate a tuple of version components.

        Returns:
            Version components as tuple
        """
        return self.components

    def as_web(self) -> str:
        """Generate a web UA-style string for release.

        Returns:
            Version’s string in web UA-style
        """
        return '{}/{}'.format(self.name, self.as_dotted())


def split_version(version: str) -> Tuple[int]:
    """Split version string to components.

    Args:
        version Version string
    Returns:
        Components of version string
    Raises:
        ValueError: Invalid version string
    """
    if not re.fullmatch(VALID_VERSION, version):
        raise ValueError('Invalid version string {!r}'.format(version))

    return tuple(int(s) for s in version.split('.'))
