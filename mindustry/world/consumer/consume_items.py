from typing import *

from mindustry.type.item_stack import ItemStack
from .consume import Consume

class ConsumeItems(Consume):
    items:List[ItemStack] = []
    def __init__(self, items:List[ItemStack]):
        super().__init__()
        self.items = items