from changelog_manager.utils import ChangelogManager


def test_changelog_current():
    cm = ChangelogManager('./tests/data/changelog_major.md')
    assert cm.current == "2.0.0"
