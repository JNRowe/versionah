#
"""test_type_guessing - File type guessings tests"""
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

from versionah.cmdline import guess_type


@mark.parametrize('filename, expected', [
    ('test.py', 'py'),
    ('test.rb', 'rb'),
    ('test', 'text'),
])
def test_guess_type_from_name(filename, expected):
    assert guess_type(filename) == expected
