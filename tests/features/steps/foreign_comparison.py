#
"""foreign_comparison - Behave step definitions"""
# Copyright (C) 2011-2012  James Rowe <jnrowe@gmail.com>
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

import re

from behave import given

import versionah


@given('I have the Version object for {version1} and tuple {version2}')
def g_have_version_tuple(context, version1, version2):
    context.version1 = versionah.Version(version1)
    context.version2 = versionah.split_version(version2)


@given('I have the Version object for {version1} and string {version2}')
def g_have_version_string(context, version1, version2):
    context.version1 = versionah.Version(version1)
    context.version2 = versionah.split_version(version2)


@given('I have the Version object for {version1} and list {version2}')
def g_have_version_list(context, version1, version2):
    context.version1 = versionah.Version(version1)
    context.version2 = list(versionah.split_version(version2))


@given('I have the Version object for {version1} and RegExp matcher for ' \
      '{version2}')
def have_version_regexp(context, version1, version2):
    context.version1 = versionah.Version(version1)
    context.version2 = re.compile(version2)
