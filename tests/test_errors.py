from expecter import expect
from mock import (Mock, patch)
from nose2.tools import params

from versionah import (Version, process_command_line)

from tests.utils import raises_OSError

expect.raises_OSError = staticmethod(raises_OSError)


PATCHES = []


def exit_wrapper(status, message):
    """Stub for OptionParser.exit() calls"""
    raise OSError(status, message.strip())


def setUpModule():
    PATCHES.extend([
        patch('versionah.argparse.ArgumentParser.exit',
              new=Mock(side_effect=exit_wrapper)),
        patch('versionah.argparse.ArgumentParser.print_usage'),
    ])
    for p in PATCHES:
        p.start()


def tearDownModule():
    for patch in PATCHES:
        patch.stop()


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
                       "Invalid component values in %r" % components):
        Version(components)


def test_version___eq___unknown_type():
    # Differs between Python 2 and 3
    true_repr = repr(type(True))
    with expect.raises(NotImplementedError,
                       "Unable to compare Version and %s" % true_repr):
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
    with expect.raises_OSError(2, "Invalid string for --name: '__'"):
        process_command_line(['--name=__', 'test'])


def test_process_command_line_invalid_package_version():
    with expect.raises_OSError(2, "Invalid string for --set: '__'"):
        process_command_line(['--set=__', 'test'])


def test_process_command_line_no_file():
    with expect.raises_OSError(2, 'too few arguments'):
        process_command_line([])


def test_process_command_line_multiple_file():
    with expect.raises_OSError(2, 'unrecognized arguments: test2'):
        process_command_line(['test1', 'test2'])
