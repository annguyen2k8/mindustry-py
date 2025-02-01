from ..content.items import *

class ItemStack:
    item:Item
    amount:int 
    def __init__(self, item:Item, amount:int) -> None:
        self.item = item
        self.amount = amount