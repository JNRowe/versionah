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
