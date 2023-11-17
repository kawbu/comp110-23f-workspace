"""File to define River class."""

__author__ = "730658017"

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear


class River:
    """Class which represents a river with attributes day, list of bears, and a list of fish, and functions to simulate life in a river."""
    day: int
    bears: list[Bear]
    fish: list[Fish]
    
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Removes fish of ages over 3 and removes bears of ages over 5."""
        temp_fish: list[Fish] = self.fish.copy()
        for idx in range(len(self.fish)):
            if self.fish[idx].age > 3:
                temp_fish.pop(idx)
        self.fish = temp_fish
        temp_bears: list[Bear] = self.bears.copy()
        for idx in range(len(self.bears)):
            if self.bears[idx].age > 5:
                temp_bears.pop(idx)
        self.bears = temp_bears

    def bears_eating(self):
        """Adds to hunger of each bear and removes fish correspondingly, granted there are at least 5 fish in the river."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                bear.eat(3)
                self.remove_fish(3)
    
    def check_hunger(self):
        """Removes bears whose hunger levels are under 0."""
        temp_bears = self.bears.copy()
        for idx in range(len(self.bears)):
            if self.bears[idx].hunger_score < 0:
                temp_bears.pop(idx)
        self.bears = temp_bears
        
    def repopulate_fish(self):
        """Multiplies population of fish by the current population // 2 and * 4."""
        for x in range((len(self.fish) // 2) * 4):
            self.fish.append(Fish())
    
    def repopulate_bears(self):
        """Multiplies population of bears by the current population // 2."""
        for x in range(len(self.bears) // 2):
            self.bears.append(Bear())
    
    def view_river(self):
        """Displays each day of the simulation with the corresponding population of fish and bears for that day."""
        print(f"~~~ Day {self.day}: ~~~\nFish population: {len(self.fish)}\nBear population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
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
    
    def one_river_week(self) -> None:
        """Simulates one week of life inthe river."""
        for i in range(7):
            self.one_river_day()
    
    def remove_fish(self, amount: int) -> None:
        """Removes fish by a given integer amount."""
        while amount != 0:
            self.fish.pop(0)
            amount -= 1