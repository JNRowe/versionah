from expecter import expect
from nose2.tools import params

from versionah import guess_type


@params(
    ('test.py', 'py'),
    ('test.rb', 'rb'),
    ('test', 'text'),
)
def test_guess_type_from_name(filename, expected):
    expect(guess_type(filename)) == expected
