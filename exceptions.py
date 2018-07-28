""" Exceptions for alias manager"""

class Error(Exception):
    pass

class AliasExistsError(Error):
    def __init__(self, message):
        self.message = message

class AliasNotFoundError(Error):
    def __init__(self, message):
        self.message = message

class InvalidAliasValue(Error):
    def __init__(self, message):
        self.message = message
