from lettuce import step as lettuce_step

import versionah


def step(match):
    """Replace values in match strings with data from versionah module

    The purpose is entirely to improve the look and readability of the steps
    defined below, it provides nothing over hard coding the values in step
    definitions.
    """
    valid_dict = dict([(s[6:], getattr(versionah, s)) for s in dir(versionah)
                       if s.startswith("VALID_")])
    return lettuce_step(match % valid_dict)
