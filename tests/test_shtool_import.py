from expecter import expect
from nose2.tools import params

from versionah import Version

from tests.utils import read_tag


@params(
    ('shtool/test.c', '1.2.3'),
    ('shtool/test.m4', '1.2.3'),
    ('shtool/test.perl', '1.2.3'),
    ('shtool/test.python', '1.2.3'),
    ('shtool/test.txt', '1.2.3'),
)
@read_tag
def test_read_shtool_files(file, expected):
    v = Version.read("tests/data/%s" % file)
    expect(v.as_dotted()) == expected
