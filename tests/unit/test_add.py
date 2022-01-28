from changelog_manager.utils import ChangelogManager


def test_changelog_add():
    cm = ChangelogManager("./tests/data/changelog_no_changes.md")
    cm.add("fixed", "some change")
    assert (
        cm._ChangelogManager__changelog["unreleased"]["fixed"][0]
        == "some change"
    )
