#
"""utils - Utility functions for versionah."""
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

    See also:
        :func:`re.sub`

    Args:
        string (str): Text to operate on
        pattern (str): Regular expression to match
        repl (str): Text to replace match with
        count (int): Number of occurrences to replace
        flags (int): Regular expression matching flags
    Returns:
        str: Text with substitutions applied
    """
    return re.sub(pattern, repl, string, count, flags)
FILTERS['regexp'] = filter_regexp  # NOQA: E305
