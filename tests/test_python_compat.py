#
"""test_python_compat - Python output compatibility tests"""
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

from os import getenv
from shutil import which
from subprocess import PIPE, call

from pytest import mark, skip

from versionah.cmdline import CliVersion


@mark.requires_exec
@mark.requires_write
@mark.parametrize('interp', [
    'python2.6',
    'python2.7',
    'python3.2',
    'python3.3',
])
def test_python_compatibility(interp, tmpdir):
    if not which(interp):
        skip('Interpreter {!r} unavailable'.format(interp))
    file_loc = tmpdir.join('test_wr.py').strpath
    CliVersion('1.0.1').write(file_loc, 'py')
    retval = call([interp, '-W', 'all', file_loc], stdout=PIPE,
                  stderr=PIPE)
    assert retval == 0


# Test interps not available on travis-ci.org, but available on all our test
# machines
@mark.skipif(getenv('TRAVIS_PYTHON_VERSION'), reason='Unavailable on travis')
@mark.requires_exec
@mark.requires_write
@mark.parametrize('interp', [
    'python2.4',
    'python2.5',
    'python3.1',
    'python3.4',
])
def test_python_compatibility_extra(interp):
    if not which(interp):
        skip('Interpreter {!r} unavailable'.format(interp))
    test_python_compatibility(interp)
