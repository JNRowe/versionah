from lettuce import (step, world)

from versionah import bump


@step(u'I have the version (\d+\.\d+\.\d+)')
def have_the_version(step, version):
    world.version = version

@step(u'I bump its major version')
def bump_major_version(step):
    world.version = bump(world.version, "major")

@step(u'I bump its minor version')
def bump_minor_version(step):
    world.version = bump(world.version, "minor")

@step(u'I bump its micro version')
def bump_micro_version(step):
    world.version = bump(world.version, "micro")

@step(u'I see the version (\d+\.\d+\.\d+)')
def see_the_version(step, expected):
    assert world.version == expected, "Got %r" % world.version
