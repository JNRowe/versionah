#
# coding=utf-8
"""utils - Testing utilities"""
# Copyright © 2011-2015  James Rowe <jnrowe@gmail.com>
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

def notravis_tag(f):
    f.no_travis = 1
    return f


def expect_from_data(file, input, result):
    try:
        assert input == result
    except AssertionError as e:
        data = open(file).read()
        raise AssertionError("%s from %r" % (e.message, data))
