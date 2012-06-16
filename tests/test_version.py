from expecter import expect
from versionah import Version


def test_version_set_str():
    v = Version()
    v.set('0.3.0')
    expect(v.components) == (0, 3, 0)


def test_version_set_list():
    v = Version()
    v.set([0, 3, 0])
    expect(v.components) == (0, 3, 0)


def test_version_bump_major():
    v = Version()
    v.bump_major()
    expect(v.components) == (1, 0, 0)


def test_version_bump_minor():
    v = Version()
    v.bump_minor()
    expect(v.components) == (0, 2, 0)


def test_version_bump_micro():
    v = Version()
    v.bump_micro()
    expect(v.components) == (0, 1, 1)


def test_version_bump_patch():
    v = Version((0, 1, 0, 0))
    v.bump_patch()
    expect(v.components) == (0, 1, 0, 1)


def test_version_display():
    v = Version()
    expect(v.display('web')) == 'unknown/0.1.0'
