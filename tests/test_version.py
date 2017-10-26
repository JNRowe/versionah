#
"""test_version - Version object tests"""
# Copyright © 2011-2017  James Rowe <jnrowe@gmail.com>
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

from datetime import date

from pytest import mark

from versionah.cmdline import CliVersion
from versionah.models import Version


@mark.parametrize('value', [
    '0.3.0',
    [0, 3, 0],
    (0, 3, 0),
])
def test_version_set(value):
    v = Version()
    v.set(value)
    assert v.components == (0, 3, 0)


@mark.parametrize('bump_type, expected', [
    ('major', (1, 0, 0, 0)),
    ('minor', (0, 2, 0, 0)),
    ('micro', (0, 1, 1, 0)),
    ('patch', (0, 1, 0, 1)),
])
def test_version_bump(bump_type, expected):
    v = Version((0, 1, 0, 0))
    getattr(v, 'bump_{}'.format(bump_type))()
    assert v.components == expected


@mark.parametrize('display_type, expected', [
    ('date', '2012-05-11'),
    ('dict', {'major': 0, 'minor': 1, 'micro': 0}),
    ('dotted', '0.1.0'),
    ('hex', '0x000100'),
    ('libtool', '1:20'),
    ('tuple', (0, 1, 0)),
    ('web', 'unknown/0.1.0'),
])
def test_version_display(display_type, expected):
    v = CliVersion(date=date(2012, 5, 11))
    assert v.display(display_type) == expected


def test_default_date():
    v = CliVersion()
    assert v.display('date') == str(date.today())
