#
# coding=utf-8
"""utils - Utility functions for versionah"""
# Copyright © 2014-2015  James Rowe <jnrowe@gmail.com>
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

import re
import sys

import click


def success(text):
    """Format a success message with colour, if possible."""
    click.secho(text, fg='green', bold=True)


def fail(text):
    """Format a failure message with colour, if possible."""
    click.secho(text, fg='green', bold=True)


def warn(text):
    """Format a warning message with colour, if possible."""
    click.secho(text, fg='yellow', bold=True)


#: Custom filters for Jinja
FILTERS = {}


def filter_regexp(string, pattern, repl, count=0, flags=0):
    """Jinja filter for regexp replacements.

    See :func:`re.sub` for documentation.

    :param str string: Text to operate on
    :param str pattern: Regular expression to match
    :param str repl: Text to replace match with
    :param int count: Number of occurrences to replace
    :param int flags: Regular expression matching flags
    :rtype: `str`
    :return: Text with substitutions applied
    """
    if sys.version_info[:2] >= (2, 7):
        return re.sub(pattern, repl, string, count, flags)
    else:
        # regexps are cached, so this uglier path is no better than the 2.7
        # one.  Once 2.6 support disappears, so can this
        match = re.compile(pattern, flags=flags)
        return match.sub(repl, string, count)
FILTERS['regexp'] = filter_regexp
