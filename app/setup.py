import sys
from setuptools import setup
from pets_api.config import Config


setup(
    # Application name:
    name="pets-api",

    # Version number (initial):
    version=Config.VERSION,

    # Application author details:
    author="gmaniac",
    # author_email="",

    cmdclass={},

    # Packages
    packages=["pets_api"],

    # Entry Point
    
    # Include additional files into the package
    include_package_data=True,

    # license="LICENSE.txt",
    description="Pets API enables a restful backend for pets-web.",

    # long_description=open("README.txt").read(),

    # Dependent packages (distributions)
    install_requires=[],
)