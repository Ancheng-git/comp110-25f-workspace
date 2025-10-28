"""practice calling + defining functions"""


# Function definition
def sum(num_1: int, num_2: int) -> int:
    return num_1 + num_2


if __name__ == "__main__":
    print(sum(num_1=int(input("first number")), num_2=int(input("second number"))))
