from __future__ import annotations
from typing import *

from .item import *

from mindustry.content.items import Items

class ItemStack:    
    item:Item
    amount:int 
    
    def __init__(self, item:Item=Items.copper, amount:int=0) -> None:
        self.item = item
        self.amount = amount
    
    @staticmethod
    def with_item(*items:List[object]) -> List[ItemStack]:
        stacks:List[ItemStack] = []
        for i in range(0, len(items), 2):
            stacks.append(ItemStack(items[i], items[i + 1]))
        return stacks