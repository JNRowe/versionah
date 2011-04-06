#
"""comparison - Lettuce step definitions"""
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

from lettuce import world

from nose.tools import assert_equal

import versionah

from util import step


@step(u'I have the versions (%(VERSION)s) and (%(VERSION)s)')
def have_versions(step, version1, version2):
    world.version1 = versionah.Version(version1)
    world.version2 = versionah.Version(version2)


@step(u'I compare them for equality')
def compare_equality(step):
    try:
        world.result = unicode(world.version1 == world.version2)
    except Exception as e:
        world.exception = e


@step(u'I see the comparison (.*)')
def see_comparison_result(step, expected):
    assert_equal(world.result, expected)


@step(u'I search for the greatest')
def find_max(step):
    world.version = max((world.version1, world.version2))
