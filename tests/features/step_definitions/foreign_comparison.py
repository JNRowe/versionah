#
"""foreign_comparison - Lettuce step definitions"""
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

import re

from lettuce import world

import versionah

from util import step


@step(u'I have the Version object for (%(VERSION)s) and (?:tuple|string) ' \
      '(%(VERSION)s)')
def have_version_object_and_tuple(step, version1, version2):
    world.version1 = versionah.Version(version1)
    world.version2 = versionah.split_version(version2)


@step(u'I have the Version object for (%(VERSION)s) and list (%(VERSION)s)')
def have_version_object_and_list(step, version1, version2):
    world.version1 = versionah.Version(version1)
    world.version2 = list(versionah.split_version(version2))


@step(u'I have the Version object for (%(VERSION)s) and RegExp matcher for ' \
      '(%(VERSION)s)')
def have_version_object_and_re_obj(step, version1, version2):
    world.version1 = versionah.Version(version1)
    world.version2 = re.compile(version2)
