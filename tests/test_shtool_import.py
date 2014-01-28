#
# coding=utf-8
"""test_shtool_import - GNU shtool import tests"""
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
    ('shtool/test.c', '1.2.3'),
    ('shtool/test.m4', '1.2.3'),
    ('shtool/test.perl', '1.2.3'),
    ('shtool/test.python', '1.2.3'),
    ('shtool/test.txt', '1.2.3'),
)
@read_tag
def test_read_shtool_files(file, expected):
    v = Version.read('tests/data/%s' % file)
    expect(v.as_dotted()) == expected
