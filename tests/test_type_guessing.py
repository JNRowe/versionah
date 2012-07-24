from expecter import expect
from nose2.tools import params

from versionah import process_command_line


@params(
    ('test.py', 'py'),
    ('test.rb', 'rb'),
    ('test', 'text'),
)
def test_guess_type_from_name(name, expected):
    args = process_command_line([name, ])
    expect(args.file_type) == expected


@params(
    ('test.py', 'py', 'py'),
    ('test.rb', 'text', 'text'),
    ('test', 'c', 'c'),
)
def test_guess_type_override(name, ftype, expected):
    args = process_command_line(['--type', ftype, name, ])
    expect(args.file_type) == expected
