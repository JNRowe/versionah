#
"""general - Lettuce step definitions"""
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

import os

from nose.tools import assert_equal

from lettuce import world

import versionah

from util import step


@step(u'I have the version (%(VERSION)s)$')
def have_the_version(step, version):
    world.version = versionah.Version(version)


@step(u'I see the version (%(VERSION)s)$')
def see_the_version(step, expected):
    assert_equal(world.version.as_dotted(), expected)


@step(u'I see the string (.*)$')
def see_the_string(step, expected):
    assert_equal(world.string, expected)


@step(u'I have the file (.*)$')
def have_the_file(step, name):
    world.name = name


@step(u'I read its content$')
def read_content(step):
    world.version = versionah.Version.read("tests/data/%s" % world.name)


@step(u'I write its value to (.*)$')
def write_value_to_file(step, name):
    world.version.write("tests/data/%s" % name, "text")
    world.version = None
    step.given('I have the file %s' % name)
    step.given("I read its content")
    os.unlink("tests/data/%s" % name)


@step(u'I have the package (%(PACKAGE)s) version (%(VERSION)s)$')
def have_named_version(step, name, version):
    world.version = versionah.Version(version, name)


@step(u'I receive (.*)$')
def receive_exception(step, expected):
    assert_equal(unicode(world.exception.__class__.__name__), expected)
