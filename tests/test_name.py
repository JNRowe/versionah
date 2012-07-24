from expecter import expect
from nose2.tools import params

from versionah import Version


@params(
    ('cat', '0.1.0', 'cat v0.1.0'),
    ('dog', '1.0.0', 'dog v1.0.0'),
    ('fish', '2.1.3', 'fish v2.1.3'),
)
def test_name_versions(name, v, expected):
    v1 = Version(v, name=name)
    expect(str(v1)) == expected


@params(
    ('cat-meow', '0.1.0', 'cat-meow v0.1.0'),
    ('dog-bark', '1.0.0', 'dog-bark v1.0.0'),
    ('fish-bubble', '2.1.3', 'fish-bubble v2.1.3'),
)
def test_name_version_with_dashes_and_underscores(name, v, expected):
    v1 = Version(v, name=name)
    expect(str(v1)) == expected


@params(
    ('cat-2', '0.1.0', 'cat-2 v0.1.0'),
    ('dog1', '1.0.0', 'dog1 v1.0.0'),
)
def test_name_version_with_numeric_suffixes(name, v, expected):
    v1 = Version(v, name=name)
    expect(str(v1)) == expected
