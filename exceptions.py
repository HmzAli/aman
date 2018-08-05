''' Exceptions for alias manager'''

class Error(Exception):
    pass

class AliasExistsError(Error):
    self.message = 'Alias already exists'

class AliasNotFoundError(Error):
    self.message = 'Alias not found'

class InvalidAliasValueError(Error):
    self.message = 'Invalid alias value'
