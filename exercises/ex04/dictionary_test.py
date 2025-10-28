"""Dictionary Unit Tests."""

__author__: str = "730922305"

from exercises.ex04.dictionary import (
    invert,
    favorite_color,
    count,
    alphabetizer,
    update_attendance,
)


def test_invert_use_case_one() -> None:
    """Check that the function invert the dictionary properly."""
    example: dict[str, str] = {"a": "z", "b": "y", "c": "x"}
    assert invert(example) == {"z": "a", "y": "b", "x": "c"}


def test_invert_use_case_two() -> None:
    """Check that the function invert the dictionary properly."""
    example: dict[str, str] = {"apple": "cat"}
    assert invert(example) == {"cat": "apple"}


def test_invert_edge_case() -> None:
    """Check that the function deal with unexpected input properly."""
    example: dict[str, str] = {}
    assert invert(example) == {}


def test_favorite_color_use_case_one() -> None:
    """Check that the function will return the most favorite color properly."""
    example: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(example) == "blue"


def test_favorite_color_use_case_two() -> None:
    """Check that the function will return the most favorite color properly."""
    example: dict[str, str] = {
        "Marc": "yellow",
        "Ezri": "yellow",
        "Kris": "blue",
        "Andrew": "red",
    }
    assert favorite_color(example) == "yellow"


def test_favorite_color_edge_case() -> None:
    """Check that the function deal with empty input well."""
    example: dict[str, str] = {}
    assert favorite_color(example) == ""


def test_count_use_case_one() -> None:
    """Check that the function count the input well."""
    example: list[str] = ["a", "a", "b", "c"]
    assert count(example) == {"a": 2, "b": 1, "c": 1}


def test_count_use_case_two() -> None:
    """Check that the function count the input well."""
    example: list[str] = ["a", "d", "b", "c", "c"]
    assert count(example) == {"a": 1, "d": 1, "b": 1, "c": 2}


def test_count_edge_case() -> None:
    """Check that the function deal with empty input well."""
    example: list[str] = []
    assert count(example) == {}


def test_alphabetizer_use_case_one() -> None:
    """Check that the function classify the input properly."""
    example: list[str] = ["cat", "apple", "boy", "angry", "bad", "car"]
    assert alphabetizer(example) == {
        "c": ["cat", "car"],
        "a": ["apple", "angry"],
        "b": ["boy", "bad"],
    }


def test_alphabetizer_use_case_two() -> None:
    """Check that the function classify the input properly."""
    example: list[str] = ["Python", "sugar", "Turtle", "party", "table"]
    assert alphabetizer(example) == {
        "p": ["Python", "party"],
        "s": ["sugar"],
        "t": ["Turtle", "table"],
    }


def test_alphabetizer_edge_case() -> None:
    """Check that the function deal with the empty input properly."""
    example: list[str] = []
    assert alphabetizer(example) == {}


def test_update_attendance_use_case_one() -> None:
    """Check if the function update attendance properly."""
    example: dict[str, list[str]] = {
        "Monday": ["Vrinda", "Kaleb"],
        "Tuesday": ["Alyssa"],
    }
    update_attendance(example, "Tuesday", "Vrinda")
    assert example == {
        "Monday": ["Vrinda", "Kaleb"],
        "Tuesday": ["Alyssa", "Vrinda"],
    }


def test_update_attendance_use_case_two() -> None:
    """Check if the function update attendance properly."""
    example: dict[str, list[str]] = {
        "Monday": ["Vrinda", "Kaleb"],
        "Tuesday": ["Alyssa", "Vrinda"],
    }
    update_attendance(example, "Wednesday", "Kaleb")
    assert example == {
        "Monday": ["Vrinda", "Kaleb"],
        "Tuesday": ["Alyssa", "Vrinda"],
        "Wednesday": ["Kaleb"],
    }


def test_update_attendance_edge_case() -> None:
    """Check that the function deal with repeat attendance well."""
    example: dict[str, list[str]] = {
        "Monday": ["Vrinda", "Kaleb"],
        "Tuesday": ["Alyssa"],
    }
    update_attendance(example, "Tuesday", "Alyssa")
    assert example == {
        "Monday": ["Vrinda", "Kaleb"],
        "Tuesday": ["Alyssa"],
    }
