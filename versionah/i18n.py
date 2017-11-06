#
"""i18n - internationalisation support for versionah."""
# Copyright © 2011-2015  James Rowe <jnrowe@gmail.com>
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

import gettext

from os import path

PACKAGE_LOCALE = path.join(path.dirname(__file__), 'locale')

gettext.install('versionah', PACKAGE_LOCALE)

_, N_ = gettext.gettext, gettext.ngettext
