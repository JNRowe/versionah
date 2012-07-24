from expecter import expect
from nose2.tools import params

from versionah import Version


@params(
    ('0.1', '1.0'),
    ('1.0', '2.0'),
    ('2.1', '3.0'),
)
def test_two_component_major_bump(v1, v2):
    start = Version(v1)
    start.bump_major()
    expect(start) == Version(v2)


@params(
    ('0.1', '0.2'),
    ('1.0', '1.1'),
    ('2.1', '2.2'),
)
def test_two_component_minor_bump(v1, v2):
    start = Version(v1)
    start.bump_minor()
    expect(start) == Version(v2)


@params(
    ('0.1.0.0', '1.0.0.0'),
    ('1.0.0.4', '2.0.0.0'),
    ('2.1.3.0', '3.0.0.0'),
)
def test_four_component_major_bump(v1, v2):
    start = Version(v1)
    start.bump_major()
    expect(start) == Version(v2)


@params(
    ('0.1.0.0', '0.2.0.0'),
    ('1.0.0.4', '1.1.0.0'),
    ('2.1.3.0', '2.2.0.0'),
)
def test_four_component_minor_bump(v1, v2):
    start = Version(v1)
    start.bump_minor()
    expect(start) == Version(v2)


@params(
    ('0.1.0.0', '0.1.1.0'),
    ('1.0.0.4', '1.0.1.0'),
    ('2.1.3.0', '2.1.4.0'),
)
def test_four_component_micro_bump(v1, v2):
    start = Version(v1)
    start.bump_micro()
    expect(start) == Version(v2)


@params(
    ('0.1.0.0', '0.1.0.1'),
    ('1.0.0.4', '1.0.0.5'),
    ('2.1.3.0', '2.1.3.1'),
)
def test_four_component_patch_bump(v1, v2):
    start = Version(v1)
    start.bump_patch()
    expect(start) == Version(v2)
