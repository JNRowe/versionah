from mock import (Mock, patch)
from nose.tools import (assert_raises, eq_, ok_)

from versionah import (Version, process_command_line)

PATCHES = []


def exit_wrapper(status, message):
    """Stub for OptionParser.exit() calls"""
    raise OSError(status, message.strip())


def setUpModule():
    PATCHES.extend([
        patch('versionah.optparse.OptionParser.exit',
              new=Mock(side_effect=exit_wrapper)),
        patch('versionah.optparse.OptionParser.print_usage'),
    ])
    for p in PATCHES:
        p.start()


def tearDownModule():
    for patch in PATCHES:
        patch.stop()


def test_version_init_too_few():
    with assert_raises(ValueError) as error:
        Version([1, ])
    eq_(error.exception.args[0], 'Invalid number of components in [1]')


def test_version_init_too_many():
    with assert_raises(ValueError) as error:
        Version([1, 2, 3, 4, 5])
    eq_(error.exception.args[0],
        'Invalid number of components in [1, 2, 3, 4, 5]')


def test_version_init_invalid_components_string():
    with assert_raises(ValueError) as error:
        Version([1, 2, 'a'])
    eq_(error.exception.args[0], "Invalid component values in [1, 2, 'a']")


def test_version_init_invalid_components_negative():
    with assert_raises(ValueError) as error:
        Version([1, 2, -4])
    eq_(error.exception.args[0], 'Invalid component values in [1, 2, -4]')


def test_version___eq___unknown_type():
    with assert_raises(NotImplementedError) as error:
        Version() == True
    # Differs between Python 2 and 3
    true_repr = repr(type(True))
    eq_(error.exception.args[0],
        "Unable to compare Version and %s" % true_repr)


def test_version_bump_invalid_type():
    v = Version()
    with assert_raises(ValueError) as error:
        v.bump('patch')
    eq_(error.exception.args[0],
        "Invalid bump_type 'patch' for version (0, 1, 0)")


def test_version_bump_invalid_type_name():
    v = Version()
    with assert_raises(ValueError) as error:
        v.bump('pico')
    eq_(error.exception.args[0], "Unknown bump_type 'pico'")


def test_version_read_no_identifier():
    with assert_raises(ValueError) as error:
        Version.read('setup.py')
    eq_(error.exception.args[0], "No valid version identifier in 'setup.py'")


def test_process_command_line_invalid_package_name():
    with assert_raises(OSError) as error:
        process_command_line(['--name=__', 'test'])
    code, message = error.exception.args
    eq_(code, 2)
    ok_(message.endswith("error: Invalid package name string '__'"))


def test_process_command_line_invalid_package_version():
    with assert_raises(OSError) as error:
        process_command_line(['--set=__', 'test'])
    code, message = error.exception.args
    eq_(code, 2)
    ok_(message.endswith("error: Invalid version string for set '__'"))


def test_process_command_line_no_file():
    with assert_raises(OSError) as error:
        process_command_line([])
    code, message = error.exception.args
    eq_(code, 2)
    ok_(message.endswith('error: One version file must be specified'))


def test_process_command_line_multiple_file():
    with assert_raises(OSError) as error:
        process_command_line(['test1', 'test2'])
    code, message = error.exception.args
    eq_(code, 2)
    ok_(message.endswith('error: Only one version file must be specified'))
