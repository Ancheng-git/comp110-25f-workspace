"""test for my list functions"""

from list_fns import get_first, remove_first, get_and_remove_first


def test_get_first_use_case() -> None:

    example: list[str] = ["chair", "desk", "lamp"]
    assert get_first(example) == "chair"


def test_get_first_edge_case() -> None:
    example: list[str] = []
    assert get_first(example) == ""


def test_remove_first_use_case() -> None:
    example: list[str] = ["chair", "desk", "lamp"]
    remove_first(example)
    assert example == ["desk", "lamp"]


def test_get_and_remove_first_use_case() -> None:
    """check that the function will remove and return the first element"""
    example: list[str] = ["chair", "desk", "lamp"]
    assert get_and_remove_first(example) == "chair"
    assert example == ["desk", "lamp"]
