from .import *

from mindustry.type import *

class ConsumeLiquidFilter(ConsumeLiquidBase):
    filter = lambda l: False
    
    def __init__(self, liquid, amount):
        super().__init__(amount)
        self.filter = liquid