"""File to define River class."""

__author__: str = "730922305"

from exercises.ex06.fish import Fish
from exercises.ex06.bear import Bear


class River:

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        new_fish: list[Fish] = []
        for i in self.fish:
            if i.age <= 3:
                new_fish.append(i)

        new_bears: list[Bear] = []
        for i in self.bears:
            if i.age <= 5:
                new_bears.append(i)

        self.fish = new_fish
        self.bears = new_bears

        return None

    def bears_eating(self):
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)

        return None

    def check_hunger(self):
        new_bears: list[Bear] = []
        for i in self.bears:
            if i.hunger_score >= 0:
                new_bears.append(i)
        self.bears = new_bears
        return None

    def repopulate_fish(self):
        for i in range((len(self.fish) // 2) * 4):
            self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        for i in range(len(self.bears) // 2):
            self.bears.append(Bear())
        return None

    def view_river(self):
        fish_pop: int = len(self.fish)
        bear_pop: int = len(self.bears)
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {fish_pop}")
        print(f"Bear population: {bear_pop}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        for index in range(7):
            self.one_river_day()
        return None

    def remove_fish(self, amount: int):
        for i in range(amount):
            self.fish.pop(0)
        return None
