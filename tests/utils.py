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

from expecter import (_RaisesExpectation, expect)
from mock import (Mock, patch)


class _RaisesOSErrorExpectation(_RaisesExpectation):
    def __init__(self, code, message):
        self.code = code
        self.message = message

    def validate_failure(self, exc_type, exc_value):
        code = exc_value.errno
        message = exc_value.strerror
        if self.code != code:
            raise AssertionError('Expected code %s but got %s'
                                 % (self.code, exc_value[0]))
        if not message.endswith(self.message):
            raise AssertionError("Expected to end with OSError('%s') but got "
                                 "%s('%s')" % (self.message, exc_type.__name__,
                                               exc_value))
        elif issubclass(exc_type, OSError):
            return True
        else:
            pass


def raises_OSError(code, message):
    return _RaisesOSErrorExpectation(code, message)


expect.raises_OSError = staticmethod(raises_OSError)

def exit_wrapper(status, message):
    """Stub for ArgumentParser.exit() calls"""
    raise OSError(status, message.strip())


def argparse_setUpModule():
    patch('versionah.argparse.ArgumentParser.exit',
          new=Mock(side_effect=exit_wrapper)).start()
    patch('versionah.argparse.ArgumentParser.print_usage').start()


def tearDownModule():
    patch.stopall()


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
