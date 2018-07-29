""" This modules handles storing and retrieval of aliases from a file"""

import re
import config

def load_aliases():
    alias_pairs = []
    with open(config.AMAN_ALIAS_FILE) as f:
        alias_pairs = extract_aliases(f.readlines(), regex=config.ALIAS_DEFINITION_REGEX)
    return alias_pairs

def extract_aliases(lines, regex=r''):
    """ Finds shell alias definition patterns """
    alias_pairs = []
    for line in lines:
        m = re.match(regex, line)
        if m:
            alias_pairs.append(m.groups())
    return alias_pairs

def save_aliases():
    """ Write aliases to a file """
    pass
