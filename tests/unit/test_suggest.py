from changelog_manager.utils import ChangelogManager


def test_changelog_suggest_major():
    cm = ChangelogManager("./tests/data/changelog_major.md")
    assert cm.suggest == "3.0.0"

def test_changelog_suggest_minor():
    cm = ChangelogManager("./tests/data/changelog_minor.md")
    assert cm.suggest == "2.1.0"

def test_changelog_suggest_bugfix():
    cm = ChangelogManager("./tests/data/changelog_bugfix.md")
    assert cm.suggest == "2.0.1"

def test_changelog_suggest_no_changes():
    cm = ChangelogManager("./tests/data/changelog_no_changes.md")
    assert cm.suggest == "2.0.0"

