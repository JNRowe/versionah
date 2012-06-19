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
            raise AssertionError(
                "Expected to end with %s('%s') but got %s('%s')" %
                 (self._exception_class.__name__,
                  str(self.message),
                  exc_type.__name__,
                  str(exc_value)))
        elif issubclass(exc_type, OSError):
            return True
        else:
            pass


def raises_OSError(code, message):
    return _RaisesOSErrorExpectation(code, message)
