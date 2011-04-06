import datetime

from lettuce import step
from lettuce import world

from nose.tools import assert_equal


@step(u"I find today's date")
def find_todays_date(step):
    assert_equal(world.version.date, datetime.date.today())
