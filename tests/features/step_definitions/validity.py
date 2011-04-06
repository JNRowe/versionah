from lettuce import step
from lettuce import world

import versionah


@step(u'I have the invalid version (.*)')
def have_invalid_version(step, string):
    try:
        world.version = versionah.Version(string)
    except Exception as e:
        world.exception = e
