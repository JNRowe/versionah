from expecter import expect
from nose2.tools import params

from versionah import Version

from tests.utils import read_tag


@params(
    ('test_a', '0.1.0'),
    ('test_b', '1.0.0'),
    ('test_c', '2.1.3'),
)
@read_tag
def test_read_version_file(file, expected):
    v = Version.read("tests/data/%s" % file)
    expect(v.as_dotted()) == expected
