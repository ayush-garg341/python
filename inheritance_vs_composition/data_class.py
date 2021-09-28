"""
    Data classes are just regular classes that are geared towards storing state, rather than containing a lot of logic. 
    Every time you create a class that mostly consists of attributes, you make a data class.

    What the dataclasses module does is to make it easier to create data classes. It takes care of a lot of boilerplate for you.
    
    This is especially useful when your data class must be hashable; 
    because this requires a __hash__ method as well as an __eq__ method.
"""


class InventoryItem:
    '''Class for keeping track of an item in inventory.'''
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def __init__(
            self, 
            name: str, 
            unit_price: float,
            quantity_on_hand: int = 0
        ) -> None:
        self.name = name
        self.unit_price = unit_price
        self.quantity_on_hand = quantity_on_hand

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand
    
    def __repr__(self) -> str:
        return (
            'InventoryItem('
            f'name={self.name!r}, unit_price={self.unit_price!r}, '
            f'quantity_on_hand={self.quantity_on_hand!r})')

    def __hash__(self):
        return hash((self.name, self.unit_price, self.quantity_on_hand))

    def __eq__(self, other):
        if not isinstance(other, InventoryItem):
            return NotImplemented
        return (
            (self.name, self.unit_price, self.quantity_on_hand) == 
            (other.name, other.unit_price, other.quantity_on_hand))


it = InventoryItem("Peanut Butter", 350.0, 2)
print("Total cost of {} is {}".format(it.name, it.total_cost()))


# With dataclass we can reduce it to:

from dataclasses import dataclass

@dataclass(unsafe_hash=True)
class InventoryItem:
    '''Class for keeping track of an item in inventory.'''
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand

"""
    With data class, we need not to have initializer method ( __init__ ) in the class.
"""