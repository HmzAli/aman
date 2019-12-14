import re
import pkg_resources

from .manager import Manager
from .exceptions import AliasNotFoundError
from .config import HELP_TEXT, USAGE_TEXT
from .io import success, error, default, prompt

manager = Manager()

def exec_command(cmd_str):
    ''' Checks if the command is valid and executes its corresponding operation

        Args:
            cmd_str (str): the command to execute e.g. ls

        Returns:
            bool: True if the command is valid. False otherwise
    '''

    # Regex for a valid alias definition pattern
    ALIAS_NAME = r'([\w_-]+)'
    ALIAS_VALUE = r'(.+)'

    # Regex for valid commands
    HELP = '--help'
    VERSION = '--version'
    ADD = r'^'+ALIAS_NAME+'='+ALIAS_VALUE
    DELETE = r'^rm '+ALIAS_NAME
    LIST = r'^(list|ls)$'

    if not cmd_str:
        show_help()
        return

    operations = {
        HELP: show_help,
        VERSION: show_version,
        ADD: add_alias,
        DELETE: delete_alias,
        LIST: list_aliases
    }

    for cmd, op in operations.items():
        match = re.match(cmd, cmd_str)
        if match:
            op(match)
            return

    error('Invalid command: {}'.format(cmd_str.split(' ')[0]))
    default(USAGE_TEXT)

def show_help():
    default('{}{}'.format(HELP_TEXT, USAGE_TEXT))

def show_version():
    default(pkg_resources.get_distribution('aman').version)

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
    message = ''
    for alias in aliases:
        message = message + '\n{:<30} -> {}'.format(alias.name, alias.value)
    success(message)
