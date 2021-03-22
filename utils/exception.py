class CrejoException(Exception):
    """Base class for exceptions"""

    def __init__(self, error_code, msg, *args, **kwargs):
        self.error_code = error_code
        self.msg = msg
        Exception.__init__(self, *args, **kwargs)

    def get_message(self):
        """ message getter"""
        return self.msg

    def get_error_code(self):
        """ error code getter"""
        return self.error_code
