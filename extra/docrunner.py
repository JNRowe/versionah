#! /usr/bin/env python
# coding=utf-8
"""docrunner - Execute shell tests"""
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

__doc__ += """.

Run shell examples in reST literal blocks."""

import doctest
import sys

import shelldoctest as sd

if __name__ == '__main__':
    sys.exit(doctest.testfile(sys.argv[1], module_relative=False,
                              extraglobs={'system_command': sd.system_command},
                              parser=sd.ShellDocTestParser())[0])
