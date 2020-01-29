import sys
from setuptools import setup, find_packages

setup(
    # Application name:
    name="pets-api",

    # Version number (initial):
    version="0.1.0",

    # Application author details:
    author="gmaniac",
    # author_email="",

    cmdclass={},

    # Packages
    packages=["papi"],

    # Entry Point
    
    # Include additional files into the package
    include_package_data=True,

    # license="LICENSE.txt",
    description="Pets API enables a restful backend for pets-web.",

    # long_description=open("README.txt").read(),

    # Dependent packages (distributions)
    install_requires=[],
)