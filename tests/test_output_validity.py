#
"""test_output_validity - Output validity tests"""
# Copyright © 2012-2017  James Rowe <jnrowe@gmail.com>
#
# This file is part of versionah.
#
# versionah is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# versionah is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# versionah.  If not, see <http://www.gnu.org/licenses/>.

from shutil import which
from subprocess import PIPE, call

from pytest import mark, skip

from versionah.cmdline import CliVersion, guess_type


@mark.requires_exec
@mark.requires_write
@mark.parametrize('v, filename, linter', [
    ('1.0.1', 'test_wr.c', 'splint'),
    ('1.0.1', 'test_wr.m4', 'm4 -P -E -E'),
    ('1.0.1', 'test_wr.py', 'python -W all'),
    ('1.0.1', 'test_wr.rb', 'ruby -c'),
])
def test_output_validatity(v, filename, linter, tmpdir):
    if not which(linter):
        skip('Linter {!r} unavailable'.format(linter))
    file_type = guess_type(filename)
    file_loc = tmpdir.join(filename).strpath
    CliVersion(v).write(file_loc, file_type)
    retval = call(linter.split() + [file_loc, ], stdout=PIPE, stderr=PIPE)
    assert retval == 0
