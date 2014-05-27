from setuptools import setup
import sys

if sys.version_info < (3, 4):
    raise 'python 3.4 is required'

setup(
    name='gitm',
    version = '0.0.1',
    description='A tool for managing multiple git repos.',
    author='Alex Couture-Beil',
    author_email='alexcb@mofo.ca',
    packages = [
        'gitm',
        'gitm.commands',
        ],
    scripts=[
        'scripts/gitm',
        ],
)
