import tomlkit

from sync_with_poetry.swp import PoetryItems, PreCommitRepo
from tests.helpers import LOCK_CONTENT


def test_poetry_items_creation() -> None:
    """Test PoetryItems init"""
    content = tomlkit.loads(LOCK_CONTENT)
    assert isinstance(content["package"], tomlkit.items.AoT)
    p = PoetryItems(content["package"])
    assert type(p._poetry_list) == list


def test_poetry_items_metadata() -> None:
    """Test PreCommitRepo metadata (returned by PoetryItems.get_by_repo)"""
    content = tomlkit.loads(LOCK_CONTENT)
    assert isinstance(content["package"], tomlkit.items.AoT)
    p = PoetryItems(content["package"])
    item = p.get_by_repo("https://github.com/pre-commit/mirrors-mypy")
    assert type(item) == PreCommitRepo
    assert item.name == "mypy"
    assert item.repo == "https://github.com/pre-commit/mirrors-mypy"
    assert item.rev == "v0.910"
