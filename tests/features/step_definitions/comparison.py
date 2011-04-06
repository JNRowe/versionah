from lettuce import world

from nose.tools import assert_equal

import versionah

from util import step


@step(u'I have the versions (%(VERSION)s) and (%(VERSION)s)')
def have_versions(step, version1, version2):
    world.version1 = versionah.Version(version1)
    world.version2 = versionah.Version(version2)


@step(u'I compare them for equality')
def compare_equality(step):
    try:
        world.result = unicode(world.version1 == world.version2)
    except Exception as e:
        world.exception = e


@step(u'I see the comparison (.*)')
def see_comparison_result(step, expected):
    assert_equal(world.result, expected)


@step(u'I search for the greatest')
def find_max(step):
    world.version = max((world.version1, world.version2))
