from datetime import date
from os import unlink

from expecter import expect
from nose2.tools import params

from versionah import Version

from tests.utils import write_tag


@params(
    ('0.1.0', 'test_wr_a'),
    ('1.0.0', 'test_wr_b'),
    ('2.1.3', 'test_wr_c'),
)
@write_tag
def test_date_metadata(v, file):
    Version(v).write('tests/data/%s' % file, 'text')
    read = Version.read('tests/data/%s' % file)
    expect(read.as_date()) == date.today().isoformat()
    # Don't wrap in try/finally, so we can inspect if we get failures
    unlink('tests/data/%s' % file)
