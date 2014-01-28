#
# coding=utf-8
"""test_read - Reading tests"""
# Copyright © 2011-2014  James Rowe <jnrowe@gmail.com>
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

from expecter import expect
from nose2.tools import params

from versionah import Version

from tests.utils import read_tag


@params(
    ('test_a', '0.1.0'),
    ('test_b', '1.0.0'),
    ('test_c', '2.1.3'),
)
@read_tag
def test_read_version_file(file, expected):
    v = Version.read('tests/data/%s' % file)
    expect(v.as_dotted()) == expected
