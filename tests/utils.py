#
# coding=utf-8
"""utils - Testing utilities"""
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

import os

from contextlib import contextmanager
from shutil import rmtree
from tempfile import mkdtemp

from expecter import expect


def read_tag(f):
    f.read = 1
    return f


def write_tag(f):
    f.write = 1
    return f


def execute_tag(f):
    f.execute = 1
    return f


def notravis_tag(f):
    f.no_travis = 1
    return f


@contextmanager
def tempdir():
    cwd = os.getcwd()
    d = mkdtemp()
    os.chdir(d)
    try:
        yield d
    finally:
        os.chdir(cwd)
        try:
            rmtree(d)
        except (OSError, IOError):
            pass


def expect_from_data(file, input, result):
    try:
        expect(input) == result
    except AssertionError as e:
        data = open(file).read()
        raise AssertionError("%s from %r" % (e.message, data))
