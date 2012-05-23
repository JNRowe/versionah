import sys

if sys.version_info < (2, 7):
    # Horrific import butchering to support 2.7 assert tools in Python 2.6, you
    # can't simply replace the module reference in nose.tools because the PEP-8
    # names are set up at import time
    import unittest2  # NOQA
    sys.modules['unittest'] = sys.modules['unittest2']
    from nose import tools
    reload(tools)
