''' This module handles storing and retrieval of aliases from a file'''

import os
import re
import subprocess

from .config import ALIAS_DIR_PATH, ALIAS_FILE_PATH
from .io import info

ALIAS_DEFINITION_REGEX = r'\s*alias (\w+)=[\'\"](.+)[\'\"]'
ALIAS_SAVING_FORMAT = '\nalias {name}="{value}"'

def load_aliases():
    alias_pairs = []

    try:
        with open(ALIAS_FILE_PATH) as f:
            lines = f.readlines()
    except EnvironmentError:
        info('\n{} file doesn\'t exist, create a new one... \n'.format(ALIAS_FILE_PATH))
        create_file()
        return alias_pairs

    for line in lines:
        m = re.match(ALIAS_DEFINITION_REGEX, line)
        if m:
            alias_pairs.append(m.groups())
    return alias_pairs

def save_aliases(alias_pairs):
    lines = []
    with open(ALIAS_FILE_PATH, 'w') as f:
        for name, value in alias_pairs:
            lines.append(ALIAS_SAVING_FORMAT.format(name=name, value=value))
        f.writelines(lines)

def create_file():
    if not os.path.exists(ALIAS_DIR_PATH):
        os.mkdir(ALIAS_DIR_PATH)

    with open(ALIAS_FILE_PATH, 'w') as f:
        pass
