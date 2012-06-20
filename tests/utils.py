from expecter import _RaisesExpectation


class _RaisesOSErrorExpectation(_RaisesExpectation):
    def __init__(self, code, message):
        self.code = code
        self.message = message

    def validate_failure(self, exc_type, exc_value):
        code, message = exc_value
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
