from .item import *
from ..content.items import *

class ItemStack:
    item:Item
    amount:int 
    def __init__(self, item:Item=Items.copper, amount:int=0) -> None:
        self.item = item
        self.amount = amount