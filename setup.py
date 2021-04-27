# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='nordpoolapi',
    version='0.1.0',
    description='Package to access N2EX data',
    long_description=readme,
    author='Max Bird',
    url='https://github.com/MaxBird300/NordPoolAPI',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=[
        'requests>=2.25',
        'pandas>=1.2',
        'python-dotenv>=0.17',
    ],
    tests_require=[
        'pytest>=6',
    ],
    
)

