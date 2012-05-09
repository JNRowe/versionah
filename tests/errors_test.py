from sys import version_info

from mock import patch
from nose.tools import (assert_raises, eq_)

from versionah import (Version, process_command_line)


def exit_wrapper(status, message):
    """Stub for OptionParser.exit() calls"""
    raise ValueError(status, message.strip())


def test_version_init_too_few():
    with assert_raises(ValueError) as error:
        Version([1, ])
    eq_(error.exception.message, 'Invalid number of components in [1]')


def test_version_init_too_many():
    with assert_raises(ValueError) as error:
        Version([1, 2, 3, 4, 5])
    eq_(error.exception.message,
        'Invalid number of components in [1, 2, 3, 4, 5]')


def test_version_init_invalid_components_string():
    with assert_raises(ValueError) as error:
        Version([1, 2, 'a'])
    eq_(error.exception.message, "Invalid component values in [1, 2, 'a']")


def test_version_init_invalid_components_negative():
    with assert_raises(ValueError) as error:
        Version([1, 2, -4])
    eq_(error.exception.message, 'Invalid component values in [1, 2, -4]')


def test_version___eq___unknown_type():
    with assert_raises(NotImplementedError) as error:
        Version() == True
    if version_info[0] == 3:
        eq_(error.exception.args[0],
            "Unable to compare Version and <class 'bool'>")
    else:
        eq_(error.exception.args[0],
            "Unable to compare Version and <type 'bool'>")


def test_version_bump_invalid_type():
    v = Version()
    with assert_raises(ValueError) as error:
        v.bump('patch')
    eq_(error.exception.message,
        "Invalid bump_type 'patch' for version (0, 1, 0)")


def test_version_bump_invalid_type_name():
    v = Version()
    with assert_raises(ValueError) as error:
        v.bump('pico')
    eq_(error.exception.message, "Unknown bump_type 'pico'")


def test_version_read_no_identifier():
    with assert_raises(ValueError) as error:
        Version.read('setup.py')
    eq_(error.exception.message, "No valid version identifier in 'setup.py'")


@patch('versionah.optparse.OptionParser.exit')
def test_process_command_line_invalid_package_name(exit_):
    exit_.side_effect = exit_wrapper
    with assert_raises(ValueError) as error:
        process_command_line(['--name=__', 'test'])
    eq_(error.exception.args,
        (2, "nosetests: error: Invalid package name string '__'"))


@patch('versionah.optparse.OptionParser.exit')
def test_process_command_line_invalid_package_version(exit_):
    exit_.side_effect = exit_wrapper
    with assert_raises(ValueError) as error:
        process_command_line(['--set=__', 'test'])
    eq_(error.exception.args,
        (2, "nosetests: error: Invalid version string for set '__'"))


@patch('versionah.optparse.OptionParser.exit')
def test_process_command_line_no_file(exit_):
    exit_.side_effect = exit_wrapper
    with assert_raises(ValueError) as error:
        process_command_line([])
    eq_(error.exception.args,
        (2, 'nosetests: error: One version file must be specified'))


@patch('versionah.optparse.OptionParser.exit')
def test_process_command_line_multiple_file(exit_):
    exit_.side_effect = exit_wrapper
    with assert_raises(ValueError) as error:
        process_command_line(['test1', 'test2'])
    eq_(error.exception.args,
        (2, 'nosetests: error: Only one version file must be specified'))
