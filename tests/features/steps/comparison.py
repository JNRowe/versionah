#
"""comparison - Behave step definitions"""
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

from behave import (given, then, when)

from nose.tools import assert_equal

import versionah


@given('I have the versions {version1} and {version2}')
def g_have_versions(context, version1, version2):
    context.version1 = versionah.Version(version1)
    context.version2 = versionah.Version(version2)


@when('I compare them for equality')
def w_comare_eq(context):
    try:
        context.result = context.version1 == context.version2
    except Exception as e:
        context.exception = e


@then('I see the comparison {result}')
def t_see_result(context, result):
    assert_equal(str(context.result), result)


@when('I search for the greatest')
def w_search_max(context):
    context.version = max((context.version1, context.version2))
