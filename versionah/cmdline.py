#
# coding=utf-8
"""cmdline - Command line functionality for versionah"""
# Copyright © 2011-2014  James Rowe <jnrowe@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from . import _version

import datetime
import errno
import os
import re
import sys

import jinja2
import click

from .i18n import _
from .models import (MONTHS, VALID_DATE, VALID_PACKAGE, VALID_VERSION,
                     VERSION_COMPS, split_version)
from .models import Version
from .utils import (FILTERS, fail, success)


class ReMatchParamType(click.ParamType):
    """Regular expression based parameter matcher"""

    def __init__(self):
        super(ReMatchParamType, self).__init__()
        # Set name to "<value>ParamType"
        self.name = self.__class__.__name__[:-9].lower()

    def convert(self, value, param, ctx):
        """Check given name is valid.

        :param str value: Value given to flag
        :param click.Argument param: Parameter being processed
        :param click.Context ctx: Current command context
        :rtype: :obj:`str`
        :return: Valid value
        """
        if not self.matcher:
            raise NotImplementedError('No matcher provided')
        if not re.match('%s$' % self.matcher, value):
            self.fail('%r' % value)
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

    env = jinja2.Environment(loader=jinja2.ChoiceLoader(
        list(jinja2.FileSystemLoader(s) for s in pkg_data_dirs)))
    env.loader.loaders.append(jinja2.PackageLoader('versionah', 'templates'))
    env.filters.update(FILTERS)
    filetypes = [s.split('.')[0] for s in env.list_templates()]

    @staticmethod
    def display_types():
        """Supported representation types.

        :rtype: `list` of `str`
        :return: Method names for representation types
        """
        return [s[3:] for s in dir(CliVersion) if s.startswith('as_')]

    def display(self, display_format):
        """Display a version string.

        :param str display_format: Format to display version string in
        :rtype: `str`
        :return: Formatted version string
        """
        return getattr(self, 'as_%s' % display_format)()

    @staticmethod
    def read(filename):
        """Read a version file.

        :param str filename: Version file to read
        :rtype: `CliVersion`
        :return: New `CliVersion` object representing file
        :raise exceptions.OSError: When ``filename`` doesn't exist
        :raise exceptions.ValueError: Unparsable version data
        """
        with open(filename) as f:
            data = f.read().strip()
        match = re.search(r'This is (%s),? [vV]ersion (%s) \((%s)\)'
                          % (VALID_PACKAGE, VALID_VERSION, VALID_DATE),
                          data)
        if not match:
            raise ValueError('No valid version identifier in %r' % filename)
        name, version_str, date_str = match.groups()
        components = split_version(version_str)
        try:
            parsed = datetime.datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError:
            parsed = datetime.datetime.strptime(date_str, '%d-%b-%Y')
        return CliVersion(components, name, parsed.date())

    def write(self, filename, file_type, shtool=False):
        """Write a version file.

        :param str filename: Version file to write
        :param str file_type: File type to write
        :param bool shtool: Write shtool_ compatible files

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
            shtool_date = "%s-%s-%s" % (self.date.day,
                                        MONTHS[self.date.month - 1],
                                        self.date.year)
            data['magic'] = 'This is %s, Version %s (%s)' % (self.name,
                                                             self.as_dotted(),
                                                             shtool_date)
        else:
            data['magic'] = 'This is %s version %s (%s)' % (self.name,
                                                            self.as_dotted(),
                                                            self.as_date())

        data.update(dict(zip(VERSION_COMPS, self.components)))
        data.update(dict([(k, getattr(self, 'as_%s' % k)())
                          for k in self.display_types()]))

        template = self.env.get_template('%s.jinja' % file_type)
        with open(filename, 'w') as f:
            f.write(template.render(data))


def guess_type(filename):
    """Guess output type from filename.

    :param str filename: File to operate on
    """
    suffix = os.path.splitext(filename)[1][1:]
    if suffix in CliVersion.filetypes:
        file_type = suffix
    else:
        file_type = 'text'

    return file_type


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
@click.argument('filename', type=click.Path(exists=True, dir_okay=False,
                writable=True, resolve_path=True), nargs=-1, required=True)
@click.argument('bump',
                type=click.Choice(['major', 'minor', 'micro', 'patch']))
def bump(display_format, file_type, shtool, filename, bump):
    """Bump version in existing file.

    :param str display_format: Format to display output in
    :type filename: `tuple` of `str`
    :param filename: File to operate on
    :type file_type: `tuple` of `str`
    :param file_type: File type to produce
    :param bool shtool: Write shtool_ compatible files
    :param str bump: Component to bump

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
            click.echo("%s: " % fname, nl=False)
        success(version.display(display_format))


@cli.command(name='set', help=_('Set version in given file.'))
@click.option('-d', '--display', 'display_format', default='dotted',
              type=click.Choice(CliVersion.display_types()),
              help=_('Display format for output.'))
@click.option('-t', '--type', 'file_type', multiple=True,
              type=click.Choice(CliVersion.filetypes),
              help=_('Define the file type used for version file.'))
@click.option('-n', '--name', default=os.path.basename(os.getenv('PWD')),
              type=NameParamType(),
              help=_('Package name for version(default from $PWD).'))
@click.argument('filename', type=click.Path(dir_okay=False, writable=True,
                resolve_path=True), nargs=-1, required=True)
@click.argument('version_str', type=VersionParamType())
def set_version(display_format, file_type, name, filename, version_str):
    """Set version in new or existing file.

    :param str display_format: Format to display output in
    :type filename: `tuple` of `str`
    :param filename: File to operate on
    :type file_type: `tuple` of `str`
    :param file_type: File type to produce
    :param str name: Project name used in output
    :param str version_str: Initial version string
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
        version.write(fname, ftype)

        if multi:
            click.echo("%s: " % fname, nl=False)
        success(version.display(display_format))


@cli.command(help=_('Display version in given file.'))
@click.option('-d', '--display', 'display_format', default='dotted',
              type=click.Choice(CliVersion.display_types()),
              help=_('Display format for output.'))
@click.argument('filename', type=click.Path(exists=True, dir_okay=False,
                resolve_path=True), nargs=-1, required=True)
def display(display_format, filename):
    """Display version in existing file.

    :param str display_format: Format to display output in
    :type filename: `tuple` of `str`
    :param filename: File to operate on
    """
    multi = len(filename) != 1
    for fname in filename:
        try:
            version = CliVersion.read(fname)
        except ValueError as error:
            fail(error.args[0])
            return errno.EIO

        if multi:
            click.echo("%s: " % fname, nl=False)
        success(version.display(display_format))
