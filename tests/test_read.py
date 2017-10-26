#
"""test_read - Reading tests"""
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
    ('test_a', '0.1.0'),
    ('test_b', '1.0.0'),
    ('test_c', '2.1.3'),
])
def test_read_version_file(file, expected):
    v = CliVersion.read('tests/data/{}'.format(file))
    assert v.as_dotted() == expected
