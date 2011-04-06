#
"""output_validity - Lettuce step definitions"""
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
import subprocess

from lettuce import step
from lettuce import world

from nose.tools import assert_equal

import versionah


@step(u'I process (.*) with (.*)')
def process_with_linter(step, name, linter):
    file_type = versionah.process_command_line([name, ])[0].file_type
    world.version.write("tests/data/%s" % name, file_type)
    world.retval = subprocess.call(
        linter.split() + ["tests/data/%s" % name, ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    os.unlink("tests/data/%s" % name)


@step(u'linter returns 0')
def checker_returns_zero(step):
    assert_equal(world.retval, 0)
