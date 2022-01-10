from setuptools import setup, find_packages
import os

with open("requirements.txt") as f:
    required_packages = f.read().splitlines()

# read the contents of your README file
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="changelog_manager",
    version="1.0.1",
    description="Easily manage your changelog using this CLI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pycom/compilation_api",
    author="Axel FAUVEL",
    author_email="axel.fauvel@gmail.com",
    license="MIT",
    packages=find_packages(include=["changelog_manager.*"]),
    install_requires=required_packages,
    zip_safe=False,
    entry_points={
        "console_scripts": [
            "changelog-manager=changelog_manager.__main__:cli"
        ],
    },
    python_requires=">=3.9",
)
