#
"""vcs - Version interface for versionah"""
# Copyright © 2014-2015  James Rowe <jnrowe@gmail.com>
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

import errno

from contextlib import suppress
from os.path import (isdir, isfile)

from sh import (CommandNotFound, Command)

# This only supports the few version control systems that users I know have
# seen in the field.  Feel free to add more, or consider submitting a pull
# request with a change to using a generic wrapper(if you can find one).


class VCS:
    """Base object for VCS wrappers.

    Warning:
        Instantiation will raise ``OSError`` if the necessary command line tool
        is not available on the system.

    Attributes
        cmd_name: If set this will override the guess-from-class-name method of
            defining the command name for the given VCS.
    """
    def __init__(self):
        cmd_name = getattr(self, 'cmd_name', self.__class__.__name__.lower())
        try:
            self.command = Command(cmd_name)
        except CommandNotFound:
            raise OSError(errno.ENOPROTOOPT, '%s not found' % cmd_name)

    def validate(self, *, allow_modified=False):
        """Ensure cwd is a VCS repository.

        Args:
            allow_modified (bool): Allow operation on dirty trees
        """
        raise NotImplementedError

    def add(self, files):
        """Add files to be committed.

        Args:
            files (list): Files to add
        """
        self.command.add(*files)

    def commit(self, files, message):
        """Commit files to repository.

        Args:
            files (list): Files to add
        """
        raise NotImplementedError

    def tag(self, name, message):
        """Create version tag

        Args:
            name (str): Tag to create
            message (str): Message to associate with tag
        """
        raise NotImplementedError


class Git(VCS):
    def validate(self, *, allow_modified=False):
        if not isdir('.git'):
            raise NotADirectoryError('Current directory is not a git '
                                     'repository')

        if allow_modified:
            return
        for line in self.command.status(porcelain=True).splitlines():
            if not line.startswith('?? '):
                raise IOError(errno.EPERM,
                              'Working tree contains modified files')

    def commit(self, files, message):
        self.command.commit(*files, message=message.encode('utf-8'))

    def tag(self, name, message):
        self.command.tag(name, message=message.encode('utf-8'), sign=True)


class Mercurial(VCS):
    cmd_name = 'hg'

    def validate(self, *, allow_modified=False):
        if not isdir('.hg'):
            raise NotADirectoryError('Current directory is not a mercurial '
                                     'repository')

        if allow_modified:
            return
        for line in self.command.status().splitlines():
            if not line.startswith('? '):
                raise IOError(errno.EPERM,
                              'Working tree contains modified files')

    def commit(self, files, message):
        self.command.commit(*files, message=message.encode('utf-8'))

    def tag(self, name, message):
        self.command.tag(name, message=message.encode('utf-8'))


class Fossil(VCS):
    def validate(self, *, allow_modified=False):
        # This is an ``isfile`` check raising a directory error, but fossil is
        # the odd one out here so we'll paper over that.
        if not isfile('.fslckout'):
            raise NotADirectoryError('Current directory is not a fossil local '
                                     'tree')

        if allow_modified:
            return
        if self.command.changes().splitlines():
            raise IOError(errno.EPERM, 'Working tree contains modified files')

    def commit(self, files, message):
        self.command.commit(*files, message=message.encode('utf-8'))

    def tag(self, name, message):
        self.command.tag(name, 'tip')


#: Version control systems available on this system
SUPPORTED_VCS = {}

for t in VCS.__subclasses__():
    with suppress(OSError):
        SUPPORTED_VCS[getattr(t, 'cmd_name', t.__name__.lower())] = t()
