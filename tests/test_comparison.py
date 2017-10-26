#
"""test_comparison - Version comparison tests"""
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
    ('0.1.0', '0.1.0'),
    ('1.0.0', '1.0.0'),
])
def test_equal_versions(v1, v2):
    assert Version(v1) == Version(v2)


@mark.parametrize('v1, v2', [
    ('1.0.0', '2.0.0'),
    ('2.1.3', '3.0.0'),
])
def test_unequal_versions(v1, v2):
    assert Version(v1) != Version(v2)


@mark.parametrize('v1, v2, expected', [
    ('2.1.1', '2.1.4', '2.1.4'),
    ('2.1.3', '3.0.0', '3.0.0'),
    ('3.0.0', '2.9.99.9', '3.0.0'),
])
def test_greatest_version(v1, v2, expected):
    assert max(Version(v1), Version(v2)) == Version(expected)


@mark.parametrize('v1, v2', [
    ('0.1.0', '0.1'),
    ('0.1', '0.1.0'),
    ('0.1.0.0', '0.1.0'),
    ('0.1.0.0', '0.1'),
])
def test_equal_versions_with_uneven_components(v1, v2):
    assert Version(v1) == Version(v2)


@mark.parametrize('v1, v2', [
    ('0.1', '0.1.0.1'),
    ('0.1.1.1', '0.1.1'),
])
def test_unequal_versions_with_uneven_components(v1, v2):
    assert Version(v1) != Version(v2)
