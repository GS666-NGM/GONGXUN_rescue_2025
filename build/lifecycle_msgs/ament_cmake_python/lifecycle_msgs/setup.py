from setuptools import find_packages
from setuptools import setup

setup(
    name='lifecycle_msgs',
    version='1.2.2',
    packages=find_packages(
        include=('lifecycle_msgs', 'lifecycle_msgs.*')),
)
