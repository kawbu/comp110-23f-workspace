"""Exercise CQ07 - Point class."""

from __future__ import annotations

__author__ = "730658017"


class Point:
    """Creates an object which holds variables 'x' and 'y' of float types."""
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float) -> None:
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