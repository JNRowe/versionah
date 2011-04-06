#
"""display - Lettuce step definitions"""
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

import datetime

from lettuce import world

from nose.tools import assert_equal

import versionah

from util import step


@step(u'I display its web representation')
def display_web_representation(step):
    world.string = world.version.as_web()


@step(u'I display its dotted representation')
def display_dotted_representation(step):
    world.string = world.version.as_dotted()


@step(u'I display its hex representation')
def display_hex_representation(step):
    world.string = world.version.as_hex()


@step(u'I display its libtool representation')
def display_libtool_representation(step):
    world.string = world.version.as_libtool()


@step(u'I display its string representation')
def display_string_representation(step):
    world.string = str(world.version)


@step(u'I display its date representation')
def display_date_representation(step):
    world.string = world.version.as_date()


@step(u'I see the date string (.*)')
def see_the_date(step, expected):
    assert_equal(world.string, expected)


@step(u'I have the version (%(VERSION)s) created on (%(DATE)s)')
def have_the_version_with_date(step, version, date):
    y, m, d = map(int, date.split("-"))
    world.version = versionah.Version(version, date=datetime.date(y, m, d))
