#! /usr/bin/python -tt

def bump(version, bump_type):
    """Bump a version string

    :type version: ``str``
    :param version: Version string to bump
    :type bump_type: ``str``
    :param bump_type: Component to bump
    :rtype: ``str``
    :return: Bumped version string
    """
    major, minor, micro = map(int, version.split("."))
    if bump_type == "major":
        major = major + 1
        minor = 0
        micro = 0
    elif bump_type == "minor":
        minor = minor + 1
        micro = 0
    elif bump_type == "micro":
        micro = micro + 1
    return ".".join(map(str, (major, minor, micro)))


def display(version, format):
    """Display a version string

    :type version: ``str``
    :param version: Version string to display
    :type format: ``str``
    :param format: Format to display version string in
    :rtype: ``str``
    :return: Formatted version string
    """
    major, minor, micro = map(int, version.split("."))
    if format == "triple":
        return ".".join(map(str, (major, minor, micro)))
    elif format == "hex":
        return "0x%02x%02x%02x" % (major, minor, micro)
    elif format == "libtool":
        return "%i:%i" % (major * 10 + minor, 20 + micro)


def read(file):
    """Read a version file

    :type file: ``str``
    :param file: Version file to read
    :rtype: ``file``
    :return: Version string
    :raise OSError: When ``file`` doesn't exist
    """
    return open(file).read().strip()
