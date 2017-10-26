#
"""test_issues - Issue regression tests"""
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

from versionah.cmdline import NameParamType


def test_8_python_namespace_packages():
    p = NameParamType()
    assert p.convert('mypackage.subpackage', None, None) \
        == 'mypackage.subpackage'
