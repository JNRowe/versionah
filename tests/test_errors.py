#! /usr/bin/python -tt
# coding=utf-8
"""test_errors - Error tests"""
# Copyright © 2012  James Rowe <jnrowe@gmail.com>
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

import argparse

from expecter import expect
from mock import (Mock, patch)
from nose2.tools import params

from versionah import (Version, ValidatingAction)

from tests.utils import raises_OSError

expect.raises_OSError = staticmethod(raises_OSError)


def exit_wrapper(status, message):
    """Stub for OptionParser.exit() calls"""
    raise OSError(status, message.strip())


def setUpModule():
    patch('versionah.argparse.ArgumentParser.exit',
          new=Mock(side_effect=exit_wrapper)).start()
    patch('versionah.argparse.ArgumentParser.print_usage').start()


def tearDownModule():
    patch.stopall()


@params(
    ([1, ], ),
    ([1, 2, 3, 4, 5], ),
)
def test_version_init_invalid_count(components):
    with expect.raises(ValueError,
                       'Invalid number of components in %r' % components):
        Version(components)


@params(
    ([1, 2, 'a'], ),
    ([1, 2, -4], ),
)
def test_version_init_invalid_component_type(components):
    with expect.raises(ValueError,
                       'Invalid component values in %r' % components):
        Version(components)


def test_version___eq___unknown_type():
    # Differs between Python 2 and 3
    true_repr = repr(type(True))
    with expect.raises(NotImplementedError,
                       'Unable to compare Version and %s' % true_repr):
        Version() == True


def test_version_bump_invalid_type():
    v = Version()
    with expect.raises(ValueError,
                       "Invalid bump_type 'patch' for version (0, 1, 0)"):
        v.bump('patch')


def test_version_bump_invalid_type_name():
    v = Version()
    with expect.raises(ValueError, "Unknown bump_type 'pico'"):
        v.bump('pico')


def test_version_read_no_identifier():
    with expect.raises(ValueError,
                       "No valid version identifier in 'setup.py'"):
        Version.read('setup.py')


def test_process_command_line_invalid_package_name():
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', action=ValidatingAction)
    with expect.raises_OSError(2, "Invalid string for --name: '__'"):
        parser.parse_args(['--name=__'])


def test_process_command_line_invalid_package_version():
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', action=ValidatingAction)
    with expect.raises_OSError(2, "Invalid string for --version: '__'"):
        parser.parse_args(['--version=__'])
