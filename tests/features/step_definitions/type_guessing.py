#
"""type_guessing - Lettuce step definitions"""
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

from nose.tools import assert_equal

import versionah


@step(u'I pass it to (.*)')
def pass_to_function(step, function):
    world.result = getattr(versionah, function)([world.name, ])


@step(u'I pass (.*) argument ([^ ]+) to (.*)')
def pass_args_to_function(step, arg, value, function):
    world.result = getattr(versionah, function)(["--%s" % arg, value,
                                                 world.name])


@step(u'I see the file type (.*)')
def see_file_type(step, file_type):
    assert_equal(world.result[0].file_type, file_type)
