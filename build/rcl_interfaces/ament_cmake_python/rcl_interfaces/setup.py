from setuptools import find_packages
from setuptools import setup

setup(
    name='rcl_interfaces',
    version='1.2.2',
    packages=find_packages(
        include=('rcl_interfaces', 'rcl_interfaces.*')),
)
