"""Exercise CQ07 - Point class."""

from __future__ import annotations

__author__ = "730658017"


class Point:
    """Creates an object which holds variables 'x' and 'y' of float types."""
    x: float
    y: float

    def __init__(self, x_init: float = 0, y_init: float = 0) -> None:
        """Initializes object with float attributes x and y."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Modifies existing x and y object attributes and multiplies them by a given integer."""
        self.x = self.x * factor
        self.y = self.y * factor
    
    def scale(self, factor: int) -> Point:
        """Creates a new point value by multiplying current x and y attributes by an integer factor and storing those values in new variables."""
        new_x: float = self.x * factor
        new_y: float = self.y * factor
        return Point(new_x, new_y)
    
    def __str__(self) -> str:
        """Combines object attributes 'x' and 'y' to a a single string, and returns a string displaying the values."""
        return f"x: {self.x}; y: {self.y}"
    
    def __mul__(self, factor: int | float) -> Point:
        """Returns a new Point object with x and y values multipled by a given factor."""
        return Point(self.x * factor, self.y * factor)
    
    def __add__(self, addend: int | float) -> Point:
        """Returns a new Point object with x and y values increased by a given addend."""
        return Point(self.x + addend, self.y + addend)