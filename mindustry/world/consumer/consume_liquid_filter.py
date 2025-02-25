from mindustry.type import *

from .consume_liquid_base import ConsumeLiquidBase

class ConsumeLiquidFilter(ConsumeLiquidBase):
    filter = lambda l: False
    
    def __init__(self, liquid, amount):
        super().__init__(amount)
        self.filter = liquid