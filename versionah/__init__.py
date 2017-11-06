#
"""versionah - Simple version specification management.

versionah is a GPL v3 licensed module for maintaining version information files
for use in project management.
"""
# Copyright © 2011-2017  James Rowe <jnrowe@gmail.com>
#                        TakesxiSximada <takeshi.shimada@ticketstar.jp>
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

from . import _version


__version__ = _version.dotted
__date__ = _version.date
__copyright__ = 'Copyright © 2011-2015  James Rowe <jnrowe@gmail.com>'

from contextlib import suppress

# This is here to workaround UserWarning messages caused by path fiddling in
# dependencies
with suppress(ImportError):
    import pkg_resources  # NOQA: F401
