"""File to define Fish class."""


class Fish:
    """Class representing a Fish with an age attribute."""
    age: int

    def __init__(self):
        """Initializes Fish object."""
        self.age = 0
    
    def one_day(self):
        """Adds one day to the current age of the current fish."""
        self.age += 1