#
"""test_impl - Model implementation tests"""
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

from versionah.models import Version


TODAY = date.today()


@mark.parametrize('v', [
    ((0, 1, 0), 'unknown'),
    ((0, 1, 0), 'unknown'),
    ((0, 1, 0), 'unknown', date(2017, 11, 5)),
])
def test_version_hash_equal(v):
    assert hash(Version(*v)) == hash(Version(*v))


@mark.parametrize('v1, v2', [
    (((0, 1, 0), 'unknown'), ((1, 0, 0), 'unknown')),
    (((0, 1, 0), 'unknown'), ((0, 1, 0), 'different')),
    (((0, 1, 0), 'unknown', date(2017, 11, 5)),
     ((0, 1, 0), 'unknown', date(1980, 11, 5))),
])
def test_version_hash_unequal(v1, v2):
    assert hash(Version(*v1)) != hash(Version(*v2))
