#
"""utils - Testing utilities"""
# Copyright © 2012-2017  James Rowe <jnrowe@gmail.com>
#                        Marc Abramowitz <marc@marc-abramowitz.com>
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


def expect_from_data(file, input, result):
    try:
        assert input == result
    except AssertionError as e:
        with open(file).read() as f:
            data = f.read()
        raise AssertionError('{} from {!r}'.format(e, data))
