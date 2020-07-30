from setuptools import setup
from fish_api.config import Config


setup(
    # Application name:
    name="fish-api",

    # Version number (initial):
    version=Config.VERSION,

    # Application author details:
    author="gmaniac",
    # author_email="",

    cmdclass={},

    # Packages
    packages=["fish_api"],

    # Entry Point
    
    # Include additional files into the package
    include_package_data=True,

    # license="LICENSE.txt",
    description="Fish API provides endpoints for sensor data.",

    # long_description=open("README.txt").read(),

    # Dependent packages (distributions)
    install_requires=[],
)