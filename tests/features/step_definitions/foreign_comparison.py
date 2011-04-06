import re

from lettuce import world

import versionah

from util import step


@step(u'I have the Version object for (%(VERSION)s) and (?:tuple|string) ' \
      '(%(VERSION)s)')
def have_version_object_and_tuple(step, version1, version2):
    world.version1 = versionah.Version(version1)
    world.version2 = versionah.split_version(version2)


@step(u'I have the Version object for (%(VERSION)s) and list (%(VERSION)s)')
def have_version_object_and_list(step, version1, version2):
    world.version1 = versionah.Version(version1)
    world.version2 = list(versionah.split_version(version2))


@step(u'I have the Version object for (%(VERSION)s) and RegExp matcher for ' \
      '(%(VERSION)s)')
def have_version_object_and_re_obj(step, version1, version2):
    import re
    world.version1 = versionah.Version(version1)
    world.version2 = re.compile(version2)
