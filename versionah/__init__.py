#
# coding=utf-8
"""versionah - Simple version specification management

versionah is a GPL v3 licensed module for maintaining version information files
for use in project management.
"""
# Copyright © 2011-2015  James Rowe <jnrowe@gmail.com>
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

from . import _version


__version__ = _version.dotted
__date__ = _version.date
__copyright__ = 'Copyright (C) 2011-2015  James Rowe <jnrowe@gmail.com>'

# This is here to workaround UserWarning messages caused by path fiddling in
# dependencies
try:
    import pkg_resources  # NOQA
except ImportError:
    pass
