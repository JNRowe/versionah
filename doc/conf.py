#
"""conf - Sphinx configuration information."""
# Copyright © 2011-2017  James Rowe <jnrowe@gmail.com>
#
# This file is part of versionah.
#
# versionah is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# versionah is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# versionah.  If not, see <http://www.gnu.org/licenses/>.

import os
import sys

from contextlib import suppress
from subprocess import PIPE, CalledProcessError, run

root_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, root_dir)

import versionah  # NOQA: E402

on_rtd = os.getenv('READTHEDOCS')
if not on_rtd:
    import sphinx_rtd_theme

# General configuration {{{
extensions = \
    ['sphinx.ext.{}'.format(ext)
     for ext in ['autodoc', 'coverage', 'doctest', 'extlinks', 'intersphinx',
                 'napoleon', 'todo', 'viewcode']] \
    + ['sphinxcontrib.{}'.format(ext) for ext in ['blockdiag', ]] \
    + []

if not on_rtd:
    # Only activate spelling if it is installed.  It is not required in the
    # general case and we don’t have the granularity to describe this in a
    # clean way
    try:
        from sphinxcontrib import spelling  # NOQA: F401
    except ImportError:
        pass
    else:
        extensions.append('sphinxcontrib.spelling')

master_doc = 'index'

rst_epilog = """
.. |PyPI| replace:: :abbr:`PyPI (Python Package Index)`
.. |progref| replace:: :program:`versionah`
"""

default_role = 'any'

needs_sphinx = '1.6'

nitpicky = True
# }}}

# Project information {{{
project = 'versionah'
copyright = '2014-2017  James Rowe'

version = '{major}.{minor}'.format_map(versionah._version.dict)
release = versionah._version.dotted

modindex_common_prefix = ['versionah.', ]

trim_footnote_reference_space = True
# }}}

# Options for HTML output {{{
# readthedocs.org handles this setup for their builds, but it is nice to see
# approximately correct builds on the local system too
if not on_rtd:
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path(), ]

with suppress(CalledProcessError):
    proc = run(['git', 'log', "--pretty=format:'%ad [%h]'", '--date=short',
                '-n1'],
               stdout=PIPE)
    html_last_updated_fmt = proc.stdout.decode()

man_pages = [
    ('versionah.1', 'versionah', 'versionah Documentation', ['James Rowe'], 1)
]

html_copy_source = False

html_experimental_html5_writer = True
# }}}

# autodoc extension settings {{{
autoclass_content = 'both'
autodoc_default_flags = ['members', ]
# }}}

# coverage extension settings {{{
coverage_write_headline = False
# }}}

# extlinks extension settings {{{
github_base = 'https://github.com/JNRowe/{}/'.format(project)
extlinks = {
    'issue': ('{}issues/%s'.format(github_base), 'issue #'),
    'pr': ('{}pull/%s'.format(github_base), 'pull request #'),
    'pypi': ('https://pypi.python.org/pypi/%s', ''),
}
# }}}

# intersphinx extension settings {{{
intersphinx_mapping = {
    k: (v, os.getenv('SPHINX_{}_OBJECTS'.format(k.upper())))
    for k, v in {
        'click': 'http://click.pocoo.org/6/',
        'jinja2': 'http://jinja.pocoo.org/docs/',
        'jnrbase': 'http://jnrbase.readthedocs.io/en/latest/',
        'python': 'http://docs.python.org/3/',
    }.items()
}
# }}}

# napoleon extension settings {{{
napoleon_numpy_docstring = False
# }}}

# spelling extension settings {{{
spelling_lang = 'en_GB'
spelling_word_list_filename = 'wordlist.txt'
# }}}

# todo extension settings {{{
todo_include_todos = True
# }}}
