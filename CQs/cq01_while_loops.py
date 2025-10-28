"""Search a Character in a Phrase"""

__author__: str = "730922305"


def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0
    i: int = 0
    while i < len(phrase):
        if search_char == phrase[i]:
            count += 1
        i = i + 1
    return count
