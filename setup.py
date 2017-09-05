import os
import sys

from setuptools import setup, find_packages

ROOT = os.path.realpath(os.path.join(os.path.dirname(
    sys.modules['__main__'].__file__)))

# Add Sentry to path so we can import distutils
sys.path.insert(0, os.path.join(ROOT, 'markdown_storage'))

VERSION = '0.1.dev0'

install_requires=[
    'Markdown',
    'PyYAML',
    'python-dateutil',
]

setup(
    name='markdown_storage',
    version=VERSION,
    long_description=open('README.md').read(),

    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,

    install_requires=install_requires,
)
