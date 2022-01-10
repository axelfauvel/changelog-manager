# pylint: disable=protected-access
import keepachangelog


class ChangelogManager:
    def __init__(self, changelog_path: str) -> None:
        self.__changelog_path = changelog_path
        self.__changelog = keepachangelog.to_dict(
            self.__changelog_path, show_unreleased=True
        )
        (
            self.__current_version,
            self.__current_semantic_version,
        ) = keepachangelog._versioning.actual_version(self.__changelog)

    @property
    def suggest(self) -> str:
        """
        suggest the future version using Unreleased part of changelog

        Returns:
            str: version number
        """
        next_version = keepachangelog._versioning.guess_unreleased_version(
            self.__changelog, self.__current_semantic_version
        )
        return next_version if next_version else self.current

    @property
    def current(self) -> str:
        """
        returns the current version using changelog

        Returns:
            str: current version number
        """
        return self.__current_version

    def display(self, version: str) -> str:
        """
        display markdown formatted changes for a given version

        Args:
            version (str): version to find in the changelog

        Returns:
            str: markdown formatted changes
        """
        changes: dict = self.__changelog[version]
        changes_md: str = ""
        changes_md += (
            f"## [{changes['metadata']['version']}] - "
            f"{changes['metadata']['release_date']}\n"
        )
        changes.pop("metadata")
        for changes_groups in changes:
            changes_md += f"### {changes_groups}\n"
            for element in changes[changes_groups]:
                changes_md += f"- {element}\n"
        return changes_md

    def release(self):
        """
        create a new release in the changelog using Unreleased part
        """
        keepachangelog.release(self.__changelog_path)
