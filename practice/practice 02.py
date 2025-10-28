def find_small_card(cards: str) -> int:
    i = 0
    smallest = int(cards[0])
    while i < len(cards):
        if int(cards[i]) < smallest:
            smallest = int(cards[i])
        i = i + 1
    return smallest
