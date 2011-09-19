from attest import Tests
from nose.tools import eq_

from versionah import Version

version = Tests()


@version.test
def version_set_str():
    v = Version()
    v.set('0.3.0')
    eq_(v.components, (0, 3, 0))


@version.test
def version_set_list():
    v = Version()
    v.set([0, 3, 0])
    eq_(v.components, (0, 3, 0))


@version.test
def version_bump_major():
    v = Version()
    v.bump_major()
    eq_(v.components, (1, 0, 0))


@version.test
def version_bump_minor():
    v = Version()
    v.bump_minor()
    eq_(v.components, (0, 2, 0))


@version.test
def version_bump_micro():
    v = Version()
    v.bump_micro()
    eq_(v.components, (0, 1, 1))


@version.test
def version_bump_patch():
    v = Version((0, 1, 0, 0))
    v.bump_patch()
    eq_(v.components, (0, 1, 0, 1))


@version.test
def version_display():
    v = Version()
    eq_(v.display('web'), 'unknown/0.1.0')
