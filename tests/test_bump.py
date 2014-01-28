#
# coding=utf-8
"""test_bump - tests"""
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


@params(
    ('0.1.0', '1.0.0'),
    ('1.0.0', '2.0.0'),
    ('2.1.3', '3.0.0'),
)
def test_major_bumps(v1, v2):
    start = Version(v1)
    start.bump_major()
    expect(start) == Version(v2)


@params(
    ('0.1.0', '0.2.0'),
    ('1.0.0', '1.1.0'),
    ('2.1.3', '2.2.0'),
)
def test_minor_bumps(v1, v2):
    start = Version(v1)
    start.bump_minor()
    expect(start) == Version(v2)


@params(
    ('0.1.0', '0.1.1'),
    ('1.0.0', '1.0.1'),
    ('2.1.3', '2.1.4'),
)
def test_micro_bumps(v1, v2):
    start = Version(v1)
    start.bump_micro()
    expect(start) == Version(v2)


@params(
    ('0.1.0.0', '0.1.0.1'),
    ('1.0.0.0', '1.0.0.1'),
    ('0.2.1.3', '0.2.1.4'),
)
def test_patch_bumps(v1, v2):
    start = Version(v1)
    start.bump_patch()
    expect(start) == Version(v2)
