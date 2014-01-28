#
# coding=utf-8
"""test_version - Version object tests"""
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

from datetime import date

from expecter import expect
from nose2.tools import params

from versionah import Version


@params(
    '0.3.0',
    [0, 3, 0],
    ((0, 3, 0), ),
)
def test_version_set(value):
    v = Version()
    v.set(value)
    expect(v.components) == (0, 3, 0)


@params(
    ('major', (1, 0, 0, 0)),
    ('minor', (0, 2, 0, 0)),
    ('micro', (0, 1, 1, 0)),
    ('patch', (0, 1, 0, 1)),
)
def test_version_bump(bump_type, expected):
    v = Version((0, 1, 0, 0))
    getattr(v, 'bump_%s' % bump_type)()
    expect(v.components) == expected


@params(
    ('date', '2012-05-11'),
    ('dict', {'major': 0, 'minor': 1, 'micro': 0}),
    ('dotted', '0.1.0'),
    ('hex', '0x000100'),
    ('libtool', '1:20'),
    ('tuple', (0, 1, 0)),
    ('web', 'unknown/0.1.0'),
)
def test_version_display(display_type, expected):
    v = Version(date=date(2012, 5, 11))
    expect(v.display(display_type)) == expected
