from setuptools import find_packages
from setuptools import setup

setup(
    name='test_msgs',
    version='1.2.2',
    packages=find_packages(
        include=('test_msgs', 'test_msgs.*')),
)
