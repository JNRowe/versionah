#
# coding=utf-8
"""test_cmp - Object comparison tests"""
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

from versionah import Version


def test_cmp_version_to_version():
    expect(Version()) == Version()


def test_cmp_version_to_tuple():
    expect(Version()) == (0, 1, 0)


def test_cmp_version_to_list():
    expect(Version()) == [0, 1, 0]


def test_cmp_version_to_str():
    expect(Version()) == '0.1.0'


def test_cmp_version_less_than():
    expect(Version((0, 1, 0))) < Version((0, 2, 0))


def test_cmp_version_less_than_equal():
    expect(Version((0, 1, 0))) <= Version((0, 2, 0))
    expect(Version((0, 2, 0))) <= Version((0, 2, 0))


def test_cmp_version_greather_than_equal():
    expect(Version((0, 2, 0))) >= Version((0, 1, 0))
    expect(Version((0, 2, 0))) >= Version((0, 2, 0))
