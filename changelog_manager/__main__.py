import click
from changelog_manager.utils import ChangelogManager
from changelog_manager._version import __version__


@click.group()
@click.version_option(__version__)
def cli():
    pass


@cli.command(help="Get current version from changelog")
@click.option(
    "--changelog",
    help="changelog file, default to CHANGELOG.md",
    default="CHANGELOG.md",
)
def current(changelog: str) -> None:
    changelog_manager = ChangelogManager(changelog)
    click.echo(changelog_manager.current)


@cli.command(help="Suggest future version from changelog")
@click.option(
    "--changelog",
    help="changelog file, default to CHANGELOG.md",
    default="CHANGELOG.md",
)
def suggest(changelog: str) -> None:
    changelog_manager = ChangelogManager(changelog)
    click.echo(changelog_manager.suggest)


@cli.command(help="Release unrealeased items in changelog")
@click.option(
    "--changelog",
    help="changelog file, default to CHANGELOG.md",
    default="CHANGELOG.md",
)
def release(changelog: str) -> None:
    changelog_manager = ChangelogManager(changelog)
    changelog_manager.release()


@cli.command(help="display changes according to changelog")
@click.option(
    "--changelog",
    help="changelog file, default to CHANGELOG.md",
    default="CHANGELOG.md",
)
@click.option("--version", required=True, help="version changes to display")
def display(changelog: str, version: str) -> None:
    changelog_manager = ChangelogManager(changelog)
    click.echo(changelog_manager.display(version))


@cli.command()
@click.argument(
    "change_type",
    type=click.Choice(
        ["fixed", "added", "changed", "deprecated", "security", "removed"]
    ),
)
@click.argument(
    "change_description",
    nargs=-1,
)
@click.option(
    "--changelog",
    help="changelog file, default to CHANGELOG.md",
    default="CHANGELOG.md",
)
def add(change_type, change_description, changelog):
    """
    Add a new changelog entry. ex:
    changelog-manager add fixed "fix bug xyz"
    """
    change_description = " ".join(change_description)
    changelog_manager = ChangelogManager(changelog)
    changelog_manager.add(change_type, change_description)
    changelog_manager.commit()


if __name__ == "__main__":
    cli()
