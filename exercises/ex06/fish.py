"""File to define Fish class."""

__author__: str = "730922305"


class Fish:
    """The fish class."""

    age: int

    def __init__(self):
        """Constructor"""
        self.age = 0
        return None

    def one_day(self):
        """Fish after one day."""
        self.age += 1
        return None
