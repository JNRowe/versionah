#
"""test_python_compat - Python output compatibility tests"""
# Copyright © 2012-2018  James Rowe <jnrowe@gmail.com>
#
# SPDX-License-Identifier: GPL-3.0-or-later
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

from shutil import which
from subprocess import PIPE, call

from pytest import mark, skip

from versionah.cmdline import CliVersion


@mark.requires_exec
@mark.requires_write
@mark.parametrize(
    "interp",
    [
        "python2.7",
        "python3.9",
        "python3.10",
        "python3.11",
        "python3.12",
        "python3.13",
    ],
)
def test_python_compatibility(interp, tmpdir):
    if not which(interp):
        skip("Interpreter {!r} unavailable".format(interp))
    file_loc = tmpdir.join("test_wr.py").strpath
    CliVersion("1.0.1").write(file_loc, "py")
    retval = call([interp, "-W", "all", file_loc], stdout=PIPE, stderr=PIPE)
    assert retval == 0
