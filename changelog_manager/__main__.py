import click
from changelog_manager.utils import ChangelogManager


@click.group()
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


if __name__ == "__main__":
    cli()
