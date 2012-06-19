#
"""type_guessing - Behave step definitions"""
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

from behave import (then, when)
from expecter import expect

import versionah


@when('I pass it to {function}')
def w_pass_to_function(context, function):
    context.result = getattr(versionah, function)([context.name, ])


@when('I pass {arg} argument {value} to {function}')
def w_pass_to_function_with_args(context, arg, value, function):
    context.result = getattr(versionah, function)(["--%s" % arg, value,
                                                  context.name])


@then('I see the file type {file_type}')
def t_see_file_type(context, file_type):
    expect(context.result[0].file_type) == file_type
