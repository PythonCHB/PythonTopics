#!/usr/bin/env python

"""
A prototype of a decorator that adds an iterator to a dataclass
so it can be passed in to the dict() constructor to make a dict.

If this is thought to be useful it could be added to the dataclass
decorator itself, to give all decorators this functionality.
"""


from dataclasses import dataclass


class DataClassIterator:
    """
    Iterator for dataclasses

    This used the class' __dataclass_fields__ dict to iterate through the
    fields and their values
    """

    def __init__(self, dataclass_instance):
        self.dataclass_instance = dataclass_instance
        self.keys_iter = iter(dataclass_instance.__dataclass_fields__.keys())

    def __iter__(self):
        return self

    def __next__(self):
        key = next(self.keys_iter)
        return (key, getattr(self.dataclass_instance, key))


def _dunder_iter(self):
    """
    function used as the __iter__ method in the dictable_dataclass decorator
    """
    return DataClassIterator(self)


def dictable_dataclass(the_dataclass):
    """
    class decorator for making a dataclass iterable in a way that is compatible
    with the dict() constructor
    """
    the_dataclass.__iter__ = _dunder_iter

    return the_dataclass


# Example from the dataclass docs:
@dictable_dataclass
@dataclass
class InventoryItem:
    '''Class for keeping track of an item in inventory.'''
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand


if __name__ == "__main__":
    # try it out:
    inv_item = InventoryItem("sneakers", 50.0, 20)

    print("an InventoryItem:\n", inv_item)
    print()

    print("And the dict you can make from it:")
    print(dict(inv_item))


