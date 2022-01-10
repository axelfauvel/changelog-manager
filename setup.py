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
    version="1.0.3",
    description="Easily manage your changelog using this CLI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/axelfauvel/changelog-manager",
    author="Axel FAUVEL",
    author_email="axel.fauvel@gmail.com",
    license="MIT",
    packages=find_packages(
        include=["changelog_manager", "changelog_manager.*"]
    ),
    install_requires=required_packages,
    zip_safe=False,
    entry_points={
        "console_scripts": [
            "changelog-manager=changelog_manager.__main__:cli"
        ],
    },
    python_requires=">=3.9",
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 4 - Beta",
        # Indicate who your project is intended for
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        # Pick your license as you wish (should match "license" above)
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
    ],
    project_urls={
        "Documentation": "https://pypi.org/project/changelog-manager/#description",
        "Say Thanks!": "https://saythanks.io/to/axel.fauvel",
        "Source": "https://github.com/axelfauvel/changelog-manager",
        "Tracker": "https://github.com/axelfauvel/changelog-manager/issues",
    },
)
