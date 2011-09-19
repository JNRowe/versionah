from attest import Tests
from nose.tools import (eq_, assert_greater_equal, assert_less,
                        assert_less_equal)

from versionah import Version

cmps = Tests()


@cmps.test
def cmp_version_to_version():
    eq_(Version(), Version())


@cmps.test
def cmp_version_to_tuple():
    eq_(Version(), (0, 1, 0))


@cmps.test
def cmp_version_to_list():
    eq_(Version(), [0, 1, 0])


@cmps.test
def cmp_version_to_str():
    eq_(Version(), '0.1.0')


@cmps.test
def cmp_version_less_than():
    assert_less(Version((0, 1, 0)), Version((0, 2, 0)))


@cmps.test
def cmp_version_less_than_equal():
    assert_less_equal(Version((0, 1, 0)), Version((0, 2, 0)))
    assert_less_equal(Version((0, 2, 0)), Version((0, 2, 0)))


@cmps.test
def cmp_version_greather_than_equal():
    assert_greater_equal(Version((0, 2, 0)), Version((0, 1, 0)))
    assert_greater_equal(Version((0, 2, 0)), Version((0, 2, 0)))
