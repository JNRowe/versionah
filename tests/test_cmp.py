#
"""test_cmp - Object comparison tests"""
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

from pytest import mark

from versionah.models import Version


def test_cmp_version_to_version():
    assert Version() == Version()


def test_cmp_version_to_tuple():
    assert Version() == (0, 1, 0)


def test_cmp_version_to_list():
    assert Version() == [0, 1, 0]


def test_cmp_version_to_str():
    assert Version() == '0.1.0'


def test_cmp_version_less_than():
    assert Version((0, 1, 0)) < Version((0, 2, 0))


@mark.parametrize('v1, v2', [
    ((0, 1, 0), (0, 2, 0)),
    ((0, 2, 0), (0, 2, 0)),
])
def test_cmp_version_less_than_equal(v1, v2):
    assert Version(v1) <= Version(v2)


@mark.parametrize('v1, v2', [
    ((0, 2, 0), (0, 1, 0)),
    ((0, 2, 0), (0, 2, 0)),
])
def test_cmp_version_greather_than_equal(v1, v2):
    assert Version(v1) >= Version(v2)
