''' Alias manager for Unix shells'''
import sys
import pkg_resources

from .operations import exec_command
from .config import HELP_TEXT, USAGE_TEXT, COLORS

def main(cmd_str):
    if cmd_str == '--help' or not cmd_str:
        default('{}{}'.format(HELP_TEXT, USAGE_TEXT))
        return

    if cmd_str == '--version':
        default(pkg_resources.get_distribution('aman').version)
        return

    if exec_command(cmd_str):
        return

    error('Invalid command: {}'.format(cmd_str.split(' ')[0]))
    default(USAGE_TEXT)

def prompt(message):
    if sys.version_info.major == 3:
        action = input(message)
    else:
        action = raw_input(message)
    return action

def default(message):
    print(message)

def success(message):
    print('{}{}\033[1;m'.format(COLORS['SUCCESS'], message))

def error(message):
    print('{}{}\033[1;m'.format(COLORS['ERROR'], message))

main(' '.join(sys.argv[1:]))