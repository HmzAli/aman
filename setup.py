from distutils.core import setup
import sys

setup(
    name='Aman',
    version='0.1',
    packages=['aman',],
    license='MIT',
    long_description=open('README.md').read(),
    scripts=['bin/aman']
)
