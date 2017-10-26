#
"""test_name - Name tests"""
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


@mark.parametrize('name, v, expected', [
    ('cat', '0.1.0', 'cat v0.1.0'),
    ('dog', '1.0.0', 'dog v1.0.0'),
    ('fish', '2.1.3', 'fish v2.1.3'),
])
def test_name_versions(name, v, expected):
    v1 = Version(v, name=name)
    assert str(v1) == expected


@mark.parametrize('name, v, expected', [
    ('cat-meow', '0.1.0', 'cat-meow v0.1.0'),
    ('dog-bark', '1.0.0', 'dog-bark v1.0.0'),
    ('fish-bubble', '2.1.3', 'fish-bubble v2.1.3'),
])
def test_name_version_with_dashes_and_underscores(name, v, expected):
    v1 = Version(v, name=name)
    assert str(v1) == expected


@mark.parametrize('name, v, expected', [
    ('cat-2', '0.1.0', 'cat-2 v0.1.0'),
    ('dog1', '1.0.0', 'dog1 v1.0.0'),
])
def test_name_version_with_numeric_suffixes(name, v, expected):
    v1 = Version(v, name=name)
    assert str(v1) == expected
