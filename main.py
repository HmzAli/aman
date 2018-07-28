""" Aliases are managed here"""
from alias import Alias

class Manager():
    aliases = []

    def __init__(self, aliases=None):
        self.aliases = aliases

    def add(self, name, value):
        self.aliases.append(Alias(name, value))
        self.save()

    def edit(self, name='', value=''):
        if name:
            self.name = name
        if value:
            self.value = value
        self.save()

    def delete(self, alias):
        self.aliases.remove(alias)

    def list_all(self):
        for (a in self.aliases):
            print('{0}={2}'.format(a.name, a.value))

    def save(self):
        """ Saves to file"""
        pass

