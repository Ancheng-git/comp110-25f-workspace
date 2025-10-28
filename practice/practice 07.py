def odd_and_even(lst: list[int]) -> list[int]:
    new_list: list[int] = []
    for i in range(0, len(lst)):
        if lst[i] % 2 == 1:
            if i % 2 == 0:
                new_list.append(lst[i])
    return new_list


"""Returns list of words that are shorter than 5 characters"""


def short_words(lst: list[str]) -> list[str]:
    new_list: list[str] = []
    for i in lst:
        if len(i) >= 5:
            print(f"{i} is too long!")
        else:
            new_list.append(i)
    return new_list


def multiples(lst: list[int]) -> list[bool]:
    new_list: list[bool] = []
    for i in range(0, len(lst)):
        if i == 0:
            if lst[i] % lst[-1] == 0:
                new_list.append(True)
            else:
                new_list.append(False)
        else:
            if lst[i] % lst[i - 1] == 0:
                new_list.append(True)
            else:
                new_list.append(False)
    return new_list


def reverse_multiply(lst: list[int]) -> list[int]:
    new_list: list[int] = []
    for i in lst:
        new_list.append(2 * i)
    another_new_list: list[int] = []
    for i in range(1, len(lst) + 1):
        i = -i
        another_new_list.append(new_list[i])
    return another_new_list


def process_and_reverse_list(lst: list[int]) -> list[int]:
    for i in range(0, len(lst)):
        lst[i] = lst[i] * lst[i]
    if len(lst) % 2 == 1:
        new_list: list[int] = []
        for i in range(0, len(lst) - 1, 2):
            new_list.append(lst[i] + lst[i + 1])
        new_list.append(lst[-1])
    else:
        new_list: list[int] = []
        for i in range(0, len(lst) - 1, 2):
            new_list.append(lst[i] + lst[i + 1])
    another_new_list = []
    for i in range(1, len(new_list) + 1):
        i = -i
        another_new_list.append(new_list[i])
    return another_new_list


def bubble_up_sort(lst: list[int]) -> None:
    for i in range(1, len(lst)):
        i = -i
        if lst[i - 1] > lst[i]:
            a = lst[i - 1]
            b = lst[i]
            lst[i - 1] = b
            lst[i] = a


def insert(lst: list[int], a: int) -> None:
    lst.append(a)
    bubble_up_sort(lst)


def value_exists(dic: dict[str, int], a: int) -> bool:
    for i in dic:
        if dic[i] == a:
            return True
    return False


def plus_or_minus_n(inp: dict[str, int], n: int) -> None:
    for i in inp:
        if inp[i] % 2 == 0:
            inp[i] += n
        else:
            inp[i] -= n
    return None


def free_biscuits(dic: dict[str, list[int]]) -> dict[str, bool]:
    new_dic: dict[str, bool] = {}
    for i in dic:
        if sum(dic[i]) >= 100:
            new_dic[i] = True
        else:
            new_dic[i] = False
    return new_dic


def max_key(dic: dict[str, list[int]]) -> str:
    lst: list[int] = []
    for i in dic:
        lst.append(sum(dic[i]))
    max_num = lst[0]
    index = 1
    while index < len(lst):
        if lst[index] > max_num:
            max_num = lst[index]
        index += 1
    for i in dic:
        if sum(dic[i]) == max_num:
            return i


def merge_lists(lst1: list[str], lst2: list[int]) -> dict[str, int]:
    if len(lst1) != len(lst2):
        return {}
    else:
        dic: dict[str, int] = {}
        for i in range(0, len(lst1)):
            dic[lst1[i]] = lst2[i]
        return dic
