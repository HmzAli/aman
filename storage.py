""" This modules handles storing and retrieval of aliases from a file"""

import re
import config

def load_aliases():
    alias_pairs = []

    with open(config.AMAN_ALIAS_FILE) as f:
        lines = f.readlines()

    for line in lines:
        m = re.match(config.ALIAS_DEFINITION_REGEX, line)
        if m:
            alias_pairs.append(m.groups())
    return alias_pairs

def save_aliases(alias_pairs):
    """ Write aliases to a file """
    lines = []
    with open(config.AMAN_ALIAS_FILE, 'w') as f:
        for name, value in alias_pairs:
            lines.append(config.ALIAS_SAVING_FORMAT.format(name=name, value=value))
        f.writelines(lines)
