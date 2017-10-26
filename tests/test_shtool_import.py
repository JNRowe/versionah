#
"""test_shtool_import - GNU shtool import tests"""
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

from pytest import mark

from versionah.cmdline import CliVersion


@mark.requires_read
@mark.parametrize('file, expected', [
    ('shtool/test.c', '1.2.3'),
    ('shtool/test.m4', '1.2.3'),
    ('shtool/test.perl', '1.2.3'),
    ('shtool/test.python', '1.2.3'),
    ('shtool/test.txt', '1.2.3'),
])
def test_read_shtool_files(file, expected):
    v = CliVersion.read('tests/data/{}'.format(file))
    assert v.as_dotted() == expected
