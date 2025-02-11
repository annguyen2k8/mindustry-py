from typing import *

from mindustry.type import *

from .consume import Consume

class ConsumeLiquids(Consume):
    liquids:List[LiquidStack] = []
    
    def __init__(self, liquids:List[LiquidStack]):
        super().__init__()
        self.liquids = liquids