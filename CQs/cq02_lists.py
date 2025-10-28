"""Mutating functions."""

__author__: str = "730922305"


def manual_append(lst: list[int], num: int) -> None:
    lst.append(num)


def double(lst: list[int]) -> None:
    for i in range(0, len(lst)):
        lst[i] = 2 * lst[i]


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)

print(list_1)
print(list_2)
