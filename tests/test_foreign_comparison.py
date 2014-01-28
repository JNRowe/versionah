#
# coding=utf-8
"""test_foreign_comparison - Foreign comparison tests"""
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
    ((0, 1, 0), '0.1.0'),
    ((1, 0, 0), '1.0.0'),
)
def test_tuple_equal_comparison(t, v2):
    expect(Version(t)) == Version(v2)


@params(
    ((1, 0, 0), '2.0.0'),
    ((2, 1, 3), '3.0.0'),
)
def test_tuple_unequal_comparison(t, v2):
    expect(Version(t)) != Version(v2)


@params(
    ('0.1.0', '0.1.0'),
    ('1.0.0', '1.0.0'),
)
def test_string_equal_comparison(s, v2):
    expect(Version(s)) == Version(v2)


@params(
    ('1.0.0', '2.0.0'),
    ('2.1.3', '3.0.0'),
)
def test_string_unequal_comparison(s, v2):
    expect(Version(s)) != Version(v2)


@params(
    ([0, 1, 0], '0.1.0'),
    ([1, 0, 0], '1.0.0'),
)
def test_list_equal_comparison(l, v2):
    expect(Version(l)) == Version(v2)


@params(
    ([1, 0, 0], '2.0.0'),
    ([2, 1, 3], '3.0.0'),
)
def test_list_unequal_comparison(l, v2):
    expect(Version(l)) != Version(v2)


def test_unsupported_comparision():
    from sys import version_info
    repr_name = 'class' if version_info[0] >= 3 else 'type'

    with expect.raises(NotImplementedError, 'Unable to compare Version and '
                       "<%s 'float'>" % repr_name):
        float(3.2) == Version('0.2.0')
