from lettuce import step
from lettuce import world


@step(u'I bump its major version')
def bump_major_version(step):
    world.version.bump("major")


@step(u'I bump its minor version')
def bump_minor_version(step):
    world.version.bump("minor")


@step(u'I bump its micro version')
def bump_micro_version(step):
    world.version.bump("micro")


@step(u'I bump its patch version')
def bump_patch_version(step):
    world.version.bump("patch")
