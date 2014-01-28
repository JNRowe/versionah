#
# coding=utf-8
"""test_reprs - String representation tests"""
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

from versionah import Version


TODAY = date.today()


def test_version_repr():
    expect(repr(Version())) == "Version((0, 1, 0), 'unknown', %r)" % TODAY


def test_version_repr_components():
    expect(repr(Version([0, 2, 0]))) \
        == "Version((0, 2, 0), 'unknown', %r)" % TODAY


def test_version_repr_name():
    expect(repr(Version(name='foo'))) \
        == "Version((0, 1, 0), 'foo', %r)" % TODAY


def test_version_repr_date():
    expect(repr(Version(date=date(1970, 1, 1)))) \
        == "Version((0, 1, 0), 'unknown', datetime.date(1970, 1, 1))"
