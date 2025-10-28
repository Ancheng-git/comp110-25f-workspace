"""A Wordle Game Program"""

__author__: str = "730922305"


def contains_char(word: str, letter: str) -> bool:
    """determine if a letter is in a word"""
    assert len(letter) == 1, f"len('{letter}') is not 1"
    i: int = 0
    while i < len(word):
        if word[i] == letter:
            return True
        else:
            i = i + 1
    return False


def emojified(guess: str, secret: str) -> str:
    """give a string of emojis as a result"""
    assert len(guess) == len(secret), "Guess must be same length as secret"
    i = 0
    result = "\U00002b1c" * len(secret)
    while i < len(secret):
        if contains_char(word=secret, letter=guess[i]):
            if guess[i] == secret[i]:
                result = result[:i] + "\U0001f7e9" + result[i + 1 :]
                i = i + 1
            else:
                result = result[:i] + "\U0001f7e8" + result[i + 1 :]
                i = i + 1
        else:
            i = i + 1
    return result


def input_guess(length: int) -> str:
    """prompt the user for a guess"""
    word: str = input("Enter a " + str(length) + " character word:")
    while len(word) != length:
        word = input("That wasn't " + str(length) + " chars! Try again:")
    return word


def main(secret: str) -> None:
    """the entrypoint of the program and main game loop."""
    turns: int = 1
    while turns < 7:
        print(f"=== Turn {turns}/6 ===")
        word = input_guess(length=len(secret))
        if emojified(guess=word, secret=secret) == "\U0001f7e9" * len(secret):
            print("\U0001f7e9" * len(secret))
            print(f"You won in {turns}/6 turns!")
            return None
        else:
            print(emojified(guess=word, secret=secret))
            turns = turns + 1
    print(" X/6 - Sorry, try again tomorrow! ")
    return None


if __name__ == "__main__":
    main(secret="codes")
