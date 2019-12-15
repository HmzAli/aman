import os

# Storage file settings
HOME_DIR = os.getenv('HOME')
DIR = '.aman'
FILE_NAME = 'aliases'
ALIAS_DIR_PATH = '{}/{}'.format(HOME_DIR, DIR)
ALIAS_FILE_PATH = '{}/{}'.format(ALIAS_DIR_PATH, FILE_NAME)

# CLI settings
HELP_TEXT = 'Shell alias manager'
USAGE_TEXT = '''

USAGE:

    To add / edit an alias to a single command:
    <name>=<command>

    For chained commands:
    <name>="command1 && command2 || command3"

    list       List all aliases
    rm         Remove an alias
    --help     Show help
    --version  Show version number'''

COLORS = {
    'SUCCESS': '\033[0;32m',
    'ERROR': '\033[0;31m',
    'INFO': '\033[0;33m'
}
