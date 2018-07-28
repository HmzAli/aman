""" This modules handles storing and retrieval of aliases from a file"""

import config

def load_aliases():
    raw_alias_strs = []
    with open(config.AMAN_ALIAS_FILE) as f:
       raw_alias_strs = extract_aliases(f.readlines())
    """ Reads aliases pattern from a file. Creates a tuble of key value pairings"""
    return ()

def extract_aliases(lines):
   """ Finds shell alias definition patterns """
   # get aliases using regex
   pass

def save_aliases():
    """ Write aliases to a file """
    pass
