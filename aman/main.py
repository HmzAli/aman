''' Alias manager for Unix shells'''
import sys

from .operations import exec_command

def main(cmd_str):
    exec_command(cmd_str)

main(' '.join(sys.argv[1:]))