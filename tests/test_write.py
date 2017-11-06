#
"""test_write - Writing tests"""
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

from versionah.cmdline import CliVersion


@mark.requires_write
@mark.parametrize('v, file', [
    ('0.1.0', 'test_wr_a'),
    ('1.0.0', 'test_wr_b'),
    ('2.1.3', 'test_wr_c'),
])
def test_write_version_file(v, file, tmpdir):
    file_loc = tmpdir.join(file).strpath
    CliVersion(v).write(file_loc, 'text')
    read = CliVersion.read(file_loc)
    assert read.as_dotted() == v
