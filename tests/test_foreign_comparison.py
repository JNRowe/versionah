#
"""test_foreign_comparison - Foreign comparison tests"""
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

from pytest import mark, raises

from versionah.models import Version


@mark.parametrize('t, v2', [
    ((0, 1, 0), '0.1.0'),
    ((1, 0, 0), '1.0.0'),
])
def test_tuple_equal_comparison(t, v2):
    assert Version(t) == Version(v2)


@mark.parametrize('t, v2', [
    ((1, 0, 0), '2.0.0'),
    ((2, 1, 3), '3.0.0'),
])
def test_tuple_unequal_comparison(t, v2):
    assert Version(t) != Version(v2)


@mark.parametrize('s, v2', [
    ('0.1.0', '0.1.0'),
    ('1.0.0', '1.0.0'),
])
def test_string_equal_comparison(s, v2):
    assert Version(s) == Version(v2)


@mark.parametrize('s, v2', [
    ('1.0.0', '2.0.0'),
    ('2.1.3', '3.0.0'),
])
def test_string_unequal_comparison(s, v2):
    assert Version(s) != Version(v2)


@mark.parametrize('l, v2', [
    ([0, 1, 0], '0.1.0'),
    ([1, 0, 0], '1.0.0'),
])
def test_list_equal_comparison(l, v2):
    assert Version(l) == Version(v2)


@mark.parametrize('l, v2', [
    ([1, 0, 0], '2.0.0'),
    ([2, 1, 3], '3.0.0'),
])
def test_list_unequal_comparison(l, v2):
    assert Version(l) != Version(v2)


def test_unsupported_comparision():
    with raises(NotImplementedError,
                match="Unable to compare Version and <class 'float'>"):
        float(3.2) == Version('0.2.0')
