from setuptools import setup, find_packages

AUTHOR = 'Andrei Gramakov'
MAINTAINER = 'Andrei Gramakov'
EMAIL = 'andrei.gramakov@espressif.com'

NAME = 'debug_backend'
VERSION = '1.0.0'
SHORT_DESCRIPTION = 'This package provides extented capabilities to interacting with ESP chips via GDB and OpenOCD.'
LICENSE = 'MIT'
URL = ''
SCRIPTS = [  # All scripts must be listed here
    'scripts/run_tests.py'
]
REQUIREMENTS = [
    'pygdbmi',
    'unittest-xml-reporting'
]

try:  # Using  README.md as a long description
    with open('README.md') as readme:
        LONG_DESCRIPTION = '/n' + readme.read()
except IOError:
    # maybe running setup.py from some other dir
    LONG_DESCRIPTION = ''

setup(
    # metadata
    name=NAME,
    description=SHORT_DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    license=LICENSE,
    version=VERSION,
    author=AUTHOR,
    maintainer=MAINTAINER,
    author_email=EMAIL,
    url=URL,
    platforms='Cross Platform',
    classifiers=['Programming Language :: Python :: 3'],
    packages=find_packages(),
    scripts=SCRIPTS,
    install_requires=REQUIREMENTS
)
