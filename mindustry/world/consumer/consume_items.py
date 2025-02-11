from typing import *

from mindustry.type import *
from .consume import *

class ConsumeItems(Consume):
    items:List[ItemStack] = []
    def __init__(self, items:List[ItemStack]):
        super().__init__()
        self.items = items