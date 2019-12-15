from distutils.core import setup
import sys
import os

setup(
    name='Aman',
    author='Hamza Ali',
    author_email='hamza.ishak.ali@gmail.com',
    version='1.1',
    packages=['aman',],
    license='MIT',
    long_description=open('README.md').read(),
    scripts=['bin/aman']
)
