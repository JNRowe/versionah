import datetime
import os
import subprocess

from nose.tools import assert_equal

from lettuce import world

import versionah

from util import step


@step(u'I have the version (%(VERSION)s)$')
def have_the_version(step, version):
    world.version = versionah.Version(version)


@step(u'I see the version (%(VERSION)s)$')
def see_the_version(step, expected):
    assert_equal(world.version.as_dotted(), expected)


@step(u'I see the string (.*)$')
def see_the_string(step, expected):
    assert_equal(world.string, expected)


@step(u'I have the file (.*)$')
def have_the_file(step, name):
    world.name = name


@step(u'I read its content$')
def read_content(step):
    world.version = versionah.Version.read("tests/data/%s" % world.name)


@step(u'I write its value to (.*)$')
def write_value_to_file(step, name):
    world.version.write("tests/data/%s" % name, "text")
    world.version = None
    step.given('I have the file %s' % name)
    step.given("I read its content")
    os.unlink("tests/data/%s" % name)


@step(u'I have the package (%(PACKAGE)s) version (%(VERSION)s)$')
def have_named_version(step, name, version):
    world.version = versionah.Version(version, name)


@step(u'I receive (.*)$')
def receive_exception(step, expected):
    assert_equal(unicode(world.exception.__class__.__name__), expected)
