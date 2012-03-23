#
"""output_validity - Behave step definitions"""
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
import subprocess

from behave import (then, when)

from nose.tools import assert_equal

import versionah


@when('I process {name} with {linter}')
def w_process_with_linter(context, name, linter):
    file_type = versionah.process_command_line([name, ])[0].file_type
    context.version.write("tests/data/%s" % name, file_type)
    context.retval = subprocess.call(
        linter.split() + ["tests/data/%s" % name, ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    os.unlink("tests/data/%s" % name)


@then('the linter returns 0')
def t_linter_returns_0(context):
    assert_equal(context.retval, 0)
