import sys

from .config import COLORS

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