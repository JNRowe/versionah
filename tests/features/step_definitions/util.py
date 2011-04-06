#
"""util - Lettuce step definition helpers"""
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

from lettuce import step as lettuce_step

import versionah


def step(match):
    """Replace values in match strings with data from versionah module

    The purpose is entirely to improve the look and readability of the steps
    defined below, it provides nothing over hard coding the values in step
    definitions.
    """
    valid_dict = dict([(s[6:], getattr(versionah, s)) for s in dir(versionah)
                       if s.startswith("VALID_")])
    return lettuce_step(match % valid_dict)
