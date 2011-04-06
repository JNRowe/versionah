from lettuce import step
from lettuce import world

from nose.tools import assert_equal

import versionah


@step(u'I pass it to (.*)')
def pass_to_function(step, function):
    world.result = getattr(versionah, function)([world.name, ])


@step(u'I pass (.*) argument ([^ ]+) to (.*)')
def pass_args_to_function(step, arg, value, function):
    world.result = getattr(versionah, function)(["--%s" % arg, value,
                                                 world.name])


@step(u'I see the file type (.*)')
def see_file_type(step, file_type):
    assert_equal(world.result[0].file_type, file_type)
