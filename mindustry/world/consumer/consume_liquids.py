from typing import *

from . import *

from mindustry.type import *


class ConsumeLiquids(Consume):
    liquids:List[LiquidStack] = []
    
    def __init__(self, liquids:List[LiquidStack]):
        super().__init__()
        self.liquids = liquids