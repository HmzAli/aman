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
# Edit command follows the same syntax as ADD. If alias exists, it's edited in place
ADD = r'^'+ALIAS_NAME+'='+ALIAS_VALUE
DELETE = r'^rm '+ALIAS_NAME
LIST = r'^list$'

HELP_TEXT = 'Alias manager for shell lovers'
USAGE_TEXT = '''USAGE:

  To add / edit an alias: 
  <name>="<value"

  list       List all aliases
  rm         Remove an alias
  --help     Show help
  --version  Show version number'''

def execute(args_str):
	if args_str == '--help' or not args_str:
		print('{}\n\n{}'.format(HELP_TEXT, USAGE_TEXT))
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