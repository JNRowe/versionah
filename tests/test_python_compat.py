from os import unlink
from subprocess import (call, PIPE)

from expecter import expect
from nose2.tools import params

from versionah import Version

from tests.utils import (execute_tag, write_tag)


@params(
    'python2.4',
    'python2.5',
    'python2.6',
    'python2.7',
    'python3.1',
    'python3.2',
)
@write_tag
@execute_tag
def test_python_compatibility(interp):
    Version('1.0.1').write('tests/data/test_wr.py', 'py')
    retval = call([interp, '-W', 'all', 'tests/data/test_wr.py'],
                  stdout=PIPE, stderr=PIPE)
    expect(retval) == 0
    # Don't wrap in try/finally, so we can inspect if we get failures
    unlink('tests/data/test_wr.py')
