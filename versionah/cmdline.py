#
"""cmdline - Command line functionality for versionah."""
# Copyright © 2014-2017  James Rowe <jnrowe@gmail.com>
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

import datetime
import errno
import os
import re

import click
import jinja2

from jnrbase import i18n
from jnrbase.colourise import pfail, psuccess
from jnrbase.iso_8601 import parse_datetime
from jnrbase.template import FILTERS
from jnrbase.xdg_basedir import get_data_dirs, user_data

from . import _version
from .models import (MONTHS, VALID_DATE, VALID_PACKAGE, VALID_VERSION,
                     VERSION_COMPS, Version, split_version)


_, N_ = i18n.setup(_version)


class ReMatchParamType(click.ParamType):

    """Regular expression based parameter matcher."""

    def __init__(self):
        """Initialise a new `ReMatchParamType` object."""
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
        if not getattr(self, 'matcher', None):
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

    mk_data_dir = lambda s: os.path.join(s, 'templates')  # NOQA: E731
    pkg_data_dirs = [mk_data_dir(s) for s in get_data_dirs('versionah')]
    pkg_data_dirs.insert(0, mk_data_dir(user_data('versionah')))

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
            list[str]: Method names for representation types
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
            parsed = parse_datetime(date_str)
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
            shtool_date = '{:02d}-{}-{}'.format(
                self.date.day, MONTHS[self.date.month - 1],
                self.date.year
            )
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

        data.update({k: v for k, v in zip(VERSION_COMPS, self.components)})
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


@click.group(help=_('A tool to manage project version files.'),
             epilog=_('Please report bugs at '
                      'https://github.com/JNRowe/versionah/issues'),
             context_settings={'help_option_names': ['-h', '--help']})
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
@click.argument('filename',
                type=click.Path(exists=True, dir_okay=False, writable=True),
                nargs=-1, required=True)
@click.argument('bump',
                type=click.Choice(['major', 'minor', 'micro', 'patch']))
def bump(display_format, file_type, shtool, filename, bump):
    """Bump version in existing file.

    Args:
        display_format (str): Format to display output in
        filename (tuple[str]): File to operate on
        file_type (tuple[str]): File type to produce
        shtool (bool): Write shtool_ compatible files
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

        version.bump(bump)
        version.write(fname, ftype, shtool=shtool)

        if multi:
            click.echo('{}: '.format(fname), nl=False)
        psuccess(version.display(display_format))


@cli.command(name='set', help=_('Set version in given file.'))
@click.option('-d', '--display', 'display_format', default='dotted',
              type=click.Choice(CliVersion.display_types()),
              help=_('Display format for output.'))
@click.option('-t', '--type', 'file_type', multiple=True,
              type=click.Choice(CliVersion.filetypes),
              help=_('Define the file type used for version file.'))
@click.option('--shtool/--no-shtool',
              help=_('Write shtool compatible output.'))
@click.option('-n', '--name', default=os.path.basename(os.getenv('PWD')),
              type=NameParamType(),
              help=_('Package name for version(default from $PWD).'))
@click.argument('filename', type=click.Path(dir_okay=False, writable=True),
                nargs=-1, required=True)
@click.argument('version_str', type=VersionParamType())
def set_version(display_format, file_type, shtool, name, filename,
                version_str):
    """Set version in file.

    Args:
        display_format (str): Format to display output in
        filename (tuple[str]): File to operate on
        file_type (tuple[str]): File type to produce
        shtool (bool): Write shtool_ compatible files
        name (str): Project name used in output
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

        version = CliVersion(version_str, name)
        version.write(fname, ftype, shtool=shtool)

        if multi:
            click.echo('{}: '.format(fname), nl=False)
        psuccess(version.display(display_format))


@cli.command(help=_('Display version in given file.'))
@click.option('-d', '--display', 'display_format', default='dotted',
              type=click.Choice(CliVersion.display_types()),
              help=_('Display format for output.'))
@click.argument('filename', type=click.Path(exists=True, dir_okay=False),
                nargs=-1, required=True)
def display(display_format, filename):
    """Display version in existing file.

    Args:
        display_format (str): Format to display output in
        filename (tuple[str]): File to operate on
    """
    multi = len(filename) != 1
    for fname in filename:
        version = CliVersion.read(fname)

        if multi:
            click.echo('{}: '.format(fname), nl=False)
        psuccess(version.display(display_format))
