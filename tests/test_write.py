#
# coding=utf-8
"""test_write - Writing tests"""
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

from os import unlink

from expecter import expect
from nose2.tools import params

from versionah import Version

from tests.utils import write_tag


@params(
    ('0.1.0', 'test_wr_a'),
    ('1.0.0', 'test_wr_b'),
    ('2.1.3', 'test_wr_c'),
)
@write_tag
def test_write_version_file(v, file):
    Version(v).write('tests/data/%s' % file, 'text')
    read = Version.read('tests/data/%s' % file)
    expect(read.as_dotted()) == v
    # Don't wrap in try/finally, so we can inspect if we get failures
    unlink('tests/data/%s' % file)
