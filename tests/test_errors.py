#
"""test_errors - Error tests"""
# Copyright © 2011-2017  James Rowe <jnrowe@gmail.com>
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

from click import BadParameter
from pytest import mark, raises

from versionah.cmdline import (CliVersion, NameParamType, ReMatchParamType,
                               VersionParamType)
from versionah.models import Version


@mark.parametrize('components', [
    [1, ],
    [1, 2, 3, 4, 5],
])
def test_version_init_invalid_count(components):
    with raises(ValueError, match='Invalid number of components'):
        Version(components)


@mark.parametrize('components', [
    [1, 2, 'a'],
    [1, 2, -4],
])
def test_version_init_invalid_component_type(components):
    with raises(ValueError, match='Invalid component values'):
        Version(components)


def test_version___eq___unknown_type():
    with raises(NotImplementedError,
                match="Unable to compare Version and <class 'bool'>"):
        Version() == True  # NOQA: E712


def test_version_bump_invalid_type():
    v = Version()
    with raises(ValueError, match="Invalid bump_type 'patch'"):
        v.bump('patch')


def test_version_bump_invalid_type_name():
    v = Version()
    with raises(ValueError, match="Unknown bump_type 'pico'"):
        v.bump('pico')


def test_version_read_no_identifier():
    with raises(ValueError,
                match="No valid version identifier in 'setup.py'"):
        CliVersion.read('setup.py')


@mark.parametrize('name', [
    '__',
    '3dom',  # initial digit
    'mypackage.',  # trailing punctuation
])
def test_process_command_line_invalid_package_name(name):
    p = NameParamType()
    with raises(BadParameter, match="'{}'".format(name)):
        p.convert(name, None, None)


def test_ReMatchParamType_no_setup():
    p = ReMatchParamType()
    with raises(NotImplementedError, match="No matcher"):
        p.convert('', None, None)


def test_process_command_line_invalid_package_version():
    p = VersionParamType()
    with raises(BadParameter, match="'__'"):
        p.convert('__', None, None)
