from attest import (Tests, raises)
from mock import patch
from nose.tools import eq_

from versionah import (Version, process_command_line)


def exit_wrapper(status, message):
    """Stub for OptionParser.exit() calls"""
    raise ValueError(status, message.strip())


errors = Tests()


@errors.test
def test_version_init_too_few():
    with raises(ValueError) as error:
        Version([1, ])
    eq_(error.message, 'Invalid number of components in [1]')


@errors.test
def test_version_init_too_many():
    with raises(ValueError) as error:
        Version([1, 2, 3, 4, 5])
    eq_(error.message, 'Invalid number of components in [1, 2, 3, 4, 5]')


@errors.test
def test_version_init_invalid_components_string():
    with raises(ValueError) as error:
        Version([1, 2, 'a'])
    eq_(error.message, "Invalid component values in [1, 2, 'a']")


@errors.test
def test_version_init_invalid_components_negative():
    with raises(ValueError) as error:
        Version([1, 2, -4])
    eq_(error.message, 'Invalid component values in [1, 2, -4]')


@errors.test
def test_version___eq___unknown_type():
    with raises(NotImplementedError) as error:
        Version() == True
    eq_(error.message, "Unable to compare Version and <type 'bool'>")


@errors.test
def test_version_bump_invalid_type():
    v = Version()
    with raises(ValueError) as error:
        v.bump('patch')
    eq_(error.message, "Invalid bump_type 'patch' for version (0, 1, 0)")


@errors.test
def test_version_bump_invalid_type_name():
    v = Version()
    with raises(ValueError) as error:
        v.bump('pico')
    eq_(error.message, "Unknown bump_type 'pico'")


@errors.test
def test_version_read_no_identifier():
    with raises(ValueError) as error:
        Version.read('setup.py')
    eq_(error.message, "No valid version identifier in 'setup.py'")


@errors.test
@patch('versionah.optparse.OptionParser.exit')
def test_process_command_line_invalid_package_name(exit_):
    exit_.side_effect = exit_wrapper
    with raises(ValueError) as error:
        process_command_line(['--name=__', 'test'])
    eq_(error.args, (2, "attest:: error: Invalid package name string '__'"))


@errors.test
@patch('versionah.optparse.OptionParser.exit')
def test_process_command_line_invalid_package_version(exit_):
    exit_.side_effect = exit_wrapper
    with raises(ValueError) as error:
        process_command_line(['--set=__', 'test'])
    eq_(error.args, (2, "attest:: error: Invalid version string for set '__'"))


@errors.test
@patch('versionah.optparse.OptionParser.exit')
def test_process_command_line_no_file(exit_):
    exit_.side_effect = exit_wrapper
    with raises(ValueError) as error:
        process_command_line([])
    eq_(error.args, (2, 'attest:: error: One version file must be specified'))


@errors.test
@patch('versionah.optparse.OptionParser.exit')
def test_process_command_line_multiple_file(exit_):
    exit_.side_effect = exit_wrapper
    with raises(ValueError) as error:
        process_command_line(['test1', 'test2'])
    eq_(error.args,
        (2, 'attest:: error: Only one version file must be specified'))
