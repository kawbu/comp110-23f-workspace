"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730658017"


class Simpy:
    """Class Simpy which contains attribute 'values' of type 'list[float]' and methods."""
    values: list[float]

    def __init__(self, given_list: list[float]) -> None:
        """Constructions a Simpy object with attribute "values" equal to a passed in list."""
        self.values = given_list
    
    def __str__(self) -> str:
        """Returns a string in the form of 'Simpy([{values}])'."""
        return f'Simpy({self.values})'
    
    def fill(self, fill_value: float, quantity: int) -> None:
        """Removes all elements in 'values' and replaces them with a given float * a given quantity of elements to clone."""
        self.values = []
        for i in range(quantity):
            self.values.append(fill_value)

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Removes all elements in 'values' and replaces them with a range of numbers from 'start' to 'stop' with an increment or decrement of a given float, defaulted to 1.0."""
        assert step != 0.0
        self.values = []
        if start > stop:
            while start > stop:
                self.values.append(start)
                start += step
        else:
            while start < stop:
                self.values.append(start)
                start += step
    
    def sum(self) -> float:
        """Returns sum of all elements in 'values'."""
        return sum(self.values)
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Returns a new Simpy object of two corresponding Simpy object's elements added together, or adds to each element by a given float value."""
        if type(rhs) is Simpy:
            assert len(rhs.values) == len(self.values)
            return Simpy([rhs.values[i] + self.values[i] for i in range(len(rhs.values))])
        else:
            return Simpy([i + rhs for i in self.values])
        
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Returns a new Simpy object of two corresponding Simpy object's with the LHS raised to the RHS element's corresponding power, or raises each element on LHS by a given float value."""
        if type(rhs) is Simpy:
            assert len(rhs.values) == len(self.values)
            return Simpy([self.values[i] ** rhs.values[i] for i in range(len(rhs.values))])
        else:
            return Simpy([i ** rhs for i in self.values])
    
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Returns a new list with boolean values representing the equality of LHS with RHS, or LHS with a given float value."""
        if type(rhs) is Simpy:
            assert len(rhs.values) == len(self.values)
            return [self.values[i] == rhs.values[i] for i in range(len(rhs.values))]
        else:
            return [i == rhs for i in self.values]
        
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Returns a new list with boolean values representing the equation 'LHS > RHS' for each corresponding value in LHS and RHS, or the equation 'LHS > RHS' for every value in LHS compared to a float value."""
        if type(rhs) is Simpy:
            assert len(rhs.values) == len(self.values)
            return [self.values[i] > rhs.values[i] for i in range(len(rhs.values))]
        else:
            return [i > rhs for i in self.values]

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Returns an element at the given index in 'values' in a Simpy object, or only filtered values of a Simpy object based on a given list of booleans."""
        if type(rhs) is int:
            return self.values[rhs]
        else:
            return Simpy([self.values[i] for i in range(len(self.values)) if rhs[i]])
