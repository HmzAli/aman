""" Aliases are managed here"""
from alias import Alias

class Manager():
    def __init__(self, aliases=None):
        self.aliases = []
        # Get from file
        self.aliases = aliases

    def add(self, name, value):
        self.aliases.append(Alias(name, value))

        self.save()

    def edit(self, name='', value=''):
        alias = get_alias(name)
        if alias:
            self.alias.value = value

        self.save()

    def modify(self, old_name, new_name):
        existing_alias = get_alias(new_name)
        if existing_alias:
            return False

        alias = get_alias(name)
        alias.name = new_name

        self.save()

    def delete(self, name):
        alias = get_alias(name)
        if alias:
          self.aliases.remove(alias)

    def list_all(self):
        for (a in self.aliases):
            print('{0}={2}'.format(a.name, a.value))

    def get_alias(name):
        try:
            return list(filter(lambda a: a.name == name, self.aliases))[0]
        except IndexError:
            return None

    def save(self):
        """ Saves to file"""
        pass

