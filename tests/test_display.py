#
# coding=utf-8
"""test_display - Display tests"""
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
    ('0.1.0', {'major': 0, 'minor': 1, 'micro': 0}),
    ('1.0.0', {'major': 1, 'minor': 0, 'micro': 0}),
    ('2.1.3', {'major': 2, 'minor': 1, 'micro': 3}),
)
def test_dict_display(v, expected):
    expect(Version(v).as_dict()) == expected


@params(
    ('0.1.0', '0.1.0'),
    ('1.0.0', '1.0.0'),
    ('2.1.3', '2.1.3'),
)
def test_dotted_display(v, expected):
    expect(Version(v).as_dotted()) == expected


@params(
    ('0.1.0', '0x000100'),
    ('1.0.0', '0x010000'),
    ('2.1.3', '0x020103'),
)
def test_hex_display(v, expected):
    expect(Version(v).as_hex()) == expected


@params(
    ('0.1.0', '1:20'),
    ('1.0.0', '10:20'),
    ('2.1.3', '21:23'),
)
def test_libtool_display(v, expected):
    expect(Version(v).as_libtool()) == expected


@params(
    ('0.1.0', '2011-03-21'),
    ('1.0.0', '2000-01-01'),
    ('2.1.3', '1970-01-01'),
)
def test_date_display(v, date_string):
    date_obj = date(*map(int, date_string.split('-')))
    expect(Version(v, date=date_obj).as_date()) == date_string


@params(
    ('unknown', '0.1.0', 'unknown/0.1.0'),
    ('test', '1.0.0', 'test/1.0.0'),
    ('cat', '2.1.3', 'cat/2.1.3'),
)
def test_web_display(name, v, expected):
    expect(Version(v, name=name).as_web()) == expected
