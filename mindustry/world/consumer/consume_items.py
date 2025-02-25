from typing import *

from . import *

from mindustry.type import *

class ConsumeItems(Consume):
    items:List[ItemStack] = []
    def __init__(self, items:List[ItemStack]):
        super().__init__()
        self.items = items