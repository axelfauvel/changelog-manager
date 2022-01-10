from setuptools import setup, find_packages
import os

with open("requirements.txt") as f:
    required_packages = f.read().splitlines()

setup(
    name="changelog_manager",
    version="1.0.0",
    description="Manage your changelog using this CLI",
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
