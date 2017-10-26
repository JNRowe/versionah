#
# coding=utf-8
"""test_python_compat - Python output compatibility tests"""
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

from pytest import mark

from versionah.cmdline import CliVersion

from tests.utils import (execute_tag, expect_from_data, notravis_tag, tempdir,
                         write_tag)


@mark.parametrize('interp', [
    'python2.6',
    'python2.7',
    'python3.2',
    'python3.3',
)
@write_tag
@execute_tag
def test_python_compatibility(interp):
    with tempdir():
        CliVersion('1.0.1').write('test_wr.py', 'py')
        retval = call([interp, '-W', 'all', 'test_wr.py'], stdout=PIPE,
                      stderr=PIPE)
        expect_from_data('test_wr.py', retval, 0)


# Test interps not available on travis-ci.org, but available on all our test
# machines
@mark.parametrize('interp', [
    'python2.4',
    'python2.5',
    'python3.1',
    'python3.4',
])
@write_tag
@execute_tag
@notravis_tag
def test_python_compatibility_extra(interp):
    test_python_compatibility(interp)
