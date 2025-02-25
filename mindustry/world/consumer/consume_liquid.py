from . import *

from mindustry.type import *

class ConsumeLiquid(ConsumeLiquidBase):
    liquid:Liquid
    def __init__(self, liquid:Liquid=None, amount:float=0.0):
        super().__init__(amount)
        self.liquid = liquid