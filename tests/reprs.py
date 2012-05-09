from datetime import date

from attest import Tests
from nose.tools import eq_

from versionah import Version

TODAY = date.today()

reprs = Tests()


@reprs.test
def version_repr():
    eq_(repr(Version()), "Version((0, 1, 0), 'unknown', %r)" % TODAY)


@reprs.test
def version_repr_components():
    eq_(repr(Version([0, 2, 0])), "Version((0, 2, 0), 'unknown', %r)" % TODAY)


@reprs.test
def version_repr_name():
    eq_(repr(Version(name='foo')), "Version((0, 1, 0), 'foo', %r)" % TODAY)


@reprs.test
def version_repr_date():
    eq_(repr(Version(date=date(1970, 1, 1))),
        "Version((0, 1, 0), 'unknown', datetime.date(1970, 1, 1))")