from expecter import expect

from versionah import Version


def test_cmp_version_to_version():
    expect(Version()) == Version()


def test_cmp_version_to_tuple():
    expect(Version()) == (0, 1, 0)


def test_cmp_version_to_list():
    expect(Version()) == [0, 1, 0]


def test_cmp_version_to_str():
    expect(Version()) == '0.1.0'


def test_cmp_version_less_than():
    expect(Version((0, 1, 0))) < Version((0, 2, 0))


def test_cmp_version_less_than_equal():
    expect(Version((0, 1, 0))) <= Version((0, 2, 0))
    expect(Version((0, 2, 0))) <= Version((0, 2, 0))


def test_cmp_version_greather_than_equal():
    expect(Version((0, 2, 0))) >= Version((0, 1, 0))
    expect(Version((0, 2, 0))) >= Version((0, 2, 0))
