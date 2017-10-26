#
"""cmdline - Command line functionality for versionah"""
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

from . import _version

import datetime
import errno
import os
import re
import sys

from functools import wraps

import jinja2
import click

from .i18n import _
from .models import (MONTHS, VALID_DATE, VALID_PACKAGE, VALID_VERSION,
                     VERSION_COMPS, split_version)
from .models import Version
from .utils import (FILTERS, fail, success)
from .vcs import SUPPORTED_VCS


class ReMatchParamType(click.ParamType):

    """Regular expression based parameter matcher"""

    def __init__(self):
        super(ReMatchParamType, self).__init__()
        # Set name to "<value>ParamType"
        self.name = self.__class__.__qualname__[:-9].lower()

    def convert(self, value, param, ctx):
        """Check given name is valid.

        Args:
            value (str): Value given to flag
            param (click.Argument): Parameter being processed
            ctx (click.Context): Current command context
        Returns:
            str: Valid value
        """
        if not self.matcher:
            raise NotImplementedError('No matcher provided')
        if not re.fullmatch(self.matcher, value):
            self.fail(repr(value))
        return value


class NameParamType(ReMatchParamType):

    """Name parameter handler."""

    matcher = VALID_PACKAGE


class VersionParamType(ReMatchParamType):

    """Version parameter handler."""

    matcher = VALID_VERSION


class CliVersion(Version):

    """Specialisation of models.Version for command line usage."""

    if sys.platform == 'darwin':
        fallback_dir = os.path.expanduser('~/Library/Application Support')
    else:
        fallback_dir = os.path.join(os.environ.get('HOME', '/'), '.local')

    user_dir = os.environ.get('XDG_DATA_HOME', fallback_dir)
    system_dirs = os.environ.get('XDG_DATA_DIRS',
                                 '/usr/local/share/:/usr/share/').split(':')
    mk_data_dir = lambda s: os.path.join(s, 'versionah', 'templates')
    pkg_data_dirs = [mk_data_dir(user_dir), ]
    for directory in system_dirs:
        pkg_data_dirs.append(mk_data_dir(directory))

    env = jinja2.Environment(
        autoescape=jinja2.select_autoescape(['html', 'xml']),
        loader=jinja2.ChoiceLoader([jinja2.FileSystemLoader(s)
                                    for s in pkg_data_dirs])
    )
    env.loader.loaders.append(jinja2.PackageLoader('versionah', 'templates'))
    env.filters.update(FILTERS)
    filetypes = [s.split('.')[0] for s in env.list_templates()]

    @staticmethod
    def display_types():
        """Supported representation types.

        Returns:
            list of str: Method names for representation types
        """
        return [s[3:] for s in dir(CliVersion) if s.startswith('as_')]

    def display(self, display_format):
        """Display a version string.

        Args:
            display_format (str): Format to display version string in
        Returns:
            str: Formatted version string
        """
        return getattr(self, 'as_{}'.format(display_format))()

    @staticmethod
    def read(filename):
        """Read a version file.

        Args:
            filename (str): Version file to read
        Returns:
            CliVersion: New `CliVersion` object representing file
        Raises:
            OSError: When ``filename`` doesn't exist
            ValueError: Unparsable version data
        """
        with open(filename) as f:
            data = f.read().strip()
        match = re.search(r'This is ({}),? [vV]ersion ({}) \(({})\)'.format(
                            VALID_PACKAGE,
                            VALID_VERSION,
                            VALID_DATE
                          ),
                          data)
        if not match:
            raise ValueError(
                'No valid version identifier in {!r}'.format(filename))
        name, version_str, date_str = match.groups()
        components = split_version(version_str)
        try:
            parsed = datetime.datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError:
            parsed = datetime.datetime.strptime(date_str, '%d-%b-%Y')
        return CliVersion(components, name, parsed.date())

    def write(self, filename, file_type, *, shtool=False):
        """Write a version file.

        Args:
            filename (str): Version file to write
            file_type (str): File type to write
            shtool (bool): Write shtool_ compatible files

        .. _shtool: http://www.gnu.org/software/shtool/shtool.html
        """
        data = vars(self)
        data.update({
            'now': datetime.datetime.now(),
            'utcnow': datetime.datetime.utcnow(),
            'filename': filename,
            'dateobj': self.date,
            'resolution': self._resolution,
        })
        if shtool:
            # %d-%b-%Y, if %b wasn't locale dependent
            shtool_date = '-'.join(self.date.day, MONTHS[self.date.month - 1],
                                   self.date.year)
            data['magic'] = 'This is {}, Version {} ({})'.format(
                self.name,
                self.as_dotted(),
                shtool_date
            )
        else:
            data['magic'] = 'This is {} version {} ({})'.format(
                self.name,
                self.as_dotted(),
                self.as_date()
            )

        data.update(dict(zip(VERSION_COMPS, self.components)))
        data.update({k: getattr(self, 'as_{}'.format(k))()
                     for k in self.display_types()})

        template = self.env.get_template('{}.jinja'.format(file_type))
        with open(filename, 'w') as f:
            f.write(template.render(data))


def guess_type(filename):
    """Guess output type from filename.

    Args:
        filename (str): File to operate on
    """
    suffix = os.path.splitext(filename)[1][1:]
    if suffix in CliVersion.filetypes:
        file_type = suffix
    else:
        file_type = 'text'

    return file_type


def guess_vcs():
    """Guess VCS type from directory.

    Returns:
        vcs.VCS: Valid VCS type for current directory
    """
    repo = None
    for vcs_type in SUPPORTED_VCS.values():
        try:
            vcs_type.validate()
        except IOError as e:
            if e.errno == 1:
                raise click.UsageError(e.args[1])
        else:
            repo = vcs_type
    if not repo:
        raise click.BadParameter('No supported VCS in this directory')
    return repo


def vcs_wrap(f):
    """Decorator to commit changes to version control

    Note:
        This is about reduction of duplication, not prettiness.

    Args:
        f (func): Function to wrap
    """
    @wraps(f)
    def wrapper(*args, **kwargs):
        if kwargs['vcs']:
            repo = guess_vcs()
        version = f(*args, **kwargs)
        if kwargs['vcs']:
            repo.add(kwargs['filename'])
            repo.commit(kwargs['filename'],
                        message='{} released'.format(version))
            repo.tag('v{}'.format(version.as_dotted()),
                     '{} released'.format(version))
    return wrapper


@click.group(help=_('A tool to manage project version files.'),
             epilog=_('Please report bugs to '
                      'https://github.com/JNRowe/versionah/issues'))
@click.version_option(_version.dotted)
def cli():
    """Main command entry point."""
    pass


@cli.command(help=_('Bump version in given file.'))
@click.option('-d', '--display', 'display_format', default='dotted',
              type=click.Choice(CliVersion.display_types()),
              help=_('Display format for output.'))
@click.option('-t', '--type', 'file_type', multiple=True,
              type=click.Choice(CliVersion.filetypes),
              help=_('Define the file type used for version file.'))
@click.option('--shtool/--no-shtool',
              help=_('Write shtool compatible output.'))
@click.option('--vcs/--no-vcs',
              help=_('Commit version and create tag.'))
@click.argument('filename', type=click.Path(exists=True, dir_okay=False,
                writable=True, resolve_path=True), nargs=-1, required=True)
@click.argument('bump',
                type=click.Choice(['major', 'minor', 'micro', 'patch']))
@vcs_wrap
def bump(display_format, file_type, shtool, vcs, filename, bump):
    """Bump version in existing file.

    Args:
        display_format (str): Format to display output in
        filename (tuple of str): File to operate on
        file_type (tuple of str): File type to produce
        shtool (bool): Write shtool_ compatible files
        vcs (bool): Tag release in version control
        bump (str): Component to bump

    .. _shtool: http://www.gnu.org/software/shtool/shtool.html
    """
    if file_type and len(file_type) != len(filename):
        raise click.BadParameter('Number of --type options and filename args '
                                 'must match!')
    multi = len(filename) != 1
    for ftype, fname in zip(file_type + (None, ) * len(filename), filename):
        if not ftype:
            ftype = guess_type(fname)

        version = CliVersion.read(fname)

        if not bump:
            bump = VERSION_COMPS[len(version.components) - 1]

        version.bump(bump)
        version.write(fname, ftype, shtool)

        if multi:
            click.echo('{}: '.format(fname), nl=False)
        success(version.display(display_format))
    return version


@cli.command(name='set', help=_('Set version in given file.'))
@click.option('-d', '--display', 'display_format', default='dotted',
              type=click.Choice(CliVersion.display_types()),
              help=_('Display format for output.'))
@click.option('-t', '--type', 'file_type', multiple=True,
              type=click.Choice(CliVersion.filetypes),
              help=_('Define the file type used for version file.'))
@click.option('--shtool/--no-shtool',
              help=_('Write shtool compatible output.'))
@click.option('--vcs/--no-vcs',
              help=_('Commit version and create tag.'))
@click.option('-n', '--name', default=os.path.basename(os.getenv('PWD')),
              type=NameParamType(),
              help=_('Package name for version(default from $PWD).'))
@click.argument('filename', type=click.Path(dir_okay=False, writable=True,
                resolve_path=True), nargs=-1, required=True)
@click.argument('version_str', type=VersionParamType())
def set_version(display_format, file_type, shtool, vcs, name, filename,
                version_str):
    """Set version in new or existing file.

    Args:
        display_format (str): Format to display output in
        filename (tuple of str): File to operate on
        file_type (tuple of str): File type to produce
        shtool (bool): Write shtool_ compatible files
        name (str): Project name used in output
        vcs (bool): Tag release in version control
        version_str (str): Initial version string

    .. _shtool: http://www.gnu.org/software/shtool/shtool.html
    """
    if file_type and len(file_type) != len(filename):
        raise click.BadParameter('Number of --type options and filename args '
                                 'must match!')
    multi = len(filename) != 1
    for ftype, fname in zip(file_type + (None, ) * len(filename), filename):
        if not ftype:
            ftype = guess_type(fname)

        try:
            version = CliVersion.read(fname)
        except IOError:
            version = CliVersion()
        except ValueError as error:
            fail(error.args[0])
            return errno.EIO

        if name:
            version.name = name

        version.set(version_str)
        version.write(fname, ftype, shtool)

        if multi:
            click.echo('{}: '.format(fname), nl=False)
        success(version.display(display_format))
    return version


@cli.command(help=_('Display version in given file.'))
@click.option('-d', '--display', 'display_format', default='dotted',
              type=click.Choice(CliVersion.display_types()),
              help=_('Display format for output.'))
@click.argument('filename', type=click.Path(exists=True, dir_okay=False,
                resolve_path=True), nargs=-1, required=True)
def display(display_format, filename):
    """Display version in existing file.

    Args:
        display_format (str): Format to display output in
        filename (tuple of str): File to operate on
    """
    multi = len(filename) != 1
    for fname in filename:
        try:
            version = CliVersion.read(fname)
        except ValueError as error:
            fail(error.args[0])
            return errno.EIO

        if multi:
            click.echo('{}: '.format(fname), nl=False)
        success(version.display(display_format))
