#
# coding=utf-8
"""test_output_validity - Output validity tests"""
# Copyright © 2011-2015  James Rowe <jnrowe@gmail.com>
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

from subprocess import (call, PIPE)

from nose2.tools import params

from versionah.cmdline import (CliVersion, guess_type)

from tests.utils import (execute_tag, expect_from_data, tempdir, write_tag)


@params(
    ('1.0.1', 'test_wr.c', 'splint'),
    ('1.0.1', 'test_wr.m4', 'm4 -P -E -E'),
    ('1.0.1', 'test_wr.py', 'python -W all'),
    ('1.0.1', 'test_wr.rb', 'ruby -c'),
)
@write_tag
@execute_tag
def test_output_validatity(v, filename, linter):
    file_type = guess_type(filename)
    with tempdir():
        CliVersion(v).write(filename, file_type)
        retval = call(linter.split() + [filename, ],
                      stdout=PIPE, stderr=PIPE)
        expect_from_data(filename, retval, 0)
