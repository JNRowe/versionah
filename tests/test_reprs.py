from datetime import date

from expecter import expect

from versionah import Version


TODAY = date.today()


def test_version_repr():
    expect(repr(Version())) == "Version((0, 1, 0), 'unknown', %r)" % TODAY


def test_version_repr_components():
    expect(repr(Version([0, 2, 0]))) \
        == "Version((0, 2, 0), 'unknown', %r)" % TODAY


def test_version_repr_name():
    expect(repr(Version(name='foo'))) \
        == "Version((0, 1, 0), 'foo', %r)" % TODAY


def test_version_repr_date():
    expect(repr(Version(date=date(1970, 1, 1)))) \
        == "Version((0, 1, 0), 'unknown', datetime.date(1970, 1, 1))"
