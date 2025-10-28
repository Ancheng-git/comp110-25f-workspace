__author__: str = "730922305"

from CQs.cq03.find_max import find_and_remove_max


def test_find_and_remove_max_use_case_one():
    example: list[int] = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
    a: int = find_and_remove_max(example)
    assert a == 5
    assert example == [1, 2, 3, 4, 4, 3, 2, 1]


def test_find_and_remove_max_use_case_two():
    example: list[int] = [8, 8, 7, 8, 8]
    a: int = find_and_remove_max(example)
    assert a == 8
    assert example == [7]


def test_find_and_remove_max_edge_case():
    example: list[int] = []
    a: int = find_and_remove_max(example)
    assert a == -1
    assert example == []
