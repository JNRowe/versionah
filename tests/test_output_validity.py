from os import unlink
from subprocess import (call, PIPE)

from expecter import expect
from nose2.tools import params

from versionah import (Version, guess_type)

from tests.utils import (execute_tag, write_tag)


@params(
    ('1.0.1', 'test_wr.c', 'splint'),
    ('1.0.1', 'test_wr.m4', 'm4 -P -E -E'),
    ('1.0.1', 'test_wr.py', 'python -W all'),
    ('1.0.1', 'test_wr.rb', 'ruby -c'),
)
@write_tag
@execute_tag
def test_output_validatity(v, filename, linter):
    file_type = guess_type(filename)
    Version(v).write('tests/data/%s' % file, file_type)
    retval = call(linter.split() + ['tests/data/%s' % file, ],
                  stdout=PIPE, stderr=PIPE)
    expect(retval) == 0
    # Don't wrap in try/finally, so we can inspect if we get failures
    unlink('tests/data/%s' % file)
