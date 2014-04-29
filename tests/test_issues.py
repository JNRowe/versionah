#
# coding=utf-8
"""test_issues - Issue regression tests"""
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

import argparse

from versionah import ValidatingAction

from tests.utils import argparse_setUpModule as setUpModule  # NOQA
from tests.utils import tearDownModule  # NOQA


def test_8_python_namespace_packages():
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', action=ValidatingAction)
    parser.parse_args(['--name=mypackage.subpackage', ])
