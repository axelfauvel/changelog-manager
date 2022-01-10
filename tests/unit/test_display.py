from changelog_manager.utils import ChangelogManager

result = """## [1.0.0] - 2017-04-10
### deprecated
- Known issue 1 (1.0.0)
- Known issue 2 (1.0.0)
"""


def test_changelog_suggest_major():
    cm = ChangelogManager("./tests/data/changelog_major.md")
    assert cm.display("1.0.0") == result
