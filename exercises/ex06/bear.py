"""File to define Bear class."""

__author__: str = "730922305"


class Bear:
    """The bear class."""

    age: int
    hunger_score: int

    def __init__(self):
        """Constructor."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Increase age and decrease hungry score."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Bears eat fishes."""
        self.hunger_score = self.hunger_score + num_fish

        return None
