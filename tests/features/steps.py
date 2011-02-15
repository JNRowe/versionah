import os

from lettuce import (step, world)

from versionah import Version


@step(u'I have the version (\d+\.\d+\.\d+)')
def have_the_version(step, version):
    world.version = Version(*map(int, version.split(".")))

@step(u'I bump its major version')
def bump_major_version(step):
    world.version.bump("major")

@step(u'I bump its minor version')
def bump_minor_version(step):
    world.version.bump("minor")

@step(u'I bump its micro version')
def bump_micro_version(step):
    world.version.bump("micro")

@step(u'I see the version (\d+\.\d+\.\d+)')
def see_the_version(step, expected):
    assert world.version.as_triple() == expected, "Got %r" % world.version

@step(u'I display its triple representation')
def display_triple_representation(step):
    world.string = world.version.as_triple()

@step(u'I display its hex representation')
def display_hex_representation(step):
    world.string = world.version.as_hex()

@step(u'I display its libtool representation')
def display_libtool_representation(step):
    world.string = world.version.as_libtool()

@step(u'I see the string (.*)')
def see_the_string(step, expected):
    assert world.string == expected, "Got %r" % world.string

@step(u'I have the file (.*)')
def have_the_file(step, name):
    world.name = name

@step(u'I read its content')
def read_content(step):
    world.version = Version.read("tests/data/%s" % world.name)

@step(u'I write its value to (.*)')
def when_i_write_its_value_to_file(step, name):
    world.version.write("tests/data/%s" % name, "text")
    world.version = None
    step.given('I have the file %s' % name)
    step.given("I read its content")
    os.unlink("tests/data/%s" % name)
