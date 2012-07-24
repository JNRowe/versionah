from expecter import expect
from nose2.tools import params

from versionah import Version


@params(
    '1',
    '1.2.3.4.5',
    '1.2.-1.0',
)
def test_version_validation(v):
    with expect.raises(ValueError, 'Invalid version string %r' % v):
        Version(v)
