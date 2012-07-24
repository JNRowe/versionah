from expecter import expect
from nose2.tools import params

from versionah import Version


@params(
    ('0.1.0', '1.0.0'),
    ('1.0.0', '2.0.0'),
    ('2.1.3', '3.0.0'),
)
def test_major_bumps(v1, v2):
    start = Version(v1)
    start.bump_major()
    expect(start) == Version(v2)


@params(
    ('0.1.0', '0.2.0'),
    ('1.0.0', '1.1.0'),
    ('2.1.3', '2.2.0'),
)
def test_minor_bumps(v1, v2):
    start = Version(v1)
    start.bump_minor()
    expect(start) == Version(v2)


@params(
    ('0.1.0', '0.1.1'),
    ('1.0.0', '1.0.1'),
    ('2.1.3', '2.1.4'),
)
def test_micro_bumps(v1, v2):
    start = Version(v1)
    start.bump_micro()
    expect(start) == Version(v2)
