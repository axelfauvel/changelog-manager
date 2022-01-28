# changelog-manager

https://pypi.org/project/changelog-manager/

changelog_manager helps you manage your changelog.

This project uses [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)

It mainly uses [keepachangelog](https://github.com/Colin-b/keepachangelog) library and adds a CLI above it.

## How to install it?

`pip install changelog_manager`

## How to use it?

```
❯ changelog-manager --help
Usage: changelog-manager [OPTIONS] COMMAND [ARGS]...

Options:
  --version  Show the version and exit.
  --help  Show this message and exit.

Commands:
  add      Add a new changelog entry.
  current  Get current version from changelog
  display  display changes according to changelog
  release  Release unrealeased items in changelog
  suggest  Suggest future version from changelog
```

## release
* release the changelog
* Update version in `changelog_manager/_version.py`
* Create a commit and tag using the version
* run `python setup.py sdist bdist_wheel`
* run `twine upload -r testpypi dist/*`
* run `twine upload -r pypi dist/*`
