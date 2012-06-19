#
"""general - Behave step definitions"""
# Copyright (C) 2011-2012  James Rowe <jnrowe@gmail.com>
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

from behave import (given, then, when)
from expecter import expect

import versionah


@given('I have the version {version}')
def g_have_version(context, version):
    context.version = versionah.Version(version)


@then('I see the version {version}')
def t_see_version(context, version):
    expect(context.version.as_dotted()) == version


@then('I see the string {text}')
def t_see_string(context, text):
    expect(context.string) == text


@given('I have the file {name}')
def g_have_file(context, name):
    context.name = name


@when('I read its content')
def w_read_content(context):
    context.version = versionah.Version.read("tests/data/%s" % context.name)


@when('I write its value to {name}')
def w_write_value(context, name):
    context.version.write("tests/data/%s" % name, "text")
    context.version = None
    context.execute_steps('''
        Given I have the file %s
        When I read its content
    ''' % name)
    os.unlink("tests/data/%s" % name)


@given('I have the package {name} version {version}')
def g_have_name_version(context, name, version):
    context.version = versionah.Version(version, name)


@then('I receive {error}')
def t_receive_exception(context, error):
    expect(context.exception.__class__.__name__) == error
