#
"""test_validity - Version validity tests"""
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


@mark.parametrize('v', [
    '1',
    '1.2.3.4.5',
    '1.2.-1.0',
])
def test_version_validation(v):
    with raises(ValueError, match='Invalid version string {!r}'.format(v)):
        Version(v)
