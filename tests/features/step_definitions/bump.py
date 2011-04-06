#
"""bump - Lettuce step definitions"""
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

from lettuce import step
from lettuce import world


@step(u'I bump its major version')
def bump_major_version(step):
    world.version.bump("major")


@step(u'I bump its minor version')
def bump_minor_version(step):
    world.version.bump("minor")


@step(u'I bump its micro version')
def bump_micro_version(step):
    world.version.bump("micro")


@step(u'I bump its patch version')
def bump_patch_version(step):
    world.version.bump("patch")
