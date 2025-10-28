def get_first(lst: list[str]) -> str:
    if len(lst) == 0:
        return ""
    else:
        return lst[0]


def remove_first(lst: list[str]) -> None:
    lst.pop(0)
    return None


def get_and_remove_first(lst: list[str]) -> str:
    removed: str = lst.pop(0)
    return removed
