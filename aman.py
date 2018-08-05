#!/usr/bin/env python3
''' Alias manager for users of Unix shells'''

import sys
import re

from manager import Manager
manager = Manager()

# Valid command parameters
ALIAS_NAME = r'([\w_-]+)'
ALIAS_VALUE = r'(.+)'

# Valid command regex
ADD = r'^'+ALIAS_NAME+'='+ALIAS_VALUE # Edit command follows the same syntax. If alias exists, it's edited in place
DELETE = r'^delete '+ALIAS_NAME
LIST = r'^list$'

HELP_TEXT = 'Alias manager for shell users'
USAGE_TEXT = '\n<name>="<value>"'

def execute(args_str):
	if args_str == '--help' or not args_str:
		return

	for cmd, fn in functions.items():
		match = re.match(cmd, args_str)
		if match:
			fn(match)
			return

	print('Invalid command')

def add_alias(match):
	name = match.group(1)
	value = match.group(2)
	manager.add(name, value)

def delete_alias(match):
	name = match.group(1)
	manager.delete(name)

def list_aliases(*args):
	aliases = manager.get_all()

	for alias in aliases:
		print(' {} = "{}"'.format(alias.name, alias.value))

functions = {
	ADD: add_alias,
	DELETE: delete_alias,
	LIST: list_aliases
}
execute(' '.join(sys.argv[1:]))