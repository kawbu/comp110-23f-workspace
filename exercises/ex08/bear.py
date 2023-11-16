"""File to define Bear class."""


class Bear:
    """Class representing a Bear with attributes age and hunger_score."""
    age: int
    hunger_score: int
    
    def __init__(self):
        """Initializes bear object."""
        self.age = 0
        self.hunger_score = 0
    
    def one_day(self):
        """Adds one day to the current bear's age and decrements its hunger score by one."""
        self.age += 1
        self.hunger_score -= 1
    
    def eat(self, num_fish: int) -> None:
        """Increments the current bear's hunger score by 3."""
        self.hunger_score += num_fish