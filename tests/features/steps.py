import datetime
import os
import subprocess

from nose.tools import assert_equal

from lettuce import (step, world)

import versionah


@step(u'I have the version (%s)' % versionah.VALID_VERSION)
def have_the_version(step, version):
    world.version = versionah.Version(versionah.split_version(version))

@step(u'I bump its major version')
def bump_major_version(step):
    world.version.bump("major")

@step(u'I bump its minor version')
def bump_minor_version(step):
    world.version.bump("minor")

@step(u'I bump its micro version')
def bump_micro_version(step):
    world.version.bump("micro")

@step(u'I see the version (%s)' % versionah.VALID_VERSION)
def see_the_version(step, expected):
    assert_equal(world.version.as_dotted(), expected)

@step(u'I display its dotted representation')
def display_dotted_representation(step):
    world.string = world.version.as_dotted()

@step(u'I display its hex representation')
def display_hex_representation(step):
    world.string = world.version.as_hex()

@step(u'I display its libtool representation')
def display_libtool_representation(step):
    world.string = world.version.as_libtool()

@step(u'I see the string (.*)')
def see_the_string(step, expected):
    assert_equal(world.string, expected)

@step(u'I have the file (.*)')
def have_the_file(step, name):
    world.name = name

@step(u'I read its content')
def read_content(step):
    world.version = versionah.Version.read("tests/data/%s" % world.name)

@step(u'I write its value to (.*)')
def write_value_to_file(step, name):
    world.version.write("tests/data/%s" % name, "text")
    world.version = None
    step.given('I have the file %s' % name)
    step.given("I read its content")
    os.unlink("tests/data/%s" % name)

@step(u'I have the package (%s) version (%s)' % (versionah.VALID_PACKAGE,
                                                 versionah.VALID_VERSION))
def have_named_version(step, name, version):
    world.version = versionah.Version(versionah.split_version(version), name)

@step(u'I display its string representation')
def display_string_representation(step):
    world.string = str(world.version)

@step(u"I find today's date")
def find_todays_date(step):
    assert_equal(world.version.date, datetime.date.today())

@step(u'I bump its patch version')
def bump_patch_version(step):
    world.version.bump("patch")

@step(u'I have the versions (%s) and (%s)' % (versionah.VALID_VERSION,
                                              versionah.VALID_VERSION))
def have_versions(step, version1, version2):
    world.version1 = versionah.Version(versionah.split_version(version1))
    world.version2 = versionah.Version(versionah.split_version(version2))

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

@step(u'I have the invalid version (.*)')
def have_invalid_version(step, string):
    try:
        world.version = versionah.Version(versionah.split_version(string))
    except Exception as e:
        world.exception = e

@step(u'I receive (.*)')
def receive_exception(step, expected):
    assert_equal(unicode(world.exception.__class__.__name__), expected)

@step(u'I pass it to (.*)')
def pass_to_function(step, function):
    world.result = getattr(versionah, function)([world.name, ])

@step(u'I pass (.*) argument ([^ ]+) to (.*)')
def pass_args_to_function(step, arg, value, function):
    world.result = getattr(versionah, function)(["--%s" % arg, value, world.name])

@step(u'I see the file type (.*)')
def see_file_type(step, file_type):
    assert_equal(world.result[0].file_type, file_type)

@step(u'I process (.*) with (.*)')
def process_with_linter(step, name, linter):
    file_type = versionah.process_command_line([name, ])[0].file_type
    world.version.write("tests/data/%s" % name, file_type)
    world.retval = subprocess.call(linter.split() + ["tests/data/%s" %name, ],
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
    os.unlink("tests/data/%s" % name)

@step(u'linter returns 0')
def checker_returns_zero(step):
    assert_equal(world.retval, 0)

@step(u'I have the version (%s) created on (%s)' % (versionah.VALID_VERSION,
                                                    versionah.VALID_DATE))
def have_the_version_with_date(step, version, date):
    y, m, d = map(int, date.split("-"))
    world.version = versionah.Version(versionah.split_version(version),
                                      date=datetime.date(y, m, d))

@step(u'I display its date representation')
def display_date_representation(step):
    world.string = world.version.as_date()

@step(u'I see the date string (.*)')
def see_the_date(step, expected):
    assert_equal(world.string, expected)

@step(u'I have the Version object for (%s) and (?:tuple|string) (%s)'
       % (versionah.VALID_VERSION, versionah.VALID_VERSION))
def have_version_object_and_tuple(step, version1, version2):
    world.version1 = versionah.Version(versionah.split_version(version1))
    world.version2 = versionah.split_version(version2)

@step(u'I have the Version object for (%s) and list (%s)'
       % (versionah.VALID_VERSION, versionah.VALID_VERSION))
def have_version_object_and_list(step, version1, version2):
    world.version1 = versionah.Version(versionah.split_version(version1))
    world.version2 = list(versionah.split_version(version2))

@step(u'I have the Version object for (%s) and RegExp matcher for (%s)'
       % (versionah.VALID_VERSION, versionah.VALID_VERSION))
def have_version_object_and_re_obj(step, version1, version2):
    import re
    world.version1 = versionah.Version(versionah.split_version(version1))
    world.version2 = re.compile(version2)
