"""Idiomatic Python Program"""

__author__: str = "730922305"


def all(lst: list[int], num: int) -> bool:
    if len(lst) == 0:  # if the list is empty, return False
        return False
    else:
        for i in range(0, len(lst)):  # iterate every element in the list by index
            if lst[i] != num:  # if one pair of them doesn't match, return False
                return False
        return True  # if they all match, return True


def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError(
            "max() arg is an empty List"
        )  # raise error if the argument list is empty
    else:
        maximum = input[0]  # set the maximum number as the first one
        """find the maximum number"""
        for i in range(1, len(input)):  # iterate every element in the list by index
            if input[i] > maximum:
                maximum = input[
                    i
                ]  # if an element is bigger than the maximum, set that number as the new maximum
        return maximum  # return the final maximum


def is_equal(lst1: list[int], lst2: list[int]) -> bool:
    if len(lst1) != len(lst2):
        return False
    else:
        for i in range(0, len(lst1)):  # iterate every element in the list by index
            if lst1[i] != lst2[i]:  # if one pair of them doesn't match, return False
                return False
        return True  # if they all match, return True


def extend(lst1: list[int], lst2: list[int]) -> None:
    for i in range(0, len(lst2)):  # iterate every element in the list by index
        lst1.append(lst2[i])  # append every element in list2 to the end of list1
