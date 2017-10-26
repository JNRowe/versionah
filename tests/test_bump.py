#
"""test_bump - tests"""
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

from versionah.models import Version


@mark.parametrize('v1, v2', [
    ('0.1.0', '1.0.0'),
    ('1.0.0', '2.0.0'),
    ('2.1.3', '3.0.0'),
])
def test_major_bumps(v1, v2):
    start = Version(v1)
    start.bump_major()
    assert start == Version(v2)


@mark.parametrize('v1, v2', [
    ('0.1.0', '0.2.0'),
    ('1.0.0', '1.1.0'),
    ('2.1.3', '2.2.0'),
])
def test_minor_bumps(v1, v2):
    start = Version(v1)
    start.bump_minor()
    assert start == Version(v2)


@mark.parametrize('v1, v2', [
    ('0.1.0', '0.1.1'),
    ('1.0.0', '1.0.1'),
    ('2.1.3', '2.1.4'),
])
def test_micro_bumps(v1, v2):
    start = Version(v1)
    start.bump_micro()
    assert start == Version(v2)


@mark.parametrize('v1, v2', [
    ('0.1.0.0', '0.1.0.1'),
    ('1.0.0.0', '1.0.0.1'),
    ('0.2.1.3', '0.2.1.4'),
])
def test_patch_bumps(v1, v2):
    start = Version(v1)
    start.bump_patch()
    assert start == Version(v2)
