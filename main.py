""" Aliases are managed here"""

import storage
from alias import Alias
from exceptions import (
    AliasNotFoundError,
    AliasExistsError,
    InvalidAliasError,
)

class Manager():
    def __init__(self):)
        for name, value in storage.load_aliases():
            self.aliases.append(Alias(name, value))

    def add(self, name, value):
        self.aliases.append(Alias(name, value))

        self.save()

    def edit(self, name, value):
        if not value:
            raise InvalidAliasError
        alias = self.get_alias(name)

        if alias:
            self.alias.value = value

        self.save()

    def modify(self, current_name, new_name):
        existing_alias = self.get_alias(new_name)
        if existing_alias:
            raise AliasExistsError

        alias = self.get_alias(current_name)
        alias.name = new_name

        self.save()

    def delete(self, name):
        alias = get_alias(name)
        if alias:
          self.aliases.remove(alias)

        self.save()

    def list_all(self):
        for a in self.aliases:
            print('{0}={2}'.format(a.name, a.value))

    def get_alias(name):
        try:
            return list(filter(lambda a: a.name == name, self.aliases))[0]
        except IndexError:
            raise AliasNotFoundError

    def save(self):
        storage.save_aliases([(alias.name, alias.value) for alias in self.aliases])
        pass

