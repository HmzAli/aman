import re
from .manager import Manager
from .exceptions import AliasNotFoundError

def exec_command(cmd_str):
    ''' Checks if the command is valid and executes its corresponding operation

        Args:
            cmd_str (str): the command to execute e.g. ls

        Returns:
            bool: True if the command is valid. False otherwise
    '''

    # Valid command regex
    ALIAS_NAME = r'([\w_-]+)'
    ALIAS_VALUE = r'(.+)'
    ADD = r'^'+ALIAS_NAME+'='+ALIAS_VALUE
    DELETE = r'^rm '+ALIAS_NAME
    LIST = r'^(list|ls)$'

    operations = {
        ADD: add_alias,
        DELETE: delete_alias,
        LIST: list_aliases
    }

    for cmd, op in operations.items():
        match = re.match(cmd, args_str)
        if match:
            op(match)
            return True

    return False

def add_alias(match):
    name = match.group(1)
    value = match.group(2)

    try:
        alias = manager.get_alias(name)
    except AliasNotFoundError:
        manager.add(name, value)
        success('Alias added successfully.')
    else:
        action = prompt('Alias already exists. Edit? (y/n): ');
        if not action in 'yn':
            error('Invalid option: {}'.format(action))
        elif action == 'y':
            manager.edit(name, value)
            success('Alias updated.')

def delete_alias(match):
    name = match.group(1)
    manager.delete(name)

def list_aliases(*args):
    aliases = manager.get_all()

    for alias in aliases:
        success('{} {:<30} -> {}'.format(COLORS['SUCCESS'], alias.name, alias.value))

manager = Manager()