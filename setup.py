from distutils.core import setup
import sys
import os

setup(
    name='Aman',
    version='0.1',
    packages=['aman',],
    license='MIT',
    long_description=open('README.md').read(),
    scripts=['bin/aman']
)

# Creating alias storage file
HOME_PATH = os.getenv('HOME')
DIR = '.aman'
ALIAS_FILE_NAME = 'aliases'
ALIAS_FILE_PATH = '{}/{}/{}'.format(HOME_PATH, DIR, ALIAS_FILE_NAME)
os.mkdir('{}/{}'.format(HOME_PATH, DIR))
with open(ALIAS_FILE_PATH, 'w') as f:
	pass
