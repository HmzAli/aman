#!/usr/bin/env python3
''' Alias manager for users of Unix shells'''

import sys
import re

from manager import Manager
from exceptions import AliasNotFoundError

manager = Manager()

# Valid command parameters
ALIAS_NAME = r'([\w_-]+)'
ALIAS_VALUE = r'(.+)'

# Valid command regex
# Edit command follows the same syntax as ADD. If alias exists, it's edited in place
ADD = r'^'+ALIAS_NAME+'='+ALIAS_VALUE
DELETE = r'^rm '+ALIAS_NAME
LIST = r'^(list|ls)$'

HELP_TEXT = 'Alias manager for shell lovers'
USAGE_TEXT = '''

USAGE:

  To add / edit an alias: 
  <name>="<value"

  list       List all aliases
  rm         Remove an alias
  --help     Show help
  --version  Show version number'''

def execute(args_str):
	if args_str == '--help' or not args_str:
		print('{}{}'.format(HELP_TEXT, USAGE_TEXT))
		return

	for cmd, fn in functions.items():
		match = re.match(cmd, args_str)
		if match:
			fn(match)
			return

	error('Invalid command: {}'.format(args_str.split(' ')[0]))
	print(USAGE_TEXT)

def add_alias(match):
	name = match.group(1)
	value = match.group(2)

	try:
		alias = manager.get_alias(name)
	except AliasNotFoundError:
		manager.add(name, value)
	else:
		action = prompt('Alias already exists. Edit? (y/n): ');

	if not action in 'yn':
		error('Invalid option: {}'.format(action))
	elif action == 'y':
		manager.edit(name, value)

def delete_alias(match):
	name = match.group(1)
	manager.delete(name)

def list_aliases(*args):
	aliases = manager.get_all()

	for alias in aliases:
		print(' {} = "{}"'.format(alias.name, alias.value))

def prompt(message):
	if sys.version_info.major == 3:
		action = input(message)
	else:
		action = raw_input(message)
	return action

def error(message):
	print(message)

functions = {
	ADD: add_alias,
	DELETE: delete_alias,
	LIST: list_aliases
}
execute(' '.join(sys.argv[1:]))