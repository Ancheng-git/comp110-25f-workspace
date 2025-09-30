"""Dictionary Utils"""

__author__: str = "730922305"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    inverted_dictionary: dict[str, str] = {}
    for i in dictionary:
        inverted_dictionary[dictionary[i]] = i
    if len(dictionary) == len(inverted_dictionary):
        return inverted_dictionary
    else:
        raise KeyError(
            "You encountered more than one of the same key when trying to invert your dictionary"
        )


def favorite_color(dictionary: dict[str, str]) -> str:
    count_dictionary: dict[str, int] = {}
    for i in dictionary:
        if dictionary[i] not in count_dictionary:
            count_dictionary[dictionary[i]] = 1
        else:
            count_dictionary[dictionary[i]] += 1
    count_list: list[int] = []
    for i in count_dictionary:
        count_list.append(count_dictionary[i])
    max_count: int = max(count_list)
    for i in count_dictionary:
        if count_dictionary[i] == max_count:
            return i


def count(lst: list[str]) -> dict[str, int]:
    dictionary: dict[str, int] = {}
    for i in lst:
        if i not in dictionary:
            dictionary[i] = 1
        else:
            dictionary[i] += 1
    return dictionary


def alphabetizer(lst: list[str]) -> dict[str, list[str]]:
    dictionary: dict[str, list[str]] = {}
    for i in lst:
        if i.lower()[0] not in dictionary:
            lst1: list[str] = []
            lst1.append(i)
            dictionary[i.lower()[0]] = lst1
        else:
            dictionary[i.lower()[0]].append(i)
    return dictionary


def update_attendance(log: dict[str, list[str]], day: str, student: str) -> None:
    if day not in log:
        lst: list[str] = []
        lst.append(student)
        log[day] = lst
    else:
        log[day].append(student)
