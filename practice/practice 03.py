def sum(number: int) -> int:
    if number > 0:
        output = number + sum(number=number - 1)
        return output
    elif number < 0:
        return -1
    else:
        return 0
