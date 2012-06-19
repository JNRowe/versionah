#
"""display - Behave step definitions"""
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

import datetime

from behave import (given, then, when)
from expecter import expect

import versionah


@when('I display its {dtype} representation')
def w_display_type(context, dtype):
    context.string = getattr(context.version, 'as_%s' % dtype)()


@then('I see the date string {date}')
def t_see_date(context, date):
    expect(context.string) == date


@given('I have version {version} created on {date}')
def g_have_version_date(context, version, date):
    y, m, d = map(int, date.split("-"))
    context.version = versionah.Version(version, date=datetime.date(y, m, d))
