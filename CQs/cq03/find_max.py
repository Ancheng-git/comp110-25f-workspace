__author__: str = "730922305"


def find_and_remove_max(lst: list[int]) -> int:
    if len(lst) == 0:
        return -1
    else:
        max_num: int = lst[0]
        for i in lst:
            if i >= max_num:
                max_num = i
        index: int = 0
        length = len(lst)
        while index < length:
            if lst[index] == max_num:
                lst.pop(index)
                index -= 1
                length -= 1
            index += 1
        return max_num
