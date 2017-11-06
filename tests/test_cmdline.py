#
"""test_cli - CLI functionality tests"""
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

from json import load
from shutil import copyfile

from click.testing import CliRunner
from pytest import mark

from versionah.cmdline import bump, cli, display, set_version


@mark.parametrize('component, expected', [
    ('major', '1.0.0'),
    ('minor', '0.2.0'),
    ('micro', '0.1.1'),
])
def test_bump(component, expected, tmpdir):
    test_file = tmpdir.join('test.txt').strpath
    copyfile('tests/data/test_a', test_file)
    runner = CliRunner()
    result = runner.invoke(bump, [test_file, component])
    assert result.exit_code == 0
    assert result.output.strip() == expected


def test_bump_with_type(tmpdir):
    test_file = tmpdir.join('test.txt')
    copyfile('tests/data/test_a', test_file.strpath)
    runner = CliRunner()
    result = runner.invoke(bump,
                           ['-t', 'json', test_file.strpath, 'minor'])
    assert result.exit_code == 0
    assert result.output.strip() == '0.2.0'
    assert load(test_file)['dotted'] == '0.2.0'


@mark.parametrize('suffix, expected', [
    ('a', '0.1.0'),
    ('b', '1.0.0'),
    ('c', '2.1.3'),
])
def test_display(suffix, expected):
    runner = CliRunner()
    result = runner.invoke(display,
                           ['tests/data/test_{}'.format(suffix), ])
    assert result.exit_code == 0
    assert result.output.strip() == expected


def test_display_multi_files():
    files = ['tests/data/test_{}'.format(suffix) for suffix in 'abc']
    runner = CliRunner()
    result = runner.invoke(display, files)
    assert result.exit_code == 0
    for suffix, expected in zip('abc', ['0.1.0', '1.0.0', '2.1.3']):
        assert 'test_{}: {}'.format(suffix, expected) in result.output


@mark.parametrize('version', [
    '1.0.0',
    '0.2.0',
    '0.1.1',
])
def test_set(version, tmpdir):
    test_file = tmpdir.join('test.txt').strpath
    runner = CliRunner()
    result = runner.invoke(set_version, [test_file, version])
    assert result.exit_code == 0
    assert result.output.strip() == version


def test_set_invalid_version(tmpdir):
    test_file = tmpdir.join('test.txt').strpath
    runner = CliRunner()
    result = runner.invoke(set_version, [test_file, 'dog', ])
    assert result.exit_code == 2
    assert 'Invalid value for "version_str"' in result.output


def test_set_with_name(tmpdir):
    test_file = tmpdir.join('test.json')
    runner = CliRunner()
    result = runner.invoke(set_version,
                           ['--name', 'unique', test_file.strpath,
                            '0.1.0'])
    assert result.exit_code == 0
    assert result.output.strip() == '0.1.0'
    assert 'This is unique' in load(test_file)['magic']


def test_set_with_type(tmpdir):
    test_file = tmpdir.join('test.txt')
    runner = CliRunner()
    result = runner.invoke(set_version,
                           ['-t', 'json', test_file.strpath, '4.3.2'])
    assert result.exit_code == 0
    assert result.output.strip() == '4.3.2'
    assert load(test_file)['dotted'] == '4.3.2'


@mark.parametrize('command, arg', [
    (bump, 'major'),
    (set_version, '1.2.3'),
])
def test_command_non_matching_files_and_types(command, arg, tmpdir):
    tmpfiles = []
    for c in 'abc':
        tmpfiles.append(tmpdir.join('test{}.txt'.format(c)).strpath)
        copyfile('tests/data/test_a', tmpfiles[-1])
    runner = CliRunner()
    result = runner.invoke(command,
                           ['-t', 'py', ] + tmpfiles + [arg, ])
    assert result.exit_code == 2
    assert '--type options and filename args must match' \
        in result.output


@mark.parametrize('command, arg, expected', [
    (bump, 'major', '1.0.0'),
    (set_version, '1.2.3', '1.2.3'),
])
def test_command_multi_files(command, arg, expected, tmpdir):
    tmpfiles = []
    for c in 'abc':
        tmpfiles.append(tmpdir.join('test{}.txt'.format(c)).strpath)
        copyfile('tests/data/test_a', tmpfiles[-1])
    runner = CliRunner()
    result = runner.invoke(command, tmpfiles + [arg, ])
    assert result.exit_code == 0
    for f in tmpfiles:
        assert '{}: {}'.format(f, expected) in result.output


def test_cli_wrapper():
    runner = CliRunner()
    result = runner.invoke(cli,
                           ['display', 'tests/data/test_c'])
    assert result.exit_code == 0
    assert result.output.strip() == '2.1.3'
