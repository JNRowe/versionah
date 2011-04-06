import os
import subprocess

from lettuce import step
from lettuce import world

from nose.tools import assert_equal

import versionah


@step(u'I process (.*) with (.*)')
def process_with_linter(step, name, linter):
    file_type = versionah.process_command_line([name, ])[0].file_type
    world.version.write("tests/data/%s" % name, file_type)
    world.retval = subprocess.call(
        linter.split() + ["tests/data/%s" % name, ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    os.unlink("tests/data/%s" % name)


@step(u'linter returns 0')
def checker_returns_zero(step):
    assert_equal(world.retval, 0)
