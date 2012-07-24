from expecter import _RaisesExpectation


class _RaisesOSErrorExpectation(_RaisesExpectation):
    def __init__(self, code, message):
        self.code = code
        self.message = message

    def validate_failure(self, exc_type, exc_value):
        code = exc_value.errno
        message = exc_value.strerror
        if self.code != code:
            raise AssertionError('Expected code %s but got %s'
                                 % (self.code, exc_value[0]))
        if not message.endswith(self.message):
            raise AssertionError("Expected to end with OSError('%s') but got "
                                 "%s('%s')" % (self.message, exc_type.__name__,
                                               exc_value))
        elif issubclass(exc_type, OSError):
            return True
        else:
            pass


def raises_OSError(code, message):
    return _RaisesOSErrorExpectation(code, message)


def read_tag(f):
    f.read = 1
    return f


def write_tag(f):
    f.write = 1
    return f


def execute_tag(f):
    f.execute = 1
    return f
