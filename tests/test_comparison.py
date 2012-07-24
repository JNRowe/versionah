from expecter import expect
from nose2.tools import params
from versionah import Version


@params(
    ('0.1.0', '0.1.0'),
    ('1.0.0', '1.0.0'),
)
def test_equal_versions(v1, v2):
    expect(Version(v1)) == Version(v2)


@params(
    ('1.0.0', '2.0.0'),
    ('2.1.3', '3.0.0'),
)
def test_unequal_versions(v1, v2):
    expect(Version(v1)) != Version(v2)


@params(
    ('2.1.1', '2.1.4', '2.1.4'),
    ('2.1.3', '3.0.0', '3.0.0'),
    ('3.0.0', '2.9.99.9', '3.0.0'),
)
def test_greatest_version(v1, v2, expected):
    expect(max(Version(v1), Version(v2))) == Version(expected)


@params(
    ('0.1.0', '0.1'),
    ('0.1', '0.1.0'),
    ('0.1.0.0', '0.1.0'),
    ('0.1.0.0', '0.1'),
)
def test_equal_versions_with_uneven_components(v1, v2):
    expect(Version(v1)) == Version(v2)


@params(
    ('0.1', '0.1.0.1'),
    ('0.1.1.1', '0.1.1'),
)
def test_unequal_versions_with_uneven_components(v1, v2):
    expect(Version(v1)) != Version(v2)
